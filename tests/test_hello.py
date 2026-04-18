from hello.hello import print_message


def test_print_message(capsys):
    """Ensure print_message writes the given message to stdout."""
    print_message("hi")
    captured = capsys.readouterr()
    assert captured.out.strip() == "hi"
