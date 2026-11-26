# GATE — Sorry, I Heard That Wrong

Competition: `u-kiencx-sorry-i-heard-that-wrong-1858c729` · $2 (0.91/0.64/0.45) ·
deadline 26 Nov 2026 21:50 WIB · Force_Last, max 5/day · transcripts required.

## Block A — judged text (the only block that applies)

- Entry: one line, 100 chars, single line, UTF-8, no trailing newline.
  Gate rule: 1–140 chars, not only whitespace → PASS (ran `main.py`).
- Deterministic replay: two runs, sha256 `40ed4d23…` both times →
  byte-identical → PASS.
- Pairwise self-judge tournament on the exact 5-criterion rubric (8
  candidates, QF/SF/F): winner is the plants line. Final turned on
  freshness (morning/mourning is a known pun; planet escalation is not).
  Simulated, not a guaranteed rank.
- Duplicate test: no shared 6-word shingle with any of the 241 live-field
  titles, and the line is not the rapid-falcon-38 checkpoint line → PASS.
- No screenshots: the artifact is a text file written by a program; there
  is no visual deliverable. No rendered image is used anywhere.
- Tree size is measured after every edit (local kit check does NOT enforce
  the 8,192 B cap).

## Kit check actually run (26 Nov 2026 15:49 WIB, --worktree, no transcripts)

- PASS: competition_open, snapshot, license_osi (MIT), entrypoint (main.py,
  python3.13). FAIL: transcripts_present (no bundle). SKIP: all 14
  transcript-gate checks (no session parsed).
- reproduces % and authored share: UNKNOWN — no bundle, gate never ran.
- At-submission checks (repo_public, repo_owner, repo_created_after_open,
  commit_in_repo, duplicate_snapshot) are decided by the site from GitHub:
  repo public, owner cashbags = account login, created 08:45 UTC after the
  07:51 UTC open, commit on main, files are original work.

## Blocker

No bundle: `makefun bundle` refuses a `--repo` that is not inside a git
repository, and no `.git` exists on the path; creating/aligning a local
checkout after the Contents-API push is forbidden by the build spec. Full
verbatim + follow-up in `../BUILD-NOTES.md`. Also: muse.db returns 0 usage
rows for this run (rows flush only after the run completes), so
thinking_priced would fail until a live-session re-bundle.

## Notes

- `.makefun/owner.json` NOT included: repo owner `cashbags` is the
  account's GitHub login, so the claim file is not required.
- Sealing needs a live session; this build is READY-HELD, unsubmitted.
