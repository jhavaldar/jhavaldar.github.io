---
layout: post
title: "Differential Geometry, Part 3"
author: "Jay Havaldar"
date:   2017-07-10
mathjax: true
category: [math]
download: true
category: notes
---

# Part III: Euclidean Geometry

In this section, we discuss Euclidean geometry in more detail using the tools introduced in the previous two parts. The main ideas of this article revolve around isometries, which will stand in for a notion of congruence for geometrical objects. This will be a shorter chapter, since there's not much to do but apply definitions.

## Isometries of $\mathbb{R}^3$

**Definition** An **isometry** (also called a rigid motion) of $\mathbb{R}^3$ is a mapping from $\mathbb{R}^3$ to itself so that $d(F(p),F(q)) = d(p,q)$ for all points $p,q \in \mathbb{R}^3$. $d(x,y)$ is Euclidean distance. 

Translations and rotations are examples of isometries. As we will see, all isometries can be built from these two fundamental transformations.

**Definition:** An **orthogonal transformation** $C$ in $\mathbb{R}^3$ preserves dot products, i.e. $C(x) \cdot C(y) = x \cdot y$

An example of an orthogonal transformation is rotation (easy to see if you consider the definition of dot products involving angles between vectors). It is hopefully easy to see that orthogonal transformations also then preserve norms, and therefore they are isometries.

##### Lemma

Suppose $F$ is an isometry such that $F(0) = 0$. Then $F$ is orthogonal. The proof is fairly straightforward. First we show that $F$ preserves norms:

<p>
$$\begin{aligned}
d(0, F(p)) = d(F(0),F(p)) = d(0,p)
\end{aligned}$$
</p>

Since $F(p)$ is an isometry which preserves norms:
<p>
$$\begin{aligned}
\vert F(p) - F(q) \vert &= \vert p - q \vert \\
(F(p) - F(q)) \cdot (F(p) - F(q)) &= (p-q)\cdot(p-q) 
\end{aligned}$$
</p>

Multiplying out and cancelling the squared terms since they are simply norms:

<p>
$$\begin{aligned}
F(p)\cdot F(q) = p \cdot q
\end{aligned}$$
</p>

And thus $F$ is indeed orthogonal. It is not hard to prove that $F$ is linear from what we have shown simply by taking dot products with a given orthonormal basis.

##### Theorem

Let $F$ be an isometry of $\mathbb{R}^3$. Then there is a unique translation $T$ and a unique orthogonal transformation $C$ so that $F=TC$.

This isn't hard to prove either. We let $T^{-1}$ be the translation by $F(0)$. Then $T^{-1}F$ sends $0$ to $0$, and by our earlier lemma it is an orthogonal transformation. Proving uniqueness isn't too enlightening. This means we can write any isometry:

<p>
$$\begin{aligned}
F(p) = a + Cp
\end{aligned}$$
</p>

Where $C$ is an orthogonal matrix and $a$ is a vector.

## The Tangent Map of an Isometry

We now calculate the tangent map of an isometry. The main theorem here is that:

##### Theorem

Let $F=TC$ be an isometry. Then:
<p>
$$\begin{aligned}
F\star(v_p) = C(v)_{F(p)}
\end{aligned}$$
</p>

Recall that $F\star$ sends tangent vectors at $p$ to tangent vectors at $F(p)$. We claim that the tangent map specifically sends any isometry to simply its orthogonal component. You can prove this from the definition:

<p>
$$\begin{aligned}
F(p+tv) &= TC(p+tv) = a + C(p)+tC(v) \\
&= F(p) + tC(v)
\end{aligned}$$
</p>

An immediate corollary is that isometries preserve dot products of tangent vectors, along with norms and orthogonality. Now, we can also prove that isometries are uniquely determined by frames:

##### Theorem

Given two frames of $\mathbb{R}^3$ $e_i$ at $p$ and $f_i$ at $q$, there exists a unique isometry $F$ so that $F_\star(e_i) = f_i$.

To prove this, we pick $C$ to be the unique linear transformation from $e_i$ to $f_i$; since both are orthogonal bases, it is not hard to see that $C$ (a change of basis matrix) is indeed orthogonal. Finally, let $T$ be the translation $T(p) = p + q - C(p)$. With these two transformations, define $F=TC$.

It is evident then that $F(p) = T(C(p)) = q$. By the earlier lemma, $F_\star(e_i) = f_{i_{q}}$.

We can compute this orthogonal component explicitly. It is not hard to check (just involves linear algebra) that if the attitude matrix of $f_i$ is $B$, and the attitude matrix of $e_i$ is $A$, then $C=B^{-1}A = B^TA$. The translation portion is as we saw earlier.

## Orientation

We define the orientation of a frame to be the determinant of its attitude matrix, or equivalently the triple product of the frame's vectors. Since the attitude matrix is orthogonal, its determinant is $\pm 1$, giving respectively **right** and **left handed** orientations.

We can also define the sign of an isometry $F$ to be the determinant of its orthogonal component, i.e. $sgn F = \det C$. It is not hard to prove that the sign multiplies against orientation, i.e. a positively oriented isometry preserves orientation while a negatively oriented isometry flips it; we call these **orientation-preserving** and **orientation-reversing** isometries. As a final theorem, we can check that the orientation of an isometry multiplies into cross products:

<p>
$$
F_\star (v\times w) = (sgn F)(F_\star(v) \times F_\star(w))
$$
</p>

## Euclidean Geometry

This is more of a philosophical point than anything. Some consider to be "Euclidean geometry" all the properties which are preserved by isometries (dot products, cross products, etc). A more specific definition would be to consider properties which are preserved by isometries but not by arbitrary diffeomorphisms or mappings. 

**Note** We define differentiation for vector fields componentwise, where the components are defined with respect to the natural coordinate functions $U_i$.

##### Velocity

First, let's take a look at the velocity vector. We define $Y = \sum y_i U_i$. Then, using the definition of the tangent map, we can write:

<p>
$$\begin{aligned}
F_\star(Y') &= F_\star(Y') = CY' \\
&= (CY)' = (F_\star(Y))'
\end{aligned}$$
</p>

As an immediate result, isometries preserve acceleration.

##### Theorem: Isometries & The Frenet Frame

Using the earlier proof, and the properties of the tangent map, we can prove that the Frenet apparatus is more or less preserved. Let $\beta$ be a unit-speed curve in $\mathbb{R}^3$ with positive curvature, and let $\overline{\beta}$ be the image of the curve under an isometry $F$. Then:

- $\overline{\kappa} = \kappa$
- $\overline{T} = F_\star(T)$
- $\overline{N} = F_\star(N)$
- $\overline{B} = (sgn F) F_\star(B)$
- $\overline{\tau} = sgn(F)\tau$

The torsion and binormal formulas involve a sign because of the involvement of the cross product.


## Congruence of Curves

**Definition:** Two curves $\alpha, \beta$ are **congruent** if there exists an isometry $F$ such that $F(\alpha) = \beta$. Curves that are the same up to translation are called **parallel**.

This is the big theorem in this section. We hope that the "unique" identifying properties of curves relates to curvature and torsion. We first note that two curves are parallel if their velocities are everywhere parallel, by integration. We state our congruence theorem:

##### Theorem

If $\alpha, \beta:\ I\rightarrow \mathbb{R}^3$ are unit speed curves such that $\kappa_\alpha = \kappa_\beta$ and $\tau_\alpha = \pm \tau_\beta$, then the two curves are congruent.

We can prove this theorem by construction. Fix an "initial point" in the interval $I$, and let $F$ be the unique orientation-preserving isometry which sends the Frenet frame of $\alpha$ at $t=0$ to the Frenet frame of $\beta$ at $t=0$. By our earlier theorem about isometries, it immediately follows that the new curve's Frenet apparatus (all three vectors, curvature, and torsion) is the same as that of $\beta$ (if there is a sign error in torsion, apply instead an orienation-reversing isometry). It is not hard to show that this curve is parallel to $\beta$, and thus we are done since the two curves start at the same location.

---
