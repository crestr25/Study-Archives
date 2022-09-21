import os
from ch4.hello_world import hello


def test_no_fixtures():
    # hello()
    with open("hello.txt", "r") as f:

        assert f.read() == "Hello World!\n"

def test_fixtures(monkeypatch, tmp_path):
    print(f"tmp_path is now located in {tmp_path}")
    monkeypatch.chdir(tmp_path)
    
    test_no_fixtures()
    print(os.listdir(tmp_path))
