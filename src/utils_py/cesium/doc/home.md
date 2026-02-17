
<h1 id="inicio" align="center" style="text-decoration: underline;"> Modulo de Cesium </h1>

- [Descripcion](#descripcion)
- [Matematicas](#matematicas)
    - [tiles](#matematicas-tiles)
        [coordenadas](#matematicas-tiles-coordenadas)

<h2 id="descripcion" align='right' style="text-decoration:underline;"> Descripcion </h2>

[inicio](#inicio)
El siguiente modulo este modulo se utilizar para manejar CesiumJS.

<h2 id="matematicas" align="right" style="text-decoration:underline;"> Matematicas </h2>

<h3 id="matematicas-tiles">tiles</h3>

[inicio](#inicio)
los tiles de cesiumJS se refiere a un arbol de tiles, el padre tiene a su vez 4 tiles hijos.
en CesiumJS los tiles tiene la particularidad que en el nivel de zoom **0** solo tiene un tile en el eje **y** se basa en la siguiente formula matematica 

<h6 id="matematicas-tiles-1"></h6>

$$
\text{world}_{x,y}^\text{tile}
\begin{cases}
x = \dfrac{360}{2^{l+1}} \\
y = \dfrac{180}{2^{l}}
\end{cases}
$$

esta formula matematica los que nos otorga es cuanto mide la cuadricula individual en grados.
un ejemplo en el caso donde el nivel de zoom es **1** y **10**

<h6 align="center">EJEMPLO</h6>

---
<h6 align="center">zoom = 1</h6>

$$
\text{tile}_{x,y}^\text{count}
\begin{cases}
x = \dfrac{360}{2^{1+1}} \\
y = \dfrac{180}{2^{1}}
\end{cases}
$$

$$
\text{tile}_{x,y}^\text{count}
\begin{cases}
x = \dfrac{360}{4} \\
y = \dfrac{180}{2}
\end{cases}
$$

$$
\text{tile}_{x,y}^\text{count}
\begin{cases}
x = 90 \\
y = 90
\end{cases}
$$

---
<h6 align="center">zoom = 10</h6>

$$
\text{tile}_{x,y}^\text{count}
\begin{cases}
x = \dfrac{360}{2^{10+1}} \\
y = \dfrac{180}{2^{10}}
\end{cases}
$$

$$
\text{tile}_{x,y}^\text{count}
\begin{cases}
x = \dfrac{360}{2048} \\
y = \dfrac{180}{1024}
\end{cases}
$$

$$
\text{tile}_{x,y}^\text{count}
\begin{cases}
x = 0.17578125 \\
y = 0.17578125
\end{cases}
$$

---
<h4 id="matematicas-tiles-coordenadas"> Optener coordenadas de tiles</h4>

[inicio](#inicio)

como un tile es la divicion de todo el plano planetario, tenemos que dividir la coordenada que optuvimos por la divicion del terreno que se mencionan en [tiles](#matematicas-tiles-1). esto nos va a dar un valor flotante que va de $ 0 \leftrightarrow N$ donde $N$ es el valor maximo de tiles en el nivel de zoom $l$ que vimos en [tiles](#matematicas-tiles-1)

$$
\text{world}_{x,y}^\text{tile}
\begin{cases}
x = \dfrac{longitud}{N} \\
y = \dfrac{latitud}{N}
\end{cases}
$$

un ejemplo es el el nivel de zoom **0**

<h6 align="center">EJEMPLO</h6>

---
<h6 align="center">zoom = 0</h6>

$$
\N
\begin{cases}
x = \dfrac{360}{2^{0+1}} \\
y = \dfrac{180}{2^{0}}
\end{cases}
$$

$$
\N
\begin{cases}
x = \dfrac{360}{2} \\
y = \dfrac{180}{1}
\end{cases}
$$

$$
\N
\begin{cases}
x = 180 \\
y = 180
\end{cases}
$$

$$
\text{world}_{x,y}^\text{tile}
\begin{cases}
x = \frac{186}{180} \\
y = \frac{158}{180}
\end{cases}
$$

$$
\text{world}_{x,y}^\text{tile}
\begin{cases}
x = \dfrac{186}{180} = 1.0333333333\ldots \\
y = \dfrac{158}{180} = 0.8777777777\ldots
\end{cases}
$$

---

para que esta valor nos sirva necesitamos un valor entero positivo de los numeros naturales, y para optenerlo tenemos que optener el modulo y luego optener el floor delnumero. ej

$$
\text{world}_{x,y}^\text{tile}
\begin{cases}
x = \left\lfloor\left|\dfrac{longitud}{N}\right|\right\rfloor \\
y = \left\lfloor\left|\dfrac{latitud}{N}\right|\right\rfloor
\end{cases}
$$

para dejarlo todo junto en una misma funcion se tendriaq ue reemplazar $N$ con su respectiva funcion de [tiles](#matematicas-tiles-1) 

$$
world_{x,y}^{\mathrm{tile}} =
\begin{cases}
x = \left\lfloor \dfrac{\mathrm{long}}{\frac{360}{2^{l+1}}} \right\rfloor \\
y = \left\lfloor \dfrac{\mathrm{lat}}{\dfrac{180}{2^{l}}} \right\rfloor
\end{cases}
$$

el problema aca es que estamos tratando esta funcion como si CesiumJS manejara los valores de coordenadas de $0 \leftrightarrow 360$ | $0 \leftrightarrow 180$ lo unico que trabaja de esta manera son los tiles y no las coordenadas, las coordenadas estan partidas a la mitad  $-180 \leftrightarrow 180$ | $-90 \leftrightarrow 90$ por lo cual tenemos que agregarle un desface como va de $este \leftrightarrow oeste$ a $x$ se le sumara 180 y aca depende de si $y$ esta invertido. En el caso basico esta invertido, a $y$ como va de $norte \leftrightarrow sur$ y no de $sur \leftrightarrow norte$ a la y le vasmos a restar 90

$$
world_{x,y}^{\mathrm{tile}} =
\begin{cases}
x = \left\lfloor \left| \dfrac{\mathrm{long+180}}{\frac{360}{2^{l+1}}} \right|\right\rfloor \\
y = \left\lfloor \left|\dfrac{\mathrm{lat-90}}{\dfrac{180}{2^{l}}} \right|\right\rfloor
\end{cases}
$$

ahora esa funcion es demaciado complejas por lo cual lo vamos a factorizar a lo siguiente

$$
world_{x,y}^{\mathrm{tile}} = \begin{Bmatrix}
x = \left \lfloor \left | \frac{(long+180).2^{l+1}}{360}\right |\right \rfloor \\
y = \left \lfloor \left | \frac{(lat-90).2^{l}}{180}\right |\right \rfloor 
\end{Bmatrix}
$$