import logging # Imports the `logging` module for logging functionality

class Customlogger: # Defines a class named `Customlogger`
    def create_custom_logger(name): # Defines a static method `create_custom_logger` that takes a `name` argument

        logger = logging.getLogger(name) # Gets a logger instance named after the provided `name`

        logger.setLevel(logging.DEBUG) # Sets the logger's level to `DEBUG`, capturing all severity levels

        # Console handler configuration
        consale_handler = logging.StreamHandler() # Creates a stream handler that outputs to the console
        consale_handler.setLevel(logging.INFO) # Sets the console handler's level to `INFO`, filtering out DEBUG messages

        # File handler configuration
        file_handler = logging.FileHandler("MonitorModelSummary.txt") # Creates a file handler that writes to a log file (location not specified)
        file_handler.setLevel(logging.DEBUG) # Sets the file handler's level to `DEBUG`, capturing all severity levels

        # Formatter definition
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") # Defines a formatter string to format log messages
        #  - %(asctime)s: Timestamp when the message was logged
        #  - %(name)s: Name of the logger that logged the message
        #  - %(levelname)s: Severity level of the message (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        #  - %(message)s: The actual message content

        consale_handler.setFormatter(formatter) # Sets the formatter for the console handler
        file_handler.setFormatter(formatter) # Sets the formatter for the file handler

        # Adding handlers to the logger
        logger.addHandler(consale_handler) # Adds the console handler to the logger
        logger.addHandler(file_handler) # Adds the file handler to the logger

        return logger # Returns the configured logger instance