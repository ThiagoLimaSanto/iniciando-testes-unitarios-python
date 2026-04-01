from run import divisao, informacoes

def test_divisao():
    val = 8
    resp = divisao(val)
    assert resp == 4
    assert isinstance(resp, float)
    
def test_informacoes():
    resp = informacoes()
    
    assert isinstance(resp, dict)
    assert "name" in resp
    assert "age" in resp
    assert "is_ok" in resp