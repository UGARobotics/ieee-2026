import cv2
import numpy as np

class AntennaSensor:
    """Lightweight antenna sensor for Raspberry Pi.
    Detects colored circles on-demand with minimal processing."""
    
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    PURPLE = "PURPLE"
    UNCERTAIN = None
    
    def __init__(self, camera_id=0, certainty_threshold=0.6, scale=0.5):
        """Initialize camera with downscaling for performance.
        
        Args:
            camera_id: Camera device ID
            certainty_threshold: Confidence threshold (0.0-1.0)
            scale: Frame downscale factor (0.5 = half resolution)
        """
        self.camera_id = camera_id
        self.certainty_threshold = certainty_threshold
        self.scale = scale
        self.cap = cv2.VideoCapture(camera_id)
        
        if not self.cap.isOpened():
            raise RuntimeError(f"Failed to open camera {camera_id}")
        
        self.current_frame = None
        self._read_frame()
    
    def _read_frame(self):
        """Read and downscale latest frame"""
        ret, frame = self.cap.read()
        if ret and self.scale != 1.0:
            h, w = frame.shape[:2]
            frame = cv2.resize(frame, (int(w * self.scale), int(h * self.scale)))
        self.current_frame = frame if ret else None
        return ret
    
    def _classify_color(self, avg_color_bgr):
        """Fast color classification using HSV hue.
        
        Returns:
            tuple: (color_name, certainty)
        """
        b, g, r = avg_color_bgr
        hsv_color = cv2.cvtColor(np.uint8([[[b, g, r]]]), cv2.COLOR_BGR2HSV)[0][0]
        h, s, v = hsv_color
        
        # Skip if too desaturated
        if s < 30:
            return self.UNCERTAIN, 0.0
        
        # Fast hue-based classification
        sat_factor = s / 255.0
        
        if h < 10 or h > 170:
            return self.RED, sat_factor
        elif 35 <= h <= 85:
            return self.GREEN, sat_factor
        elif 100 <= h <= 125:
            return self.BLUE, sat_factor
        elif 125 <= h <= 160:
            return self.PURPLE, sat_factor
        
        return self.UNCERTAIN, 0.0
    
    def detect_color(self):
        """Fast circle detection and color classification.
        
        Returns:
            str: Color name or None if uncertain
        """
        if self.current_frame is None:
            self._read_frame()
            if self.current_frame is None:
                return self.UNCERTAIN
        
        # Simple grayscale and blur
        gray = cv2.cvtColor(self.current_frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 1)
        
        # Lightweight circle detection
        circles = cv2.HoughCircles(
            blurred,
            cv2.HOUGH_GRADIENT,
            dp=1,
            minDist=80,
            param1=30,
            param2=20,
            minRadius=15,
            maxRadius=100
        )
        
        if circles is None or len(circles[0]) == 0:
            return self.UNCERTAIN
        
        # Use first circle
        circle = circles[0][0]
        center = (int(circle[0]), int(circle[1]))
        radius = int(circle[2])
        
        # Create mask for circle region
        mask = np.zeros(self.current_frame.shape[:2], dtype=np.uint8)
        cv2.circle(mask, center, radius, 255, -1)
        
        # Get average color
        circle_pixels = self.current_frame[mask == 255]
        if len(circle_pixels) == 0:
            return self.UNCERTAIN
        
        avg_color = np.mean(circle_pixels, axis=0).astype(np.uint8)
        color_name, certainty = self._classify_color(avg_color)
        
        return color_name if certainty >= self.certainty_threshold else self.UNCERTAIN
    
    def update(self):
        """Keep camera stream fresh"""
        self._read_frame()
    
    def set_certainty_threshold(self, threshold):
        """Adjust detection sensitivity"""
        self.certainty_threshold = max(0.0, min(1.0, threshold))
    
    def shutdown(self):
        """Release camera"""
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()


