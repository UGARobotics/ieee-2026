"""
Example usage of AntennaSensor for detecting antenna colors with visual display
"""

from camera_filter import AntennaSensor
import cv2
import numpy as np
import time

# Initialize sensor
sensor = AntennaSensor(camera_id=0, certainty_threshold=0.6, scale=1.0)  # scale=1.0 for full resolution display

print("Antenna Sensor initialized. Press ESC to exit.\n")

def display_with_bounding_box():
    """Display live feed with circle detection and bounding boxes"""
    frame_count = 0
    
    try:
        while True:
            # Update stream
            sensor.update()
            frame = sensor.current_frame
            
            if frame is None:
                print("No frame captured")
                continue
            
            display_frame = frame.copy()
            
            # Convert to grayscale for circle detection
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
                maxRadius=150
            )
            
            circle_found = False
            
            if circles is not None and len(circles[0]) > 0:
                circles = np.uint16(np.around(circles))
                
                for i in circles[0, :]:
                    center = (i[0], i[1])
                    radius = i[2]
                    circle_found = True
                    
                    # Draw green circle outline
                    cv2.circle(display_frame, center, radius, (0, 255, 0), 3)
                    
                    # Draw blue bounding box
                    x1 = max(0, center[0] - radius)
                    y1 = max(0, center[1] - radius)
                    x2 = min(frame.shape[1], center[0] + radius)
                    y2 = min(frame.shape[0], center[1] + radius)
                    cv2.rectangle(display_frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                    
                    # Get color classification
                    mask = np.zeros(frame.shape[:2], dtype=np.uint8)
                    cv2.circle(mask, center, radius, 255, -1)
                    circle_pixels = frame[mask == 255]
                    
                    color = sensor.detect_color()
                    color_text = f"Color: {color}" if color else "Color: UNCERTAIN"
                    
                    # Put text with color info
                    cv2.putText(display_frame, color_text, (center[0] - 50, center[1] - radius - 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
            
            # Show status
            status = "CIRCLE FOUND" if circle_found else "NO CIRCLE"
            cv2.putText(display_frame, status, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            cv2.putText(display_frame, f"Frame: {frame_count}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            # Display
            cv2.imshow("ANTENNA DETECTION - Press ESC to exit", display_frame)
            
            # Save frame for inspection
            if frame_count % 10 == 0:
                cv2.imwrite(f"antenna_frame_{frame_count}.jpg", display_frame)
                print(f"Frame {frame_count}: {status}")
            
            frame_count += 1
            
            # ESC key to exit
            if cv2.waitKey(30) & 0xFF == 27:
                break
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        print("Shutting down...")
        sensor.shutdown()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    display_with_bounding_box()

