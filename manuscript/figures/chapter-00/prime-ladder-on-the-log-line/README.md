# Figure — Prime Ladder on the Log Line

**Goal:** strip-plot of the first N primes on a logarithmic x-axis, with tick marks at 10^k.

**Inputs:** N (default 1000)  
**Prime source:** deterministic generation (sieve)  
**Axis:** log10 x-scale; y is jitter/stack index only (orientation)

**Caption:** Before we build phase, circle, or spectrum, we set the scale: primes live most naturally on the log line.

Repro script: `scripts/prime_ladder_log_line.py`
