import subprocess
import cards
from typer.testing import CliRunner

def test_version_v1():
    process = subprocess.run(["cards", "version"], capture_output=True, text=True)
    output = process.stdout.rstrip()
    print(output)
    assert output == cards.__version__

def test_version_v2(capsys):
    print(f"this is capsys: {capsys}")
    cards.cli.version()
    output = capsys.readouterr().out.split("\n")
    print(f"this is the stdout: {output}")
    assert output[1] == cards.__version__

def test_version_v3():
    runner = CliRunner()
    result = runner.invoke(cards.app, ["version"])
    output = result.output.rstrip()
    assert output == cards.__version__
