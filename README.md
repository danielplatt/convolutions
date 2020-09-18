# convolutions

## Background

This repository compares ordinary convolution of smooth functions on the 2-torus with the spectral graph convolution defined in _Bruna, Joan, et al. "Spectral networks and locally connected networks on graphs"_ (https://arxiv.org/abs/1312.6203).

Define the 2-torus <img src="https://render.githubusercontent.com/render/math?math=T^2"> to be the unit square 2-torus <img src="https://render.githubusercontent.com/render/math?math=[0,1]^2"> with opposing sides identified, i.e. the unit square with the property that one reappears on the other side if one leaves the square on one side.
Let <img src="https://render.githubusercontent.com/render/math?math=f,g"> be functions on <img src="https://render.githubusercontent.com/render/math?math=T^2">.
The ordinary convolution of <img src="https://render.githubusercontent.com/render/math?math=f,g"> is defined to be:

<img src="https://render.githubusercontent.com/render/math?math=f \star g(x) = \int_{T^2} f(y)g(x-y) \, \text{d}y">

Let <img src="https://render.githubusercontent.com/render/math?math=\Gamma"> be an evenly spaced grid on <img src="https://render.githubusercontent.com/render/math?math=T^2"> with <img src="https://render.githubusercontent.com/render/math?math=n^2"> vertices, denote the vertex set by <img src="https://render.githubusercontent.com/render/math?math=V">.
For any function <img src="https://render.githubusercontent.com/render/math?math=f"> on <img src="https://render.githubusercontent.com/render/math?math=T^2"> denote by <img src="https://render.githubusercontent.com/render/math?math=\widehat{f}=f \mid _V"> its restriction to the vertices of the graph.
I.e., <img src="https://render.githubusercontent.com/render/math?math=f"> can be seen as a matrix of size <img src="https://render.githubusercontent.com/render/math?math=n \times n"> with real entries.
Let <img src="https://render.githubusercontent.com/render/math?math=(w_1, \dots, w_{n^2})"> be an orthonormal basis of eigenvectors of the graph Laplacian of <img src="https://render.githubusercontent.com/render/math?math=\Gamma"> (this basis has <img src="https://render.githubusercontent.com/render/math?math=n^2"> elements).
The spectral graph convolution of <img src="https://render.githubusercontent.com/render/math?math=\widehat{f},\widehat{g}"> is then defined to be:

<img src="https://render.githubusercontent.com/render/math?math=\widehat{f} \star \widehat{g} = \sum_{i=1}^{n^2} \langle \widehat{f}, v_i \rangle \langle \widehat{g}, v_i \rangle v_i">

Here, <img src="https://render.githubusercontent.com/render/math?math=\langle \cdot, \cdot \rangle"> denotes the <img src="https://render.githubusercontent.com/render/math?math=L^2">-inner product on <img src="https://render.githubusercontent.com/render/math?math=\mathbb{R}^{n \times n}">.

We answer the question to what extent to following approximate equality holds:
<img src="https://render.githubusercontent.com/render/math?math=\widehat{f} \star \widehat{g} \approx \widehat{(f \star g)}">.
That is:
to what extent do convolution and restricting a function to <img src="https://render.githubusercontent.com/render/math?math=\Gamma"> commute?

## Answer

We observe that the two convolutions are close to agreeing if one chooses the eigenbasis <img src="https://render.githubusercontent.com/render/math?math=(w_1, \dots, w_{n^2})"> to mimic the eigenbasis of the smooth Laplacian on the circle.
To be precise, basis elements are given by restricting the functions 
<img src="https://render.githubusercontent.com/render/math?math=e^{2 \pi i x k/n}e^{2 \pi i y l/n}"> to the vertices of the graph.
Using this basis, we apply smooth convolution and graph convolution in some test cases and observe that the two approximately agree.
Note that the very non-smooth sixth example gives different results.

![Comparing convolutions 1](graph_laplacian/images/fourier_convolution_1.png)
![Comparing convolutions 2](graph_laplacian/images/fourier_convolution_2.png)
![Comparing convolutions 3](graph_laplacian/images/fourier_convolution_3.png)
![Comparing convolutions 4](graph_laplacian/images/fourier_convolution_4.png)
![Comparing convolutions 5](graph_laplacian/images/fourier_convolution_5.png)
![Comparing convolutions 6](graph_laplacian/images/fourier_convolution_6.png)

If choosing the eigenbasis computed by scipy, we find that the two convolutions do not agree:

![Comparing scipy convolutions 1](graph_laplacian/images/scipy_convolution_1.png)
![Comparing scipy convolutions 2](graph_laplacian/images/scipy_convolution_2.png)
![Comparing scipy convolutions 3](graph_laplacian/images/scipy_convolution_3.png)
![Comparing scipy convolutions 4](graph_laplacian/images/scipy_convolution_4.png)
![Comparing scipy convolutions 5](graph_laplacian/images/scipy_convolution_5.png)
![Comparing scipy convolutions 6](graph_laplacian/images/scipy_convolution_6.png)

## Reproducing the experiment

Run ```graph_laplacian/commuting_operations_experiments.py``` and change line 55 ```path1_conv = path1(f, g, n, 'fourier_series')``` back and forth from ```'fourier_series'``` to ```'scipy'``` to observe the effect of choosing different eigenbases.
