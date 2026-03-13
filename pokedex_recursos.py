from pokemon_obj import Pokemon

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