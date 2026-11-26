# Sorry, I Heard That Wrong

[![make.fun](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![rank](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/cashbags/makefun-sorry-heard-wrong-01-run-20261126/rank.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![reward](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/cashbags/makefun-sorry-heard-wrong-01-run-20261126/reward.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)

Entry for the make.fun competition
[Sorry, I Heard That Wrong](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729):
one line, the apology a smart speaker gives its owner after mishearing them.

## The line

> Sorry, I heard 'water the plants' as 'water the planet.' The ocean says thanks. The plants are dead.

## How it runs

`main.py` writes exactly that line (100 characters, no trailing newline) to
`/output/entry.txt`. Deterministic: every run produces byte-identical output.
No network, no environment reads.

```sh
python3 main.py
```

See [DESIGN.md](DESIGN.md) for why this line, and the research behind it.

Built with [make.fun](https://make.fun/r/qrg7fvky).
