---
layout: post
title: "Symmetric Matrices Are Great"
date:   2017-07-02
mathjax: true
tags: [math, linear algebra]
download: true
---

## Symmetric Matrices Are Great
Matrices are incredibly useful for a multitude of reasons in programming and science in general. For one, a matrix can be used to store two dimensional collections of data, like tables or even images (which are collections of pixels). Arguably more importantly, matrices are synonymous with **linear maps**. A linear map is a special, "nicely behaved" function of one or more variables which we can do a lot of interesting math with, and in fact there is an entire branch of math which studies the ways in which we can approximate the world of non-linear functions by linear functions -- otherwise known as calculus.

<center><img src="https://artsineducationblogdotcom.files.wordpress.com/2014/12/transformation.gif"></center>

<div class="caption">
<sub>All three of these types of transformations are linear maps</sub>
</div>

Symmetric matrices are a particular class of matrices defined as follows: let us introduce the **transpose** $A^T$ of a matrix $A$, the matrix we get when we read the columns of $A$ as rows and vice versa. A symmetric matrix is simply one where $A=A^T$. In other words, we can read the matrix either horizontally or vertically due to its symmetry.

In many ways, we can consider symmetric matrices as the "building blocks" of all matrices. or example, take the following statement:

---

##### Claim: Every square matrix can be written as the sum of a symmetric matrix and a skew-symmetric matrix.

This is a fun, short proof. We define a **skew-symmetric** matrix as a matrix $A$ where $A^T = -A$; so, reading the matrix horizontally or vertically returns the same matrix but with a flipped sign in each entry. We consider the following two sums:
<p>
$$M = \frac{1}{2}(A+A^T) $$
</p>
What can we say about this matrix? Well, we look at its entry in row $i$ and column $j$ (denoted $M_{ij}$), which is the sum $A_{ij}+A_{ji}$. But since addition is commutative, we also have
<p>
$$M_{ji}=M_{ij}=A_{ji}+A_{ij}$$
</p>
Indeed, the matrix reads the same horizontally and vertically; $M$ is symmetric. In the same way, we can define:
<p>
$$N = \frac{1}{2}(A-A^T)$$
</p>
And by a nearly identical argument, we can show that $N$ is skew symmetric. And looking at our definitions, we can see that $A=M+N$, and we are done. Here's another, far more useful fact about symmetric matrices.

---

##### Symmetric matrices have an orthonormal basis of eigenvectors

If you don't know what any of these words mean, I'll be coming out soon with an explanation of the terms basis and eigenvectors soon. We can define an **orthonormal** basis as a basis consisting only of unit vectors (vectors with magnitude $1$) so that any two distinct vectors in the basis are perpendicular to one another (to put it another way, the inner product between any two vectors is $0$). Let's prove this statement.

First, consider the following fact about dot products (inner products). We can represent them with matrix multiplication. In short, the dot product between two column vectors can be computed by making the first of those two a row vector:
<p>
$$x\cdot y = x^Ty$$
</p>
This will be crucial to this short proof. Consider two distinct eigenvalues of $A$, $\lambda_1$ and $\lambda_2$, with corresponding eigenvectors $v_1$ and $v_2$. We will show that they are perpendicular to one another (once we have this, we can always pick multiple orthogonal vectors corresponding the same eigenvalue, and also we are free to pick vectors with length $1$). We consider the following sum:
<p>
$$(Av_1)^T v_2 - v_1^TAv_2$$
</p>
We can simplify this a little bit knowing that $v_1,v_2$ are eigenvectors and thus $Av_1=\lambda v_1$. We can rewrite (note that we can take constants out of matrix multiplication)
<p>
$$ = \lambda_1 v_1^T v_2 - \lambda_2 v_1^Tv_2$$
$$ = (\lambda_1 - \lambda_2) (v_1^T v2) $$
$$ = (\lambda_1 - \lambda_2) (v_1 \cdot v2) $$
</p>
Now, we can use the fact that for any two matrices $A$ and $B$, $AB^T$=$B^TA^T$. Rewriting the first equation above, we arrive at:
<p>
$$v_1^TA^Tv_2 - v_1^TAv_2$$
</p>
But $A=A^T$, since $A$ is symmetric! So in fact this quantity is zero. This means either $(\lambda_1 - \lambda_2)$ is zero (it isn't, since we picked two different eigenvalues); or $v_1 \cdot v_2$ is zero. Therefore, the two eigenvectors are perpendicular to one another.

---