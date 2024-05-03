# RubicsCube
# Author: Bence Fulop

class RubicsCube:
    def __init__(self):
        self.front = ['ULW', 'URW', 'DLW', 'DRW']  # Up Left White, Up Right White, Down Left White, Down Right White
        self.back = ['ULG', 'URG', 'DLG', 'DRG']   # Up Left Green, Up Right Green, Down Left Green, Down Right Green
        self.left = ['ULY', 'URY', 'DLY', 'DRY']   # Up Left Yellow, Up Right Yellow, Down Left Yellow, Down Right Yellow
        self.right = ['ULO', 'URO', 'DLO', 'DRO']  # Up Left Orange, Up Right Orange, Down Left Orange, Down Right Orange
        self.up = ['ULP', 'URP', 'DLP', 'DRP']     # Up Left Purple, Up Right Purple, Down Left Purple, Down Right Purple
        self.down = ['ULR', 'URR', 'DLR', 'DRR']   # Up Left Red, Up Right Red, Down Left Red, Down Right Red


if __name__ == "__main__":
    cube = RubicsCube()
    print("Front:", cube.front)
    print("Back:", cube.back)
    print("Left:", cube.left)
    print("Right:", cube.right)
    print("Up:", cube.up)
    print("Down:", cube.down)
