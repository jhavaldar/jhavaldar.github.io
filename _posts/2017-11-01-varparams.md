---
layout: post
title: "A Note on the Variation of Parameters Method"
author: "Jay Havaldar"
date:   2017-11-01
mathjax: true
category: [math]
download: true
category: post
---

I was thinking today about the obscure method of 'variation of parameters', which is generally taught in an ODEs course. The proof was always somewhat mysterious to me in undergrad, and I think I've come up with a decent explanation.

First, by analogy, we consider the method of [integrating factors](/notes/2017/07/11/diffeq1.html). We begin with a first order differential equation which looks like:

<p>$$
y' + p(t)y = f(t) 
$$</p>

The idea behind that method was to multiply by a factor $\mu(t)$, hoping to simplify the equation. We have:
<p>$$
y'\mu + p\mu y = \mu f(t)
$$</p>

The guess is made so that the left hand side ought to be an instance of the product rule, i.e.:
<p>$$
\begin{aligned}
y'\mu + p \mu y &= (y\mu)' \\
y'\mu + p \mu y &= y'\mu + y\mu'
\end{aligned}
$$</p>

Therefore, we have the condition:
<p>$$
p\mu = \mu'
$$</p>

And using this condition, we can solve for $\mu$ and find the proper integrating factor. The major idea here is that we guess that our solution will become easier by multiplying by an auxiliary function. This is much the same idea as variation of parameters--educated guesing. 


## The Rational Canonical Form

Before we get into the derivation, we first note that there are many ways to identify similar matrices (matrices which represent the same linear transformation, but perhaps under a different basis). One is the Jordan canonical form, which can be used if our matrix has entries in the complex numbers. Another more general form is the rational canonical form. 

Suppose, for simplicity, that the linear transormation $A$ has characteristic polynomial given by $c_A(x) = x^n + a_{n-1}x^{n-1} + \dots + a_0$. Suppose furthermore that the *minimal polnyomial* of $A$ is exactly its characteristic polynomial (i.e., $A$ satisfies no polynomial of degree smaller than $n$). Then, $A$ is similar to the following matrix:
<p>$$
A \sim \begin{bmatrix}0 & 0 & \dots & -a_0 \\ 
1 & 0 & \dots & -a_1 \\
\vdots & 1 & \dots & \vdots \\
0 & \dots & 1 & -a_{n-1}
\end{bmatrix}
$$</p>
The proof is pretty complicated, and is a corollary of the more general structure theorem for modules. The above matrix is called the **companion matrix** for the polynomial $c_A(x)$, and indeed its characteristic polynomial is $c_A(x)$, since this matrix is similar to $A$ and similar matrices have the same characteristic polynomial. One can prove the above theorem by induction.

## Higher Order Linear ODEs

We can write any linear ordinary differential equations as a statement in linear algebra. Suppose that we have a (homogeneous, for simplicity's sake) differential equation:

<p>$$
y^{(n)} + a_{n-1}y^{(n-1)} + \dots + a_0 = 0
$$</p>

Then we can instead construct the following vector (forgive the abuse in notation):
<p>$$
y = \begin{bmatrix} y \\ y' \\ \dots \\ y^{n-1}\end{bmatrix}
$$</p>

We can write the differential equation as a matrix system below (check the matrix multiplication for yourself):

<p>$$
\begin{bmatrix} y' \\ y'' \\ \dots \\ y^n\end{bmatrix} = 
\begin{bmatrix}0 & 1 & \dots & 0 & 0\\
0 & 0 & 1 & \dots & 0 \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
-a_0 & -a_1 & -a_2 & \dots & -a_{n-1} \end{bmatrix} \cdot \begin{bmatrix} y \\ y' \\ \dots \\ y^{n-1}\end{bmatrix}
$$</p>

We can write this more succinctly as the equation:
<p>$$
y' = Cy
$$</p>

Where $C$ is the $n \times n$ matrix above. Hopefully it is not too difficult to see that this matrix is indeed the **transpose** of the companion matrix for:
<p>$$
x^n + a_{n-1}x^{n-1} + \dots + a_0 = 0
$$</p>

Therefore, the characteristic polynomial of $C$ is indeed the characteristic polynomial of its transpose (determinants are invariant udner transpose). This explains the mysterious dual use of the term 'characteristic polynomial'. On the one hand, we have a polynomial in $D$, the differential operator, given by:
<p>$$
(D^n + a_{n-1}D^{n-1} + \dots + a_0)y = 0
$$</p>
And indeed we have a corresponding matrix $C$, which has the exact same characteristic polynomial.

Finally, we know that an order $n$ linear differential equation has $n$ linearly independent solutions $y_1, \dots, y_n$. They give rise to (with the same construction as earlier, listing the derivatives in a column) $n$ linearly independent vectors. 

We define a **fundamental matrix** as a matrix with $n$ such linearly independent vectors in its columns. For example, we can write a fundamental matrix as:

<p>$$
X = \begin{bmatrix}y_1 & y_2 & \dots & y_n \\
y_1' & y_2' & \dots & y_n' \\
\vdots & \vdots & \vdots & \vdots \\
y_1^{n-1} & y_2^{n-1} & \dots & y_n^{n-1}
\end{bmatrix}
$$</p>

Abbrevating this, we write:
<p>$$X = \begin{bmatrix} y_1 & y_2 & \dots & y_n \end{bmatrix}$$</p>

It is not hard to check (because matrix multiplication can be done column-wise), that indeed we can write for any fundamental matrix $X$ for the homogeneous equation $x' = Cx$ the following identity:

<p>$$
X' = CX
$$</p>

This is a statement about matrix multiplication derived entirely from our linear ODE. 

## The Inhomogeneous Case

We now turn to solving the differential equation given by:

<p>$$
y^{n} + a_{n-1}y^{n} + \dots + a_0 = f(t)
$$</p>

Using the same construction as before, we can write this is a matrix system:
<p>$$
y' = Cy + b
$$</p>

Where $C$ is, as before, the companion matrix for the characteristic polynomial of the equation. $b$ is, finally:
<p>$$
b = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ f(x)\end{bmatrix}
$$</p>

And suppose furthermore that we have a fundamental matrix $X$ for the associated homogeneous equation:
<p>$$
y' = Cy
$$</p>

We have a fundamental matrix $X$, which is an $n\times n$ matrix; a fairly natural guess for a column vector which is a solution to the *inhomogeneous* equation is a vector of the form:
<p>$$
Xu
$$</p>

Where $X$ is an $n\times n$ matrix, and $u$ is a $n\times 1$ column vector; the product is an $n\times 1$ vector (which is the right size!) and if we pick $u$ cleverly, we hope to be able to find a solution. Note however that by the product rule we can write:
<p>$$
(Xu)' = X'u + Xu'
$$</p>

However, $X' = CX$ since $X$ is a fundamental matrix, so we are left wth:
<p>$$
(Xu)' = C(Xu) + Xu'
$$</p>

So $Xu$ is nearly a solution to the inhomogeneous equation! The only thing that's missing is the constraint:
<p>$$
Xu' = b
$$</p>

And solving the above equation is exactly the method of the variation of parameters. Indeed, solving the homogeneous equation amounts to picking $u' = 0$; indeed, then $u$ is a constant matrix. The statement, then, is that if we take a linear combination of a fundamental system of homogeneous solutions, we arrive at another homogeneous solution (this is sometimes called the principle of superposition).

Hopefully this is an illuminating way to look at the variation of parameters from the perspective of linear algebra!

