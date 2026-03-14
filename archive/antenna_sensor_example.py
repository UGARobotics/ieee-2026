"""
Example usage of AntennaSensor for detecting antenna colors
"""

from camera_filter import AntennaSensor
import time

# Initialize sensor with half-resolution for Raspberry Pi performance
sensor = AntennaSensor(camera_id=0, certainty_threshold=0.6, scale=0.5)

print("Antenna Sensor initialized. Press Ctrl+C to exit.\n")

try:
    while True:
        # Keep camera stream updated
        sensor.update()
        
        # Detect antenna color
        color = sensor.detect_color()
        
        if color is not None:
            print(f"Detected antenna color: {color}")
        else:
            print("No confident detection (uncertain)")
        
        # Small delay to avoid spamming
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nShutting down...")
    sensor.shutdown()


# ===== Alternative usage patterns =====

# Adjust certainty threshold for stricter/looser detection:
def example_with_tuning():
    sensor = AntennaSensor(scale=0.5)
    
    # Start strict, then loosen if needed
    sensor.set_certainty_threshold(0.8)
    
    for i in range(5):
        sensor.update()
        color = sensor.detect_color()
        print(f"Read {i+1}: {color}")
    
    # Lower threshold for more lenient detection
    sensor.set_certainty_threshold(0.5)
    color = sensor.detect_color()
    print(f"With lower threshold: {color}")
    
    sensor.shutdown()


# Use in a robot subsystem:
def example_integration():
    """Show how to integrate into existing subsystem"""
    sensor = AntennaSensor(scale=0.5)
    
    # In your main loop
    for _ in range(100):
        sensor.update()
        antenna_color = sensor.detect_color()
        
        if antenna_color == AntennaSensor.RED:
            print("Move to RED zone")
        elif antenna_color == AntennaSensor.BLUE:
            print("Move to BLUE zone")
        elif antenna_color == AntennaSensor.GREEN:
            print("Move to GREEN zone")
        elif antenna_color == AntennaSensor.PURPLE:
            print("Move to PURPLE zone")
        else:
            print("Searching...")
        
        time.sleep(0.1)
    
    sensor.shutdown()


if __name__ == "__main__":
    # Run basic example
    # example_with_tuning()
    # example_integration()
    pass
