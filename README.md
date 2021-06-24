# Linear Algebra Refresher Course

Python class for vector algebra

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;v&space;=&space;\begin{bmatrix}&space;x\\&space;y\\&space;z\\&space;\end{bmatrix}" title="v = \begin{bmatrix} x\\ y\\ z\\ \end{bmatrix}" style="margin: 0 20px;" />
<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;v_{1}&space;=&space;\begin{bmatrix}&space;x_{1}\\&space;y_{1}\\&space;z_{1}\\&space;\end{bmatrix}" title="v_{1} = \begin{bmatrix} x_{1}\\ y_{1}\\ z_{1}\\ \end{bmatrix}" style="margin:0  20px;" />
<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;v_{2}&space;=&space;\begin{bmatrix}&space;x_{2}\\&space;y_{2}\\&space;z_{2}\\&space;\end{bmatrix}" title="v_{2} = \begin{bmatrix} x_{2}\\ y_{2}\\ z_{2}\\ \end{bmatrix}" style="margin: 0 20px;" />

## Addition

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;v_{1}&space;&plus;&space;v_{2}&space;=&space;\begin{bmatrix}&space;x_{1}\\&space;y_{1}\\&space;z_{1}\\&space;\end{bmatrix}&space;&plus;\begin{bmatrix}&space;x_{2}\\&space;y_{2}\\&space;z_{2}\\&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;x_{1}&space;&plus;x_{2}\\&space;y_{1}&space;&plus;&space;y_{2}\\&space;z_{1}&space;&plus;&space;z_{2}\\&space;\end{bmatrix}" title="v_{1} + v_{2} = \begin{bmatrix} x_{1}\\ y_{1}\\ z_{1}\\ \end{bmatrix} +\begin{bmatrix} x_{2}\\ y_{2}\\ z_{2}\\ \end{bmatrix} = \begin{bmatrix} x_{1} +x_{2}\\ y_{1} + y_{2}\\ z_{1} + z_{2}\\ \end{bmatrix}" />

## Subtraction

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;v_{1}&space;-&space;v_{2}&space;=&space;\begin{bmatrix}&space;x_{1}\\&space;y_{1}\\&space;z_{1}\\&space;\end{bmatrix}&space;-\begin{bmatrix}&space;x_{2}\\&space;y_{2}\\&space;z_{2}\\&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;x_{1}&space;-&space;x_{2}\\&space;y_{1}&space;-&space;y_{2}\\&space;z_{1}&space;-&space;z_{2}\\&space;\end{bmatrix}" title="v_{1} - v_{2} = \begin{bmatrix} x_{1}\\ y_{1}\\ z_{1}\\ \end{bmatrix} -\begin{bmatrix} x_{2}\\ y_{2}\\ z_{2}\\ \end{bmatrix} = \begin{bmatrix} x_{1} - x_{2}\\ y_{1} - y_{2}\\ z_{1} - z_{2}\\ \end{bmatrix}" />

## Magnitude (Length)

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\left&space;\|&space;\bar{v}&space;\right&space;\|&space;=&space;\sqrt{x^{2}&space;&plus;&space;y^{2}&space;&plus;&space;z^{2}}" title="\left \| \bar{v} \right \| = \sqrt{x^{2} + y^{2} + z^{2}}" />

## Normalization

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\frac{\bar{v}}{\left&space;\|&space;\bar{v}&space;\right&space;\|}" title="\frac{\bar{v}}{\left \| \bar{v} \right \|}" />

## Multiplication

### By Scalar

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\bar{v}&space;*&space;k&space;=&space;\begin{bmatrix}&space;x&space;*&space;k\\&space;y&space;*&space;k\\&space;z&space;*&space;k&space;\end{bmatrix}" title="\bar{v} * k = \begin{bmatrix} x * k\\ y * k\\ z * k \end{bmatrix}" />

### Dot Product (Inner Product)

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\bar{v_{1}}&space;\cdot&space;\bar{v_{2}}&space;=&space;\left&space;\|&space;\bar{v_{1}}&space;\right&space;\|&space;\cdot&space;\left&space;\|&space;\bar{v_{2}}&space;\right&space;\|&space;\cdot&space;\cos&space;(\alpha&space;)" title="\bar{v_{1}} \cdot \bar{v_{2}} = \left \| \bar{v_{1}} \right \| \cdot \left \| \bar{v_{2}} \right \| \cdot \cos (\alpha )" /><br/>

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\alpha&space;=&space;\arccos&space;(\frac{\bar{v_{1}}}{\left&space;\|&space;\bar{v_{1}}&space;\right&space;\|}&space;\cdot&space;\frac{\bar{v_{2}}}{\left&space;\|&space;\bar{v_{2}}&space;\right&space;\|})" title="\alpha = \arccos (\frac{\bar{v_{1}}}{\left \| \bar{v_{1}} \right \|} \cdot \frac{\bar{v_{2}}}{\left \| \bar{v_{2}} \right \|})" /><br/>

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\bar{v_{1}}&space;\cdot&space;\bar{v_{2}}&space;=&space;x_{1}\cdot&space;x_{2}&space;&plus;&space;y_{1}\cdot&space;y_{2}&space;&plus;&space;z_{1}\cdot&space;z_{2}" title="\bar{v_{1}} \cdot \bar{v_{2}} = x_{1}\cdot x_{2} + y_{1}\cdot y_{2} + z_{1}\cdot z_{2}" />

2 vectors are parallel, if

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\cos&space;(\alpha&space;)&space;=&space;\pm&space;1" title="\cos (\alpha ) = \pm 1" style="margin-right: 20px;" />
or
<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\frac{\bar{v_{1}}}{\left&space;\|&space;\bar{v_{1}}&space;\right&space;\|}\cdot&space;\frac{\bar{v_{2}}}{\left&space;\|&space;\bar{v_{2}}&space;\right&space;\|}&space;=&space;\pm&space;1" title="\frac{\bar{v_{1}}}{\left \| \bar{v_{1}} \right \|}\cdot \frac{\bar{v_{2}}}{\left \| \bar{v_{2}} \right \|} = \pm 1" style="margin-left: 20px;" />

2 vectors are orthogonal, if

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\cos&space;(\alpha&space;)&space;=&space;0" title="\cos (\alpha ) = 0" style="margin-right: 20px;" />
or
<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\bar{^{v_{1}}}&space;\cdot&space;\bar{^{v_{2}}}&space;=&space;0" title="\bar{^{v_{1}}} \cdot \bar{^{v_{2}}} = 0" style="margin-left: 20px;" />

### Projecting Vectors

#### Parallel projection on vector b

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\bar{v^{\parallel}}&space;=&space;(\bar{v}&space;\cdot&space;\bar{u_{b}})&space;\cdot&space;\bar{u_{b}}" title="\bar{v^{\parallel}} = (\bar{v} \cdot \bar{u_{b}}) \cdot \bar{u_{b}}" style="margin-right: 40px;" />,<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\bar{u_{b}}&space;=&space;\frac{\bar{b}}{\left&space;\|&space;\bar{b}&space;\right&space;\|}" title="\bar{u_{b}} = \frac{\bar{b}}{\left \| \bar{b} \right \|}" style="margin: 0 20px;" />

#### Orthogonal projection on vector b

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\bar{v}^{\perp&space;}&space;=&space;\bar{v}&space;-&space;\bar{v}^{\parallel&space;}" title="\bar{v}^{\perp } = \bar{v} - \bar{v}^{\parallel }" />

### Cross Product

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\bar{v}&space;\times&space;\bar{w}" title="\bar{v} \times \bar{w}" style="margin-right: 20px;" /> orthogonal to both <img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\bar{v}" title="\bar{v}" style="margin: 0 10px;" /> and <img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\bar{w}" title="\bar{w}" style="margin-left: 10px;" /> (right hand rule)

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\left&space;\|&space;\bar{v}&space;\times&space;\bar{w}&space;\right&space;\|&space;=&space;\left&space;\|&space;\bar{v}&space;\right&space;\|&space;\cdot&space;\left&space;\|&space;\bar{w}&space;\right&space;\|&space;\cdot&space;\sin&space;(\alpha&space;)" title="\left \| \bar{v} \times \bar{w} \right \| = \left \| \bar{v} \right \| \cdot \left \| \bar{w} \right \| \cdot \sin (\alpha )" /><br/>

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\left&space;\|&space;\bar{v}&space;\times&space;\bar{w}&space;\right&space;\|&space;=&space;-(\left&space;\|&space;\bar{w}&space;\times&space;\bar{v}&space;\right&space;\|)" title="\left \| \bar{v} \times \bar{w} \right \| = -(\left \| \bar{w} \times \bar{v} \right \|)" /><br/>

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\left&space;\|&space;\bar{v}&space;\times&space;\bar{w}&space;\right&space;\|" title="\left \| \bar{v} \times \bar{w} \right \|" style="margin-right: 20px;" /> - area of parallelogram

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\frac{1}{2}\left&space;\|&space;\bar{v}&space;\times&space;\bar{w}&space;\right&space;\|" title="\frac{1}{2}\left \| \bar{v} \times \bar{w} \right \|" style="margin-right: 20px;" /> - area of triangle

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\left&space;\|&space;\bar{v}&space;\times&space;\bar{w}&space;\right&space;\|&space;=&space;\begin{bmatrix}&space;y_{1}z_{2}&space;-&space;y_{2}z_{1}\\&space;-(x_{1}z_{2}&space;-&space;x_{2}z_{1})\\&space;x_{1}y_{2}&space;-&space;x_{2}y_{1}&space;\end{bmatrix}" title="\left \| \bar{v} \times \bar{w} \right \| = \begin{bmatrix} y_{1}z_{2} - y_{2}z_{1}\\ -(x_{1}z_{2} - x_{2}z_{1})\\ x_{1}y_{2} - x_{2}y_{1} \end{bmatrix}" />

## Intersections

### Lines in 2D

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;A&space;x&space;&plus;&space;B&space;y&space;=&space;k" title="A\cdot x + B\cdot y = k" />

Basepoints:

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\left&space;(&space;0,\frac{k}{B}&space;\right&space;)" title="\left ( 0,\frac{k}{B} \right )" style="margin-right: 20px" />, if B&#8800;0<br/>

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\left&space;(&space;\frac{k}{A},0&space;\right&space;)" title="\left ( \frac{k}{A}, 0\right )" style="margin-right: 20px" />, if A&#8800;0

With basepoint (0,0):

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;A&space;x&space;&plus;&space;B&space;y&space;=&space;0" title="A\cdot x + B\cdot y = 0" /><br/>

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\begin{bmatrix}&space;A\\&space;B&space;\end{bmatrix}&space;\cdot&space;\begin{bmatrix}&space;x\\&space;y&space;\end{bmatrix}&space;=&space;0" title="\begin{bmatrix} A\\ B \end{bmatrix} \cdot \begin{bmatrix} x\\ y \end{bmatrix} = 0" />

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\begin{bmatrix}&space;A\\&space;B&space;\end{bmatrix}" title="\begin{bmatrix} A\\ B \end{bmatrix}" style="margin-right: 10px;" /> and <img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\begin{bmatrix}&space;x\\&space;y&space;\end{bmatrix}" title="\begin{bmatrix} x\\ y \end{bmatrix}" style="margin: 0 10px;" /> orthogonal


<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\begin{bmatrix}&space;A\\&space;B&space;\end{bmatrix}" title="\begin{bmatrix} A\\ B \end{bmatrix}" style="margin-right: 20px;" /> normal vector for the line <img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;A&space;x&space;&plus;&space;B&space;y&space;=&space;k" title="A\cdot x + B\cdot y = k" style="margin-left: 20px;" /><br/>

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\begin{bmatrix}&space;B\\&space;-A&space;\end{bmatrix}" title="\begin{bmatrix} B\\ -A \end{bmatrix}" style="margin-right: 20px;" /> direction vector for the line <img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;A&space;x&space;&plus;&space;B&space;y&space;=&space;k" title="A\cdot x + B\cdot y = k" style="margin-left: 20px;" />

#### Intersection of 2 lines

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\left\{\begin{matrix}&space;Ax&plus;By=k_{1}\\&space;Cx&plus;Dy=k_{2}&space;\end{matrix}\right." title="\left\{\begin{matrix} Ax+By=k_{1}\\ Cx+Dy=k_{2} \end{matrix}\right." /><br/>

<img src="https://latex.codecogs.com/png.latex?\inline&space;\fn_jvn&space;\left\{\begin{matrix}&space;x=\frac{Dk_{1}-Bk_{2}}{AD-BC}\\&space;\\&space;y=\frac{-Ck_{1}&plus;Ak_{2}}{AD-BC}&space;\end{matrix}\right." title="\left\{\begin{matrix} x=\frac{Dk_{1}-Bk_{2}}{AD-BC}\\ \\ y=\frac{-Ck_{1}+Ak_{2}}{AD-BC} \end{matrix}\right." />
