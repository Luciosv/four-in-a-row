import flet as ft

class PointCounter(ft.Row):
    def __init__(self,color):
        super().__init__()
        
        self.expand = True
        self.alignment = ft.MainAxisAlignment.CENTER
        
        self.counter = ft.Text("0")
        
        self.controls = [
            ft.Icon(
                ft.icons.PERSON,
                color=color
            ),
            self.counter
        ]


class GameLogo(ft.Container):
    def __init__(self):
        super().__init__()
        
        self.width = 40
        self.height = 40
        self.border_radius = 40
        self.border = ft.border.all(color="#5F6D62")
        
        self.content = ft.Icon(
            ft.icons.GRID_VIEW_ROUNDED,
            expand=True,
            color="#5F6D62"
        )

class AppBar(ft.Container):
    def __init__(self):
        super().__init__()
        
        self.height = 50
        self.padding = 10
        self.border_radius = 30
        self.border = ft.border.all(color="#FCFAFA")
        
        self.content = ft.Row(
            expand=True,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                PointCounter("#1446A3"),
                GameLogo(),
                PointCounter("#D14D74")
            ]
        )