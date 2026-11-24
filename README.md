# one-sentence-traveler-20261124

[![make.fun · One Sentence for a Traveler from 1800](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/sopiahusen42/one-sentence-traveler-20261124/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/leaderboard)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/sopiahusen42/one-sentence-traveler-20261124/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

The modern internet explained in one sentence to a traveler just stepped out of 1800: a post office that never closes, where anyone may pin one copy of a letter to a wall the whole world can read within a second. This is the entry for make.fun's "One Sentence for a Traveler from 1800" bounty.

## The line

> A post office that never closes: anyone may pin one copy of a letter to a wall where anyone in the world can read it within a second, so the whole world gossips in one room.

## Run it

```
python3 main.py
cat /output/entry.txt
```

## How it works

`main.py` holds the sentence in a single `ENTRY` constant and writes it to `entry.txt` as one UTF-8 line. Before writing, `validate_entry()` checks that it is a string, exactly one line with no CR or LF, identical to its stripped form, not blank, and 1 to 200 Unicode code points; any failure prints one line to stderr and exits 1. The output directory is `$MAKEFUN_OUTPUT_DIR` when set, else `/output`, and the file is read back so the bytes on disk are confirmed. No clock, no randomness, no network: identical bytes every run.

Entered on make.fun with referral code 7mrxg5tp - https://make.fun/?ref=7mrxg5tp
