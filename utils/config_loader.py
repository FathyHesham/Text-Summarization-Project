import yaml # Imports the `yaml` module for working with YAML files
from custom_logging.custom_logger import Customlogger # Imports the `Customlogger` class from the `custom_logging` module

# Create a logger instance using the custom logger class
logger = Customlogger.create_custom_logger("ConfigLoader") # Creates a logger named "ConfigLoader" for logging messages related to configuration loading

class ConfigLoader:
    def load_config(file_name="config.yaml"): # Defines a static method `load_config` with a default argument `file_name` set to "config.yaml"

        # Attempt to open and load the YAML file
        try:
            with open(file_name, "r") as file: # Opens the file in read mode ("r")
                config = yaml.safe_load(file) # Safely loads and parses the YAML content
                logger.info("Config file loaded successfully.") # Logs a success message
                return config # Returns the parsed configuration dictionary

        # Handle file not found exception
        except FileNotFoundError:
            logger.error(f"config file not found at {file_name}") # Logs an error message with the file path
            return None # Returns `None` to indicate an error

        # Handle YAML parsing errors
        except yaml.YAMLError as e:
            logger.error(f"error parsing config file: {e}") # Logs an error message with the exception details
            return None # Returns `None` to indicate an error