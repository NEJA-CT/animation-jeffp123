import pyxel
import math


def rotate(x, y, cx, cy, angle):
    s, c = math.sin(angle), math.cos(angle)
    x -= cx
    y -= cy
    return (
        cx + x * c - y * s,
        cy + x * s + y * c
    )


GRAVITY = 0.3
BOUNCE = 0.7
W, H = 320, 240


# initial position and velocity
x, y = W // 2, H // 2
vx, vy = 0, 0


pyxel.init(W, H, title="some title")

mario_image = pyxel.Image.from_image(
    "../assets/mario.png", incl_colors=False
)
pyxel.images[0] = pyxel.Image.from_image(
    "../assets/mario.png", incl_colors=False
)
mario_width = mario_image.width / 3
mario_height = mario_image.height

distance = (W - mario_width) / 2

mario_frame = 0
mario_x = 0
mario_y = (H - mario_height) / 2
mario_dir = 1

tri_rotation_angle = 0


def update():
    global mario_frame, mario_x, mario_dir, tri_rotation_angle

    f = pyxel.frame_count / 20
    mario_x = distance + distance * math.sin(f)
    mario_dir = 1 if math.cos(f) > 0 else -1

    mario_frame = int(pyxel.frame_count / 4) % 3

    tri_rotation_angle = (pyxel.frame_count * 0.2) % (2 * math.pi)


def draw():
    pyxel.cls(0)
    # pyxel.circ(x, y, circ_radius, 10)  # the ball  # ground

    pyxel.blt(
        mario_x, mario_y, 0,
        mario_width * mario_frame, 0,
        mario_dir * (mario_width - 1), mario_height - 1
    )

    tri_center_x, tri_center_y = 25, 22  # TODO: Get actual center!
    tri_x1, tri_y1 = 20, 30
    tri_x2, tri_y2 = 10, 15
    tri_x3, tri_y3 = 30, 15

    tri_x1, tri_y1 = rotate(tri_x1, tri_y1, tri_center_x, tri_center_y, tri_rotation_angle)
    tri_x2, tri_y2 = rotate(tri_x2, tri_y2, tri_center_x, tri_center_y, tri_rotation_angle)
    tri_x3, tri_y3 = rotate(tri_x3, tri_y3, tri_center_x, tri_center_y, tri_rotation_angle)

    pyxel.tri(tri_x1, tri_y1, tri_x2, tri_y2, tri_x3, tri_y3, 7)


pyxel.run(update, draw)
