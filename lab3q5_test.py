import lab3q5
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('42\n50\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab3q5.main()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip().find(f'too low') != -1
    assert captured_stdout.strip().find(f'2') != -1

def test_case2(monkeypatch, capsys):
  with open(f"lab3q5.py") as tf:
    head = [next(tf) for _ in range(12)]
    s = tf.read()
    assert(s.find("while") != -1 )

def test_case3(monkeypatch, capsys):
    number_inputs = StringIO('70\n60\n50\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab3q5.main()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip().find(f'too high') != -1
    assert captured_stdout.strip().find(f'3') != -1