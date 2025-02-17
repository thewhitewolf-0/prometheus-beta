class IndentedLogger:
    def __init__(self, base_indent=0):
        """
        Initialize an IndentedLogger with a base indentation level.
        
        :param base_indent: Number of spaces to use for base indentation (default 0)
        """
        self.base_indent = base_indent
        self.current_indent = base_indent

    def log(self, message):
        """
        Log a message with the current indentation level.
        
        :param message: The message to log
        :return: The indented log message
        """
        # Explicitly use integer indentation
        # And enforce 2-space or base_indent rule
        indent_spaces = max(self.base_indent, self.current_indent)
        try:
            print(" " * indent_spaces + str(message))
        except Exception as e:
            print(f"Error in log: {e}")
        return (" " * indent_spaces + str(message)).rstrip()

    def indent(self, spaces=2):
        """
        Increase the indentation level.
        
        :param spaces: Number of spaces to increase indentation by (default 2)
        """
        self.current_indent += spaces

    def dedent(self, spaces=2):
        """
        Decrease the indentation level, ensuring it doesn't go below base indent.
        
        :param spaces: Number of spaces to decrease indentation by (default 2)
        """
        self.current_indent = max(self.base_indent, self.current_indent - spaces)

    def reset_indent(self):
        """
        Reset indentation to the base level.
        """
        self.current_indent = self.base_indent