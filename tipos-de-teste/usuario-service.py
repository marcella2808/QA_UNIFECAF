usuarios = []

def cadastrar_usuario(nome, cpf, email, senha):
    if len(cpf) != 11:
        return "CPF deve conter 11 dígitos."
    if len(senha) < 4:
        return "A senha deve ter pelo menos 4 dígitos."
    usuarios.append({'nome': nome, 'cpf': cpf, 'email': email, 'senha': senha})
    return "Usuário cadastrado com sucesso!"

def login_usuario(email, senha):
  if not email or not senha:
    return "Preencha todos os campos"
  for usuario in usuarios:
    if usuario['email'] == email and usuario['senha'] == senha:
        return "Login bem-sucedido"
  return "Falha no login"

