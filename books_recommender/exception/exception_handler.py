import os
import sys


class AppException(Exception):
    """
    Organization: iNeuron Intelligence Private Limited
    AppException is customized exception class designed to capture refined details about exception
    such as python script file line number along with error message
    With custom exception one can easily spot source of error and provide quick fix.
    """

    def __init__(self, error_message: Exception, error_detail: sys):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)
        self.error_message = AppException.error_message_detail(
            error_message, error_detail=error_detail
        )

    @staticmethod
    def error_message_detail(error: Exception, error_detail: sys):
        """
        error: Exception object raised from module
        error_detail: sys module contains detail information about system execution.
        """
        _, _, exc_tb = error_detail.exc_info()
        # extracting file name from exception traceback
        file_name = exc_tb.tb_frame.f_code.co_filename

        # preparing error message
        error_message = (
            f"Error occurred python script name [{file_name}]"
            f" line number [{exc_tb.tb_lineno}] error message [{error}]."
        )

        return error_message

    def __repr__(self):
        """
        Formatting object of AppException
        """
        return AppException.__name__.__str__()

    def __str__(self):
        """
        Formatting how an object should be visible if used in print statement.
        """
        return self.error_message


# ✅ Quick test block (only runs if you execute this file directly)
if __name__ == "__main__":
    try:
        print("Testing AppException...")
        x = 1 / 0  # deliberate error
    except Exception as e:
        raise AppException(e, sys)
