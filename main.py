from camera import Camera
import pygame

WIDTH = 500
HEIGHT = 500

camera = Camera(500, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

point_pos_list = [
    # (0, 0, 0),
    # (90, 0, 0),
    # (90, 90, 0),
    # (0, 90, 0),
    # (0, 0, 90),
    # (90, 0, 90),
    # (90, 90, 90),
    # (0, 90, 90),
    (100, 0, 0),
    (0, 100, 0),
    (0, 0, 100)
]
point_pos_screens = []

for point_pos in point_pos_list:
    point_pos_screens.append(camera.get_point_position(point_pos, WIDTH, HEIGHT))

while running:
    dt = clock.tick(60)/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    camera.update()

    camera.turn(dt, 0.5)
    window.fill((0, 0, 0))


    # pygame.draw.line(window, (255, 255, 255), (camera.x - 500 + WIDTH / 2, camera.y - 500 * camera.m + WIDTH / 2), (500 + camera.x + WIDTH / 2, camera.y + 500 * camera.m + WIDTH/2), 10)
    # normal_x, normal_y, _ = camera.get_normal()
    # pygame.draw.line(window, (255, 255, 255), (camera.x + WIDTH/2, camera.y + WIDTH/2), (camera.x + WIDTH/2 + normal_x*100, camera.y + WIDTH/2 + normal_y*100))

    for i, point_pos in enumerate(point_pos_list):
        point_pos_screens[i] = camera.get_point_position(point_pos, WIDTH, HEIGHT)

    for i, point_pos_screen in enumerate(point_pos_screens):
        pygame.draw.rect(window, (255, 255, 255), (point_pos_screen[0] + WIDTH/3, point_pos_screen[1] + HEIGHT/3, 5, 5))

    for i in range(len(point_pos_screens)):
        for j in range(len(point_pos_screens)):
            pygame.draw.line(window, (255, 255, 255), (point_pos_screens[i][0] + WIDTH/3, point_pos_screens[i][1] + HEIGHT/3), (point_pos_screens[j][0] + WIDTH/3, point_pos_screens[j][1] + HEIGHT/3))


    pygame.display.update()


pygame.quit()