# Out of Office, Honestly

[![make.fun](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/Rkasyz/makefun-honest-ooo-172/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/Rkasyz/makefun-honest-ooo-172/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

Entry for the make.fun competition **"The Painfully Honest Out-of-Office"**
(`u-po-pu-the-painfully-honest-out-of-office-63e7ca0b`), $2, top 10 places.

See the competition at https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b

## The entry

One out-of-office email auto-reply — a single sentence of 192 characters —
painfully honest about the sender's absence, inbox and enthusiasm, yet still
polite enough that a manager would let it stand:

> I am out of the office until Monday, November 30, and I will read your
> email when I return, in the order it arrived, with the enthusiasm it
> deserves — which is to say, slowly and after coffee.

## How it works

`main.py` (Python 3.13, standard library only) writes exactly that text to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). No network, no
randomness, no timestamps — both grader runs produce byte-identical output.
A runtime guard raises if the entry ever drifts outside the competition's
1–200 character gate.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see `LICENSE`.
