class Usuario():
    def __init__(self, id, nome, email) -> None:
        self.id = id
        self.nome = nome
        self.email = email
        self.livros_emprestados = []

    def pegar_livro(self, livro: str) -> str:
        """
        Função para pegar livro

        param1: nome do livro a ser emprestado
        """
        if livro.emprestar() == f"Livro '{livro.titulo}' emprestado com sucesso!":
            self.livros_emprestados.append(livro)
            return f"{self.nome} pegou o livro '{livro.titulo}'"
        return f"{self.nome} não pode pegar o livro '{livro.titulo}', ele não está disponível."
    
    def devolver_livro(self, livro: str) -> str:
        """
        Função para devolver livro

        param1: nome do livro a ser devolvido
        """
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
            return f"{self.nome} devolveu o livro '{livro.titulo}'."
        return f"{self.nome} não tem o livro '{livro.titulo}' para devolver."