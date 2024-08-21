import flet as ft
from connect4 import Connect4

def main(page : ft.Page):
    game = Connect4(page)
    page.add(game)


ft.app(target=main)