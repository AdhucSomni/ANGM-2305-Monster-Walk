class Camera:
    """Horizontal camera that follows the sprite along the x-axis"""

    def __init__(self, screen_width: int):
        self.screen_width = screen_width
        self.offset_x = 0

    def follow(self, target_rect):