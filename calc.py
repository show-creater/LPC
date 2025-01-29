import numpy as np
from scipy.linalg import solve_toeplitz

def compute_lpc(signal, p):
    """
    自己相関法を用いたLPC係数の計算
    :param signal: 入力信号
    :param p: LPCの次数
    :return: LPC係数
    """
    # 自己相関 r の計算
    r = np.correlate(signal, signal, mode='full')
    r = r[len(signal)-1:len(signal)+p]

    # ヤング・ウォーカー方程式を解く
    a = solve_toeplitz((r[:-1], r[:-1]), -r[1:])
    return np.concatenate(([1], a))
