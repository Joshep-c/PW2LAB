WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTGRAY = (200, 200, 200)
GRAY = (127, 127, 127)
DARKGRAY = (50, 50, 50)
BLUE = (0, 0, 255)
TRANSPARENT = (0, 0, 0, 0)

color = {
  '_': LIGHTGRAY,
  '=': GRAY,
  '.': WHITE,
  '@': BLACK,
  '#': DARKGRAY,
  ' ': TRANSPARENT,
}
inverter = {
  '_': '=',
  '=': '_',
  '.': '@',
  '@': '.',
}