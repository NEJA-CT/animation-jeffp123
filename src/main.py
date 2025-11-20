import pyxel

W, H = 320, 240
pyxel.init(W, H, title="mario moves")

mario_image = pyxel.Image.from_image("../assets/mario.png")
pyxel.images[0] = mario_image

def draw_mario(mario_x, mario_y, mario_tile):
    mario_width = mario_image.width / 3
    pyxel.blt(
        mario_x, mario_y,  # position of Mario in the viewport
        0, # image id
        (mario_width * mario_tile) - 1, 0, # top-left pixel in the Mario image
        mario_width, mario_image.height, # width/height of the Mario image
    )

mario_frame = 0

def draw():
    pyxel.cls(0)
    draw_mario(30, 20, mario_frame)

def update():
    global mario_frame
    mario_frame = int(pyxel.frame_count / 4) % 3

pyxel.run(update, draw)


###

import math

def rotate(x, y, cx, cy, angle):
    s, c = math.sin(angle), math.cos(angle)
    x -= cx
    y -= cy
    return (
        cx + x * c - y * s,
        cy + x * s + y * c
    )

def draw_new():
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



# GRAVITY = 0.3
# BOUNCE = 0.7
# W, H = 320, 240


# # initial position and velocity
# x, y = W // 2, H // 2
# vx, vy = 0, 0


# pyxel.init(W, H, title="some title")

# mario_image = pyxel.Image.from_image(
#     "../assets/mario.png", incl_colors=False
# )
# pyxel.images[0] = pyxel.Image.from_image(
#     "../assets/mario.png", incl_colors=False
# )
# mario_width = mario_image.width / 3
# mario_height = mario_image.height

# distance = (W - mario_width) / 2

# mario_frame = 0
# mario_x = 0
# mario_y = (H - mario_height) / 2
# mario_dir = 1

# tri_rotation_angle = 0


# def update_prev():
#     global mario_frame, mario_x, mario_dir, tri_rotation_angle

#     f = pyxel.frame_count / 20
#     mario_x = distance + distance * math.sin(f)
#     mario_dir = 1 if math.cos(f) > 0 else -1

#     mario_frame = int(pyxel.frame_count / 4) % 3

#     tri_rotation_angle = (pyxel.frame_count * 0.2) % (2 * math.pi)

import math

def translate(point, tx, ty):
    x, y = point
    return x + tx, y + ty

def scale(point, sx, sy):
    x, y = point
    return x * sx, y * sy

def rotate(point, angle_radians):
    x, y = point
    c = math.cos(angle_radians)
    s = math.sin(angle_radians)
    return x*c - y*s, x*s + y*c



def mat_translate(tx, ty):
    return [
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1 ],
    ]

def mat_scale(sx, sy):
    return [
        [sx, 0,  0],
        [0,  sy, 0],
        [0,  0,  1],
    ]

def mat_rotate(a):
    c, s = math.cos(a), math.sin(a)
    return [
        [c, -s, 0],
        [s,  c, 0],
        [0,  0, 1],
    ]

def mat_mul(A, B):
    # Standard 3x3 multiplication
    M = [[0,0,0],[0,0,0],[0,0,0]]
    for r in range(3):
        for c in range(3):
            M[r][c] = sum(A[r][k] * B[k][c] for k in range(3))
    return M

def apply_matrix(M, point):
    x, y = point
    x2 = M[0][0]*x + M[0][1]*y + M[0][2]
    y2 = M[1][0]*x + M[1][1]*y + M[1][2]
    return x2, y2

M = mat_mul(mat_translate(80, 60),
    mat_mul(mat_rotate(math.pi / 2),
            mat_scale(2, 2)))

for point in points:
    apply_matrix(M, point)