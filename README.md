# fixed-point
Krasnosel'skii-Mannアルゴリズムの実装例です。
Krasnosel'skii-Mannアルゴリズムは以下のようなアルゴリズムです。ただし、Tは非拡大写像です。

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?x_{k&plus;1}&space;=&space;\alpha&space;x_k&space;&plus;(1-\alpha)T(x_k)">
</p>

## 実行方法
2次元の場合に4つの閉球への距離射影を与えた場合のサンプルプログラムを実行できます。
```
python3 src/main.py
```

サンプルプログラムで扱う非拡大写像は、各Piを閉球への距離射影として、

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?T_1(x)&space;:=&space;P_1&space;\cdots&space;P_m(x)">
</p>
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?T_2(x)&space;:=&space;P_1\left(&space;\sum_{i=2}^mw_iP_i(x)&space;\right&space;)">
</p>
  
の二つです。
比較するアルゴリズムは以下の4種類です。

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?\\&space;\text{KM0}:&space;\quad&space;\alpha&space;=&space;0.5,&space;\,&space;T&space;=&space;T_1&space;\\&space;\text{KM1}:&space;\quad&space;\alpha&space;=&space;0.5,&space;\,&space;T&space;=&space;T_2,&space;\,&space;w_2&space;=&space;w_3&space;=&space;w_4&space;=&space;1/3&space;\\&space;\text{KM2}:&space;\quad&space;\alpha&space;=&space;0.9,&space;\,&space;T&space;=&space;T_1&space;\\&space;\text{KM3}:&space;\quad&space;\alpha&space;=&space;0.9,&space;\,&space;T&space;=&space;T_2,&space;\,&space;w_2&space;=&space;w_3&space;=&space;w_4&space;=&space;1/3">
</p>
  
### 実行結果
サンプルプログラムの問題の4つの閉球とKrasnosel'skii-Mannアルゴリズムにより生成された点列を2次元平面に描画した結果です。
反復回数は30回としています。

![fig1](./img/fig1.jpg)

特に、解の周辺での振る舞いは以下のようになっています。

![fig2](./img/fig2.jpg)

KM2およびKM3のアルゴリズムは、30回の反復では不動点を十分に近似できていないようです。
