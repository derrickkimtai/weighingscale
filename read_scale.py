import serial
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_weight_from_scale():
    ser = None
    try:
        # Adjust the serial port settings according to your scale's requirements
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        logging.info(f"Serial port opened: {ser.is_open}")

        # Send command to request weight
        ser.write(b'W\r\n')  # This command might need to be adjusted based on your scale's protocol
        logging.info("Command sent to scale")

        # Add a small delay to give the scale time to respond
        time.sleep(0.5)

        # Read the weight from the scale
        raw_data = ser.readline()
        logging.info(f"Raw data received: {raw_data}")

        # Decode and split the raw data
        decoded_data = raw_data.decode('latin-1').strip()
        logging.info(f"Decoded data: {decoded_data}")

        # Extract the weight value from the comma-separated string
        data_parts = decoded_data.split(',')
        if len(data_parts) > 1:
            weight_str = data_parts[1]
            weight = float(weight_str)
            return weight
        else:
            logging.error("Unexpected data format")
            return None
    except serial.SerialException as e:
        logging.error(f"Serial error: {e}")
    except Exception as e:
        logging.error(f"Error reading weight from scale: {e}")
    finally:
        if ser:
            ser.close()
            logging.info("Serial port closed")

if __name__ == "__main__":
    weight = read_weight_from_scale()
    if weight is not None:
        logging.info(f"Weight: {weight} kgs")
        print(f"Weight: {weight} kgs")  # Display the weight on the terminal
    else:
        logging.error("Failed to read weight")
        print("Failed to read weight")  # Display error message on the terminal
