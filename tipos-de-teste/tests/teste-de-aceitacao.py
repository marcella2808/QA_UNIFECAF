from tipos-de-teste.usuario-service import cadastrar_usuario, login_usuario
from tipos-de-teste.Carrinho import Carrinho

def test_aceitacao_fluxo_completo():
    assert cadastrar_usuario("Maria", "12345678910", "maria@email.com", "abcd") == "Usuário cadastrado com sucesso!"
    assert login_usuario("maria@email.com", "abcd") == "Login bem-sucedido"
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Calça")
    carrinho.adicionar_item("Tênis")
    carrinho.excluir_item("Calça")
    assert carrinho.finalizar_compra() == "Compra finalizada com sucesso!"
    print("Teste de aceitação do fluxo completo passou!")

test_aceitacao_fluxo_completo()
