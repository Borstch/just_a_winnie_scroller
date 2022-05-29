from pathlib import Path


ASSETS_ROOT = Path("./assets")
ICON_PATH = ASSETS_ROOT / "icons" / "honey.png"
BG_PATH = ASSETS_ROOT / "images" / "bg.png"
MENU_BG_PATH = ASSETS_ROOT / "images" / "bg.png"
MENU_BUTTON_PATH = ASSETS_ROOT / "images" / "button.png"
HONEY_SPRITE_PATH = ASSETS_ROOT / "images" / "honey.png"
PLAYER_SPRITES_PATH = list((ASSETS_ROOT / "images").glob("winnie*.png"))
BEE_SPRITES_PATH = list((ASSETS_ROOT / "images").glob("bee*.png"))
ANGRY_BEE_SPRITES_PATH = list((ASSETS_ROOT / "images").glob("angry_bee*.png"))

MAIN_MENU_THEME_PATH = ASSETS_ROOT / "sound" / "main_menu_theme.mp3"
GAME_OVER_SOUND_PATH = ASSETS_ROOT / "sound" / "balloon.mp3"
HONEY_PICKING_SOUND_PATH = ASSETS_ROOT / "sound" / "eat.mp3"
BACKGROUND_SOUND_PATH = ASSETS_ROOT / "sound" / "bg.mp3"

GAME_TITLE = "JustAWinnieScroller"
SCREEN_SIZE = 400, 640

FRAME_RATE = 60

MOVEMENT_SPEED = 3.5
SCROLLING_SPEED = 1.75
MAX_SCROLLING_SPEED = 4
SCROLLING_COEF = 1.11
