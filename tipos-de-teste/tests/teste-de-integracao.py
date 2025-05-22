from tipos-de-teste.usuario-service import login_usuario.py

def test_integracao_login():
    assert login_usuario("joao@email.com", "1234") == "Login bem-sucedido"
    assert login_usuario("joao@email.com", "senhaerrada") == "Falha no login"
    print("Teste de integração entre cadastro e login passou!")

test_integracao_login()
