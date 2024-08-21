import flet as ft


class ColumnSlot(ft.Container):
    def __init__(self,controls):
        super().__init__()
        
        self.content = ft.Column(
            expand=True,
            controls=controls,
            alignment=ft.MainAxisAlignment.END
        )
        
        self.bgcolor = "#5F6D62"
        self.expand = True

class Board(ft.Container):
    def __init__(self):
        super().__init__()
        
        self.bgcolor = "#131200"
        self.expand = True
        self.padding = 10
        
        self.discs = [[],[],[],[],[],[],[]]
        
        self.content = ft.Row(
            expand=True,
            controls=[
                ColumnSlot(self.discs[0]),
                ColumnSlot(self.discs[1]),
                ColumnSlot(self.discs[2]),
                ColumnSlot(self.discs[3]),
                ColumnSlot(self.discs[4]),
                ColumnSlot(self.discs[5]),
                ColumnSlot(self.discs[6])
            ]
        )