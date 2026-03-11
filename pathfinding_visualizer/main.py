import pygame

from algorithms import a_star, bfs, dfs, dijkstra
from grid import make_grid, generate_maze, get_clicked_pos, draw
from settings import WIDTH, ROWS, FPS, WINDOW_TITLE


def main():
    pygame.init()
    pygame.font.init()

    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption(WINDOW_TITLE)

    grid = make_grid(ROWS, WIDTH)

    start = None
    end = None

    algorithm = "A*"

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        draw(win, grid, ROWS, WIDTH, algorithm)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    algorithm = "A*"

                if event.key == pygame.K_2:
                    algorithm = "BFS"

                if event.key == pygame.K_3:
                    algorithm = "DFS"

                if event.key == pygame.K_4:
                    algorithm = "Dijkstra"

                if event.key == pygame.K_m:
                    generate_maze(grid)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, WIDTH)

                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    if algorithm == "A*":
                        a_star(lambda: draw(win, grid, ROWS, WIDTH, algorithm), grid, start, end)

                    elif algorithm == "BFS":
                        bfs(lambda: draw(win, grid, ROWS, WIDTH, algorithm), grid, start, end)

                    elif algorithm == "DFS":
                        dfs(lambda: draw(win, grid, ROWS, WIDTH, algorithm), grid, start, end)

                    elif algorithm == "Dijkstra":
                        dijkstra(lambda: draw(win, grid, ROWS, WIDTH, algorithm), grid, start, end)

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            row, col = get_clicked_pos(pos, ROWS, WIDTH)
            spot = grid[row][col]

            if not start:
                start = spot
                start.make_start()

            elif not end and spot != start:
                end = spot
                end.make_end()

            elif spot != end and spot != start:
                spot.make_barrier()

        elif pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            row, col = get_clicked_pos(pos, ROWS, WIDTH)
            spot = grid[row][col]

            spot.reset()

            if spot == start:
                start = None

            if spot == end:
                end = None

    pygame.quit()


if __name__ == "__main__":
    main()
