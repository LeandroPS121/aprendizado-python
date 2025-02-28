from models.usuario import Usuario
from models.livro import Livro

class BibliotecaController:
    def __init__(self) -> None:
        self.usuarios = []
        self.livros = []
    
    def cadastrar_usuario(self, id: int, nome: str, email: str) -> str:
        """
        Função para cadastrar usuário

        param1: id do usuário
        param2: nome do usuário
        param3: email do usuário
        """
        usuario = Usuario(id, nome, email)
        self.usuarios.append(usuario)
        return f"Usuário '{nome}' cadastrado com sucesso!"
    
    def adicionar_livro(self, id: int, titulo: str, autor: str) -> str:
        """
        Função para adicionar novo livro

        param1: id do livro
        param2: titulo do livro
        param3: autor do livro
        """
        livro = Livro(id, titulo, autor)
        self.livros.append(livro)
        return f"Livro '{titulo}' adicionado com sucesso!"
    
    def emprestar_livro(self, usuario_id: int, livro_id: int) -> function | None:
        """
        Função para emprestar livro

        param1: id do usuário
        param2: id do livro
        """
        usuario = next((u for u in self.usuarios if u.id == usuario_id), None)
        livro = next((l for l in self.livros if l.id == livro_id), None)

        if usuario and livro:
            return usuario.devolver_livro(livro)
        return "Erro: Usuário ou livro não encontrado."