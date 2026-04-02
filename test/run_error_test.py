import pytest
from run import func_erro, divisao

def test_error():
    try:
        func_erro()
    except Exception as e:
        assert str(e) == "Meu erro está aqui!"
        
def test_error_with_pytest():
    with pytest.raises(Exception):
        divisao(4)