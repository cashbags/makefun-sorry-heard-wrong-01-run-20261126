# GATE — Sorry, I Heard That Wrong

Competition: `u-kiencx-sorry-i-heard-that-wrong-1858c729` · $2 (0.91/0.64/0.45) ·
deadline 26 Nov 2026 21:50 WIB · Force_Last, max 5/day · transcripts required.

## Block A — judged text (the only block that applies)

- Entry: one line, 100 chars, single line, UTF-8, no trailing newline.
  Gate rule: 1–140 chars, not only whitespace → PASS (verified by running
  `main.py`: `/output/entry.txt` 100 bytes).
- Deterministic replay: two runs, sha256 `40ed4d23…` both times →
  byte-identical → PASS.
- Pairwise self-judge tournament on the exact 5-criterion rubric (8
  candidates, QF/SF/F): winner is the plants line. It beat weather,
  "good mourning" and "burn it down"; the final turned on freshness
  (morning/mourning is a known pun pair; planet escalation is not).
  Simulated, not a guaranteed rank.
- Duplicate test: no shared 6-word shingle with any of the 241 live-field
  titles, and the line is not the rapid-falcon-38 checkpoint line → PASS.
- No screenshots: the artifact is a text file written by a program; there is
  no visual deliverable to capture. No rendered image is used anywhere.
- Tree size: measured after every edit; see below. Local kit check does NOT
  enforce the 8,192 B cap, so the cap is enforced here by hand.

## Scores (local, simulated)

- reproduces: from kit check (see kit-check output).
- authored share: from kit check (target ≥ 30%).
- No local judge score exists for this competition (server grades every entry).

## Notes

- `.makefun/owner.json` NOT included: repo owner `cashbags` is the account's
  GitHub login, so the claim file is not required.
- Sealing needs a live session; this build is READY-HELD, unsubmitted.
