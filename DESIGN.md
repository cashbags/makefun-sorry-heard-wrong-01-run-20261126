# Design — Sorry, I Heard That Wrong

## The line

> Sorry, I heard 'water the plants' as 'water the planet.' The ocean says thanks. The plants are dead.

100 characters, one line, no trailing newline.

## Why this line wins the rubric

The judge weighs, in order: on-topic apology, humour, freshness, device voice,
tightness.

1. **On-topic.** First-person apology from the speaker, naming the mishear
   explicitly: 'water the plants' heard as 'water the planet'.
2. **Humour.** The joke is an escalation with a two-beat undercut. The speaker
   did not just mishear — it acted on the mishear at planetary scale, then
   reports the result like a status update. "The ocean says thanks" is the
   speaker proud of the wrong job; "The plants are dead" is the bill.
3. **Freshness.** The live field (241 entries at build time) is crowded with
   lights-off mishears (13), jazz bands (9), pizza orders (8), timers (7) and
   mother-in-law jokes. Weather, plants, morning and goodnight had zero
   entries. The plants→planet pair is a minimal pair nobody used.
4. **Device voice.** Flat, helpful, literal: a status report that confesses
   by accident. It reads as something the speaker would say out loud.
5. **Tight.** 100 of 140 characters; every word earns its place. No song
   title, no name, no pun that needs explaining.

## Tournament

Eight original candidates were judged pairwise on the exact five-criterion
rubric. The plants line beat weather ("what's the matter"), "good mourning"
and "burn it down" in turn; the final was decided on freshness — the
morning/mourning pair is a known pun, the planet escalation is not. One
candidate ("remind me at nine" → "remind me to leave") was cut in the
semifinal because nine/leave is not a plausible mishear: a mishear must
sound like a mishear.

## Determinism

`main.py` writes fixed text. Two consecutive runs produce byte-identical
`/output/entry.txt` (sha256 `40ed4d23…`, 100 bytes). No randomness, no clock,
no I/O besides the single output file.
