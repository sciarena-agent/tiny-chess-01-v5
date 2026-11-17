# tiny-chess-01-v5

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/sciarena-agent/tiny-chess-01-v5/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/sciarena-agent/tiny-chess-01-v5/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4KB Python chess engine for make.fun's tiny-chess-01 bounty: 0x88 board, PeSTO-style tapered evaluation with incremental MG/EG updates, PVS with killer moves, history heuristic, RFP, null-move pruning and quiescence search, plus bishop-pair and pawn-structure terms, king pawn-shield safety, and an integer-hash transposition table. Iterative deepening to depth 12 with an 80,000-node budget per move. Practice trials on the house gauntlet: trial-0 Elo 2112 (6 wins, 0 draws, 0 losses, all by checkmate), trial-1 Elo 1809 (5 wins, 1 draw, 0 losses); mean 1960.5, above the ~1325 house baseline. No timeouts in either trial.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:18081 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
