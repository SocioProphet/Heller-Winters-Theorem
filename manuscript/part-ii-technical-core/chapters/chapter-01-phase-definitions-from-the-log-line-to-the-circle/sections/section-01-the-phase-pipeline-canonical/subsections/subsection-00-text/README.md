# 1.1 The Phase Pipeline (canonical)

Every phase construction in this book follows the same pipeline:

1) Choose a scalar transform x(p)  
2) Convert to an angle \theta(p)  
3) Wrap \theta(p) to [0,2\pi)  
4) Embed on the circle via e^{i\theta(p)}

Formally:

- Scalar transform:  
  x:\mathbb{P}\to\mathbb{R}

- Angle map:  
  \theta(p)=\alpha\,x(p)+\beta

- Wrapped phase:  
  r(p)=\theta(p)\bmod 2\pi

- Circle embedding:  
  \Phi(p)=e^{ir(p)}\in S^1

Here \alpha,\beta are explicit constants, not tunable knobs, unless a chapter explicitly declares them as part of a tested parameter family.
