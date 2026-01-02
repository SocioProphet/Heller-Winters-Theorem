# 03.3 Symmetry governance via the Crystallographic Restriction Theorem

## 03.3.1 Statement and lattice-trace constraint
When we demand a periodic discrete lattice (translation invariance plus discreteness) the allowable rotational symmetries are restricted. In two dimensions (and by projection, for rotation axes in three dimensions), an n-fold rotation by angle 2π/n is compatible with a lattice only for n ∈ {1,2,3,4,6}. Equivalently, the only nontrivial allowed angles are 60°, 90°, 120°, 180°.

A standard proof route uses a lattice basis and the fact that the rotation must map lattice vectors to integer linear combinations of lattice vectors. The rotation matrix in a lattice basis must have integer entries, hence integer trace; since the trace of a rotation in 2D is 2cosθ, we obtain the integrality constraint 2cosθ ∈ ℤ, θ = 2π/n, which forces n ∈ {1,2,3,4,6}.

## 03.3.2 Why this is a policy operator here
Our construction contains explicitly periodic layers:
- wheel sieves (mod M),
- base-(b) digit compartments (mod b^k),
- residue-sector partitions used as stable “phase classes.”

Whenever we treat these compartments as forming a lattice of states (translation-like steps in index space plus periodic recurrence), crystallographic restriction becomes a hard admissibility law: only {2,3,4,6}-fold phase quantizations can be used as periodic backbone quantizations.

**CR-policy:** Any phase/sector discretization asserted to be stable under a periodic lattice model must restrict to n ∈ {2,3,4,6}. Other rotational orders are relegated to aperiodic probe layers and cannot be used as backbone invariants.

## 03.3.3 Quasicrystal boundary (division of labor)
If we allow aperiodic order, “forbidden” symmetries (e.g., 5-fold) can appear precisely because translation periodicity is dropped. That’s not a loophole; it’s a separation rule: periodic layers obey crystallographic restriction; aperiodic layers are used deliberately as anti-aliasing probes rather than structural axioms.
