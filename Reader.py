
"""
======================
= Informal interface =
======================

Reader interface

"""

class ReaderInterface:

    def get_data_source(self, path: str, file_name: str) -> str:
        """
        :param path:
        :param file_name:
        :return:
        """
        pass

    def extract_data_text(self, full_file_path: str) -> dict:
        """
        :param full_file_path:
        :return:
        """
        pass
