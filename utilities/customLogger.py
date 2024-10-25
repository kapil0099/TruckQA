import logging
import os

class LogGen:
    @staticmethod
    def log():
        # Get the project root directory (one level up from the current file's directory)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_folder = os.path.join(project_root, "Logs")

        # Ensure the Logs directory exists
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        # Define the log file path
        log_file = os.path.join(log_folder, "automation.log")
        print(f"Log file path: {log_file}")  # Print the log file path for debugging

        # Create or get the logger
        logger = logging.getLogger("automationLogger")
        logger.setLevel(logging.INFO)  # Set logger level globally

        # Check if the logger already has handlers to prevent adding multiple handlers
        if not logger.handlers:
            # Create file handler
            file_handler = logging.FileHandler(log_file, mode='a')  # Append to the file
            file_handler.setLevel(logging.INFO)

            # Create formatter and add it to the handler
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            file_handler.setFormatter(formatter)

            # Add the handler to the logger
            logger.addHandler(file_handler)

            # Optional: Log initialization message
            logger.info("Logging system initialized successfully.")

        return logger
