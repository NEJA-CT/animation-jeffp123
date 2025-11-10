import pyxel
import math

W, H = 320, 240
cx, cy = W // 2, H // 2

last_x, last_y = cx, cy

angle = 0.0
radius = 0.0

def update():
    global angle, radius
    angle += 0.1
    radius += 0.3
    if radius > min(W, H):
        radius = 0
        angle = 0

def draw():
    global last_x, last_y

    x = cx + radius * math.cos(angle)
    y = cy + radius * math.sin(angle)
    pyxel.line(x, y, last_x, last_y, 7)

    last_x = x
    last_y = y

pyxel.init(W, H, title="Pyxel Spiral Art")
pyxel.run(update, draw)


