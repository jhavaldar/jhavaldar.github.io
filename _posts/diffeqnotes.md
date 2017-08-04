---
layout: post
title: "Elementary Differential Equations"
author: "Jay Havaldar"
date:   2017-08-01
mathjax: true
---

# First Order Differential Equations

This post will be a brief overview of first-order differential equations. I won't be focusing mainly on proofs here, but instead techniques for solving equations, as well as existence and uniqueness theorems. Uniqueness tells us that there is only one solution to the differential equation in the specified interval.

These notes require cursory knowledge of linear algebra and multivariable calculus.

## Integrating Factors

Integrating factors can be used to solve first order equations of degree $1$, in other words equations of the form:

<p>
$$
y' + P(t)y = Q(t)
$$
</p>

The idea is to multiply through by a factor $\mu(t)$ suitably chosen so that the left hand side is an instance of the product rule. This integrating factor turns out to be:

<p>
$$
\mu(t) = e^{\int P(t)dt}
$$
</p>

Multiplying through, we are left with the product rule on the left hand side, yielding a new simpler differential equation:

<p>
$$
(\mu(t)y(t))' = \mu(t)Q(t)
$$
</p>

And this shouldn't be difficult to integrate in general.

## Separable Equations

A separable differential equation can be rewritten in the form:

<p>
$$
N(y)\frac{dy}{dx} = M(x)
$$
</p>

Rewriting:

<p>
$$
N(y)dy = M(x)dx
$$
</p>

Integrating both sides gives a solution for $y$.

## Exact Equations

We start with a differential equation of the form:
<p>
$$
\frac{dy}{dx} = -\frac{M(x,y)}{N(x,y)}
$$
</p>

Or equivalently, we can write:
<p>
$$
M + N\frac{dy}{dx} = 0
$$
</p>

Now, we can arrive at this same differential equation in another way. Suppose we have an implicit function $f(x,y) = c$, which describes some sort of level set of a curve. For example, we could have circles, with $f(x,y) = x^2 + y^2 = c$ defining a circle of radius $\sqrt{c}$.

Then, by the Implicit Function Theorem, assuming the Jacobian matrix of $f$ is invertible, then we can write:

<p>
$$
f(x,y(x)) = c
$$
</p>

In other words, we can write $y$ in terms of $x$. Furthermore, $dy/dx$, the rate of change, can be computed:
<p>
$$
\frac{dy}{dx} = - \frac{\frac{\partial f}{\partial x}}{\frac{\partial f}{\partial y}}
$$
</p>

So instead of studying the above differential equation, we study the related implicitly defined surface with $f(x,y)=c$ for some constant, such that $f_x = M, f_y = N$ (where $f_x$ denotes the partial derivative $\frac{\partial f}{\partial x}$). It isn't too hard to find such a function $f$ in general by integrating $M$ with respect to $x$ and $N$ with respect to $y$.

We could equivalently say that we can check for exactness with the necessary and sufficient condition that $M_y = N_x$, and then use the above method.

##### Example

Let us look at: $\frac{dy}{dx} = -\frac{x}{y}$ defined in an open set away from $y=0$. We have $M=x, N=y$ (note: you can pick other pairs, such as $M=2x, N=2y$ and the only thing that will change is our choice of constant). It is not hard to see by integration that we can pick $f(x,y) = x^2 + y^2 = c$. So instead of solving the above differential equation, we simply use the initial conditions to find $c$ and then solve for $y$ in terms of $x$.

## Existence and Uniqueness

How do we assure existence and uniqueness of solutions to a first order differential equation?

##### Theorem

>If $p(x), g(x)$ are continuous in an open interval $I$ containing $x=x_0$, then there exists a unique function $y(x)$ satisfying the equation:
><p>
$$
y' + p(x)y = g(x)
$$
></p>
>As well as the initial condition $y(x_0) = 0$ for each $x\in I$.

The proof of existence is given by construction in the "integrating factors" method. Uniqueness is guaranteed by the continuity of $p,g$. This tells us that linear first order differential equations have unique solutions.

##### Theorem

>Let $f(x,y)$ be a real-valued function with continuous derivative $\frac{\partial f}{\partial y}$ which is continuous in some rectangle in the plane containing the point $(x_0, y_0)$. As a stronger condition, we could simply set $f$ to be differentiable in some rectangle. Then in some interval $(x_0 - h, x_0+h)$, there is a unique function $y=\phi(x)$ such that:
><p>
$$
\phi(x)' = f(x,y)
$$
></p>
><p>
$$
\phi(x_0) = y_0
$$
></p>
>For a given $y_0$.

This tells us that, given certain conditions, we can even have unique solutions to non-linear first order differential equations satisfying initial conditions (namely ,we just need $y' = f(x,y)$ continuous with $f_y$ continuous).

##### Euler's Method

To approximate a solution, we could set a sufficiently small parameter $h$ and walk a distance $h$ the tangent line at any point. The error is the quadratic term of the Taylor expansion; by making $h$ sufficiently small, we can remain close to the curve. We can also create $n$ equations, called "finite difference equations", expressing $y_n$, a value at stage $n$, in terms of $y_{n-1}$ recursively. In these cases, it is useful to consider the equilibrium solutions $y_n = y_{n+1}$.

# Second Order Linear Equations

We move onto second order linear differential equations. First, we need a theorem that tells us what kinds of solutions exist for differential equations.

## Existence and Uniqueness

We need a suitable theorem guaranteeing uniqueness. The theorem goes just as we expected:

##### Theorem

Let $p,q,r$ be continuous in an interval $I$. Then the differential equation:

<p>
$$
y'' + py' + qy = r
$$
</p>

With initial conditions $y(t_0) = y_0$ and $y'(t_0)= v_0$, has a unique solution in the interval.

We start with looking at the simplest type of second order linear differential equations. To make things simple, we set the coefficients to be constants, and the right hand side to be zero.

## Homogeneous Equations with Constant Coefficients

We have a differential equation of the form:
<p>
$$
ay'' + by' + cy = 0
$$
</p>

Such an equation where the right hand side is zero is called a **homogeneous** equation.

We could then we could use a trial solution $y= e^{rt}$, which yields the associated **auxiliary equation (or characteristic equation)**:

<p>
$$
ar^2 + br + c = 0
$$
</p>

Since $e^{rt} \ne 0$. Solving this yields two solutions.

As an alternative way of writing this, we can call the derivative $D$ with $Df = f', D^2f = f''$, etcetera. Then the differential equation becomes:

<p>
$$
(aD^2 + bD + c)y =0
$$
</p>

And to get a nontrivial solution $y\ne 0$, we solve the same auxiliary equation for $D$.

First note that for a homogeneous linear equation, linear combinations of solutions yield solutions; this creates a vector space structure for the solutions.

This is called the **superposition principle**: for any two solutions to a homogeneous linear equation, any linear combination of the solutions is also a solution.

In general, for a linear constant coefficient differential equation of order $n$, the space of solutions is dimension $n$. So we only need to construct $n$ linearly independent solutions, which we do as follows:

- For a real root, we use $e^{rt}$.
- For a real root repeated with multiplicity $m$, we add $e^{rt}, te^{rt},...,t^{m-1}e^{rt}$. You can check that these are all solutions to the differential equation $(D-r)^m y = 0$ and are linearly independent away from $t=0$.
- For complex roots $a\pm bi$ we can write $e^{at}\cos bt, e^{at}\sin bt$.
- For repeated complex roots $a\pm bi$ we can write $e^{at}\cos bt, e^{at}\sin bt, te^{at}\cos bt, te^{at}\sin bt$, etcetera.

## Linear Independence

As mentioned earlier, the solutions to a linear homogeneous differential equation of order $n$ on an interval $I$ form a vector space of order $n$. So what we're looking for is a basis of solutions. The above construction gives us $n$ solutions, so we need to check that they are linearly independent; if they are, we have indeed found a basis.

**Definition:** Let $f_1, f_2, ... f_n$ be a set of smooth functions on an interval $I$. We look at the following equation:

<p>
$$
c_1f_1 + c_2f_2 + ... + c_nfn = 0
$$
</p>

Where $c_i$ are constants. Note that by $0$ here we are denoting the zero function; in other words, this equation should hold for all inputs $x$. 

If we can find a solution where at least one $c_i$ is nonzero, we call the functions **linearly dependent** on the interval; if instead the only solution has each $c_i =0$, the functions are called **linearly independent**.

---

If we can find a solution $c_i$, it is clear that the above equation still holds when we take the derivative of both sides (and thus the second derivative, third derivative, etc). Thus, if the set $f_i$ is linearly independent, then we have a non-trivial solution to the following system of equations.

<p>
$$
\begin{bmatrix}
f_1 && ... && f_n \\
\vdots && \ddots && \vdots \\
f_1^{n-1} && ... && f_n^{n-1}
\end{bmatrix}
\begin{bmatrix}
c_1 \\
\vdots\\
c_n
\end{bmatrix}
=
\begin{bmatrix}
0 \\
\vdots\\
0
\end{bmatrix}
$$
</p>

This system of equations has a nontrivial solution if and only if:

<p>
$$
\det
\begin{bmatrix}
f_1 && ... && f_n \\
\vdots && \ddots && \vdots \\
f_1^{n-1} && ... && f_n^{n-1}
\end{bmatrix}
= 0
$$
</p>

**Definition:** For functions $f_1,...f_n$, the above determinant is called the **Wronskian** of $f_1,...f_n$, denoted $W(f_1,...f_n)$. The above matrix is called a **fundamental matrix**.

Now, we can leverage our knowledge of linear algebra to state the following theorem.

##### Theorem

Let $f_1,...f_n$ are solutions to an order $n$ linear homogeneous differential equation in an interval. Then, $f_1,...f_n$ are linearly independent if and only if the Wronskian $W(f_1,...,f_n)$ is nonzero somewhere in the interval.

## Reduction of Order

So how exactly did we come to the above construction of solutions for repeated roots in a linear constant coefficient homogeneous equation? The answer lies in the method known as reduction of order.

Suppose we have a linear differential equation of the form:
<p>
$$
y'' + p(t)y'' + q(t)y = r(t)
$$
</p>

With $p,q,r$ continuous and $r$ possibly zero. And suppose that we know some solution $y_1$ (with continuous derivative) which is never zero in an interval. Then, we can try a solution of the form $y_2=vy_1$ for some twice differentiable function $v$. Substitution and some algebra yields:

<p>
$$
v'' + \left( \frac{2y_1'}{y_1}+p \right)v' = \frac{r}{y_1}
$$
</p>

Since this is a linear first order differential equation and $y_1', p, r$ are assumed to be continuous with $y_1$ nonzero, we know there is a unique solution in our interval.

Note that though we are essentially dealing with a first order differential equation for $v'$, when we integrate $v'$ we obtain an integration constant. We can WLOG write $v = \tilde{v}+c$, and thus write:
<p>
$$y_2 = \tilde{v}y_1 + cy_1$$</p>

As we expected, we end up with two integration constants: the first comes from solving the above differential equation for $v'$; the second comes from integrating $v$. With two initial conditions, then, we can solve for these two constants uniquely.

Thus, we can use reduction of order to solve a general (homogeneous or non-homogeneous) 2nd order linear differential equation where we know one solution.

##### Example

Take a constant coefficient differential equation with repeated roots, such as $(D-r)^2y = (D^2 - 2Dr + r^2)y = 0$. We already have a solution of the form $e^{rt}$, so we set:

<p>
$$
y = ve^{rt}
$$
</p>

We know that $y_1 = e^{rt}, y_1' = re^{rt}$ Our equation for $v$ becomes:

<p>
$$\begin{aligned}
v'' + \left( \frac{2y_1'}{y_1}+ 2p \right)v' &= \frac{r}{y_1} \\
v'' &= 0 \\
\end{aligned}$$
</p>

Thus, we have $v = at +b$, for some real coefficients $a,b$. Our linearly independent solution to the differential equation is then:

<p>
$$\begin{aligned}
y = vy_1 = ate^{rt} + be^{rt}
\end{aligned}$$
</p>

And for simplicity sake, we can set $a=1, b=0$ and still have a linearly independent pair.

## General Solutions to Non-Homogeneous Linear Differential Equations

Suppose we are working with a second order linear equation:

<p>
$$
y'' + p(t)y'' + q(t)y = r(t)
$$
</p>

And suppose we have two solutions to the above equation, $y_1$ and $y_2$. Then, we know the following:

<p>
$$\begin{aligned}
y_1'' + p(t)y_1'' + q(t)y_1 &= r(t) \\
y_2'' + p(t)y_2'' + q(t)y_2 &= r(t) \\
(y_1-y_2)'' + p(t)(y_2-y_1)' +q(t)(y_2-y_1) &= 0
\end{aligned} $$
</p>

So, $y_1-y_2$ is a solution to the associated homogeneous equation! This is useful for the following theorem that allows us to solve non-homogeneous linear differential equations.

##### Theorem

Suppose we have have a linear, non-homogeneous differential equation. Then the general solution can be written:

<p>
$$\begin{aligned}
y(t) = y_c + y_p
\end{aligned} $$
</p>

Where $y_c$ is a solution of the associated homogeneous equation, called the **complementary solution**, and $y_p$ is one particular solution of the homogeneous equation, called the **particular solution**.

From now on, we will call a linearly independent set of solutions $y_1,...,y_n$ to a homogeneous equation, a set of **fundamental solutions** (which, accordingly, fill out the first row in a fundamental matrix). We can then rewrite the above solution:

<p>
$$\begin{aligned}
y(t) = \sum\limits_{i=1}^n c_iy_i + y_p
\end{aligned} $$
</p>

Where the coefficients $c_i$ can be solved for if we are given $n$ initial conditions.

---

This theorem gives us a method of solving a general non-homogeneous linear differential equation:

- Solve the associated homogeneous equation to get a general solution $c_1y_1+...+c_ny_n$.
- Find one solution of the non-homogeneous equation $y_p$.
- Sum the two quantities above to obtain a general solution of the non-homogeneous equation.
- Use $n$ initial conditions to solve for $c_i$ in the complementary solution.


##### The Method of Undetermined Coefficients

We first covered the case where we are working with a linear constant coefficient homogeneous differential equation. Using the previous section, we know that a general solution to a non-homogeneous linear equation can be written as $y=y_c+y_p$. Let's take a look at a special case where we can solve for such a solution easily.

Using the technique from earlier of writing first derivatives as $D$, second derivatives as $D^2$, etcetera, we can indeed write a **linear differential operator**, or a polynomial function of $D$. For example:

<p>
$$\begin{aligned}
y'' + y &= 0 \\
(D^2 + 1)y &= 0 \\
P(D)y &= 0
\end{aligned} $$
</p>

Where $P(D) = D^2 + 1$ is a polynomial in $D$.

##### Conditions

Suppose we are working with a non-homogeneous differential equation of the form:

<p>
$$\begin{aligned}
P(D)y = F(t)
\end{aligned} $$
</p>

And further suppose that $F(t)$ is a solution of some linear homogeneous constant coefficient equation $A(D)y = 0$. We call $A(D)$ an **annihiliator** of $F(t)$.

Because we know what these kinds of solutions look like, that means that $F(t)$ could be:
- $F(t)$ is of the form $t^k e^{rt}$ for some real number $r$ and non-negative integer $k$.
- $F(t)$ is of the form $c_1t^k e^{at}\cos (bt) + c_2 t^k e^{at} \sin (bt)$, where $a,b,c_1,c_2$ are real and $k$ is non-negative.
- $F(t)$ is a linear combination of the above forms of solutions.

In this case, we can "multiply" both sides by $A(D)$ to get a higher order homogeneous equation:

<p>
$$\begin{aligned}
A(D)P(D)y = A(D)F(t) = 0
\end{aligned} $$
</p>

And we know exactly how to solve this kind of equation. Note that if $y$ is a solution to $P(D)y = 0$, then $y$ is a solution to $A(D)P(D)y = 0$. This fact will become important in just a second.

##### Finding a Solution

From our theorem, we know that the solutions to $P(D)y=F(t)$ are of the form $y=y_c +y_p$, where $P(D)y_c = 0$. So the first thing we do to solve our equation is find the complementary solutions $y_c$ using above methods.

Next, we solve $A(D)P(D)y = 0$ to obtain a set of solutions $c_1y+1 + ... + c_ky_k$. As we noted before, every solution of our target non-homogeneous differential equation is also a solution to the equation $A(D)P(D)y=0$, and is thus of the form $c_1y_1 + ... + c_ky_k$. Furthermore, from computing the complementary solutions we know that $y_c = c_1y_1 + ... + c_ny_n$ for some $n < k$. Thus, we know that $y_p = y - y_c$ is of the form $c_{n+1}y_{n+1} + ... + c_ky_k$. 

Finally, substituting into the equation $P(D)y_p = F(t)$, we can solve for these coefficients; hence the name, the method of undetermined coefficients. Once we have $y_p$, we can write our general solution $y=y_c+y_p$.

To summarize the method:
- Find an annihilator $A(D)$ of $F(t)$.
- Find the complementary solution $y_c$ by solving the equation $P(D)y_c = 0$.
- Solve the equation $A(D)P(D)y = 0$, obtaining a solution of the form $\tilde{y} = y_c + y_p$, where $y_p$ is written as a linear combination of other functions with unknown coefficients.
- Substitute $y_p$ into the equation $P(D)y_p = F(t)$ to solve for the undetermined coefficients.
- Write solutions to the differential equation as $y=y_p+y_c$.
- Given $n$ initial conditions, solve for the coefficients in $y_c$.

## Summary

With these tools, we can do the following for linear differential equations:
- Guarantee the existence and uniqueness of solutions to the equation on an interval.
- Check if solutions to a differential equation are linearly independent.
- Given one solution to a second-order equation, we can find another linearly independent solution using reduction of order, thus completely solving the equation.
- Given a constant coefficient homogeneous equation, we can find all the solutions.
- Given a non-homogeneous constant coefficient equation of a particular form, we can use the method of undetermined coefficients to find all the solutions.

In the next section, we tackle the problem of finding solutions to arbitrary non-homogeneous equations of any order.

# Higher Order Linear Equations

We move onto higher order linear differential equations. As before, we need some suitable existence and uniqueness theorem which works for the general case.

## Existence and Uniqueness

In general, a linear differential equation is of the form:

<p>
$$
a_ny^{(n)} + a_{n-1}y^{(n-1)} + ... + a_0y = g(t)
$$
</p>

Where $a_n$ are functions and $y^{(n)}$ represents the $n$th derivative of $y$.

##### Theorem

>Suppose we have a linear differential equation with coefficients $a_i(t)$ and right hand side equal to $g(t)$ defined in an interval $I$. Then, given $n$ initial conditions $y^{(n)}(t_0) = c_n$, there exists a unique solution to the differential equation in the interval.

Note that we already know how to solve this equation in many cases by borrowing techniques from the first two chapters:

- If the coefficients are constant and the right hand side is zero, we use the same methods as in Chapter 2.

- If the coefficients are constant and the right hand side is of a particular form, we can use the method of undetermined coefficients.

- If we know one solution, we can reduce our order $n$ equation into an order $n-1$ equation using the method of reduction of order.

Furthermore, we still know the form of a general solution of a non-homogeneous linear equation as a sum of a complementary and a particular solution; and the Wronskian can still be used to check for linear independence of solutions. The following theorem tells us that the solution space for a homogeneous equation is exactly dimension $n$.

##### Theorem

>Suppose we have an equation of the form:
><p>
$$
a_ny^{(n)} + a_{n-1}y^{(n-1)} + ... + a_0y = 0
$$
></p>
>Where $a_i$ are continuous on an interval. Then, if we find $y_1,y_2,...y_n$ linearly independent solutions to the equation, then every solution can be expressed as a linear combination of $y_1,...,y_n$. 

We call such a solution set a **fundamental set of solutions**.

## Variation of Parameters

Finally, we arrive at the most important tool we have for solving a non-homogeneous $n$th order linear differential equation.

Suppose we have an equation of the form:
<p>
$$
y^{(n)} + a_{n-1}y^{(n-1)} + ... + a_0y = f(t)
$$
</p>

In other words, the first coefficient is $1$.

Taking the associated homogeneous equation, let $y_1,...,y_n$ be its fundamental solutions. Then we try to find a solution to the non-homogeneous equation of the form:
<p>
$$
y = u_1y_1 + u_2y_2 + ... +u_ny_n
$$
</p>

Where $u_i$ are functions.

To solve uniquely for each $u_i$, we need $n$ equations. To find them, we first take the derivative of $y$:

<p>
$$
y' = \sum\limits_{i=1}^{n} u_i'y_i + u_i y_i'
$$
</p>

To make things easier for us, we set the condition $\sum\limits_{i=1}^{n} u_i'y_i = 0$. Taking the second derivative, we get:

<p>
$$
y' = \sum\limits_{i=1}^{n-1} u_i'y_i + u_i y_i'
$$
</p>

And similarly, we set the condition $\sum\limits_{i=1}^{n} u_i'y_i' = 0$. Repeating this process until we hit the $n-1$th derivative, we get $n-1$ conditions. The final condition comes from substituting in our trial solution into the differential equation:

<p>
$$
y^{ (n) } + a_{n-1}y^{(n-1)} + \dots + a_0y = f(t)
$$
</p>

Now substituting in $y^{(n)} = \sum\limits_{i=1}^n u_iy_i^{(n)} + u_i' y_i^{(n-1)}$, we get:

<p>
$$
\sum\limits_{i=1}^n u_iy_i^{(n)} + u_i' y_i^{(n-1)} + a_{n-1} \sum u_iy_i^{(n-1)} + ... + a_0 \sum u_iy_i = f(t)
$$
</p>

But note that for each $y_i$, since it is a solution to the associated homogeneous equation, we have:

<p>
$$
y_i^{(n)} + a_{n-1} y_i^{(n-1)} + ... + a_0y_i = 0
$$
</p>

So most of these terms drop out! The only terms that remain give us:

<p>
$$
\sum\limits_{i=1}^n u_i' y_i^{(n-1)} = f(t)
$$
</p>

To summarize, our conditions look like:

<p>
$$\begin{aligned}
u_1' y_1 + ... + u_1'y_n &= 0 \\
u_1' y_1' + ... + u_1'y_n' &= 0 \\
\vdots \\
u_1' y_1^{(n-1)} + ... + u_1'y_n^{(n-1)} &= f(t)
\end{aligned}$$
</p>

And to put this in matrix form:

<p>
$$
\begin{bmatrix}
f_1 && ... && f_n \\
\vdots && \ddots && \vdots \\
f_1^{n-1} && ... && f_n^{n-1}
\end{bmatrix}
\begin{bmatrix}
u_1 \\
\vdots \\
u_n
\end{bmatrix}'
=
\begin{bmatrix}
0 \\
\vdots \\
f(t)
\end{bmatrix}
$$
</p>

So, as long as $W \ne 0$, we can solve for $u_i'$ and thus integrate to find $u_i$.

##### Summary of Method

Suppose we have an equation of the form:
<p>
$$
y^{(n)} + a_{n-1}y^{(n-1)} + ... + a_0y = f(t)
$$
</p>

Where we have a set of fundamental solutions $y_i$ to the associated homogeneous equation. Then, we can write a solution as:

<p>
$$
y = u_1 y_1 + ... + u_n y_n
$$
</p>

Where $u_i$ are found by solving the equation:

<p>
$$
\begin{bmatrix}
f_1 && ... && f_n \\
\vdots && \ddots && \vdots \\
f_1^{n-1} && ... && f_n^{n-1}
\end{bmatrix}
\begin{bmatrix}
u_1 \\
\vdots \\
u_n
\end{bmatrix}'
=
\begin{bmatrix}
0 \\
\vdots \\
f(t)
\end{bmatrix}
$$
</p>

# Systems of First Order Linear Equations

We now generalize to first-order systems of linear equations, in other words systems of the form:

<p>
$$\begin{aligned}
x_1' &= a_{11}x_1 + ... + a_{1n}x_n + b_1 \\
x_2' &= a_{21}x_1 + ... + a_{2n}x_n + b_2 \\
\vdots \\
x_n' &= a_{n1}x_1 + ... + a_{nn}x_n + b_n
\end{aligned}$$
</p>

Where $a_{ij}(t)$ and $b_i(t)$ are functions. Of course, we can write this in matrix form as:

<p>
$$
\begin{bmatrix}
x_1 \\
\vdots \\
x_n
\end{bmatrix}'
=
\begin{bmatrix}
a_{11} && ... && a_{1n} \\
\vdots && \ddots && \vdots \\
a_{n1} && ... && a_{nn}
\end{bmatrix}
\begin{bmatrix}
x_1 \\
\vdots \\
x_n
\end{bmatrix}
+
\begin{bmatrix}
b_1 \\
\vdots \\
b_n
\end{bmatrix}
$$
</p>

Or more succinctly, writing $x$ as the vector with $x_i$ as its entries, we can write:

<p>
$$
\textbf{x'} = A\textbf{x} + \textbf{b}
$$
</p>

By analogy, we say that the equation is **homogeneous** if $\textbf{b} = 0$. A solution is written as a vector with the $i$th entry representing a solution for the $i$th equation.

As an analogy with the dimension $1$ case, we have the **superposition principle**, which states that for solutions $x_1, x_2$ to a homogeneous linear system, $c_1x_1 + c_2x_2$ yields a solution for any constants $c_1,c_2$.

From here on out, we will focus on homogeneous systems, and later on discuss non-homogeneous systems using the methods outlined earlier.

As before, we start with the guarantee of existence and uniqueness of solutions.

## Existence and Uniqueness

Suppose we have a linear system defined on an interval:

<p>
$$
\textbf{x'} = A\textbf{x} + \textbf{b}
$$
</p>

With initial conditions given by the vector equation $\textbf{x}(t_0) = x_0$. Then, if the entries of $A$ and the entries of $\textbf{b}$ all continuous functions in the interval, there is a unique solution vector $\textbf{x}(t)$ which exists throughout the interval.

## Linear Independence

Perhaps more concretely, we can see that a homogeneous system of equations should have $n$ linearly independent solutions (and in fact, this implies our earlier result that an order $n$ linear equation ought to have $n$ linearly independent solutions).

This makes sense because, if we evaluate both sides of the matrix equation at a particular point, we have nothing more than an $n\times n$ matrix system of equations.

**Definition:** Let $x_1,...,x_n$ be a set of solutions to a homogeneous linear system. Then the matrix $X(t)$ with these vectors as its columns is called the **fundamental matrix**:

<p>
$$
X = \begin{bmatrix} x_1 && x_2 && \dots &&  x_n \end{bmatrix}
$$
</p>

The determinant of $X$ is called the **Wronskian** of $x_1,\dots,x_n$.

We now have essentially the same criteria for independence: **a set of solutions is linearly independent at a point if and only if their Wronskian is nonzero there.**

If the Wronskian is nonzero, we call $x_1,\dots,x_n$ a set of **fundamental solutions**, as before.

Furthermore, we want to say something like the earlier theorem which guarantees that every solution can be written as a combination of enough linearly independent solutions.

##### Theorem

>If the vector functions $x_1,\dots,x_n$ are linearly independent solutions of an order $n$ linear system in an interval, then each solution for the system can be written uniquely as a combination (there is only one choice for each $c_i$):

<p>
$$
x = c_1 x_1 + \dots c_nx_n
$$
</p>

We accordingly will call the form $c_1x_1 + \dots c_nx_n$ the **general solution**, and given a vector of initial conditions $x(0) = x_0$, we can indeed set $t=0$ and solve for the coefficients in the general linear algebra way.

##### Theorem

>Given a set of solutions to an order $n$ linear system $x_1,\dots,x_n$, then in an interval $\alpha < t < \beta$, the Wronskian is either zero everywhere or never vanishes.

<br>

This theorem makes our lives a lot easier. We know how to check linear independence at a point by taking the Wronskian at that point. Now we can further say that all we have to do is check a single point, and we have linear independence in an entire interval.

The proof, while interesting, will be ommitted since it doesn't add much to our dsicussion of differential equations.

The last thing we should do is, as promised, guarantee that a set of $n$ fundamental solutions exists, i.e. that there are $n$ linearly independent solutions to our equation.

##### Theorem

>In particular, suppose we have a linear system $x'=Ax$ and solve this system with the initial condition that $X(t_0)=I$ (i.e, $x_i(t_0)$ is the $i$th column of the identity matrix). Then, $x_1,\dots,x_n$ form a fundamental set of solutions.

To prove this theorem, first we know that for each row $I_j$ of the identity matrix, we have the existence and uniqueness of a solution to the equation $x_j' =Ax_j$ with $x(t_0) = I_j$. And it isn't hard to see that if we pick $t=t_0$, our fundamental matrix is defined to be the identity matrix, which has nonzero determinant. From our earlier theorem, this tells us that $x_1,\dots,x_n$ are linearly independent throughout the interval, and thus form a fundamental set of solutions.

Our last theorem guarantees a nice result for complex solutions.

##### Theorem

>Consider a linear system $x'=Ax$, where each entry of $A$ is continuous and real-valued in an interval. Then, if we have a complex solution $x = u(t) + iv(t)$, both its real parts and its complex parts are solutions to the original equation.

This theorem becomes clear by taking the derivative of $x$, and then noticing both sides of the equation have to agree in both the real and imaginary parts.

##### Summary

The general theory for linear systems tells us:

* If $A,b$ are continuous and initial conditions are given, then a solution $x'=Ax+b$ exists and is unique in an interval.

* For a linear system, there exists at least one set of $n$ fundamental solutions $x_1,\dots,x_n$, for which the Wronskian is nonzero at a point. If the Wronskian is nonzero at a point, it is nonzero throughout an interval.

* Every solution can be written as a linear combination of fundamental solutions, with the coefficients determined by the initial conditions.

## Connection to Higher Order Linear Equations

We can transform a higher order linear equation into a matrix system as above, and thus everything we proved in the last system about the theory of higher order linear equations is just a special case. As an example, look at the second order homogeneous equation:

<p>
$$
y'' + a_1y' + a_0y = 0
$$
</p>

We can pick a vector $y = \begin{bmatrix} y \\ y' \end{bmatrix}$. Solving for $y''$, we obtain $y'' = -(by + ay')$, so we get a system of equations:
<p>
$$
\begin{bmatrix} y \\ y' \end{bmatrix}' = \begin{bmatrix} 0 && 1 \\ -a_0 && -a_1 \end{bmatrix} \begin{bmatrix} y \\ y' \end{bmatrix}
$$
</p>

Note that the determinant of the coefficient matrix is simply $a_0$. We could do the same thing for a third order equation to obtain:

<p>
$$
\begin{bmatrix} y \\ y' \\ y'' \end{bmatrix}' = \begin{bmatrix} 0 && 1 && 0 \\ 0 && 0 && 1 \\ -a_0 && -a_1 && -a_2 \end{bmatrix} \begin{bmatrix} y \\ y' \\ y''\end{bmatrix}
$$
</p>

And here the determinant is $-a_0$.

It is not hard to see that in general, we can turn an order $n$ linear differential equation into an order $n$ linear system. The determinant of the coefficient matrix will always be $\pm a_0$, In particular, if $a_0=0$ at a point, we are indeed left with an order $n-1$ equation, since $y$ does not appear in the equation at all.

We now move on to solving systems of equations with constant coefficients.

## Homogeneous Linear Systems With Constant Coefficients

As before, we start with the simplest case, in which all the coefficients are constant and the right hand side is zero. We come up with a trial solution.

Suppose that $v$ is an eigenvector of the matrix $A$ with eigenvalue $\lambda$. Then any multiple of $v$ is also an eigenvector of $x$ with eigenvalue $\lambda$.

In particular, the equation $v'=Av$ becomes $v' = \lambda v$ for any eigenvector. So we pick $x = e^{\lambda t} v$, thus solving our equation since $x' = \lambda e^{\lambda t}v = \lambda x$.

This means that if $A$ has $n$ real, distinct eigenvalues, then we're done, since eigenvectors for distinct eigenvalues are linearly independent -- so we have found a fundamental set of solutions. But as you might expect, there are other cases than that.

### Complex Eigenvalues

First, we know that complex eigenvalues occur in conjugate pairs. We can tell this because when finding eigenvalues, we solve a polynomial with real coefficients, and such polynomials have conjugate pair roots. It is not hard to see that eigenvectors, as well, occur in conjugate pairs.

Suppose we have such a complex pair of eigenvalues, $\lambda \pm i\mu$. Then using the same methods outlined above, we have a solution:

<p>
$$
x = (a+bi)e^{(\lambda + i\mu)t}
$$
</p>

Where $a,b$ are vectors which are the real and imaginary parts of an eigenvector. But we can use Euler's identity $e^{it} = \cos t + i \sin t$, and rearrange to get:

<p>
$$
x = e^{\lambda t}(a \cos \mu t - b\sin \mu t) + ie^{\lambda t}(a \sin \mu t + b\cos \mu t)
$$
</p>

We know from an earlier theorem that both the real and the imaginary parts of this expression are solutions to the differential equation. So instead of writing two complex solutions, we can write two real solutions instead:

<p>
$$\begin{aligned}
x_1 &= e^{\lambda t}(a \cos \mu t - b\sin \mu t) \\
x_2 &= e^{\lambda t}(a \sin \mu t + b\cos \mu t)
\end{aligned}$$
</p>

### Repeated Eigenvalues

Say we have an eigenvalue $\lambda$ which is repeated in the characteristic equation. If there are $n$ linearly independent eigenvectors associated with $\lambda$, we are done; the problem is when there are not. Earlier in the 1 dimensional case, when we had an issue of repeated roots in a characteristic equation, we picked $te^{\lambda t}$ as a trial solution. We did this by performing reduction of order to get a linearly independent solution of the form $c_1e^{rt} + c_2te^{rt}$, and setting $c_1=0$. We will apply a similar trick here.

Suppose $x_0 = e^{\lambda t} v$ is a solution to the equation $x' = Ax$, where $v$ is an eigenvector for eigenvalue $\lambda$. Then we try to construct another solution of the form:

<p>
$$\begin{aligned}
x_1 = te^{\lambda t}v + e^{\lambda t}w
\end{aligned}$$
</p>

Setting $x_1' = Ax$, and noting $A \left( e^{\lambda t} v \right) = \lambda \left( e^{\lambda t} v \right)$ we have:

<p>
$$\begin{aligned}
x_1' &= e^{\lambda t}v + \lambda t e^{\lambda t} v + \lambda e^{\lambda t}w \\
Ax_1 &= \lambda t e^{\lambda t} v + Ae^{\lambda t}w
\end{aligned}$$
</p>

Cancelling the equal terms and setting the two equal, we get:

<p>
$$\begin{aligned}
v = \left(A - \lambda I \right)w
\end{aligned}$$
</p>

Because we know that $(A-\lambda I) v = 0$, we can equivalently write:

<p>
$$\begin{aligned}
\left(A - \lambda I \right) ^2 w = 0
\end{aligned}$$
</p>

This is the essential idea behind constructing solutions to matrix systems of differential equations with repeated eigenvalues. Our solution looks like:
<p>
$$\begin{aligned}
x_1 = te^{\lambda t}v + e^{\lambda t}w
\end{aligned}$$
</p>

Where $(A-\lambda I)w = v$.

**Definition:** A vector $w$ is called a **generalized eigenvector** of rank $m$ of $A$ if we have:
<p>
$$\begin{aligned}
\left(A - \lambda I \right)^m w &= 0 \\
\left(A - \lambda I \right)^{m-1} w &\ne 0
\end{aligned}$$
</p>

Note that if $w$ is a generalized eigenvector of rank $m$, then $(A-\lambda I)w$ is a generalized eigenvector of rank $m-1$, and so on. By repeating this process, we can get a chain of $m-1$ generalized eigenvectors called a **Jordan chain**. Jordan chains are linearly independent. Note that the last vector in this chain is a generalized eigenvector of rank $1$, which is just an eigenvector.

##### Theorem

> Every $n\times n$ matrix has a set of linearly independent generalized eigenvectors.

This theorem allows us to construct $n$ linearly independent solutions. In fact, if you're familiar with linear algebra, this is equivalent to stating the existence of the Jordan canonical form.

##### Method For Solving

We aim to solve $x'=Ax$, in general. For each eigenvalue $\lambda$, we look at the equation $(A-\lambda I)v = 0$.

* Compute the solutions to $(A-\lambda I)^m v =0$ for each $m$ until $(A-\lambda I)^{m} = 0$.

* Pick a vector $v_{m}$ such that $(A-\lambda I)^m v =0$ but $(A-\lambda I)^{m-1} v \ne 0$. This is called a generalized eigenvector of rank $m$.

* Compute the associated Jordan chain, with $v_m$ as chosen above, $v_{m-1} = (A-\lambda I)v_m$, $v_{m-2} = (A-\lambda I)^2 v_m$ etc.

* Use the Jordan chain above to construct the following linearly independent solutions to the differential equation:
<p>
$$\begin{aligned}
x_1 &= e^{\lambda t} v_1 \\
x_2 &= te^{\lambda t}v_1 + e^{\lambda t}v_2 \\
x_3 &= \frac{t^2}{2!} e^{\lambda t}v_1 + t e^{\lambda t} v_2 + e^{\lambda t} v_3 \\
&\vdots \\
x_{m} &= e^{\lambda t} \left( \sum\limits_{i=1}^{m} \frac{t^{k-1}}{(k-1)!}v_i \right)
\end{aligned}$$
</p>

* If we need more solutions, pick a linearly independent generalized eigenvector of rank $k$ and repeat this process.

With some knowledge of linear algebra, you can say that in a sense, the Jordan chains are uniquely determined. That is to say, we can say the $\lambda$ has a certain number of Jordan chains with certain sizes, and these sizes are fixed. However, that's outside of the scope of these notes for now.

## Non-Homogeneous Linear Systems

We now move to a discussion of linear systems of the form:
<p>
$$\begin{aligned}
x' = Ax + b
\end{aligned}$$
</p>

Where once again, the entries of $A,b$ are continous to guarantee a solution. By the same exact argument we made before, we can write the solution to any such equation in the form:

<p>
$$\begin{aligned}
x = c_1x_1 + \dots + c_n x_n + v
\end{aligned}$$
</p>

Where $x_i$ form a set of fundamental solutions to the associated homogeneous equation (something like a complementary solution), and $v$ is a solution to the non-homogeneous equation (a particular solution). Furthermore, we can use matrix multiplication to rewrite:

<p>
$$\begin{aligned}
x = Xc + v
\end{aligned}$$
</p>

Where $c = \begin{bmatrix}c_1 \\ \dots \\ c_n \end{bmatrix}$ is a vector of coefficients. We start with a simple case

### Diagonalization

Let's say $A$ is a diagonalizable matrix. From linear algebra, this means $A$ can be written as $A = SDS^{-1}$, where $D$ is a diagonal matrix. If this is the case, then we can perform a change of variables by picking $x=Sy$ or equivalently, $y=S^-1x$. Then we have:

<p>
$$\begin{aligned}
x' &= Ax + b \\
Sy' &= SDS^{-1}Sy + b \\
Sy' &= SDy + b \\
y' &= Dy + b
\end{aligned}$$
</p>

Since $D$ is a diagonal matrix, this reduces to a set of first order equations:
<p>
$$\begin{aligned}
y_1' &= \lambda_1 y_1 + b_1 \\
y_2' &= \lambda_1 y_2 + b_2 \\
\vdots \\
y_n' &= \lambda_n y_n + b_n \\
\end{aligned}$$
</p>

We have effectively uncoupled the equations; instead of solving them simultaneously, we can now solve them separately, and to get $x$ we apply the transformation $x=Sy$. If $b=0$, we have the manifest solution $y_i = c_i e^{\lambda t}$. If $b\ne 0$, we still have a set of first order linear equations, which we know we can solve from the first chapter. In the next chapter we'll see another way of solving this type of differential equation.

### Variation of Parameters

Recall that given a set of solutions to the associated homogeneous equation, we used the variation of parameters method to find a solution for the non-homogeneous equation by writing $y = u_1 y_1 + \dots + u_n y_n$ for some functions $u_i$. We can do the same thing for matrix systems.

Assume we have already found a fundamental matrix $X$ for the associated equation $x' = Ax$. Then we search for a solution for the non-homogeneous equation of the form $x = Xu$, where $u$ is any vector of functions. Differentiating, we get:
<p>
$$\begin{aligned}
x' &= Ax + b \\
X'u + Xu' &= AXu + b
\end{aligned}$$
</p>

You can verify for yourself that the product rule does work for matrices. Since $X$ is a fundamental matrix, we have $X' = AX$, so we can write:

<p>
$$\begin{aligned}
Xu' &= b
\end{aligned}$$
</p>

Since the fundamental matrix has a nonzero determinant, it has an inverse, and indeed we can solve for $u$:

<p>
$$\begin{aligned}
u = \int X^{-1}b dt + c
\end{aligned}$$
</p>

Where $c$ is any constant vector. In the first part of this chapter, we discovered that higher order linear systems are special cases of matrix systems. Using that same transformation, we get exactly the setup for variation of parameters as before. The only difference is that now, the constraints that felt like odd choices before now make more sense. As long as the Wronskian is nonzero, the fundamental matrix is invertible and the method works.

# Further Topics

In this chapter, we'll take a look at various additional topics which are generally covered in a differential equations course, in no particular order.

## Series Solutions for Second Order Linear Homogeneous Equations

We look at the equations of the form:
<p>
$$
P(x)y'' + Q(x)y' + R(x)y = 0
$$
</p>

Where $P,Q,R$ are functions have convergent power series around a point $x_0$. For simplicity sake, $P,Q,R$ are generally restricted to polynomials in an intro differential equations course, and we assume that there is no common divisor for $P,Q,R$.

**Definition:** $x_0$ is called an **ordinary point** if $P(x_0) \ne 0$.

From continuity, we know that there is a small interval where $x_0 \ne 0$. In that interval, we divide through to get the differential equation:

<p>
$$
y'' + p(x) y' + q(x) y = 0
$$
</p>

And the coefficients are then continuous. Therefore, there exists a unique solution for given initial conditions in the interval.

**Definition:** $x_0$ is called an **singular point** if $P(x_0) = 0$.

At a singular point, the coefficients $p,q$ are not continuous, and solutions are not guaranteed.

We want to find solutions of the form:

<p>
$$
y = \sum\limits_{n=0}^\infty a_n(x-x_0)^n
$$
</p>

It may be helpful to review some basic facts about power series. We assume that there is some **radius of convergence** $\rho > 0$ so that if $\vert x - x_0 \vert < rho$, the series converges at $x$. In the interval of convergence, we can deal with power series term by term -- treating them essentially like polynomials.

##### Example

Let's try to solve the differential equation:

<p>
$$
y'' + y = 0
$$
</p>

At the point $t=0$, which we know has solutions $\cos t, \sin t$. Assume our solution is of the form $y = \sum\limits_{n=0}^\infty a_nx^n$, and substitute into the equation. Note that power series can be differentiated term by term:

<p>
$$\begin{aligned}
y'' + y &= 0 \\
\end{aligned}$$
</p>

We can take derivatives to get:

<p>
$$\begin{aligned}
y'' = \sum\limits_{n=0}^\infty n(n-1)a_nx^{n-1}
\end{aligned}$$
</p>

And renumbering the indices, we can rewrite:

<p>
$$\begin{aligned}
y'' = \sum\limits_{n=0}^\infty (n+2)(n+1)a_{n+2}x^n
\end{aligned}$$
</p>

Adding together the series for $y'' + y$, we arrive at the following equation:

<p>
$$\begin{aligned}
y'' + y = \sum\limits_{n=0}^\infty \left[ (n+1)(n+2)a_{n+2} + a_n \right] x^n
\end{aligned}$$
</p>

It is not hard to see that for this power series to be $0$, each coefficient must be $0$ (to prove this, set $x=0$ and thus the first coefficient is zero, take the derivative, and repeat this process). Therefore, we have the **recurrence relations** given by:

<p>
$$\begin{aligned}
a_{n+2} = \frac{-a_n}{(n+1)(n+2)}
\end{aligned}$$
</p>

We can solve for $a_0, a_1$ by giving initial conditions for $y, y'$. Now, let's for example, look at the first few even terms:

<p>
$$\begin{aligned}
a_2 &= \frac{(-1)a_0}{2\cdot 1} \\
a_4 &= \frac{(-1)^2 a_0}{4\cdot 3\cdot 2\cdot 1} \\
a_6 &= \frac{(-1)^3 a_0}{6 \cdot 5 \cdot 4\cdot 3\cdot 2\cdot 1}
\end{aligned}$$
</p>

In general, this pattern gives:

<p>
$$\begin{aligned}
a_{2n} = a_0\frac{(-1)^{2n}}{(2n)!}
\end{aligned}$$
</p>

But these are exactly the coefficients for the power series of $a_0 \cos x$! Looking at the odd coefficients, we similarly get the coefficients for the power series of $a_1 \sin x$. So we can indeed write our series solution:

<p>
$$\begin{aligned}
y = a_0 \cos x + a_1 \sin x
\end{aligned}$$
</p>

Just as we expected. Note that this sort of thing doesn't always happen. However, in many cases it may be useful to compute quite a few coefficients to get a reasonable approximation of solutions. In the non-homogeneous case, this is essentially the technique used in Fourier series, but that topic is generally covered in a partial differential equations course.

##### Generalizations

We considered the problem of equations of the form:

<p>
$$
P(x)y'' + Q(x)y' + R(x)y = 0
$$
</p>

Where $P,Q,R$ are polynomials, $P(x_0) \ne 0$, which we defined as an ordinary point. We wish to find more general conditions under which a solution exists. 

Assume that we have a solution $y=f(x) = \sum\limits_{n=0}^\infty a_n(x-x_0)^n$ which converges for $\vert x-x_0 \vert < \rho$. Taking the $m$th derivative $f^{(m)}$ and setting $x=x_0$, we get the equation:

<p>
$$
f^{(m)}(x_0) = m!a_m
$$
</p>

So the problem of finding the coefficients of a series solution reduces to the problem of finding $f^{(m)}$ for some solution $y=f(x)$ to the differential equation. But we know that:

<p>
$$\begin{aligned}
P(x)f'' + Q(x)f' + R(x)f &= 0 \\
f'' &= -p(x)f' - q(x)f
\end{aligned}$$
</p>

Where as before, $p=Q/P, q=R/P$. In particular at $x=x_0$, we have:

<p>
$$\begin{aligned}
f''(x_0) &= -p(x_0)f'(x_0) - q(x_0)f(x_0)
\end{aligned}$$
</p>

And therefore, if we are given initial conditions $y(x_0), y'(x_0)$, then we can solve for $a_2$ in our power series.

Similarly, we can differentiate the above expression to obtain:

<p>
$$\begin{aligned}
f''' &= -\left [ q'f + (q+p')f' + pf'' \right]
\end{aligned}$$
</p>

And thus, if $p,q$ can be differentiated, then we can solve for the third coefficient $a_3$ since all the quantities above are known at $x=x_0$. This motivates the condition we need to guarantee the existence of the power series solution. We don't just require that $p,q$ can be differentiated infinitely many times, we also require that their power series converge.

**Definition:** A function $f(x)$ is **analytic** at $f(x_0)$ if it has a Taylor series expansion which converges to $f(x)$ in some interval around $x_0$.

This motivates a stronger definition for ordinary points.

**Definition:** A point $x=x_0$ of a differential equation is **ordinary** if $p(x),q(x)$ are analytic at $x_0$; otherwise, $x_0$ is said to be a **singular** point.

Finally, the following theorem connects our new definition of an ordinary point to the existence of solutions.

##### Theorem

>If $x_0$ is an ordinary point of the above differential equation:
><p>
$$
P(x)y'' + Q(x)y' + R(x)y = 0
$$
></p>
>then, the general solution of the differential equation can be written:
><p>
$$
y = \sum\limits_{n=0}^\infty a_n (x-x_0)^n = a_0 y_1(x) + a_1 y_2(x)
$$
></p>
>Where $y_1,y_2$ are a fundamental set of solutions which are both analytic at $x_0$. The radius of convergence of $y_1,y_2$ is at least as large as the minimum radius at which the series $p,q$ both converge.

This theorem tells us that at an ordinary point (one where the coefficients are analytic), two series solutions exist, which form a set fundamental solutions. Furthermore, as long as $p,q$ both converge at a point, $y_1, y_2$ also converge at that point.

In general, once we have found a bound on our radius of convergence, the idea is to substitute $y = \sum\limits_{n=0}^\infty a_n (x-x_0)^n$ into the differential equation and see what kinds of conditions we can place on the coefficients.

## Cauchy-Euler Equations

A Cauchy-Euler equation is of the form:

<p>
$$\begin{aligned}
a_nx^n y^{(n)} + a_{n-1}x^{n-1}y^{(n-1)} + \dots a_0y = 0
\end{aligned}$$
</p>

We will consider constant coefficient equations at first. Take a second order equation of the form:

<p>
$$\begin{aligned}
x^2y'' + axy' + by = 0
\end{aligned}$$
</p>

We assume that $x > 0$. Our guess of a solution looks like $y=x^r$ for some integer $r$, since in each term, we take $n$ derivatives and multiply by $x^n$. In the case $x<0$ we would similarly substitute $-x^r$, or in general substitute $\vert x \vert ^r$ it In particular, we get:

<p>
$$\begin{aligned}
x^2y'' + axy' + by &= 0 \\
r(r-1)x^r + arx^r + bx^r &= 0 \\
\left[ r(r-1) + ar + b\right] x^r &= 0
\end{aligned}$$
</p>

Assuming $x\ne 0$, we now are left with a characteristic equation for $r$. This all should look very familiar to you, as it's an almost identical process to the constant coefficient homogeneous equations we studied earlier, where we subtituted in a trial solution $y=e^{rx}$. Since $e^{x^r} = e^{rx}$, this clues us into a substitution we can make.

In the above equation, let $x = e^t$, which we can do so long as $x > 0$; then the equation becomes a differential equation in terms of $t$. With some use of the chain rule, we indeed get:

<p>
$$\begin{aligned}
y'' + ay' + by = 0
\end{aligned}$$
</p>

Which is a constant coefficient equation with the _same characteristic equation_ which we know how to solve. Now we can look at solutions of the Cauchy Euler equation by looking at the roots of the characteristic equation.

- For a real repeated root, $y = e^{rt}, te^{rt}, t^2e^{rt}$, etc. Substituting in $x=e^t$, we have:
<p>
$$
y=x^r, (\ln x)x^r, (\ln x)^2 x^r, \dots
$$
</p>
- For a complex root, $y = e^{at}\cos bt, e^{at} \sin bt$, etc. Substituting in $x=e^t$, we have:
<p>
$$
y = x^r \cos (b\ln x), x^r \sin (b\ln x), \\
x^r (\ln x)\cos (b\ln x), x^r (\ln x) \sin (b\ln x), \dots
$$
</p>

And you can check that these solutions are linearly independent. To obtain the result for $x<0$, we can simply do a coordinate transformation $\tilde{x} = -x$ and reduce to the earlier case. You can check that in the above formulas, we need only replace $x$ with $\vert x \vert$ to get a solution for all cases.

## The Laplace Transform

The Laplace Transform is a method of transforming a problem in one domain to a problem in another. Once we have solved the transformed version of a differential equation, we can use the inverse transformation to get a set of solutions. We define:

**Definition:** Let $f(t)$ be defined for $t \ge 0$. Then we define the **Laplace Transform** $F(s)$, or $\mathcal{L}\{ f(t) \}$, to be the improper integral:

<p>
$$
\mathcal{L}\{ f(t) \} = F(s) = \int_0^\infty e^{-st}f(t)dt
$$
</p>

The following theorem gives us conditions for which the Laplace transform is well-defined.

##### Theorem

> Let $f$ be piecewise continuous on $0\le t \le A$, for any $A$. Furthermore, suppose there exists a positive value $M$ so that for all $t \ge M$, we have: $\vert f(t) \vert \le Ke^{at}$, for some $K >0$ and $a$ real. Then, the Laplace Transform $\mathcal{L}\{ f(t) \}$ exists for all $s > a$.

This theorem essentially tells that for some large enough value, we need $f(t)$ to not overpower $e^{at}$, which is a reasonable condition to have. The proof is using basic calculus.

One important property of the Laplacian is that it is **linear**, meaning $\mathcal{L} [ af+bg ] = a \mathcal{L} [ f ] + b \mathcal{L} [ g ]$, for any constants $a,b$ and functions $f,g$. This follows from the fact that integration is linear. Furthermore, we assume the inverse of the Laplace transform is well-defined, though we will not prove it.

### Table of Laplace Transforms

The following table gives a few of the useful Laplace Transforms that we can use to solve differential equations.

| $\textbf{f(t)}$   |     $\textbf{F(s)} = \mathcal{L}[ f(t) ] = F(s)$     |
|----------|:-------------:|
| $e^{at}f(t)$ |  $F(s-a)$ |
| $1$ |  $\frac{1}{s}$ |
| $e^{at}$ |  $\frac{1}{s-a}$ |
| $t^n$ |  $\frac{n!}{s^{n+1}}$ |
| $\sin bt$ |  $\frac{b}{s^2 + b^2}$ |
| $\cos bt$ |  $\frac{s}{s^2 + b^2}$ |
| $t \sin bt$ |  $\frac{2b}{(s^2 + b^2)^2}$ |
| $t \cos bt$ |  $\frac{s^2 - b^2}{(s^2 + b^2)^2}$ |
| $f'(t)$ |  $sF(s) - f(0)$ |
| $f'' (t)$ |  $s^2F(s) - sf(0) - f'(0)$ |

A key point here is that if you look at derivatives, the Laplace transform turns a differential equation into an algebraic equation, which are in general far easier to solve.

##### Example

Let's solve our prototypical example:
<p>
$$
y'' + y = 0
$$
</p>

With initial conditions $y(0) = 1, y'(0) = 0$. We already know the solution is $cos x$. Taking the Laplace transform of both sides using our table, we get:

<p>
$$
s^2 F(s) - sy(0) - y'(0) + F(s) = 0 \\
(s^2 + 1)F(s) = s \\
F(s) = \frac{s}{1+s^2}
$$
</p>

And indeed, $F(s)$ is the Laplace transform of $\cos x$, as we expected.

This example may seem fairly trivial; Laplace transform only truly becomes useful when dealing with non-continuous quantites. We take a look at two important such cases.

### Heaviside Function

We define the **Heaviside** or **step** function:

<p>
$$
u_c(t) = \begin{cases} 
      0 & t < c \\
      1 & t \geq c
   \end{cases}
$$
</p>

We can use this to create a "step up - step down" function. For example, if we wanted a function which was zero everywhere except in the region $a < t < b$, we can simply use the difference $u_a(t) - u_b(t)$.

We determine the Laplace transform of the Heaviside function by integration.

<p>
$$\begin{aligned}
\mathcal{L}[u_c(t)] &= \int_0^\infty e^{-st}u_c(t) dt \\
&= \int_c^\infty e^{-st} dt \\
&= \frac{e^{-cs}}{s}
\end{aligned}$$
</p>

One application of the Heaviside function is to translate a function. Look at the product $u_c(t)f(t-c)$:

<p>
$$
u_c(t)f(t-c) = \begin{cases}
      0 & t < c \\
      f(t-c) & t \geq c
   \end{cases}
$$
</p>

So we have essentially translated $f$ over to the right by $c$. You can check that the Laplace transform gives:
<p>
$$\begin{aligned}
\mathcal{L}[u_c(t)f(t-c)] &= \int_0^\infty e^{-st}f(t-c) dt \\
&= e^{-cs}F(s)
\end{aligned}$$
</p>

So translating a function to the right by $c$ results in multiplying its Laplace transform by $e^{-cs}$.

These types of shapes occur often in signal processing, which is when the Laplace transform is the most useful.

### Dirac Delta Function

We define the **Dirac delta function** $\delta(t)$:

<p>
$$\begin{aligned}
\int_{-\infty}^\infty f(t)\delta(t) = f(0)
\end{aligned}$$
</p>

We can interpret the Dirac delta function (which is not technically a function) as a function which is zero everywhere except the origin, where it is infinite. We can construct it as the limit of a step-up, step-down function:

<p>
$$\begin{aligned}
\delta(t-c) = \underset{\epsilon \to 0}{\lim} \frac{1}{2\epsilon} (u_{c-\epsilon}(t) - u_{c+ \epsilon}(t))
\end{aligned}$$
</p>


Now using this definition, we can integrate and get the Laplace transform of the Dirac delta function:

<p>
$$\begin{aligned}
\mathcal{L}[\delta(t-c)] &= \int_0^\infty e^{-st}\delta(t-c) dt \\
&= e^{-cs}
\end{aligned}$$
</p>

And indeed, we have $\mathcal{L}[\delta(t)] = 1$.

For nonhomogeneous linear equations where the right hand side is discontinuous, we can often use the Laplace transform to make the problem easier to solve, though generally we may need to use some algebraic tricks such as partial fractions and completing the square.

## The Matrix Exponential

Recall that earlier when we were dealing with the matrix system:

<p>
$$\begin{aligned}
x' = Ax
\end{aligned}$$
</p>

And where $A$ was diagonalizable, we were able to uncouple our equations and get $n$ separate linear equations. However, in that section we mentioned there was an easier method, which involves something called the matrix exponential.

##### Theorem

>Suppose we have the equation:
><p>
$$\begin{aligned}
x' = Ax
\end{aligned}$$
></p>
>With $A$ as a constant matrix, and the initial condition given by $x(0) = x_0$. Then the solution is given by:
><p>
$$\begin{aligned}
x = e^{At}x_0
\end{aligned}$$
></p>
>Where $e^{At}$ is the matrix exponential.

This can be seen by analogy with the one dimensional case. Suppose we had:
<p>
$$\begin{aligned}
x' = ax
\end{aligned}$$
</p>

For some constant $a$, and $x(0) = x_0$. Then the solution, by integration, is $x=Ce^{at}$ for some constant $C$. Using the initial condition gives $C=x_0$.

### Defining the Matrix Exponential

We use the definition of the one dimensional exponential:
<p>
$$\begin{aligned}
e^{at} = 1 + at + (at)^2/2 \dots = \sum\limits_{k=0}^\infty \frac{(at)^k}{k!}
\end{aligned}$$
</p>

We can define the matrix exponential in a similar way:

<p>
$$\begin{aligned}
e^{At} = I + At + (At)^2/2 \dots = \sum\limits_{k=0}^\infty \frac{(At)^k}{k!}
\end{aligned}$$
</p>

The matrix exponential enjoys many properties which we associate with the exponential. We will list a few of the useful ones here:

- $e^{0} = I$.

- $e^{aX}e^{bX} = e^{a+b}X$

- $\frac{d}{dt}e^{At} = Ae^{At}X$

- If $A$ is diagonalizable, i.e. $A=SDS^{-1}$, then $e^A = Se^DS^{-1}$.

- $\det(e^A) = e^{\text{tr} (A)}$

Where $\text{tr}$ refers to the trace of $A$. The first three properties can be proved using direct computation. Note that the first property tells us that when we constructed a fundamental matrix so that $X(0) = I$, we indeed had a matrix which was a matrix exponential. The final property is called **Jacobi's formula** and requires an involved proof we won't get into here.

With some knowledge of linear algebra, we can generalize the above property for diagonalizable matrices to all matrices using the Jordan normal form. The exercise of computing the matrix exponential of a Jordan normal form is left to the reader, but the key point is to compute each block separately and break each block into the sum of a diagonal matrix and another matrix.

We can use the matrix exponential to generalize the method of integrating factors.

### The Non-homogeneous Case

Suppose instead we have a system which looks like:
<p>
$$\begin{aligned}
x' = Ax + b
\end{aligned}$$
</p>

And again, $A$ is constant. We attempt to multiply both sides by $e^{-At}$ (an integrating factor) to obtain:

<p>
$$\begin{aligned}
e^{-At}x' -Ae^{-At}x = e^{-At}b
\end{aligned}$$
</p>

The key here is that the matrix exponential works like the regular exponential, and so the left hand side becomes an instance of the product rule:

<p>
$$\begin{aligned}
\frac{d}{dt} (e^{-At}x) = e^{-At}b
\end{aligned}$$
</p>

Integrating, we have:

<p>
$$\begin{aligned}
x = e^{At} \int e^{-At}b
\end{aligned}$$
</p>

Thus, the matrix exponential, if it can be easily computed, can be used to efficiently solve homogeneous or non-homogeneous matrix systems with constant coefficients.

## Nonlinear Differential Equations

We begin with the one dimensional case. Suppose we are working with a non-linear differential equation of the form:

<p>
$$\begin{aligned}
x' = f(x)
\end{aligned}$$
</p>

We say that $x_0$ is a **fixed point** or **equilibrium point** if $f(x_0) = 0$. The reason behind this term is because if we set $x(0) = x_0$, then $x'(0) = 0$; indeed the derivative never changes, and $x$ remains constant forever.

We next consider what happens under small perturbations; will $x$ eventually return to its stable point or will it shoot off to infinity? We let $x = x_0 + \epsilon(t)$, where $\epsilon(t)$ starts out small. Note that $x' = \epsilon'$, and $f(x_0) = 0$, so we can use Taylor series to get the first few terms of $\epsilon'$:

<p>
$$\begin{aligned}
x' = \epsilon' \approx \epsilon f'(x_0) + \frac{\epsilon^2}{2} f''(x_0)
\end{aligned}$$
</p>

We ignore the second term, to get:

<p>
$$\begin{aligned}
\epsilon' = \epsilon f'(x_0) \\
\epsilon \approx e^{f'(x_0)}
\end{aligned}$$
</p>

So we can summarize the above discussion as follows:
- If $f' > 0$ at an equilbirium point, then a small perturbation will blow up exponentially, and we say such a point is **unstable**.

- If $f' < 0$ at an equilbirium point, then a small perturbation will decay exponentially, and we say such a point is **stable**.

- If $f' = 0$ at an equilbirium point, then a small perturbation will lead to neither exponential decay nor exponential growth, and we say such a point is **marginally stable**.

We can indeed try to find an approximate solution to such an equation near an equilbrium point by calculating the first few terms of the Taylor series for $f(x)$.

### Two Dimensions

We move on to the two dimensional case, where we have:

<p>
$$\begin{aligned}
x' = F(x,y) \\
y' = G(x,y)
\end{aligned}$$
</p>

Here, we have both $x$ and $y$ are functions of $t$, but the functions $F,G$ only depend on $x,y$. We call such a system an **autonomous system**.

Again, we define an **equilibrium point** as $F(x,y) = G(x,y) = 0$.

To get a qualitative idea of what the solutions look like, we can plot $x,y$ for various values and draw vectors indicating the direction of change at each point. This is called a **phase plane** diagram, and is particularly useful in physics, where we can plot for example position and velocity.

To find an approximation $F,G$ near an equilibrium point, we use the nearest linear approximation to the pair of functions at that point. In one dimension, this would be simply the derivative. In two dimensions, we use the **Jacobian**:

<p>
$$\begin{aligned}
A = \begin{bmatrix} \frac{\partial F}{\partial x} && \frac{\partial F}{\partial y} \\
\frac{\partial G}{\partial x} && \frac{\partial G}{\partial y} \end{bmatrix}
\end{aligned}$$
</p>

We evaluate this matrix at a particular equilibrium point $x_0, y_0$. Using something like a Taylor series, we get the following differential equation

<p>
$$\begin{aligned}
\begin{bmatrix} x \\ y \end{bmatrix}' = A(x_0, y_0) \begin{bmatrix} x -x_0 \\ y -y_0\end{bmatrix}
\end{aligned}$$
</p>

### Types of Equilibrium Points

As in the one dimensional case, the behavior of our system near an equilibrium point depends on the first derivative. In particular, we look at the eigenvalues of the Jacobian matrix $A$. We have the following definitions:

| Eigenvalues  |   Type of Equilbrium Point    |
|----------|:-------------:|
| Real, negative|  Stable node |
| Real, positive | Unstable node |
| Opposite sign | Saddle |
| Complex with negative real part|  Stable spiral |
| Complex with positive real part|  Unstable spiral |
| Complex with zero real part | Stable center |

These definitions come from the types of shapes the system makes in the phase plane.

For example, if the eigenvalues are both pure imaginary, then we know from Chapter 4 what the fundamental solutions to this system look like. Let the eigenvalues be called $\pm \mu$. Then we have two fundamental solutions:

<p>
$$\begin{aligned}
x_1 = v_1\cos \mu t \\
x_2 = v_1\sin \mu t
\end{aligned}$$
</p>

For some vector $v_1$ which is the imaginary part of an eigenvector. This means every solution $\textbf{x} = (x,y)$ looks like:

<p>
$$\begin{aligned}
\textbf{x} = (a\cos \mu t + b \sin \mu t)v_1
\end{aligned}$$
</p>

And as we plot this in the phase plane, we get nothing more than an ellipse.


# References

- Boyce & DiPrima, Elementary Differential Equations and Boundary Value Problems, 7th ed.
- Goode & Annin, Differential Equations and Linear Algebra 3rd ed.
- Chasnov, Introduction to Differential Equations. Available at [http://www.math.ust.hk/~machas/differential-equations.pdf](http://www.math.ust.hk/~machas/differential-equations.pdf)