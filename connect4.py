import flet as ft

class Connect4(ft.Container):
    def __init__(self,page:ft.Page):
        super().__init__()
        
        self.expand = True
        page.theme_mode = ft.ThemeMode.DARK
        
        self.content = ft.ResponsiveRow(
            controls=[
                ft.Container(col=1,border=ft.border.all()),
                ft.Container(col=10,border=ft.border.all()),
                ft.Container(col=1,border=ft.border.all())
            ]
        )