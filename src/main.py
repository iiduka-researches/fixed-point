import numpy as np
from typing import List
from collections.abc import Callable

from utils import show_result_2D, show_dist


class KrasnoselskiiMann(object):
    '''
        Krasnoselskii-Mannアルゴリズムのクラス.
    '''
    count = 0

    def __init__(self, alpha: float, T: Callable[[np.ndarray], np.ndarray], name: str=None) -> None:
        '''
            <引数>
                alpha:  0より大きく1未満のパラメータ.

                T:      不動点を求めたい非拡大写像.

                name:   このKrasnoselskii-Mannアルゴリズムの名前
        '''
        if not 0 < alpha < 1:
            raise ValueError(f'Invalid alpha value: {alpha}')
        self.alpha = alpha
        self.T = T
        if name is None:
            self.name = f'KM{KrasnoselskiiMann.count}'
            KrasnoselskiiMann.count += 1
        else:
            self.name = name
        self.history = None  # 結果の保存用辞書

    def __repr__(self) -> str:
        return self.history.__repr__()

    def solve(self, x0: np.ndarray, n_iter: int=10) -> dict:
        '''
            Krasnoselskii-Mannアルゴリズムを実行する。
            <引数>
                x0:     初期点を表す1次元のNumPy配列.

                n_iter: 反復回数. 初期値は10.
        '''
        
        alpha = self.alpha
        T = self.T

        # 結果の保存用辞書
        history = {
                    'name': self.name,
                    'xk': [x0.tolist()],
                    'dist': [np.linalg.norm(x0 - T(x0))],
                    'final': None
                }
        
        xk = x0
        
        # Krasnoselskii-Mannアルゴリズムの本体.
        for n in range(n_iter):
            xk = alpha * xk + (1 - alpha) * T(xk)
            history['xk'].append(xk.tolist())  # 点の保存
            history['dist'].append(np.linalg.norm(xk - T(xk)))
        
        history['final'] = xk
        history['xk'] = np.array(history['xk'])
        self.history = history

        return history


def create_projection(center: np.ndarray, radius: float) -> Callable[[np.ndarray], np.ndarray]:
    '''
        閉球への距離射影を返す.
        <引数>
            center:     閉球の中心を表す1次元のNumPy配列

            radius:     閉球の族の半径を表すfloat型変数.
    '''
    def projection(x: np.ndarray) -> np.ndarray:
        dist = np.linalg.norm(x - center)
        if dist <= radius:
            return x
        else:
            return center + (x - center) / dist
    
    return projection


def create_T(centers: np.ndarray, raiduses: np.ndarray, w: List[float]=None) -> Callable[[np.ndarray], np.ndarray]:
    '''
        閉球への距離射影の族 P1, ... ,Pm から作られる非拡大写像を返す.
        <引数>
            center:     閉球の族の中心を表す2次元のNumPy配列.
                            [[1., 0.], [0., 1.], [1., 1.]]
                        で中心をそれぞれ (1, 0), (0, 1), (1, 1) とする3つの閉球を表す.
            
            radius:     閉球の族の半径を表す1次元のNumPy配列.
                            [1., 2., 3.]
                        で半径をそれぞれ 1, 2, 3 とする3つの閉球を表す.
            
            w:          None(初期値)を与えた場合、返す非拡大写像は
                            $T_1(x) = P_1 \cdots P_m(x)$
                        リストを与えた場合は、
                            $T_2(x) = P_1(\sum_{i=2}^mw_iP_i(x))$

                        P2, ..., Pmへ与える距離射影の重みのリスト [w2, ..., wm].
                        また、リスト内の数を全て足すと1になることを要請する.
                            [0.5, 0.5]
                        とすれば、w2 = w3 = 0.5 となる.
    '''
    if centers.shape[0] != raiduses.shape[0]:
        raise Exception()
    if w is not None and len(w) != centers.shape[0] - 1:
        raise Exception()
    
    projections = []
    for c, r in zip(centers, raiduses): 
        p = create_projection(c, r)
        projections.append(p)
    
    def T1(x: np.ndarray) -> np.ndarray:
        _x = x
        for p in projections:
            _x = p(_x)
        return _x
    
    def T2(x: np.ndarray) -> np.ndarray:
        _x = np.zeros_like(x)
        for i, p in enumerate(projections[1:]):
            _x += w[i] * p(x)
        _x = projections[0](_x)
        return _x
    
    if w is None:
        return T1
    else:
        return T2


if __name__ == '__main__':
    # 問題設定
    centers = np.array([[1., 2.], [0., 3.], [-1., 1.], [0., 2.]])
    radiuses = np.array([1.5, 1., 2., 1.])
    x0 = np.array([6., 4.])

    histories = []

    # 非拡大写像の用意
    T1 = create_T(centers, radiuses)
    T2 = create_T(centers, radiuses, [1/3, 1/3, 1/3])

    # アルゴリズムの用意
    km1 = KrasnoselskiiMann(0.5, T1)  # alpha = 0.5 の実験のパターン1
    km2 = KrasnoselskiiMann(0.5, T2)  # alpha = 0.5 の実験のパターン2
    km3 = KrasnoselskiiMann(0.9, T1)  # alpha = 0.9 の実験のパターン3
    km4 = KrasnoselskiiMann(0.9, T2)  # alpha = 0.9 の実験のパターン4
    km_list = [km1, km2, km3, km4]

    for km in km_list:
        history = km.solve(x0, n_iter=30)
        histories.append(history)

    show_result_2D(centers, radiuses, histories)  # 2次元なので視覚化する.
    show_dist(histories) # x_kとT(x_k)の関係をグラフ化する(2次元以上でも可).
