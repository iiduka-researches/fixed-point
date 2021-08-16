# fixed-point
Krasnoselskii-Mannアルゴリズムの実装例です。
Krasnoselskii-Mannアルゴリズムは以下のようなアルゴリズムです。ただし、Tは非拡大写像です。

<img src="https://latex.codecogs.com/gif.latex?x_{k&plus;1}&space;=&space;\alpha&space;x_k&space;&plus;(1-\alpha)T(x_k)">

## 実行方法
2次元の場合に4つの閉球への距離射影を与えた場合のサンプルプログラムを実行できます。
```
python3 src/main.py
```

サンプルプログラムで扱う非拡大写像は、各Piを閉球への距離射影として、

<img src="https://latex.codecogs.com/gif.latex?T_1(x)&space;:=&space;P_1&space;\cdots&space;P_m(x)">
<img src="https://latex.codecogs.com/gif.latex?T_2(x)&space;:=&space;P_1\left(&space;\sum_{i=2}^mw_iP_i(x)&space;\right&space;)">

の二つです。
比較するアルゴリズムの詳細は、コードを参照してください。

### 実行結果
サンプルプログラムの問題の4つの閉球とKrasnoselskii-Mannアルゴリズムにより生成された点列を2次元平面に描画した結果です。

![fig1](./img/fig1.jpg)

特に、解の周辺での振る舞いは以下のようになっています。

![fig2](./img/fig2.jpg)
