class Pokemon:
    def __init__(self, nome, hp, tipo, nivel):
        self.nome = nome
        self.hp = hp
        self.tipo = tipo
        self.nivel = nivel

    #retorna os atributos da classe pokemon de uma forma mais limpa e organizada como Str
    def __str__(self):
        return f"{self.nome} | Tipo: {self.tipo} | HP: {self.hp} | Nivel: {self.nivel}"
