def test_tmp_path(tmp_path):
    print(type(tmp_path)) # pathlib.posixpath
    file = tmp_path / "file.txt" # /private/var/folders
    print(f"path in system {file}")
    file.write_text("hello")
    assert file.read_text() == "hello"
    

def test_tmp_path_factory(tmp_path_factory):
    print(type(tmp_path_factory)) 
    path = tmp_path_factory.mktemp("sub") # pathlib.posixpath
    print(type(path))
    file = path / "file.txt" # /private/var/folders
    print(f"path in system {file}")
    file.write_text("hello")
    assert file.read_text() == "hello"
