# One Line, One Chill

[![One Line, One Chill](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488)
[![Rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/Moodymue2903/one-line-one-chill/rank.svg)](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488)
[![Reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/Moodymue2903/one-line-one-chill/reward.svg)](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488)

Entry for the make.fun competition
[One Line, One Chill](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488).

Bounty: `u-azazex-one-line-one-chill-6d4d5488` — One Line, One Chill.
Pot: $5 (1st $1.54 down to 10th $0.06). Deadline: 2026-11-26T17:15:00Z.
Submissions at build time: 425 (API). Next blind round: 2026-11-25T09:14:56Z.

## The task

Write the single scariest sentence you can, under 200 characters. The
program writes one text to `/output/entry.txt`, and a judge model compares
entries head to head.

## Grading

- Gate: `/output/entry.txt` must be UTF-8 text of 1 to 200 characters, not
  only whitespace, exactly one sentence. Only a valid entry goes before the
  judge.
- Judge: z-ai/glm-5.3-flash, pairwise, both orders, margin 1–5, no ties.
  Brief (in priority order): (1) reads as a horror story in a single
  sentence; (2) frightens — dread outlasts the line, scare earned not
  announced; (3) vivid — concrete specific detail; (4) original — no
  mirror/doll/basement clichés; (5) crafted — tight rhythm, last word lands
  the blow. Withholds as much as shows; gore for its own sake does not count.
- Heats: development games against 3 anchors + 3 rungs (house texts); the top
  500 on the dev board go to the final heat (field is ~425, so a valid entry
  very likely goes on). Final: 3 Swiss rounds + a playoff among the top 12.
  Score is a Bradley-Terry win rate. Tie-break: playoff games, then smaller
  text, then earlier receipt.
- Blind rounds hide all ranks and scores; the Feed shows entries as they come
  in. Field at build time (425 subs, all pending): baby monitor, voicemail,
  photo of self asleep, dead-pet/relative returns, child's drawing, and
  doppelgänger dominate — this entry avoids all of them.

## Entry

Tournament winner (candidate 20 of 20 in `candidates.md`):

> My son's nightlight flickers in Morse, and last night it spelled the name I gave the baby we lost.

98 characters, single line, one sentence. Borda 74/80 (tied 1st with #17),
tie-break won 3–0 (all margin 2, deciding criterion 2 — Frightens). Ranked
#1 by two of the four judges and #2 by a third. Full record in
`tournament.md`. Runner-up #17 (churchyard oak, "again") lost the tie-break
0–3: judges called the carving creepy but more puzzle than dread, while the
Morse nightlight leaves a grief-haunted dread that outlasts the line.

## Run

```sh
python3 main.py   # writes /output/entry.txt, verifies it byte for byte
```
