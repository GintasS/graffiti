import pytest
from pathlib import Path
import os
import os.path as pathh
from secrets import token_urlsafe
import GraffLibAPI.utils.file_helper as FileHelperClass

def test_get_current_directory():
    test_directory = os.path.join(str(Path.cwd()), "GraffLibAPI", "static", "markers", "123")
    result_directory = FileHelperClass.get_current_directory("123")
    assert result_directory == test_directory