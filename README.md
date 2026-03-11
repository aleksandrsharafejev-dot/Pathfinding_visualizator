# Pathfinding Visualizer

A small Pygame app that visualizes common pathfinding algorithms.

## Run

1. Install dependencies:

```bash
pip install pygame
```

2. Start the app:

```bash
python pathfinding_visualizer/main.py
```

## Controls

- `Left mouse` — place start, end, and walls
- `Right mouse` — erase a cell
- `1` — A*
- `2` — BFS
- `3` — DFS
- `4` — Dijkstra
- `M` — generate a random maze
- `C` — clear the grid
- `SPACE` — run the selected algorithm

## Project Structure

- `main.py` — entry point
- `algorithms.py` — A*, BFS, DFS, Dijkstra
- `node.py` — `Spot` class
- `grid.py` — grid, rendering, helpers
- `/colors.py` — colors
- `settings.py` — window settings
- `astar.py` — compatibility entry (runs `main`)

## Notes

- Algorithms allow diagonal moves.
- For a clean run, press `C` before starting a new algorithm.
