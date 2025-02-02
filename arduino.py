import serial
import json
import time
from typing import Dict, Any, Optional

class ArduinoCommunicator:
    def __init__(self, port: str = 'COM3', baud_rate: int = 9600, timeout: int = 1):
        """
        Initialize Arduino communication.
        
        Args:
            port (str): Serial port (default: COM3 for Windows)
            baud_rate (int): Baud rate for serial communication
            timeout (int): Serial timeout in seconds
        """
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.serial_connection: Optional[serial.Serial] = None

    def connect(self) -> bool:
        """
        Establish connection with Arduino.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baud_rate,
                timeout=self.timeout
            )
            # Allow Arduino to reset
            time.sleep(2)
            return True
        except serial.SerialException as e:
            print(f"Error connecting to Arduino: {e}")
            return False

    def disconnect(self):
        """Close the serial connection."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()

    def send_json(self, data: Dict[str, Any]) -> bool:
        """
        Send JSON data to Arduino.
        
        Args:
            data (Dict[str, Any]): Dictionary to be sent as JSON
            
        Returns:
            bool: True if send successful, False otherwise
        """
        if not self.serial_connection or not self.serial_connection.is_open:
            print("Serial connection not established")
            return False

        try:
            # Convert dictionary to JSON string and add newline for Arduino parsing
            json_string = json.dumps(data) + '\n'
            # Send as bytes
            self.serial_connection.write(json_string.encode())
            return True
        except Exception as e:
            print(f"Error sending JSON data: {e}")
            return False

    def receive_json(self) -> Optional[Dict[str, Any]]:
        """
        Receive JSON data from Arduino.
        
        Returns:
            Optional[Dict[str, Any]]: Received JSON data as dictionary, None if error occurs
        """
        if not self.serial_connection or not self.serial_connection.is_open:
            print("Serial connection not established")
            return None

        try:
            # Read until newline character
            line = self.serial_connection.readline().decode().strip()
            if line:
                return json.loads(line)
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON data: {e}")
            return None
        except Exception as e:
            print(f"Error receiving data: {e}")
            return None

    def flush_input_buffer(self):
        """Clear any pending input data."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.reset_input_buffer()

    def flush_output_buffer(self):
        """Clear any pending output data."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.reset_output_buffer()
