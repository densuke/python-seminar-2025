import pytest
import tempfile
import os

@pytest.fixture
def temp_file():
    # --- 準備 (テスト前) ---
    fp = tempfile.NamedTemporaryFile(mode='w+', delete=False)
    file_path = fp.name
    fp.close()
    yield file_path # テストにファイルパスを渡す
    # --- 後片付け (テスト後) ---
    os.remove(file_path)

def test_read_write_file(temp_file):
    # temp_fileには、yieldされたファイルパスが入る
    with open(temp_file, 'w') as f:
        f.write("hello")
    with open(temp_file, 'r') as f:
        assert f.read() == "hello"
