# Chapter 4 Figures (Render Queue + Specs)

## Fig 4.1 — Density baseline: \pi(x) vs x/\ln x vs Li(x)
- x-axis: log scale (declare explicitly)
- y-axis: counts
- curves: step plot \pi(x), smooth x/\ln x, smooth Li(x)
- range: at least up to 10^5 (so the convergence is visible)

## Fig 4.2 — Local intensity \lambda(x)=1/\ln x
- show thinning directly over same x-range as Fig 4.1
- x-axis: log scale

## Fig 4.3 — Window expectation operator
- schematic: shade area under 1/\ln t over [a,b]
- label: \int_a^b dt/\ln t as expected prime count

## Fig 4.4 — Worked micro-example panel [100,200]
- text on-figure:
  - actual: 21 primes
  - mean-field approx: \int_{100}^{200} dt/\ln t \approx 19.96 (midpoint estimate)
- make the comparison tactile and audit-friendly

## Fig 4.5 — Log-volume windows (optional but recommended)
- show equal-ratio windows in x-space mapping to equal-length windows in u=\ln x
