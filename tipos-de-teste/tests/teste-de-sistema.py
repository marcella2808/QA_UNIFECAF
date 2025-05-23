def test_sistema_carrinho():
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Camiseta")
    carrinho.adicionar_item("Tênis")
    carrinho.adicionar_item("Short")
    carrinho.excluir_item("Tênis")
    assert len(carrinho.itens) == 2
    assert carrinho.finalizar_compra() == "Compra finalizada com sucesso!"
    print("Teste de sistema do carrinho de compras passou!")

test_sistema_carrinho()
