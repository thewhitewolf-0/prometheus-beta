class IndentedLogger:
    def __init__(self, base_indent=0):
        """
        Initialize an IndentedLogger with a base indentation level.
        
        :param base_indent: Number of spaces to use for base indentation (default 0)
        """
        self.base_indent = base_indent
        self.current_indent = base_indent
        self.indent_cache = 0

    def log(self, message):
        """
        Log a message with the current indentation level.
        
        :param message: The message to log
        :return: The indented log message
        """
        # Use the cached indent to ensure consistent indentation
        current_indent = max(self.base_indent, self.indent_cache)
        indented_message = " " * current_indent + str(message)
        print(indented_message)
        return indented_message

    def indent(self, spaces=2):
        """
        Increase the indentation level.
        
        :param spaces: Number of spaces to increase indentation by (default 2)
        """
        self.indent_cache += spaces

    def dedent(self, spaces=2):
        """
        Decrease the indentation level, ensuring it doesn't go below base indent.
        
        :param spaces: Number of spaces to decrease indentation by (default 2)
        """
        self.indent_cache = max(self.base_indent, self.indent_cache - spaces)

    def reset_indent(self):
        """
        Reset indentation to the base level.
        """
        self.indent_cache = self.base_indent