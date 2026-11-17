# tiny-chess-01 — V5

A 4KB Python chess engine for the make.fun tiny-chess-01
competition (deadline 2026-11-24T17:00:00Z).

- `main.py` is the whole engine: 0x88 board, alpha-beta with
  transposition table, PVS, killer moves, history heuristic,
  RFP, null-move pruning and quiescence search.
- PeSTO-style tapered eval: precomputed MG/EG tables with
  incremental mg/eg/phase updates in the move function,
  so evaluation is O(1) per node.
- Iterative deepening to depth 8, 55,000 nodes per move.
- Practice trial-0: Elo 1451 (4 wins, 0 draws, 2 losses;
  beat depth-2/3/4 and nodes-100k, lost to nodes-250k/500k).
  Slowest single move 6.5s, no timeouts.
- Practice trial-1: Elo 1545 (4 wins, 1 draw, 1 loss;
  beat depth-2/3/4 and nodes-100k, drew nodes-250k,
  lost to nodes-500k). Slowest single move 7.4s, no timeouts.
  (Revised version: node budget BG 55000 -> 60000.)
- House baseline ~1325 Elo.

License: MIT (see LICENSE).
