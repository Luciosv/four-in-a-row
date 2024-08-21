import flet as ft

from ui_modules.light_indicator import LightIndicator

class Connect4(ft.Container):
    def __init__(self,page:ft.Page):
        super().__init__()
        
        self.expand = True
        page.theme_mode = ft.ThemeMode.DARK
        
        self.content = ft.ResponsiveRow(
            controls=[
                LightIndicator(),
                ft.Container(col=10,border=ft.border.all()),
                LightIndicator()
            ]
        )