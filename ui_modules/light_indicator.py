import flet as ft

class LightIndicator(ft.Container):
    def __init__(self):
        super().__init__()
        
        self.color_player_1 = ft.colors.BLUE_300
        self.color_player_2 = ft.colors.RED_300
        
        self.col = 1
        self.bgcolor = self.color_player_1
    
    
    def toggle(self):
        if self.bgcolor == self.color_player_1:
            self.bgcolor = self.color_player_2
        else:
            self.bgcolor = self.color_player_1