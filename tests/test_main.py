from app.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello, Python Template!" in captured.out
