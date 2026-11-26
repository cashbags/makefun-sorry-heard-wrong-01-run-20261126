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

- reproduces: UNKNOWN — no bundle exists yet (see blocker below), so the
  transcript gate has never run; the kit check skips all thinking_* checks.
  Do NOT quote a reproduces % for this build.
- authored share: UNKNOWN for the same reason (target ≥ 30% at bundle time).
- No local judge score exists for this competition (server grades every entry).

## Kit check actually run (26 Nov 2026 15:49 WIB, --worktree, no transcripts)

- PASS competition_open, snapshot (5 files, 6,933 B), license_osi (MIT),
  entrypoint (main.py, python3.13).
- FAIL transcripts_present — no transcripts uploaded (no bundle).
- SKIP all 14 transcript-gate checks (no session parsed).
- At-submission checks (repo_public, repo_owner, repo_created_after_open,
  commit_in_repo, duplicate_snapshot) are decided by the site at submit
  time from GitHub: repo is public, owner cashbags = account login, created
  08:45 UTC after the 07:51 UTC open, commit b2605598 is on main, files are
  original work.

## BLOCKER — bundle needs a git repository (verbatim)

`makefun bundle: /home/hatch/workspace/makefun/bounties/u-kiencx-sorry-i-heard-that-wrong-1858c729/entry is not inside a git repository`

No `.git` exists on the path to the entry dir, and creating or aligning a
local git checkout after the Contents-API push is forbidden by the build
spec, so no bundle was made and the transcript gate is untested. Needs a
parent decision (e.g. authorise a clone in a live session, or another
bundling route). Secondary known limit: muse.db returns 0 usage rows for
this run (rows flush only after the run completes), so even with a bundle,
thinking_priced would fail until a live-session re-bundle — the same
READY-HELD state as today's earlier batches.

## Notes

- `.makefun/owner.json` NOT included: repo owner `cashbags` is the account's
  GitHub login, so the claim file is not required.
- Sealing needs a live session; this build is READY-HELD, unsubmitted.
