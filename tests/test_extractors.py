from .fixtures import *

def test_wget_broken_pipe(tmp_path, process):
    add_process = subprocess.run(['archivebox', 'add', 'http://127.0.0.1:8080/static/example.com.html'], capture_output=True)
    assert "TypeError chmod_file(..., path: str) got unexpected NoneType argument path=None" not in add_process.stdout.decode("utf-8")