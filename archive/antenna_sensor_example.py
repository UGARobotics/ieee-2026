"""
Example usage of AntennaSensor for detecting antenna colors
"""

from camera_filter import AntennaSensor
import cv2
import numpy as np
import time

# Initialize sensor with half-resolution for Raspberry Pi performance
sensor = AntennaSensor(camera_id=0, certainty_threshold=0.6, scale=0.5)

print("Antenna Sensor initialized. Press Ctrl+C to exit.\n")

def display_detection():
    """Display frame with circle detection and color classification"""
    try:
        while True:
            # Keep camera stream updated
            sensor.update()
            
            # Get current frame for visualization
            frame = sensor.current_frame
            if frame is None:
                continue
            
            # Detect antenna color
            color = sensor.detect_color()
            
            # Process frame for visualization
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 1)
            
            # Detect circles
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
            
            display_frame = frame.copy()
            
            if circles is not None:
                circles = np.uint16(np.around(circles))
                
                for i in circles[0, :]:
                    center = (i[0], i[1])
                    radius = i[2]
                    
                    # Draw circle outline
                    cv2.circle(display_frame, center, radius, (0, 255, 0), 2)
                    
                    # Draw bounding box
                    x1 = max(0, center[0] - radius)
                    y1 = max(0, center[1] - radius)
                    x2 = min(frame.shape[1], center[0] + radius)
                    y2 = min(frame.shape[0], center[1] + radius)
                    cv2.rectangle(display_frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    
                    # Extract circle region for color
                    mask = np.zeros(frame.shape[:2], dtype=np.uint8)
                    cv2.circle(mask, center, radius, 255, -1)
                    circle_pixels = frame[mask == 255]
                    
                    if len(circle_pixels) > 0:
                        avg_color = np.mean(circle_pixels, axis=0).astype(np.uint8)
            
            # Display detected color
            status_text = f"Color: {color if color else 'UNCERTAIN'}"
            cv2.putText(display_frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Show frame
            cv2.imshow("Antenna Sensor", display_frame)
            
            print(f"Detected: {color if color else 'UNCERTAIN'}")
            
            if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
                break

    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        sensor.shutdown()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    display_detection()
