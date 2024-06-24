# read_scale.py

import serial
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_weight_from_scale():
    ser = None
    try:
        # Adjust the serial port settings according to your scale's requirements
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        ser.write(b'W\r\n')  # Command to request weight (depends on scale)
        weight = ser.readline().decode('utf-8').strip()
        return weight
    except serial.SerialException as e:
        logging.error(f"Serial error: {e}")
    except Exception as e:
        logging.error(f"Error reading weight from scale: {e}")
    finally:
        if ser:
            ser.close()

if __name__ == "__main__":
    weight = read_weight_from_scale()
    if weight:
        logging.info(f"Weight: {weight} kgs")
    else:
        logging.error("Failed to read weight")
