import os
import numpy as np
from typing import List
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from numpy.core.fromnumeric import reshape


def show_result_2D(centers: np.ndarray, raiduses: np.ndarray,
                    histories: List[dict], dir: str=None, name: str='2d_fig.pdf') -> None:
    '''
        2次元の不動点問題を解いた場合の結果を視覚化する.
        <引数>
            center:     閉球の族の中心を表す2次元のNumPy配列.
                            [[1., 0.], [0., 1.], [1., 1.]]
                        で中心をそれぞれ (1, 0), (0, 1), (1, 1) とする3つの閉球を表す.
            
            radius:     閉球の族の半径を表す1次元のNumPy配列.
                            [1., 2., 3.]
                        で半径をそれぞれ 1, 2, 3 とする3つの閉球を表す.

            results:    アルゴリズムによって得られた結果を保持する辞書のリスト.

            dir:        指定することで画像として保存する.

            name:       画像として保存する際の名前.
    '''
    
    fig = plt.figure()
    ax = plt.axes()

    for history in histories:
        result = history['xk']
        if result.shape[1] > 2:
            raise Exception()
        ax.plot(result[:, 0], result[:, 1], marker='o',
            linewidth=0.75, markersize=3., label=history['name'])

    # 閉球の描画
    for center, radius in zip(centers, raiduses):
        circle = patches.Circle(center, radius=radius, fill=False)
        ax.add_patch(circle)

    plt.axis('scaled')
    ax.set_aspect('equal')
    ax.legend()
    ax.set_xlabel(r'$x_1$')
    ax.set_ylabel(r'$x_2$')

    if dir is None:
        plt.show()
    else:
        plt.savefig(os.path.join(dir, name))


def show_dist(histories: List[list], dir: str=None, name: str='dist_fig.pdf') -> None:
    '''
        不動点問題を解いた場合のxとT(x)の距離の結果を視覚化する.
        <引数>
            results:    アルゴリズムによって得られた結果を保持する辞書のリスト.

            dir:        指定することで画像として保存する.

            name:       画像として保存する際の名前.
    '''
    fig = plt.figure()
    ax = plt.axes()

    for history in histories:
        result = history['dist']
        ax.plot(range(len(result)), result, label=history['name'])
    
    ax.set_yscale('log')
    ax.legend()
    ax.set_xlabel('iteration')
    ax.set_ylabel(r'$\||x_k - T(x_k)\||$')
    
    if dir is None:
        plt.show()
    else:
        plt.savefig(os.path.join(dir, name))
