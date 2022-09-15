def test_normal(capsys):
    print("\nnormal print")
    print(capsys.readouterr().out)


def test_fail():
    """This test will always show output,
    because it fails.
    """
    print("\nPrint in failing test")
    assert True
    # assert False

def test_disabled(capsys):
    """This print will always show"""
    with capsys.disabled():
        print("holi my babies")
