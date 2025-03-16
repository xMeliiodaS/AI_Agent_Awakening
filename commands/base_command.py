import logging
from abc import ABC, abstractmethod


class BaseCommand:
    def __init__(self, **kwargs):
        """
        Initialize the command with any required parameters.
        """
        self.params = kwargs  # Store command parameters
        self.description = self.__class__.__name__  # Default to class name
        self.validate_params()  # Validate required parameters before execution

    def set_params(self, **kwargs):
        """
        Sets the parameters dynamically for the command.
        """
        self.params.update(kwargs)  # Updates the params with new values

    @abstractmethod
    def execute_command(self):
        """
        Abstract method to be implemented by subclasses to execute the command.
        """
        pass

    def undo_command(self):
        """
        Undo the command (optional, can be overridden by subclasses).
        """
        logging.warning(f"Undo not implemented for {self.description}")

    def validate_params(self):
        """
        Ensure all required parameters are provided.
        """
        required_params = getattr(self, "required_params", [])
        missing_params = [param for param in required_params if param not in self.params]

        if missing_params:
            raise ValueError(f"Missing required parameters for {self.description}: {missing_params}")
