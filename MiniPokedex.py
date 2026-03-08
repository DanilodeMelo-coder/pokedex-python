class Pokemon:
    def __init__(self, nome, hp, tipo, nivel):
        self.nome = nome
        self.hp = hp
        self.tipo = tipo
        self.nivel = nivel

    #retorna os atributos da classe pokemon de uma forma mais limpa e organizada como Str
    def __str__(self):
        return f"{self.nome} | Tipo: {self.tipo} | HP: {self.hp} | Nivel: {self.nivel}"

class Pokedex:
    #iniciar pokedex
    def __init__(self):
        self.pokemons = []

    #adicionar pokemon (input- Nome, Hp, Tipo, Nivel)
    def adicionar_pokemon(self,nome_pk, hp_pk, tipo_pk, nivel_pk):

        pokemon_adicionado = Pokemon(nome_pk, hp_pk, tipo_pk, nivel_pk)
        pokemon_nome = nome_pk
        
        #retorna o Objeto Pokemon e o nome do Pokemon
        return pokemon_nome, pokemon_adicionado

    #listar pokemon
    def listar_pokemons(self):
        for pokemon in self.pokemons:
            print(pokemon)

    #buscar pokemon pelo nome (input- nome do pokemon)
    def buscar_pokemon(self, nome_pk):

        for pokemon in self.pokemons:
            #se pokemon.nome for = nome digitado
            if pokemon.nome == nome_pk:
                #retorne pokemon
                return pokemon
            
            #se nao, retorne None
            return None

    #mostrar detalhes do pokemon, pelo nome
    def mostrar_detalhes(self, nome_pk):
        
        for pokemon in self.pokemons:
            if pokemon.nome == nome_pk:

                return pokemon

            return None


#menu inicial
def menu():
    print("1- Adicionar Pokemon")
    print("2- Exibir pokemons")
    print("3- Buscar Pokemon")
    print("4- Exibir informações do Pokemon")
    print("5- Sair")

#entrada do user para escolher uma opção do menu
def entrada_user():
    resposta_user = input("Escolha uma Opção: ")

    return resposta_user

#função que executa tudo
def executar():
    pokedex = Pokedex()

    while True:
        menu()

        resposta_user = entrada_user()

        if resposta_user == "1":
            nome_pk = input("Adicione o nome do pokemon: ")
            hp_pk = input("Adicione o hp do pokemon: ")
            tipo_pk = input("Adicione o tipo do pokemon: ")
            nivel_pk = input("Adicione o nivel do pokemon: ")

            pokemon_adicionado_nome, pokemon_adicionado = pokedex.adicionar_pokemon(nome_pk, hp_pk, tipo_pk, nivel_pk)
            pokedex.pokemons.append(pokemon_adicionado)

            print("-------------------------------------------")
            print(f"{pokemon_adicionado_nome} adicionado com sucesso a Pokedéx")
            print("-------------------------------------------")

        elif resposta_user == "2":
            print("----------------------POKEDEX----------------------")
            pokedex.listar_pokemons()
            print("---------------------------------------------------")

        elif resposta_user == "3":
            nome_pk = input("Digite o nome do pokemon: ").lower().strip()

            pokemon = pokedex.buscar_pokemon(nome_pk)

            if pokemon:
                print("----------------------POKEDEX----------------------")
                print(f"{nome_pk} ja esta registrado na pokedex")
                print("---------------------------------------------------")
            
            else:
                print(f"{nome_pk} ainda não esta registrado na pokedex")

        elif resposta_user == "4":
            nome_pk = input("Digite o nome do pokemon que busca: ")

            pokemon = pokedex.mostrar_detalhes(nome_pk)

            if pokemon is not None:
                print("----------------------POKEDEX----------------------")
                print(pokemon)
                print("---------------------------------------------------")
            
            else:
                print("----------------------POKEDEX----------------------")
                print("Pokemon não encontrado")
                print("---------------------------------------------------")

        elif resposta_user == "5":
            break



executar()




# pokedex = Pokedex()

# Pikachu = Pokemon("Pikachu", 70, "eletrico", 13)
# Charmander = Pokemon("Charmander", 70, "Fogo", 15)

# Pokedex.adicionar_pokemon(pokedex, "Pikachu")
# Pokedex.adicionar_pokemon(pokedex, "Charmander")

# Pokedex.listar_pokemons(pokedex)