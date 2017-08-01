---
layout: post
title: "Differential Geometry, Part 5: Shape Operators"
author: "Jay Havaldar"
date:   2017-07-18
mathjax: true
category: [math]
download: true
category: notes
---

# Part V: Shape Operators

We can now study the shape of surfaces through the lens of linear algebra, namely a symmetric operator called the shape operator. We draw comparison with the [Frenet formulas and their generalizations using the connection forms](/notes/2017/07/08/dffgeo2.html), which describe curves in terms of their curvature and torsion, to develop similar machinery describing surfaces. Finally, we generalize the [uniqueness theorem for curves](/notes/2017/07/10/diffgeo-notes3.html) to a congruence theorem for surfaces, although that will have to wait until Part VI.

## The Shape Operator of $M \subset \mathbb{R}^3$

Recall how we defined the covariant derivative of a vector field $Z$ with respect to a vector $v$, denoted as $\nabla_v Z$. By an earlier lemma, we were able to show that in Euclidean space:

<p>
$$\begin{aligned}
\nabla_v Z &= \frac{d}{dt}Z(p+tv) \mid_t=0 \\ 
&= \sum v[w_i] U_i
\end{aligned}$$
</p>

This definition still more or less makes sense for any vector field on a surface if we pick $v$ tangent to a surface $M$ so that the derivative is defined. In addition to the earlier method of computation, we can also refer to the definition of derivatives on surfaces to obtain:

<p>
$$\begin{aligned}
\nabla_v Z &= (Z_\alpha)'(0)\\ 
&= \sum v[w_i] U_i
\end{aligned}$$
</p>

Where $Z_\alpha$ is the vector field $Z$ restricted to a curve $\alpha$ through a point $p$ where $\alpha'(0) = v$.

Using the covariant derivative, we now define the shape operator. 

Note that if a surface is orientable, it has a (differentiable) unit normal vector field $U$ everywhere. If it is connected, there are exactly two (in opposite directions). For a non-orientable surface, we still have local parameter curves, which allow us to create a local unit normal vector field. All this tells us that the following definition makes sense for surfaces.

**Definition:** If $p\in M$, then for each tangent vector $v$ to $M$ at $p$, define the **shape operator**:

<p>
$$\begin{aligned}
S_p(v) &= - \nabla_v U
\end{aligned}$$
</p>

Where $U$ is a normal vector field to $M$ defined in a neighborhood of $p$.

The shape operator tells us how the normal to the tangent plane (and thus the tangent plane itself) is moving in every direction; so it tells us the way $M$ is curving in all directions at $p$.

##### Lemma

Suppose $p \in M \subset \mathbb{R}^3$. Then $S_p$ is a linear map from the tangent space $T_p(M)$ to itself.

The linearity of the shape operator is clear from the properties of covariant derivatives. Furthermore, since $U$ has unit length everywhere, the derivative of $\vert U \vert = 0$ everywhere. So we have:

<p>
$$\begin{aligned}
0 = v[U\cdot U] = (\nabla_v U)\cdot U(p)
\end{aligned}$$
</p>

So indeed the shape operator is orthogonal to the unit normal, and thus lies in the tangent plane.

##### Example

For example, take a sphere of radius $r$. It is evident that the unit normal is pointing out radially from the center everywhere. So we have:

<p>
$$\begin{aligned}
S_p(v) = - \nabla_v U &= -\frac{1}{r} \sum v[x_i] U_i \\ 
&= - \frac{v}{r}
\end{aligned}$$
</p>

This has some geometric meaning; the shape operator simply is scalar multiplication, and this reflects in the uniformity of the sphere itself. The sphere bends in the same exact way at every point.

##### Lemma

The shape operator is symmetric, i.e.:
<p>
$$\begin{aligned}
S(v)\cdot w = S(w) \cdot v
\end{aligned}$$
</p>

This proof appears later on the chapter.

## Normal Curvature

The first application of the shape operator is in the discussion of normal curvature.

**Definition:** Suppose $u$ is a unit vector tangent to $M$ at $p$. Then $k(u) = S(u)\cdot u$ is called the normal curvature of $M$ in the $u$ direction.

So what does the normal curvature mean? First, we prove a brief lemma.

##### Lemma

Suppose $\alpha$ is a curve in $M$. Then:
<p>
$$\begin{aligned}
(\alpha \cdot U) &= 0 \\
\alpha''\cdot U + \alpha'\cdot U' &= 0 \\
\alpha''\cdot U &= - \alpha'\cdot U' = S(\alpha') \cdot \alpha'
\end{aligned}$$
</p>

First, we differentiated both sides. In the second step, we note that $S(\alpha) = -U'$, perhaps abusing notation to really get across the point that covariant derivatives are derivatives, and in a fairly straightforward way, too. In fact, using the chain rule we can define $S(\alpha') = - \nabla_{\alpha'}U = - U(\alpha(t))'(0)$.

The interpretation of this lemma is that all curves with a given velocity $v$ have the same normal component of acceleration; namely a multiple of the normal curvature of $\hat{v}$.

So we parametrize $\alpha$ to be in particular a unit speed curve in $M$ so that $\alpha'(0)=u$. Then we can compute:

<p>
$$\begin{aligned}
k(u) &= S(u)\cdot u \\
& = \alpha''\cdot U \\
&= \kappa N \cdot U \\
&= \kappa \cos(\theta)
\end{aligned}$$
</p>

Where $\theta$ is the angle between the normal vector to the curve ($N$) and the unit normal to the surface ($U$), and $\kappa$ is our familiar curvature. So the maximum possible value the normal curvature can take is in fact, our regular notion of curvature. 

To make more geometric sense of this, we define the normal section of $M$ through the $u$ direction, which is the plane containing $U$ as well as $u$; this plane slices out a curve $\sigma$ inside of $M$. If we choose to make $\sigma$ unit speed, then $\sigma'(0) = u$, and indeed the normal vector $N = \pm U$, the unit normal vector for the surface. So we can say that the normal curvature of $M$ in the direction of $u$ is just the curvature of the unit-speed curve determined by the corresponding normal section.

**Definition:** The maximum and minimum values of $k(u)$ at $M$ are called the **principal curvatures** of $M$ at $p$, denoted $k_1, k_2$. The corresponding directions are called **principal directions**.

It should maybe become clear to you now that these are precisely the eigenvalues and eigenvectors of the shape operator, for these are precisely the vectors $u$ such that $S(u) = \pm c u$.

**Definition:** A point $p$ is unmbilic if $k(u)$ is constant everywhere.

At an umbilic point, the shape operator is just multiplication on tangent vectors. So the following computations only apply to a non-umbilic point. Due to the fact that $S$ is linear, its action is completely determined by its evaluation in principal directions. And furthermore due to the fact that $S$ is symmetric, [it has a set of orthogonal eigenvectors](post/2017/07/02/symmetric-matrices.html). So for any unit vector $u$, we can write $u = \cos\theta e_1 + \sin\theta e_2$, where $e_1, e_2$ are unit vectors in the principal directions. Then, by linear algebra:

<p>
$$\begin{aligned}
k(u) &= S(u)\cdot u = S(\cos\theta e_1 + \sin\theta e_2) \cdot (\cos\theta e_1 + \sin\theta e_2) \\
&= k_1 \cos^2 \theta + k_2 \sin^2 \theta
\end{aligned}$$
</p>

Fun fact, this is called the Euler curvature formula. He really got around, didn't he.

## Gaussian Curvature

The following two measures have some geometric significance, but their use won't become totally obvious until a bit later. We define:

**Definition:** The Gaussian curvature of a surface $K = k_1k_2$ is the product of its principal values (the determinant of the shape operator).

**Definition:** The Mean curvature of a surface $H = \frac{k_1 + k_2}{2}$ is the mean of its principal values (half the trace of the shape operator).

Interestingly, the Gaussian curvature does not change if we change the sign of $U$. The sign of the Gaussian curvature can actually tell us quite a lot about the surface. For example:

- If $K>0$, the principal directions have the same signs, so $M$ is bending away from the tangent plane in all directions (like a bowl), though it could be upwards or downwards.
- If $K<0$, the principal directions have opposite signs, so $M$ is "saddle"-shaped.
- If $K=0$, one or both of the principal values is zero. If it's just one, $M$ is shaped like a "U". If it's both, then $M$ looks like a plane near the point.

Using $K$ and $H$, you can determine computational formulas for $k_1, k_2$. I won't get too much into those, as they all really have the same upshot. Let's take for example the algebraic identity:

<p>
$$
k_1, k_2 = H \pm \sqrt{H^2 - K}
$$
</p>

An immediate corollary of this is that $k_1, k_2$ are continuous, and away from umbilic points where the quadratic discriminant is zero, they are also differentiable.

**Definition:** A surface $M$ is **flat** if $K=0$, and **minimal** if $H=0$.

## Computational Techniques

Now we get into the every-day process of computing shape operators. We first define for any patch $x$ of a surface $M$:

<p>
$$\begin{aligned}
E &= x_u \cdot x_u \\
F &= x_u \cdot x_v \\
G &= x_v \cdot x_v \\
\end{aligned}$$
</p>

These tell us more or less what the inner product looks like on $T_p(M)$, since we know that $x_u,x_v$ form a basis for the tangent space at a point. For example, if $v=a x_u + b x_v$ and $w = cx_u + dx_v$, then we can easily check that:

<p>
$$\begin{aligned}
v\cdot w = Eac + F(ac+bd) + G(bd)
\end{aligned}$$
</p>

Furthermore, $\vert x_u \times x_v \vert ^2 = EG-F^2$ by distributivity. You may recognize this as a quadratic form. 

We also generally compute the unit normal vector. Luckily, for a patch $x$, we can always use:

<p>
$$\begin{aligned}
U = \frac{x_u \times x_v}{\vert x_u \times x_v \vert}
\end{aligned}$$
</p>

And finally, we can define the shape operator just by looking at the following values:

<p>
$$\begin{aligned}
L &= S(x_u) \cdot x_u \\
M &= S(x_u) \cdot x_v = S(x_v) \cdot x_u \\
N &= S(x_v) \cdot x_v \\
\end{aligned}$$
</p>

Similarly to the earlier case, these coefficients allow us to compute $S(v)\cdot w$ where $v,w$ are expressed with respect to the $x_u, x_v$ basis, and indeed we get a quadratic form again. As promised before, we have essentially proven that the shape operator is symmetric. So how do we compute $L,M,N$? Well, by the Leibniz rule we have:

<p>
$$\begin{aligned}
0 &= \frac{\partial}{\partial v} (U \cdot x_u)  \\
0 &= \nabla_v U \cdot x_u + U\cdot x_{uv} \\
S(x_u) \cdot x_v &= U \cdot x_{uv} \\
\end{aligned}$$
</p>

So this gives us easier formulas to compute $L,M,N$:

<p>
$$\begin{aligned}
L &= S(x_u) \cdot x_u = U\cdot x_{uu} \\
M &= S(x_u) \cdot x_v = U\cdot x_{uv} \\
N &= S(x_v) \cdot x_v = U\cdot x_{vv}\\
\end{aligned}$$
</p>

So we merely need to compute the normal components of the second derivatives of $x$.

Using vector formulas, we can get the following convenient formula for the Gaussian curvature:

<p>
$$
K = \frac{LN - M^2}{EG - F^2}
$$
</p>

## Special Curves in a Surface

Now we look at some important classes of curves on a surface, the principal, normal, and asymptotic curves.

**Definition:** A regular curve $\alpha$ is a principal curve if $\alpha'$ always points in a principal direction.

##### Lemma

If $\alpha$ is a regular curve, and $U$ is a normal vector field, then $\alpha$ is a principal curve iff $\alpha'$ is collinear with $U'$ at each point. Furthermore, the principal curvature of $M$ in the direction of $\alpha'$ is $k=\frac{\alpha'' \cdot U}{\alpha' \cdot \alpha'}$.

The first part of the theorem we get basically for free as a consequence of how we defined principal curves (they maximize the covariant derivative of $U$). The second theorem follows from a few steps of vector algebra:

<p>
$$\begin{aligned}
k_1 &= k(\frac{\alpha'}{\vert \alpha' \vert}) \\
&= S(\frac{\alpha'}{\vert \alpha' \vert}) \cdot \frac{\alpha'}{\vert \alpha' \vert} \\
&= \frac{S(\alpha') \cdot \alpha'}{\alpha' \cdot \alpha'} \\
&= \frac{\alpha'' \cdot U }{\alpha' \cdot \alpha'}
\end{aligned}$$
</p>

The second equality comes from the linearity of the shape operator. The final equality comes from a lemma in the normal curvature section of this chapter.

##### Lemma

Let $\alpha$ be a curve cut from a surface $M$ by a plane $P$. If the angle between $M$ and $P$ is constant along $\alpha$, then $\alpha$ is a principal curve of $M$.

Let $U,V$ be the normal vector fields to $M,P$ respectively. Since the angle between them is constant, we have:

<p>
$$
0 = (U\cdot V)' = U\cdot V' + U' \cdot V = U' \cdot V
$$
</p>

Where the last equality follows from the fact that $V$ is constant. So we know that $U'$ is orthogonal to $U$ and to $V$. Similarly, $\alpha'$ is orthogonal to $U$ since it is a tangent vector, and orthogonal to $V$ since it lies on the plane $P$. So the two are collinear. By our earlier lemma, $\alpha$ is a principal curve. We omit the case where $U=\pm V$, in which case $\alpha$ is trivially principal.

The geometric meaning of this theorem is that for a surface of revolution, the meridians and parallels (which are cut from the surface with the "right" planes) are principal curves.

So we covered curves for which the normal curvature is $k_1$ or $k_2$. On the other extreme, what about points where the normal curvature $k=0$?

**Definition:** A direction in which the normal curvature is zero is called **asymptotic**. An asymptotic curve $\alpha$ is one where $\alpha'$ always points in an asymptotic direction.

The asymptotic directions at a point are the ones where $M$ does not bend away from the tangent plane at all. Let's take a look at the possibilities depending on the Gaussian curvature.

- $K(p) > 0$. In this case $k_1,k_2$ share the same sign. By the intermediate value theorem, there is no asymptotic direction.
- $K(p) < 0$. There are exactly two asymptotic directions at $p$. They are bisected by the principal curves. From Euler's curvature formula, it should be easy to see that $\tan^2 \theta = - \frac{k_1}{k_2}$ defines the angle between the asymptotic and a principal direction.
- $K(p) = 0$. There is either one asymptotic (also principal) direction; or $p$ is a planar point, and all directions are asymptotic trivially.

As a quick corollary, we can check the following fact. Suppose $\alpha$ is on $M$; then $U\cdot \alpha' = 0$. By the product rule, this means that $U' \cdot \alpha' = - U \cdot \alpha''$. Thus, a curve is asymptotic if and only if its acceleration has no normal component.

By the Euler curvature formula, we also have an important result for minimal surfaces. We find that minimal surfaces have two orthogonal asymptotic curves at each point which is non-planar.

Finally, we discuss special curves called geodesics.

**Definition:** A curve $\alpha \in M$ is **geodesic** if $\alpha''$ is always normal to $M$.

So, whereas an asymptotic curve has no normal component of acceleration, a geodesic has only a normal component of acceleration. For inhabitants of the surface, a geodesic is a curve where there appears to be no acceleration at all, so these are the "straight lines". 

It isn't hard to show as well that geodesics have constant speed, since $\alpha''$ is normal to $\alpha'$.

In particular, if a unit-speed curve $\alpha$ lies in a plane $P$ everywhere orthogonal to $M$ along the curve, the $\alpha$ is a geodesic. The two orthogonal vectors $\alpha'$ and $\alpha''$ are both orthogonal to $M$, and $\alpha'$ is tangent to $M$, so it must be the case that $\alpha''$ is normal to $M$. As a consequence, all meridians are geodesics on a surface of revolution.

We summarize these three special kinds of curves:

- A principal curve: $k(\alpha) = k_1, k_2$. $S(\alpha')$ is collinear to $\alpha'$.
- An asymptotic curve: $k(\alpha) = 0$. $S(\alpha')$ is orthogonal to $\alpha'$. $\alpha''$ is tangent to $M$.
- An geodesic curve: $\alpha''$ is normal to $M$.

Since the shape operator is a linear map on the tangent space, think of principal curves as "eigencurves". A geodesic curve is, as we mentioned before, kind of a generalization of a straight line. One interesting application of geodesics is in finding shortest paths on surfaces, but we'll get to that later.

## Surfaces of Revolution

_This section is pretty much optional and exists solely to show the apparatus in action._

We discuss a particular class of surfaces to get a better sense of these concepts: surfaces of revolution. These have a "profile" curve:

<p>
$$
x(u) =(g(u), h(u))
$$
</p>

And we can extend this to a surface of revolution if $h(u) > 0$:

<p>
$$
x(u,v) =(g(u), h(u)\cos(v), h(u)\sin v)
$$
</p>

We'll compute the whole shape operator apparatus for a surface of revolution. First, we compute a basis for the tangent space:

<p>
$$\begin{aligned}
x_u &= (g', h'\cos v, h'\sin v) \\
x_v &= (0, -h\sin v, h\cos v)
\end{aligned}$$
</p>

Take their dot products to get $E, F, G$:

Take their cross product to get a unit vector field:

<p>
$$\begin{aligned}
U &= \frac{x_u \times x_v}{\vert x_u \times x_v \vert} \\
&= \frac{(h', -g'\cos v, -g'\sin v)}{\sqrt{g'^2 + h'^2}}
\end{aligned}$$
</p>

Note that the denominator here is simply the speed of our profile curve, or equivalently, $\sqrt{E}$. We continue onwards, taking second derivatives:

<p>
$$\begin{aligned}
x_{uu} = (g'', h''\cos v, h''\sin v) \\
x_{uv} = (0, -h'\sin v, h'\cos v) \\
x_{vv} = (0, -h\cos v, -h\sin v)
\end{aligned}$$
</p>

Now, computing dot products we can compute $L, M, N$:

<p>
$$\begin{aligned}
L = \frac{-g'h'' + g''h'}{\sqrt{g'^2 + h'^2}}\\
M = 0 \\
N = \frac{g'h}{\sqrt{g'^2 + h'^2}}
\end{aligned}$$
</p>

So we are finally ready to compute the shape operators. We know that $x_u, x_v$ are principal directions (well, we don't know, but I don't want to prove it here; essentially all you need to know is that the matrices of the quadratic forms we discussed in the last section are diagonal here, so this gives us a good idea that we picked the "right basis").

Given the lemma in the "normal curvature" section, we can write:

<p>
$$\begin{aligned}
S(x_u)\cdot x_u &= \frac{U\cdot x_uu}{x_u \cdot x_u} = \frac{L}{E} \\
S(x_v)\cdot x_v &= \frac{U\cdot x_v}{x_v \cdot x_v} = \frac{N}{G} \\
\end{aligned}$$
</p>

And by plugging in, we can compute the principal curvatures, and their product, the Gaussian curvature.

Before going on to do all the ugly computations, let me go back and direct your attention to the term appearing everywhere relating to the speed of the profile curve. If the curve is one-to-one (does not cross back on itself), then by the implicit function theorem we can pick $g(u) = u$ without losing generality. Then, most of the terms above disappear. Note that $g'h'' + g''h' = (g'h')' = h''$, and that the speed term becomes $(1+h'^2)$. So we now have the principal directions:

<p>
$$\begin{aligned}
k_\mu &= -\frac{h''}{(1+h'^2)^{3/2}} \\
k_\pi &= -\frac{1}{h(1+h'^2)^{3/2}} \\
K &= k_\mu k_\pi = -\frac{h''}{h(1+h'^2)^{2}} \\
\end{aligned}$$
</p>

We can further simplify this by picking a unit-speed profile curve, called the **canonical parametrization** of the surface. In this case, it is easy to see that:

<p>
$$\begin{aligned}
E = g'^2 + h'^2 = 1\\
F = 0 \\
G = h^2
\end{aligned}$$
</p>

And our principal curvatures and Gausssian curvature are now:

<p>
$$\begin{aligned}
k_\mu &= -h'' \\
k_\pi &= -\frac{1}{h} \\
K &= k_\mu k_\pi = -\frac{h''}{h} \\
\end{aligned}$$
</p>

##### Theorem

Suppose $M$ is a minimal surface of revolution. Then $M$ is a section of either a plane of a catenoid.

To prove this theorem, we look at $x = (g, h\cos v, h\sin v)$. We consider three cases.

**Case 1**
In this case, $g'=0$ everywhere. Then, $g$ is constant, so $M$ is planar.

**Case 2**
In this case, $g'=0$ nowhere. Then, we can repeat the earlier trick of picking another parametrization $y(u,v) = (u, h\cos v, h\sin v)$. However, looking at the earlier formulas, if $M$ is minimal, then

<p>
$$
h''h = 1+ h'^2
$$
</p>

You can solve this differential equation by setting $v=y'$ and using separation of variables to arrive at:

<p>
$$
1+v^2 = ah^2
$$
</p>

And by inspection, we can see that $v=\sinh(u/a + b)$ gives us a solution. This is precisely a catenoid.

**Case 2**
In this case, $g'=0$ somewhere, but not everywhere. This is a contradiction. If $g'\ne 0$ at a point, we showed earlier that it locally looks like a catenoid. We cannot preserve continuity and yet have $h'/g'$ tend to infinity.

So indeed, the only complete minimal surface is a catenoid (this means something in physics! We'll get to that later)

## Summary

The shape operator $S$ measures the instantaneous change of the unit normal. The unit normal is a sort of "first derivative" (telling us about the tangent plane), and so $S$ is something like a second derivative. By looking at $S$ as an algebraic object, we get some invariants of a surface which will become helpful in defining, as we did for curves, the notion of congruence: principal curvatures and directions, the Gaussian curvature, and the mean curvature (algebraically: the eigenvalues of the shape operator).

