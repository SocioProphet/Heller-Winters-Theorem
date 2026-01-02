#!/usr/bin/env python3
"""
Prime Ladder on the Log Line
- strip-plot of first N primes on a log axis with decade ticks 10^k.
Reproducibility: figure is fully specified by N and output path.
"""
import argparse
import math

def first_n_primes(n: int):
    if n <= 0:
        return []
    # upper bound for nth prime (Rosser) for n >= 6: p_n < n(ln n + ln ln n)
    if n < 6:
        limit = 15
    else:
        limit = int(n * (math.log(n) + math.log(math.log(n))) + 10)
    while True:
        sieve = bytearray(b"\x01") * (limit + 1)
        sieve[:2] = b"\x00\x00"
        for p in range(2, int(limit**0.5) + 1):
            if sieve[p]:
                step = p
                start = p * p
                sieve[start:limit+1:step] = b"\x00" * (((limit - start) // step) + 1)
        primes = [i for i in range(2, limit + 1) if sieve[i]]
        if len(primes) >= n:
            return primes[:n]
        limit = int(limit * 1.5) + 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=1000, help="number of primes")
    ap.add_argument("--out", type=str, default="manuscript/figures/chapter-00/prime-ladder-on-the-log-line/prime_ladder.png")
    args = ap.parse_args()

    primes = first_n_primes(args.N)

    import matplotlib.pyplot as plt

    xs = primes
    ys = list(range(1, len(primes) + 1))  # simple ladder index

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xs, ys, s=6)
    ax.set_xscale("log")
    ax.set_xlabel("p (log scale)")
    ax.set_ylabel("index in first N primes")
    ax.set_title(f"Prime Ladder on the Log Line (N={args.N})")

    # decade ticks 10^k within range
    xmin, xmax = min(xs), max(xs)
    kmin = int(math.floor(math.log10(xmin)))
    kmax = int(math.ceil(math.log10(xmax)))
    ticks = [10**k for k in range(kmin, kmax + 1)]
    ax.set_xticks(ticks)
    ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda v, pos: f"10^{int(round(math.log10(v)))}" if v > 0 else "0"))

    fig.tight_layout()
    fig.savefig(args.out, dpi=200)
    print(f"Wrote {args.out}")

if __name__ == "__main__":
    main()
