class CarrinhoDeCompras:
    def __init__(self):
      self.itens = []

    def adicionar_item(self, item):
      self.itens.append(item)

    def excluir_item(self, item):
      self.itens.remove(item)

    def finalizar_compra(self):
        if self.itens:
            return "Compra finalizada com sucesso!"
        return "Carrinho vazio!"

