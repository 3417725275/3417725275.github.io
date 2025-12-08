---
layout: post
title: NURBS曲线
cover: /img/cover12.webp
categories:
  - 计算几何
  - 几何表示
  - 曲线表示
tags:
  - 计算几何
  - 曲线曲面
keywords: 'NURBS曲线, NURBS, 计算几何, 曲线曲面'
abbrlink: ad4cd7c6
date: 2025-11-18 10:57:09
updated: 2025-12-02 10:00:00
---


# NURBS: 由来

**NURBS(Non-Uniform Rational B-Splines)** 是一种用于数学建模和计算机图形学的技术。它是一种灵活的用于描述曲线和曲面的方法，具有广泛的应用，包括计算机辅助设计（CAD）、计算机图形学、虚拟现实等领域。NURBS之所以受到青睐，是因为它们可以以高度灵活的方式控制曲线和曲面的形状，同时保持数学上的精确性。

NURBS通过基函数的组合来定义曲线和曲面，这些基函数是基于**B样条（B-Splines）**基函数的改进，但与B样条不同的是，NURBS允许在基函数中引入**权重**，从而更灵活地控制曲线和曲面的形状。具体来说，NURBS曲线和曲面可以由**控制点**、**权重**以及**次数**为基础的基函数来定义。这种灵活性使得NURBS能够更好地适应不同形状和设计需求。

B-样条曲线是**多项式曲线**。虽然它们灵活且在曲线设计中具有许多良好的特性，但**它们不能表示最简单的曲线：圆**。圆只能用**有理函数**表示（即，两个多项式的商）。为了处理圆、椭圆和许多其他不能用多项式表示的曲线，因此需要对B样条曲线进行扩展。



> **圆是一个二次曲线。为什么B样条曲线不能表示它？**

以下是四个闭合的B样条曲线，具有8个控制点。从左到右的度数分别是2、3、5和10。二次闭合的B样条看起来不像一个圆，它看起来像一个圆角正方形。三次曲线看起来稍微好一些。随着度数的增加，曲线的"圆润程度"变得更好。十次闭合曲线与圆非常相似；但它依旧不是一个圆。即使你可以把这个十次曲线作为一个圆接受，这也是近似的。

![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/closed-deg-2.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/closed-deg-3.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/closed-deg-5.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/closed-deg-10.jpg)


为了解决这个问题，我们将使用 **“齐次坐标”** 将B样条推广为 **有理曲线**。因此，我们有了**N**on-**U**niform **R**ational **B**-**S**plines，即**NURBS曲线**。



# NURBS曲线的定义

我们将**齐次坐标**引入到B样条曲线中并推导**NURBS**曲线的定义：

给定 $n+1$ 个控制点 $P_0, P_1, ..., P_n$ 和 $m+1$ 个节点的结点向量 ：$U = { u_0, u_1, ..., u_m }$
由这些参数定义的次数为 $p$ 的B样条曲线定义如下： 

$$
\mathbf{C}(u)=\sum_{i=0}^nN_{i,p}(u)\mathbf{P}_i
$$

其中，$N_{i,p}(u)$ 是B样条基函数。


将控制点 $\mathbf{P}_i$ 重写为一个具有四个分量的列向量，第四个分量为 1：

$$
\mathbf{P}_i=\left[\begin{array}{c}x_i\\y_i\\z_i\\1\end{array}\right]
$$


我们可以将这个 $\mathbf{P}_i$ 视为齐次坐标。由于将一个点的坐标（以齐次形式表示）与非零数相乘不会改变其位置，因此，我们将 $\mathbf{P}_i$ 的坐标乘以一个权重 $w_i$，这样可以获得一个新的齐次坐标形式：

$$
\mathbf{P}_{i}^{w}=\left[\begin{array}{c}w_{i}x_{i}\\w_{i}y_{i}\\w_{i}z_{i}\\w_{i}\end{array}\right]
$$

注意，$\mathbf{P}_{i}^{w}$ 和 $\mathbf{P}_{i}$ 在齐次坐标中代表同一点。将这种新的齐次形式代入上述B样条曲线的方程中，我们可以得到：

$$
\mathbf{C}^w(u)=\sum\limits_{i=0}^nN_{i,p}(u)\mathbf{P}_i^w=\sum\limits_{i=0}^nN_{i,p}(u)\left[\begin{array}{c}w_ix_i\\w_iy_i\\w_iz_i\\w_i\end{array}\right]=\left[\begin{array}{c}\sum\limits_{i=0}^nN_{i,p}(u)(w_ix_i)\\\sum\limits_{i=0}^nN_{i,p}(u)(w_iy_i)\\\sum\limits_{i=0}^nN_{i,p}(u)(w_iz_i)\\\sum\limits_{i=0}^nN_{i,p}(u)w_i\end{array}\right]
$$

因此，点 $C^{w}(u)$ 是齐次坐标形式下的B样条曲线表示。

现在，通过将 $C_w(u)$ 除以第四个坐标来将其转换回笛卡尔坐标：

$$
\mathbf{C}(u)=\begin{bmatrix}\frac{\sum_{i=0}^nN_{i,p}(u)(w_ix_i)}{\sum_{i=0}^nN_{i,p}(u)w_i}\\\frac{\sum_{i=0}^nN_{i,p}(u)(w_iy_i)}{\sum_{i=0}^nN_{i,p}(u)w_i}\\\frac{\sum_{i=0}^nN_{i,p}(u)(w_iz_i)}{\sum_{i=0}^nN_{i,p}(u)w_i}\\1\end{bmatrix}=\sum_{i=0}^n\frac{N_{i,p}(u)w_i}{\sum_{j=0}^nN_{j,p}(u)w_j}\begin{bmatrix}x_i\\y_i\\z_i\\1\end{bmatrix}
$$


最后，我们得到以下形式：

$$
\mathbf{C}(u)=\frac{1}{\sum_{i=0}^nN_{i,p}(u)w_i}\sum_{i=0}^nN_{i,p}(u)w_i\mathbf{P}_i
$$

**上式是由控制点$\mathbf{P}_{0}, \mathbf{P}_{1}, ...\mathbf{P}_{n}$ 定义的次数为 $p$ 的NURBS曲线，节点向量为: $U = {u_0, u_1, ..., u_m }$，权重分别为 $w_0，w_1,...,w_n$**

**Tips: 由于权重 $w_i$ 与控制点 $\mathbf{P}_i$ 相关联，作为其第四个分量，所以权重的数量和控制点的数量必须一致。**

一般情况下，权重$w_i$是正的。但当权重为负值时也会有特别的效果。例如，如果一个权重$w_i$变成零，那么$\mathbf{P}_i$的系数也是零，因此，控制点$\mathbf{P}_i$对于曲线上任意一点$u$的计算没有影响。因此零权重有时候也被称为**“无穷控制点”**。



## 两个结论

从上述定义式中，我们可以立即得出两个结论：

1. **如果所有的权重都等于1，那么一个NURBS曲线将简化为一个B样条曲线。**
   这是显而易见的，因为在这种情况下，齐次形式的控制点与传统笛卡尔形式相同，而$\frac1{\sum_{i=0}^{n}N_{i,p}(u)w_{i}}$ 分母为1。

2. **NURBS曲线是有理曲线**
 $N_{i,p}(u)w_{i}$的值是一个 $p$ 次多项式，控制点$\mathbf{p}_i$ 是常数，$\frac1{\sum_{i=0}^{n}N_{i,p}(u)w_{i}}$中分母是所有系数的和，也是一个$p$次多项式。因此，控制点$\mathbf{P}_i$ 的系数是两个次数为 $p$ 的多项式的商，因此**NURBS**曲线$C(u)$是有理的。

**这两个结论表明B样条曲线是NURBS曲线的特殊情况。此外，由于NURBS曲线是有理的，因此圆、椭圆和许多其他用B样条无法表示的曲线现在都可以通过NURBS曲线定义。**



## 几何解释

NURBS曲线是特殊类型的曲线吗？事实证明它们并不是。实际上，它们只是B样条曲线的另一面。

控制点$\mathbf{P}^{W}_{i}=(\begin{array}{ccc}w_{i}x_{i},&w_{i}y_{i},&w_{i}z_{i},&w_{i}\end{array})$有四个分量，可以被看作是四维空间中的一个点，因此下面的$C(u)$为四维空间中的B样条曲线: 

$$
\mathbf{C}^w(u)=\sum\limits_{i=0}^nN_{i,p}(u)\mathbf{P}_i^w=\sum\limits_{i=0}^nN_{i,p}(u)\left[\begin{array}{c}w_ix_i\\w_iy_i\\w_iz_i\\w_i\end{array}\right]=\left[\begin{array}{c}\sum\limits_{i=0}^nN_{i,p}(u)(w_ix_i)\\\sum\limits_{i=0}^nN_{i,p}(u)(w_iy_i)\\\sum\limits_{i=0}^nN_{i,p}(u)(w_iz_i)\end{array}\right]
$$

**齐次坐标的几何解释：通过将前三个坐标分量除以第四个坐标相当于将四维点投影到平面 $w = 1$**

上述曲线定义中，通过将前三个坐标除以第四个坐标，可以将B样条曲线定义转换为NURBS曲线定义。

所以我们有结论：**三维空间中的NURBS曲线仅仅是四维空间中B样条曲线的投影。** 



给定$n+1$个控制点$\mathbf{P}_0,\mathbf{P}_1,\ldots,\mathbf{P}_n$，每个点有一个非负权重 $w_i$（$w_i >= 0$），以及一个包含 $m+1$ 个节点的节点向量 $U = { u_0， u_1， ...， u_m }$，$p$次NURBS曲线的定义如下：

$$
\mathbf{C}(u)=\sum_{i=0}^nR_{i,p}(u)\mathbf{P}_i
$$

**$R_{i,p}(u)$ 表示NURBS曲线基函数**，其定义如下：

$$
R_{i,p}(u)=\frac{N_{i,p}(u)w_i}{\sum_{j=0}^nN_{j,p}(u)w_j}
$$




## NURBS曲线基函数的重要性质

由于NURBS曲线是B样条的泛化，它应该具有B样条的所有性质。

以下是NURBS曲线基函数最重要的性质

1. **$R_{i,p}(u)$ 是关于 $u$ 的 $p$ 次有理函数**
2. **非负性：对于任意 $i$ 和 $p$，$R_{i,p}(u)$ 都是非负的**
3. **局部支撑： $R_{i,p}(u)$ 在 $[u_i, u_{i+p+1})$ 上非零**

> 因为 $N_{i,p}(u)$​ 在 $[u_i, u_{i+p+1})$​ 上非零，所以 $R_{i,p}(u)$​ 也是非零的。（假设 $w_i$​ 非负）

4. **在节点区间 $[u_i, u_{i+1})$ 上，最多有 $p+1$ 个 $p$ 次基函数是非零的，即：$R_{i-p,p}(u)$，$R_{i-p+1,p}(u)$，$R_{i-p+2,p}(u)$，... $R_{i,p}(u)$。**
5. **单位分割：在区间 $[u_i, u_{i+1})$ 上所有非零$p$次基函数之和为1**：
6. **如果节点数为$m+1$，基函数的次数为$p$，且次数为$p$的基函数数量为$n+1$，则$m=n+p+1$**：
7. **基函数 $R_{i,p}(u)$ 是一个次数为 $p$ 的有理函数复合曲线，由多个p次有理函数在节点处 $[u_i, u_{i+p+1})$ 连接组成。**
8. **在一个重数为 $k$ 的节点处，基函数 $R_{i,p}(u)$ 是 $C^{p-k}$ 连续的。**
   因此，增加多重性会降低曲线在该点连续性，增加次数会增加连续性。
9. **如果对任意$i$，都有 $w_i = c$，其中 $c$ 是一个非零常数，则$R_{i,p}(u)=N_{i,p}(u)$。**
   因此，当所有权重变为非零常数时，B样条基函数是NURBS基函数的特殊情况
   我们已经提过，当 $c = 1$ 时，NURBS曲线的定义会退化成B样条曲线。 



## NURBS 曲线的重要特性

下面列出了NURBS曲线的重要特性。

与B样条曲线一样，NURBS曲线可以是$Open$的、$Clamped$的或$Closed$的。如果前$p+1$个节点值为0，后$p+1$个节点值为1，（前提是曲线的定义域为$[0,1]$）则曲线是$Clamped$的。

1. **NURBS曲线** $C(u)$ **是一个分段曲线，其中每个曲线段都是一个次数为 $p$ 的有理曲线。**
   实际上，每个曲线段都是一个有理贝塞尔曲线。

2. **NURBS曲线必须满足 $m = n + p + 1$**

3. **$Clamped$ NURBS曲线$C(u)$通过端点的两个控制点$P_0$和$P_n$。**

4. 强凸包性质：**NURBS曲线位于其控制点定义的凸包内。**并且，如果$u$在节点区间$[u_i,u_{i+1})$内，则$C(u)$位于控制点$P_{i-p}, P_{i-p+1}, ..., P_i$定义的的凸包内。

   

   NURBS基函数的权重必须是**非负的**，如果其中一些是负数，则强凸包性质甚至凸包性质都有可能不满足。

   在下面，左图是一个2次NURBS曲线，$n = 2，m = 5$，前三个节点和后三个节点是Clamped的。两端的两个控制点权重为1，中间的控制点的权重为0.5。此时NURBS曲线是一个椭圆弧，曲线段位于凸壳内。

   ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-ell-pos-weight.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-ell-zer-weight.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-ell-neg-weight.jpg)
   中间图中的中间控制点的权重被设为零，结果就是NUBRS退化为由端点确定的线段。它仍然位于凸包内。如果将中间控制点权重改为-0.5（右图)，则曲线段不包含在凸包中，因此凸包性质失效。

5. **局部修改特性：改变控制点 $\mathbf{P}_i$ 仅会影响到曲线 $C(u)$ 在区间 $[u_i, u_{i+p+1})$ 上的部分**。

   这是基于B样条基函数的局部修改特性得出的。回想一下，$R_{i,p}(u)$在区间 $[u_i,u_{i+p+1})$上是非零的。
   如果 $u$ 不在这个区间内，由于$R_{i,p}(u)$为零且在计算 $\mathbf{p}(u)$ 时， $R_{i,p}(u)\mathbf{p}(u)$ 没有影响。另一方面，如果 $u$ 在指定的区间内，$R_{i,p}(u)$非零的，此时如果改变 $R_{i,p}(u)\mathbf{p}(u)$，那么 $C(u)$ 也会改变。

**这种局部修改方案对曲线设计非常重要，因为我们可以在局部修改曲线而不会在全局范围内改变形状。此外，如果需要微调曲线形状，可以插入更多的节点（或者更多的控制点），以便受影响的区域可以被限制在非常窄的范围内。**

6. **如果 $u$ 是一个重数为 $k$ 的节点，那么 $C(u)$ 在该节点处是 $C^{p-k}$ 连续的。**
   **如果 $u$ 不是一个节点，$C(u)$ 位于一个 $p$ 次曲线段的中间，因此是无限可微的。**
   **如果 $u$ 是在 $R_{i,p}(u)$的非零定义域上的一个节点，由于$R_{i,p}(u)$仅是$C^{p-k}$连续的，所以 $C(u)$ 也是$C^{p-k}$连续的。**

7. **变差缩减特性：**
   如果曲线包含在一个平面（或空间）中，这意味着没有直线（或平面）比它与曲线的控制折线相交的次数更多。

8. **B样条曲线和贝塞尔曲线是NURBS曲线的特殊情况**

   如果所有的权重都相等，那么NURBS曲线就变成了B样条曲线。
   进一步地，令$n = p$（即，B样条曲线的阶数等于$n$，即控制点数量减1），并且有$2(p + 1) = 2(n + 1)$个节点，其中前$p + 1$个节点和后$p+1$个节点在端部被$clamped$，那么这个NURBS曲线就退化为一个贝塞尔曲线。

9. **投影变换不变性**

   如果将投影变换应用于NURBS曲线，则结果可以由其经过投影变换后的控制点构造而成。当我们想要对 NURBS 曲线应用**几何变换**甚至**投影变换**时，我们可以将变换应用于控制点，而转换后的 NURBS 曲线由转换后的控制点定义。因此，无需直接对曲线进行变换。
   **注意，贝塞尔曲线和B样条曲线只满足仿射不变性质，而不是这种投影不变性质。这是因为只有NURBS曲线涉及投影变换。**



# NURBS曲线：修改权重的影响

NURBS曲线的基函数为


$$
R_{i,p}(u)=\frac{N_{i,p}(u)w_i}{\sum_{j=0}^nN_{j,p}(u)w_j}
$$

因此，增加和减少$w_i$的值将分别增加和减少$R_{i,p}(u)$的值。**更准确地说，增加$w_i$的值将会拉动曲线朝向控制点$\mathbf{p}_i$。**

**并且，曲线上所有受影响的点也将朝向$\mathbf{p}_i$的方向被拉动。当$w_i$趋近于无穷时，曲线将通过控制点$\mathbf{p}_i$。另一方面，减少$w_i$的值将使曲线远离控制点$\mathbf{p}_i$。**

下图显示了一个6次NURBS曲线及其基函数。所选观察控制点为 $\mathbf{p}_9$。在第一个图中，所有权重都是1，曲线是B样条曲线。在第二个图中，$w_9$增加到2，可以看到曲线的一部分向 $\mathbf{p}_9$ 移动。由于 $w_9$增加了，所以$R_{9,6}(u)$也如右图所示增加了。

![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-010.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-pu010.jpg)


![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-020.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-pu020.jpg)


下面，我们将$w_9$进一步增加到5、10和20，相应的也$R_{9,6}(u)$也变得更大，这也将曲线进一步拉向控制点$\mathbf{p}_9$。当$w_9$ = 20时，曲线已经非常接近$\mathbf{p}_9$点了。

![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-050.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-pu050.jpg)


![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-100.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-pu100.jpg)


![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-200.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-pu200.jpg)



再来看看相反的效果。以下是所有权重都为1的初始情况。然后，$w_9$ 被减小到0.5，**这将曲线推离控制点 $\mathbf{p}_9$。由于权重减少，相应的 $R_{9,6}(u)$也会减小，控制点 $\mathbf{p}_9$ 对曲线 $w_9$ 的影响也会减小。**
当 $w_9$ 改变为0.1时，曲线被进一步推离。最后一幅图显示了 $w_9$ 为零时的曲线。由于 $R_{9,6}(u)$为零，它对曲线没有影响，因此，与控制点 $\mathbf{p}_9$ 相对的曲线段几乎变成平坦的线段。

![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-010-17142007279151.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-pu010-17142007304903.jpg)


![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-005.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-pu005.jpg)


![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-001.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-pu001.jpg)


![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-000.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-weight-pu000.jpg)



因此，我们有以下结论：

**增加（ 或减少 ）权重 $w_i$ 的值会使曲线朝着（或远离）控制点 $\mathbf{p}_i$ 移动。当 $w_i$ 的值变为无穷大时，曲线通过控制点 $\mathbf{p}_i$，而当 $w_i$ 为零时，控制点 $\mathbf{p}_i$ 对曲线没有影响。**



## 进一步讨论

我们想要更准确地分析改变控制点权重的影响。

NURBS曲线的定义：

$$
\mathbf{C}(u)=\frac{1}{\sum_{i=0}^{n}N_{i,p}(u)w_{i}}\sum_{i=0}^{n}N_{i,p}(u)w_{i}\mathbf{P}_{i}
$$

我们选择控制点 $P_k$ ，并观察改变权重 $w_k$ 对曲线的影响。

由于 $P_k$ 仅在其系数 $N_{k,p}(u)$ 非零的区域（即，$[u_k, u_{k+p+1})$ ）上对曲线 $C(u)$ 有影响，因此，在接下来的讨论中，我们假设 $u$ 在 $[u_k, u_{k+p+1})$ 内。

将涉及$w_k$的项从曲线定义中分离出来，得到下式：

$$
\mathbf{C}(u)=\frac{1}{N_{k,p}(u)w_{k}+\sum_{i\neq k}^{n}N_{i,p}(u)w_{i}}\left(N_{k,p}(u)w_{k}\mathbf{P}_{k}+\sum_{i\neq k}^{n}N_{i,p}(u)w_{i}\mathbf{P}_{i}\right)
$$


我们简化一下这个公式，令：

$$
\begin{aligned}&A=N_{k,p}(u)w_{k}\\&B=\sum_{i\neq k}N_{i,p}(u)w_{i}\\&\mathbf{X}=\sum_{i\neq k}^{n}N_{i,p}(u)w_{i}\mathbf{P}_{i}\end{aligned}
$$


上式曲线的定义变成如下：

$$
\mathbf{C}(u)=\frac{1}{A+B}(A\mathbf{P}_{k}+\mathbf{X})
$$


考虑首先 $w_k = 0$ 的情况。我们有 $\mathbf{A} = 0$，曲线上的点，记为 $C^0(u)$：

$$
\mathbf{C}^0(u)=\frac{\mathbf{X}}{B}
$$


现在计算从这个**基本点** $C^0(u)$到任意$w_k$对应的点 $C(𝑢)$的向量

$$
\begin{aligned}
\mathbf{C}(u)-\mathbf{C}^{0}(u)& =\frac{1}{A+B}(A\mathbf{P}_{k}+\mathbf{X})-\frac{\mathbf{X}}{B}  \\
&={\frac{A}{A+B}}\left(\mathbf{P}_{k}-{\frac{\mathbf{X}}{B}}\right) \\
&=\frac{A}{A+B}\left(\mathbf{P}_{k}-\mathbf{C}^{0}(u)\right)
\end{aligned}
$$

**这意味着向量 $C(u)-C^0(u)$ 和向量 $C_k-C^0(u)$ 有相同的方向，前者的长度是后者的 $A/(A+B)$ 倍**

对于 $[u_k, u_{k+p+1})$ 上的每一个 $u$ 都是如此。因为点 $C_k$ 和 $C^0(u)$ 是固定的，我们可以认为 $C(u)$ 位于 $\mathbf{P}_k$ 和 $C^0(u)$ 的线上

如果所有的权重都是非负的，那么 $A$ 和 $B$ 都是非负的，且 $A/(A+B)$ 的值在0和1之间。也就是说，**点 $C(u)$ 位于 $\mathbf{P}_k$ 和 $C^0(u)$ 的线段上。**

如果 $w_k$ 趋向无穷大会怎么样？我们将曲线$C(u)$ 的分子和分母除以 $w_k$，得到如下：

$$
\mathbf{C}(u)=\frac{1}{N_{k,p}(u)w_{k}+\sum_{i\neq k}N_{i,p}(u)w_{i}}\left(N_{k,p}(u)w_{k}\mathbf{P}_{k}+\sum_{i\neq k}^{n}N_{i,p}(u)w_{i}\mathbf{P}_{i}\right)\\=\frac{1}{N_{k,p}(u)+\frac{1}{w_{k}}\sum_{i\neq k}N_{i,p}(u)w_{i}}\left(N_{k,p}(u)\mathbf{P}_{k}+\frac{1}{w_{k}}\sum_{i\neq k}^{n}N_{i,p}(u)w_{i}\mathbf{P}_{i}\right)
$$

**如果$w_k$趋近于无穷大，那么 $\frac{1}{w_k}$ 趋近于零，则 $\mathbf{P}(u)$ 趋近于$\mathbf{P}_k$，即所选控制点。**



因此我们有以下结论：

**如果 $w_k$ 是非负的， $C(u)$ 总是位于 $C^0(u)$ 和 $\mathbf{P}_k$ 的线段上，其中 $C^0(u)$ 是对应于 $w_k = 0$ 的点 , $u$ 在 $[u_k, u_{k+p}+1)$ 范围内。**
**当 $w_k$ 从0变化到无穷大时， $C(u)$ 从 $C^0(u)$ 移动到 $\mathbf{P}_k$ ，如果 $w_k$ 是无穷大， $C(u)$ 变成 $C_k$ **

我们有一个由9个控制点（$n = 8$）和16个节点（$m = 15$）定义的6次NURBS曲线，如下所示。

![image-20240425104226622](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/image-20240425104226622.png)

所选的控制点是 $\mathbf{P}_4$。由于 $\mathbf{P}_4$的系数 $N_{4,6}(u)$ 在 $[u_4, u_{4+6+1}) = [0,1)$ 上非零，因此，改变 $w_4$ 会影响整条曲线！如下图所示：

![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/weight-change-scheme.jpg)

对应于 $u = 1/3$ 和 $u = 2/3$ 的点在曲线上以不同的颜色标记。对应于 $w_4 = 0$ 的曲线是最低的，标记为0。图中显示了 $w_4$ 为2、3、4、5、10、20和50的曲线。随着 $w_4$ 的值增加，曲线被拉向控制点 $\mathbf{P}_4$。当 $w_4$ 增加到50时，曲线变得非常接近$\mathbf{P}_4$。

注意，所有对应于 $C(\frac{1}{3})$ 的点都在$C^0(\frac{1}{3})$  和 的$\mathbf{P}_4$线段上，所有对应于$C(\frac{2}{3})$的点都在 $C^0(\frac{2}{3})$ 和 $\mathbf{P}_4$ 的线段上。

随着 $w_4$ 的值增加， $C(\frac{1}{3})$ 和 $C(\frac{2}{3})$ 之间的曲线段变短。最终，当 $w_4$ 为无穷大时，这个曲线段的长度变为零（即，$C(\frac{1}{3})$ 和$C(\frac{2}{3})$ 变为与 $\mathbf{P}_4$ 相同）。


# NURBS曲线：节点插入

由于NURBS曲线是四维空间中的B样条曲线投影到三维空间的结果，因此对NURBS曲线进行节点插入是很容易的。

对NURBS曲线进行节点插入分为三个步骤：
**（1）将给定三维空间中的NURBS曲线转换为四维空间中的B样条曲线**
**（2）对这个四维B样条曲线执行节点插入**
**（3）将新的控制点集投影回三维空间，得到NURBS曲线的新的一组控制点。**

假设我们有 $n + 1$ 个控制点 $\mathbf{P}_0, \mathbf{P}_1, ..., \mathbf{P}_n$，带有权重 $w_0, w_1, ..., w_n$，一个节点向量 $U$ 和一个次数 $p$。令 $\mathbf{P}_i = (x_i, y_i, z_i)$。

那么，控制点 $\mathbf{P}^w_i = ( w_i x_i, w_i y_i, w_i z_i, w_i )$，$0 \leq i \leq n$，和节点向量 $U$ 定义了一个四维的 $p$ 次B样条曲线。向这个四维B样条曲线插入一个新节点 $t$，得到一个新的控制点集合 $Q^w_i = ( X_i, Y_i, Z_i, W_i )$，$0 \leq i \leq n$。然后将它们投影回三维空间，即通过将坐标的前三个分量除以第四个分量，可得到给定 NURBS 曲线的新的控制点集合。

让我们来看一个例子。假设我们有 9 个结点

![image-20240427100547095](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/image-20240427100547095.png)

下面是在$xy$平面上定义的次数为3的NURBS曲线的5个控制点：

![image-20240427101204029](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/image-20240427101204029.png)

下图展示了曲线形状及其基础函数。

![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-w-knot-in-1-1.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-w-knot-in-1-2.jpg)


我们插入一个新的节点 $t = 0.4$。由于 $t$ 在节点区间 $[u_3, u_4)$ 中，并且 NURBS 曲线的次数是3，受影响的控制点是 $\mathbf{P}_3、\mathbf{P}_2、\mathbf{P}_1$ 和  $\mathbf{P}_0$。由于这是一条 NURBS 曲线，通过将所有控制点乘以它们对应的权重来计算齐次坐标，这些新的控制点为$\mathbf{P}^w_i$：

![image-20240427101146396](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/image-20240427101146396.png)

注意，由于 $\mathbf{P}_4$ 不受影响，因此未在上表中计算。我们将按以下方式计算 $a_3、a_2$ 和 $a_1$：

$a_{3}=\frac{t-u_{3}}{u_{6}-u_{3}}=\frac{0.4-0}{1-0}=0.4\\a_{2}=\frac{t-u_{2}}{u_{5}-u_{2}}=\frac{0.4-0}{1-0}=0.4\\a_{1}=\frac{t-u_{1}}{u_{4}-u_{1}}=\frac{0.4-0}{0.5-0}=0.8$


新的控制点$\mathbf{Q}^w_3, \mathbf{Q}^w_2$ 和 $\mathbf{Q}^w_1$ 为:

$$
\mathbf{Q}_{3}^{w}=(1-a_{3})\mathbf{P}_{2}^{w}+a_{3}\mathbf{P}_{3}^{w}=(325.6,26,4.4)\\\mathbf{Q}_{2}^{w}=(1-a_{2})\mathbf{P}_{1}^{w}+a_{2}\mathbf{P}_{2}^{w}=(97.4,142.5,1.9)\\\mathbf{Q}_{1}^{w}=(1-a_{1})\mathbf{P}_{0}^{w}+a_{1}\mathbf{P}_{1}^{w}=(-42,14.8,0.6)
$$


将这些控制点的前两个分量除以第三个分量投影回二维空间，得到

$$
\begin{array}{rcll}\mathrm{newP}_3&=&(74,5.9)&\mathrm{with~weight~4.4}\\\mathrm{newP}_2&=&(51.3,75)&\mathrm{with~weight~1.9}\\\mathrm{newP}_1&=&(-70,24.6)&\mathrm{with~weight~0.6}\end{array}
$$


下图是生成的NURBS曲线及其基函数：

![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-w-knot-in-2-1.jpg) ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/nurbs-w-knot-in-2-2.jpg)



# de Boor（德布尔）算法

一旦我们知道如何插入节点，NURBS曲线的de Boor算法就简单了。

我们只需要将每个控制点乘以它的权重，**将NURBS曲线转换为四维空间中的B样条曲线**，在这个四维B样条曲线上执行de Boor算法，然后通过将控制点的前三个分量除以第四个分量，并将第四个分量作为新的权重，就可以**将四维曲线投影回三维空间**。



# 有理贝塞尔曲线

将一个四维B样条曲线投影到 $w=1$ 的超平面会得到一个三维NURBS曲线。
那么如果这个B样条曲线是一个贝塞尔曲线呢？结果就是一个**有理贝塞尔曲线**！

下面的左图显示了一个4阶有理贝塞尔曲线，右图显示了一个三维4阶贝塞尔曲线（红色）及其在超平面 $w=1$ 中的投影有理贝塞尔曲线（蓝色）。

 ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/RB-curve-1.jpg)  ![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/RB-curve-projection-1.jpg) 



由一组$n+1$个控制点$\mathbf{P}_0, \mathbf{P}_1, ..., \mathbf{P}_n$定义的曲线是什么？每个控制点对应一个非负权重 $w_i$ (即$\mathbf{P}_i$的权重 $w_i$ >= 0)。增加控制点权重$\mathbf{P}^w_i (0 <= i <= n)$，可以使四维B样条曲线退化为一个$n$次贝塞尔曲线，它的基函数为 $B_{n,0}(u),B_{n,1}(u),...,B_{n,n}(u)$。将这个贝塞尔曲线投影到平面 $w = 1$，可以得到： 

$$
\mathbf{C}(u)=\sum_{i=0}^nR_{i,n}(u)\mathbf{P}_i
$$


$R_{i,n}(u)$的定义如下：

$$
R_{i,n}(u)=\frac{B_{n,i}(u)w_i}{\sum_{j=0}^nB_{n,j}(u)w_j}
$$

这是NURBS曲线的一个特殊情况，称为**有理Bézier**曲线。

由于**有理Bézier曲线是NURBS曲线的一个特例**，因此有理Bézier曲线满足所有NURBS曲线具有的重要性质。

然而，由于没有内部节点，**有理Bézier曲线不具备局部修改的特性**，这意味着修改控制点或其权重将导致整个曲线发生变化。修改控制点的权重将使曲线远离或朝向控制点。



# 有理贝塞尔曲线：圆锥曲线



由于贝塞尔曲线和B样条曲线是多项式曲线，只能表示抛物线。但NURBS和有理贝塞尔曲线是有理的，它们是否能表示椭圆、圆和双曲线，如果可以的话，应该如何做？



## 五个条件唯一地确定一个圆锥曲线

由三个不共线的控制点 $\mathbf{P}_0=(U_0,V_0),\mathbf{P}_1=(U_1,V_1)\mathrm{~and~}\mathbf{P}_2=(U_2,V_2)$ 定义的二次 Bézier曲线表示的是一个**抛物线**。我们希望扩展这个概念，以定义椭圆和双曲线的部分。

假设圆锥曲线通过$\mathbf{P}_0$和$\mathbf{P}_2$并且在$\mathbf{P}_0$和$\mathbf{P}_2$处分别与$\mathbf{P}_0\mathbf{P}_1$和$\mathbf{P}_1\mathbf{P}_2$相切，那么圆锥曲线可以用如下二次隐式方程表示，其中六个系数是未知数： 

$$
p(x,y)=ax^2+2bxy+cy^2+2dx+2ey+f=0
$$


如果$f$在上述方程中不为零，我们可以将整个方程除以$f$：

$$
ax^2+2bxy+cy^2+2dx+2ey+1=0
$$


这样我们只有五个未知数！如果$f$是零，我们已经有五个未知数了。由于这条曲线通过 $\mathbf{P}_0$点，将$\mathbf{P}_0$的坐标代入上述方程得到：

$$
aU_0^2+2bU_0V_0+cV_0^2+2dU_0+2eV_0+1=0
$$


方程的梯度计算如下：

$$
\nabla_{p(x,y)}=\langle2ax+2by+2d,2bx+2cy+2e\rangle 
$$

切线和梯度在点$\mathbf{P}_0=(U_0,V_0)$处互相垂直。

由于梯度的斜率为
$$
\frac{\mathrm{b}U_0+\mathrm{c}V_0+\mathrm{e}}{\mathrm{a}U_0+\mathrm{b}V_0+\mathrm{d}}
$$

在点$\mathbf{P}_0=(U_0,V_0)$处的切线的斜率为：
$$
-\frac{\mathrm{a}U_0+\mathrm{b}V_0+\mathrm{d}}{\mathrm{b}U_0+\mathrm{c}V_0+\mathrm{e}}
$$

由于$\mathbf{P}_0\mathbf{P}_1$是在$\mathbf{P}_0$处与圆锥曲线相切，且线段$\mathbf{P}_0\mathbf{P}_1$的斜率为$(V_1-V_0)/(U_1-U_0)$，这两个斜率值必须相等。因此，以下关系必须成立：

$$
\frac{V_1-V_0}{U_1-U_0}=-\frac{aU_0+bV_0+d}{bU_0+cV_0+e}
$$


由于圆锥曲线也通过 $\mathbf{P}_2$，因此我们有：

$$
aU_2^2+2bU_2V_2+cV_2^2+2dU_2+2eV_2+1=0
$$


圆锥曲线在$\mathbf{P}_2$点处与$\mathbf{P}_1\mathbf{P}_2$相切，因此有：

$$
\frac{V_{2}-V_{1}}{U_{2}-U_{1}}=-\frac{aU_{2}+bV_{2}+d}{bU_{2}+cV_{2}+e}
$$


现在，我们有四个方程。如果我们能找到另一个条件，我们将得到五个带有五个未知数的线性方程。解这个线性方程组将得到所有五个系数，从而唯一确定了圆锥曲线。

一种方式是再将一个点的坐标代入方程，得到一个类似于控制点 $\mathbf{P}_0$ 和 $\mathbf{P}_2$ 的方程。

但是，**这个点在哪里**？

这个点应该位于三个控制点构成的三角形内部，以保持凸包性质。
这个点的位置也应该是“规则的”，以便我们可以轻松地改变这个点以生成另一个圆锥曲线。

一种方法是允许这个点位于 $\mathbf{P}_1$ 和 $\mathbf{P}_0\mathbf{P}_2$ 中点的连线上。通过这种方式，将第五个点沿着这条连线移动会生成不同的圆锥曲线，如下所示：

![img$](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/BR-FIG-a-point.jpg)



## 连接点在哪里？

很容易看出，如果选择的点从$\mathbf{P}_0\mathbf{P}_2$的中点向$\mathbf{P}_1$移动，定义的椭圆曲线也会向控制点$\mathbf{P}_1$移动。如果点远离$\mathbf{P}_1$，它定义的曲线也会远离$\mathbf{P}_1$。因此，我们猜测，这个移动点的位置可以通过控制$\mathbf{P}_1$的权重来控制。

由于我们只需要一个点，该点受控制点$\mathbf{P}_1$的权重影响，我们可以用控制点$\mathbf{P}_0、\mathbf{P}_1$和$\mathbf{P}_2$定义的有理贝塞尔曲线，它们的权重分别为$1、w$和$1$。分配给控制点$\mathbf{P}_1$的权重将控制额外点的位置。二次有理贝塞尔曲线的系数如下所示：

$$
\begin{aligned}&B_{2,0}(u)=&&(1-u)^2\\&B_{2,1}(u)=&&2(1-u)u\\&B_{2,2}(u)=&&u^{2}\end{aligned}
$$


这个二次有理贝塞尔曲线的方程表示为：

$$
\mathbf{C}(u)=\frac{1}{(1-u)^{2}+2(1-u)uw+u^{2}}\Big((1-u)^{2}\mathbf{P}_{0}+2(1-u)uw\mathbf{P}_{1}+u^{2}\mathbf{P}_{2}\Big)
$$

我们将$\mathbf{P}_0$和$\mathbf{P}_2$放在$x$轴的两侧，并使$\mathbf{P}_0\mathbf{P}_2$的中点为坐标原点。因为有理贝塞尔曲线是投影不变的，因此简单的平移和旋转都不会改变曲线的形状。

如下图，我们有$\mathbf{P}_0 = -\mathbf{P}_2$，令$\mathbf{P}_0\mathbf{P}_2$的中点为$\mathbf{M}$，有理贝塞尔曲线与线段$\mathbf{M}\mathbf{P}_1$相交于$\mathbf{X}$点。

![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/BR-FIG-mid-point.jpg)

计算一下$u=0.5$处对应曲线上的点$C(u)$:

$$
\mathbf{C}(0.5)=\frac{w}{1+w}\mathbf{P}_1
$$

由于$C(0.5)$和$\mathbf{X}$是同一点，$\mathbf{X}$和控制点$\mathbf{P}_1$位于通过坐标原点$\mathbf{M}$的同一条直线上，且满足：

$$
|\overrightarrow{MX}|/|\overrightarrow{MP}_1| = \frac{w}{1+w}
$$

如果$w=1$，有理贝塞尔曲线就成为了贝塞尔曲线，即抛物线。在这种情况下
$$
|\overrightarrow{MX}|/|\overrightarrow{MP}_1| = \frac{w}{1+w} = 1/2
$$
此时点$\mathbf{X}$是线段$\mathbf{M}\mathbf{P}_1$的中点。



## 有理贝塞尔曲线如何表示椭圆或双曲线？

从给定圆锥曲线外的点 $\mathbf{A}$ 开始，画出两条切线，分别在 $\mathbf{X}$ 和 $\mathbf{Y}$ 处与曲线相交，并画一条任意的割线，使其与弦 $\mathbf{X}\mathbf{Y}$ 在点 $\mathbf{C}$ 处相交，并在点 $\mathbf{B}$  和 $\mathbf{D}$  处与圆锥曲线相交，其中 $\mathbf{B}$  在三角形 $\mathbf{A}\mathbf{X}\mathbf{Y}$  内，如下图所示。如果曲线是椭圆，则这些点的顺序是  $\mathbf{A}、\mathbf{B}、\mathbf{C}$ 和 $\mathbf{A}$（图a）； 如果它是双曲线，则点 $\mathbf{D}$ 位于曲线的另一侧上（图b）！

![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/BR-FIG-ellipse.jpg)  (a) Ellipse![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/BR-FIG-hyperbola.jpg)  (b) Hyperbola


根据投影的关系，我们有：
$$
\frac{|\mathrm{DC}|}{|\mathrm{CB}|}=\frac{|\mathrm{DA}|}{|\mathrm{AB}|}
$$
通过变换可以得到如下关系：
$$
\frac{|\mathrm{AB}|}{|\mathrm{CB}|}=\frac{|\mathrm{DA}|}{|\mathrm{DC}|}
$$
因为 $|\mathbf{CA}| = |\mathbf{CB}| + |\mathbf{BA}|$，我们可以按如下方式计算 $|\mathbf{CB}|/|\mathbf{CA}|$：
$$
\frac{|\mathrm{CB}|}{|\mathrm{CA}|}=\frac{|\mathrm{CB}|}{|\mathrm{CB}|+|\mathrm{BA}|}=\frac{1}{1+\frac{|\mathrm{BA}|}{|\mathrm{CB}|}}=\frac{1}{1+\frac{|\mathrm{DA}|}{|\mathrm{DC}|}}
$$
如果曲线是一个椭圆（或者双曲线），我们有 $|DA|>|DC|$ （或者$|DA|<|DC|$)，因此，$|CB|/|CA|$ 小于1/2（或大于）。

对于有理贝塞尔曲线，我们有$\mathbf{P}_{0}=\mathbf{X},\mathbf{P}_{1}=\mathbf{A},\mathbf{P}_{2}=\mathbf{Y},\mathbf{M}=\mathbf{C}$和$\mathbf{X}=\mathbf{C}(0.5)=\mathbf{B}$。因此，如果有理贝塞尔曲线表示的是椭圆，有
$$
\frac{w}{1+w}=\frac{|\mathrm{MX}|}{|\mathrm{MP}_1|}<\frac{1}{2}
$$


**这说明如果 $w < 1$，有理贝塞尔曲线表示的是椭圆。如果 $w > 1$，有理贝塞尔曲线表示的是双曲线。**



我们有以下结论：

**由三个非共线控制点$\mathbf{P}_0,\mathbf{P}_1$和 $\mathbf{P}_2$ 定义的有理贝塞尔曲线，三个控制点的权重分别为1、$w$ 和 1，如果 $w>1$ 则该曲线是一个双曲线；如果$w=1$，该曲线是抛物线；如果$w<1$，该曲线表示椭圆。**


# 圆弧和圆



最后，我们希望能够表示圆弧和圆。**前者使用有理贝塞尔曲线，后者使用NURBS**。

由于**圆是椭圆的特例，它们可以使用度数为2的有理贝塞尔曲线表示，唯一的权重$w<1$。**因此，如果我们修改这个权重为特殊值，我们就可以表示圆。

首先，我们知道控制多边形的两条边必须相等，即$\mathbf{P}_0\mathbf{P}_1=\mathbf{P}_1\mathbf{P}_2$。

假设有理贝塞尔曲线表示的圆其圆心和半径分别为 $\mathbf{O}$ 和 $\mathbf{r}$，如下图所示。

弦$P_0P_2$的中点为$\mathbf{M}$，圆与线段 $\mathbf{MP}_1$ 相交于 $\mathbf{X}$，设 $\mathbf{P}_1$ 的角度为 $2a$。我们需要找到一个$w$的值，使其满足$|\mathrm{MX}|/|\mathrm{MP}_1|=w/(1+w)$，从而确定定义该圆的有理贝塞尔曲线。

![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/BR-FIG-circular.jpg)


从直角三角形$OMP_0$，我们有$|OM| = r \sin(a)$，因此

$$
|\mathrm{MX}|=|\mathrm{OX}|-|\mathrm{OM}|=r-r\sin(a)=r(1-\sin(a))
$$


根据直角三角形$OP_oP_1$，我们有$\mathrm{OP}_1=r/\sin(a)$，因此$MP_1$为： 

$$
|\mathrm{MP}_1|=|\mathrm{OP}_1|-|\mathrm{OM}|=\frac{r}{\sin(a)}-r\sin(a)=\frac{r(1-\sin^2(a))}{\sin(a)}
$$


现在，我们可以使用$|\mathrm{MX}|/|\mathrm{MP}_1|$计算，$w/(1+w)$：

$$
\frac{w}{1+w}=\frac{|\mathrm{MX}|}{|\mathrm{MP}_1|}=\frac{\sin(a)}{1+\sin(a)}
$$


求解 $w$，我们得到一个令人惊讶的结果：**唯一权重值 $w$ 等于控制点 $\mathbf{P}_1$处的半角的正弦！**

$w=\sin(a)$


这说明：**给定三个控制点$P_{0},P_{1}$和$P_{2}$，并且满足$\mathsf{P}_0\mathsf{P}_1=\mathsf{P}_1\mathsf{P}_2$，$𝑤$为$\mathbf{P}_1$的权重，其中$𝑎$是控制点$\mathbf{P}_1$角度的一半，此时有理贝塞尔曲线是一个圆。**



有两个常见的例子：

## 四分之一圆

第一个例子是四分之一圆。点$\mathbf{P}_1$处的角度为90°，$a$为45度。因此，令$w = sin(45°) = 20.5/2$ 将生成一个四分之一圆。下图显示了这个四分之一圆和由相同控制点集定义的 $w= 1$时的抛物线。

![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/BR-FIG-90-degree.jpg)



## 三分之一圆

第二个例子是一个圆的三分之一。由于圆可以内切于一个等边三角形，这个圆的三分之一对应的角度为60度，因此，$a$为30°。如果令$w=sin(30°) = 1/2$，那么我们有下面所示的圆弧：

![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/BR-FIG-60-degree.jpg)



## 完整圆

我们可以取三个$1/3$圆弧或四个$1/4$圆弧，然后将它们拼接在一起组成一个完整的圆，如下图所示。但是，它是如何表示的？它必须是一个二次NURBS曲线。因此我们需要控制点和节点信息。

![img](https://raw.githubusercontent.com/3417725275/MarkdownImage/master/img/BR-FIG-2-circles.jpg)

让我们首先考虑等边三角形的情况。

如上图左侧所示。每个等边三角形的顶点都是先前描述的权重为$1/2$ 的控制点。
左下方的$1/3$由控制点 $\mathbf{P}_0$，$\mathbf{P}_1$ 和 $\mathbf{P}_2$ 定义；
顶部的$1/3$由 $\mathbf{P}_2$，**P**3 和 $\mathbf{P}_4$ 定义；
右下方的$1/3$由 $\mathbf{P}_4$，$\mathbf{P}_5$ 和 $\mathbf{P}_6 = \mathbf{P}_0$ 定义。

接下来，我们要研究节点。由于 $n = 6，p = 2$，那么 $m = 6 + 2 + 1$（即，10 个节点）。在这 10 个节点中，前三个和后三个是 0 和 1（即$u_0 = u_1 = u_2 = 0，u_7 = u_8 = u_9 = 1$）。

到目前为止，未知的节点是 $u_3，u_4，u_5$ 和 $u_6$。

一种方式是将$1/3$和$2/3$作为内部节点，因为在区间 $[0, 1/3]，[1/3, 2/3]$ 和 $[2/3, 1]$ 上的圆弧将整个圆分成三个等长的圆弧。因此，我们还需要两个节点。

在上图中，你会看到控制点$\mathbf{P}_2$位于圆上，其位置是其长度的$1/3$。

我们如何让曲线通过一个控制点呢？可以采用**de Boor**算法。当计算一个B样条/NURBS曲线上对应于$u$的点时，我们将$u$多次插入，直到$u$的重数是$p$，其中$p$是曲线的次数。当最后一次插入$u$时，曲线上对应的点实际上是一个(新)控制点$\mathbf{P}_2$！

这个结论告诉我们，如果$1/3$的重数是2，那么曲线上对应的点是一个控制点。

因此可以得到$u_3 = u_4 = 1/3$和$u_5 = u_6 = 2/3$。

我们有结论：

**要用等边三角形形定义一个完整的圆，我们要有节点$0,0,0,1/3,1/3,2/3,2/3,1,1,1$**
**要用一个正方形定义一个完整的圆，我们需要如图所示的九个控制点和节点向量$0,0,0,1/4,1/4,1/2,1/2,3/4,3/4,1,1,1$**

**那么，如何用一个有$n$条边的正多边形来定义一个完整的圆？**

