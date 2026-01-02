# 1.4 The Winters Log-Circle Instrument (credited visualization step)

We now state the instrument in its most minimal, reproducible form.

Given a prime p, define:
z(p)=\log p + i\,(\log p)
and project to the unit circle by argument:
\Phi_{\arg}(p)=e^{i\arg(z(p))}

Equivalent explicit form:
\arg(\log p + i\log p)=\arg(1+i)=\frac{\pi}{4}
so this construction collapses unless we separate the real and imaginary channels.

Therefore the usable log-circle instrument is:

\Phi_{\log}(p)=e^{i(\log p \bmod 2\pi)}

together with a second channel (radial or density) derived from x(p), for example:

- radial scaling: \rho(p)=\operatorname{frac}(\log p / 2\pi)  
- density layering by prime index windows  

This is the point of the instrument: the circle is the phase; the windowing and density are the signal probes.
