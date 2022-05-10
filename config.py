from pathlib import Path


ASSETS_ROOT = Path("./assets")
ICON_PATH = ASSETS_ROOT / "icons" / "honey.png"
BG_PATH = ASSETS_ROOT / "images" / "bg.png"
MENU_BG_PATH = ASSETS_ROOT / "images" / "bg.png"
MENU_BUTTON_PATH = ASSETS_ROOT / "images" / "button.png"
HONEY_SPRITE_PATH = ASSETS_ROOT / "images" / "honey.png"
PLAYER_SPRITES_PATH = list((ASSETS_ROOT / "images").glob("winnie*.png"))
BEE_SPRITES_PATH = list((ASSETS_ROOT / "images").glob("bee*.png"))

GAME_TITLE = "JustAWinnieScroller"
SCREEN_SIZE = 400, 640

FRAME_RATE = 30
MOVEMENT_SPEED = 7
HONEY_PROBABILITY = 0.4

SCROLLING_SPEED = 2.5
MAX_SCROLLING_SPEED = 8
SCROLLING_COEF = 1.2
