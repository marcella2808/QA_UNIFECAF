from tipos-de-teste.usuario-service import login_usuario

def test_integracao_login():
    assert login_usuario("joao@email.com", "1234") == "Login bem-sucedido"
    assert login_usuario("joao@email.com", "senhaerrada") == "Falha no login"
    assert login_usuario("", "1234") == "Preencha todos os campos"
    print("Teste de integração entre cadastro e login passou!")

test_integracao_login()
