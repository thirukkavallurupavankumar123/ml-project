import sys
from src logger import logging


def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: {file_name} at line number: {line_number} with message: {str(error)}"
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message
        



