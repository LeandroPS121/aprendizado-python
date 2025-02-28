class Livro:
    def __init__(self, titulo, autor, disponibilidade=True) -> None:
        self.titulo = titulo
        self.autor = autor
        self.disponibilidade = disponibilidade
    
    def emprestar(self) -> str:
        """
        Função para emprestar livros
        """
        if self.disponibilidade:
            self.disponibilidade = False
            return f"Livro '{self.titulo}' emprestado com sucesso!"
        return f"Livro '{self.titulo}' não está disponível para empréstimo."
    
    def devolver(self) -> str:
        """
        Função para devolver livros
        """
        self.disponibilidade = True
        return f"Livro '{self.titulo}' devolvido com sucesso!"