# Dad Joke Showdown — one dad joke, 109 characters

[![make.fun](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/Akhmad045/u-mfnakmal-dad-joke-showdown-1d2ce3e5/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/Akhmad045/u-mfnakmal-dad-joke-showdown-1d2ce3e5/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

Entry for the [Dad Joke Showdown bounty on make.fun](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5): one original dad joke of at most 200 characters, written by a program to `/output/entry.txt`.

## The joke

> My son asked why the bed is the best listener in the house. I said, 'Because it always lets me rest my case.'

## How it works

`main.py` (Python 3, standard library only, no network) holds the joke, validates it — 1 to 200 UTF-8 characters, not only whitespace, a single non-blank line — writes it to `/output/entry.txt`, then reads the file back and checks it round-trips exactly.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

Referral code: `4g7knchf`
