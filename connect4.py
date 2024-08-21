import flet as ft

from ui_modules.light_indicator import LightIndicator
from ui_modules.board import Board

class Connect4(ft.Container):
    def __init__(self,page:ft.Page):
        super().__init__()
        
        self.expand = True
        page.theme_mode = ft.ThemeMode.DARK
        
        self.content = ft.Row(
            expand=True,
            controls=[
                LightIndicator(),
                Board(),
                LightIndicator()
            ]
        )