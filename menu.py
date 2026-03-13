from pokedex_recursos import Pokedex

pokedex = Pokedex()

class Menu():
    def __init__(self, pokedex):
        self.pokedex = pokedex
        self.opcoes = {
            "1": self.adicionar_pokemon,
            "2": self.listar_pokemons,
            "3": self.buscar_pokemon,
            "4": self.mostrar_detalhes,
            "5": self.sair
        }

    def mostrar_menu(self):
        print("1- Adicionar Pokemon")
        print("2- Exibir pokemons")
        print("3- Buscar Pokemon")
        print("4- Exibir informações do Pokemon")
        print("5- Sair")

    def acao_entrada(self, resposta_user):
        acao = self.opcoes.get(resposta_user)

        return acao
    
    def adicionar_pokemon(self):

        nome_pk = input("Adicione o nome do pokemon: ")
        hp_pk = input("Adicione o hp do pokemon: ")
        tipo_pk = input("Adicione o tipo do pokemon: ")
        nivel_pk = input("Adicione o nivel do pokemon: ")

        self.pokedex.adicionar_pokemon(nome_pk, hp_pk, tipo_pk, nivel_pk)

        pokemon_adicionado_nome, pokemon_adicionado = pokedex.adicionar_pokemon(nome_pk, hp_pk, tipo_pk, nivel_pk)
        pokedex.pokemons.append(pokemon_adicionado)

        return pokemon_adicionado_nome

    def listar_pokemons(self):
        self.pokedex.listar_pokemons()

        return pokedex.listar_pokemons()

    def buscar_pokemon(self):

        nome_pk = input("Digite o nome do pokemon: ").lower().strip()

        self.pokedex.buscar_pokemon(nome_pk)

        pokemon = pokedex.buscar_pokemon(nome_pk)

        return pokemon

    def mostrar_detalhes(self):

        nome_pk = input("Digite o nome do pokemon que busca: ")

        self.pokedex.mostrar_detalhes(nome_pk)

        pokemon = pokedex.mostrar_detalhes(nome_pk)

        return pokemon

    def sair(self):
        exit()