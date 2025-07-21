import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    """Base class for all network security exceptions."""
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()

        if exc_tb is not None:
            self.file_name = exc_tb.tb_frame.f_code.co_filename
            self.line_no = exc_tb.tb_lineno
        else:
            self.file_name = "Unknown"
            self.line_no = -1

    def __str__(self):
        return f"Error occurred in file {self.file_name} at line {self.line_no}: {self.error_message}"
        self.file_name,self.line_no ,str(self.error_message)

# Testing
if __name__ == "__main__":
    try:
        logger.logging.info("Testing NetworkSecurityException")
        a=1 / 0  # 🔥 Actual error
        print(a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
