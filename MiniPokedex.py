class Pokemon:
    def __init__(self, nome, hp, tipo, nivel):
        self.nome = nome
        self.hp = hp
        self.tipo = tipo
        self.nivel = nivel

    def __str__(self):
        return f"{self.nome} | Tipo: {self.tipo} | HP: {self.hp} | Nivel: {self.nivel}"

class Pokedex:
    def __init__(self):
        self.pokemons = []

    def adicionar_pokemon(self):

        nome_pk = input("Adicione o nome do pokemon: ")
        hp_pk = input("Adicione o hp do pokemon: ")
        tipo_pk = input("Adicione o tipo do pokemon: ")
        nivel_pk = input("Adicione o nivel do pokemon: ")

        dados = nome_pk, hp_pk, tipo_pk, nivel_pk
        return dados

    def listar_pokemons(self):
        for pokemon in self.pokemons:
            print(pokemon)
    
    def buscar_pokemon(self):
        ...
    
    def mostrar_detalhes(self, nome):
        ...


def menu():
    print("1- Adicionar Pokemon")
    print("2- Exibir pokemons")
    print("3- Buscar Pokemon")
    print("4- Exibir informações do Pokemon")
    print("5- Sair")

def entrada_user():
    resposta_user = input("Escolha uma Opção: ")

    return resposta_user


def executar():
    pokedex = Pokedex()

    while True:
        menu()

        resposta_user = entrada_user()

        if resposta_user == "1":

            nome_pk, hp_pk, tipo_pk, nivel_pk = pokedex.adicionar_pokemon()

            pokemon_nome = Pokemon(nome_pk, hp_pk, tipo_pk, nivel_pk)

            pokedex.pokemons.append(pokemon_nome)

        elif resposta_user == "2":
            pokedex.listar_pokemons()

        elif resposta_user == "5":
            break



executar()




# pokedex = Pokedex()

# Pikachu = Pokemon("Pikachu", 70, "eletrico", 13)
# Charmander = Pokemon("Charmander", 70, "Fogo", 15)

# Pokedex.adicionar_pokemon(pokedex, "Pikachu")
# Pokedex.adicionar_pokemon(pokedex, "Charmander")

# Pokedex.listar_pokemons(pokedex)