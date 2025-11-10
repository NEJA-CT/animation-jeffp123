import pyxel
import math

W, H = 160, 120
cx, cy = W // 2, H // 2

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
    # pyxel.cls(0)

    x = cx + radius * math.cos(angle)
    y = cy + radius * math.sin(angle)
    pyxel.pset(x, y, 7)

pyxel.init(W, H, title="Pyxel Spiral Art")
pyxel.run(update, draw)


