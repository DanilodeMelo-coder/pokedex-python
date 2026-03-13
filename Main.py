from pokedex_recursos import Pokedex
from menu import Menu
#from pokemon_obj import Pokemon

#entrada do user para escolher uma opção do menu
def entrada_user():
    resposta_user = input("Escolha uma Opção: ")

    return resposta_user

#função que executa tudo
def executar():
    pokedex = Pokedex()
    menu = Menu(pokedex)

    while True:
        menu.mostrar_menu()

        resposta_user = entrada_user()

        acao = menu.acao_entrada(resposta_user)

        acao()

        

executar()

