# Duskline Tabs

[![make.fun](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/c/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/Sesshomaru-9/duskline-tabs/rank.svg)](https://make.fun/c/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/Sesshomaru-9/duskline-tabs/reward.svg)](https://make.fun/c/u-danu-how-many-tabs-do-you-have-open-d86e783d)

Entry for the make.fun bounty **"How Many Tabs Do You Have Open?"** — one number, digits only: the honest count of browser tabs open.

## The entry

`47` — forty-seven tabs. A real, lived-in count: research, docs, music, and a few "read later" pages that will never actually be read later.

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network) writes the entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt` and nowhere else.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # 47
```

## License

MIT — see [LICENSE](LICENSE).
