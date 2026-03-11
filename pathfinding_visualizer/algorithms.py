from queue import PriorityQueue, Queue, LifoQueue


def heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def a_star(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))

    came_from = {}

    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = heuristic(start.get_pos(), end.get_pos())

    open_hash = {start}

    while not open_set.empty():
        current = open_set.get()[2]
        open_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            return True

        for neighbor in current.neighbors:
            temp = g_score[current] + 1

            if temp < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp
                f_score[neighbor] = temp + heuristic(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False


def dijkstra(draw, grid, start, end):
    dist = {spot: float("inf") for row in grid for spot in row}
    dist[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))

    came_from = {}

    while not pq.empty():
        current = pq.get()[1]

        if current == end:
            reconstruct_path(came_from, end, draw)
            return True

        for neighbor in current.neighbors:
            temp = dist[current] + 1

            if temp < dist[neighbor]:
                dist[neighbor] = temp
                pq.put((temp, neighbor))
                came_from[neighbor] = current
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False


def bfs(draw, grid, start, end):
    q = Queue()
    q.put(start)

    came_from = {}
    visited = {start}

    while not q.empty():
        current = q.get()

        if current == end:
            reconstruct_path(came_from, end, draw)
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                q.put(neighbor)
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False


def dfs(draw, grid, start, end):
    stack = LifoQueue()
    stack.put(start)

    came_from = {}
    visited = {start}

    while not stack.empty():
        current = stack.get()

        if current == end:
            reconstruct_path(came_from, end, draw)
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                stack.put(neighbor)
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False
