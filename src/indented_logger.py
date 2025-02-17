import sys

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
        current_indent = max(self.base_indent, self.current_indent)
        
        # Override sys.stdout to ensure our exact spaces are printed
        orig_stdout = sys.stdout
        sys.stdout = type('IndentWrapper', (object,), {
            'write': lambda self, x: orig_stdout.write(" " * current_indent + x if x.strip() else x),
            'flush': orig_stdout.flush
        })()
        
        print(str(message))
        sys.stdout = orig_stdout
        
        return " " * current_indent + str(message)

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