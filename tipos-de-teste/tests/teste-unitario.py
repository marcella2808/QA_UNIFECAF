def test_cadastro_usuario():
    assert cadastrar_usuario("João", "18374829387", "joao@email.com", "1234") == "Usuário cadastrado com sucesso!"
    assert cadastrar_usuario("Maria", "8374", "maria@email.com", "abcdefgh") == "CPF deve conter 11 dígitos."
    assert cadastrar_usuario("Caroline", "47283748293", "caroline@email.com", "123") == "A senha deve ter pelo menos 4 dígitos."
    assert len(usuarios) == 1
    print("Teste unitário de cadastro de usuário passou!")

test_cadastro_usuario()
