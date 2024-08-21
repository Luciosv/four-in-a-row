import flet as ft

class LightIndicator(ft.Container):
    def __init__(self):
        super().__init__()
        
        self.color_player_1 = ft.colors.BLUE_300
        self.color_player_2 = ft.colors.RED_300
        
        self.col = 1
        self.bgcolor = self.color_player_1
        self.blur = 5
        
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors.AMBER_100,
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )
        
        self.border_radius = 10
    
    
    def toggle(self):
        if self.bgcolor == self.color_player_1:
            self.bgcolor = self.color_player_2
        else:
            self.bgcolor = self.color_player_1