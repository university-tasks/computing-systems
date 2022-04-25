from email.mime import image
import math
from typing import Tuple

import numpy as np

from .utils.dist import dist


def scale(image: np.array, scale: int = 2) -> Tuple:
    h = image.shape[0]
    w = image.shape[1]
    m, n = h // scale, w // scale
    X = image.copy().astype(np.int32)
    image_sc = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            image_sc[i, j] = np.sum(
                X[
                    i * scale : min((i + 1) * scale, h),
                    j * scale : min((j + 1) * scale, w),
                ]
            )
    return image_sc, np.asarray(image_sc).reshape(-1)


def dft(img, P=20) -> Tuple:
    C = np.abs(np.fft.fft2(img)[0:P, 0:P])
    zigzag = np.array([C[y + 1 - k, k] for y in range(P) for k in range(y, 0, -1)])
    return C, zigzag


def dct(img, P=20) -> Tuple:
    M, N = img.shape
    X = img.copy().astype(np.int32)
    t = lambda S, i, j: math.sqrt(2 / S) * math.cos(math.pi * (2 * j + 1) * i / (2 * S))
    T_P_M = np.array([[t(M, p, m) if p != 0 else 1 / math.sqrt(M) for m in range(M)] for p in range(P)])
    T_N_P = np.array([[t(N, p, n) if p != 0 else 1 / math.sqrt(N) for p in range(P)] for n in range(N)])
    C = np.dot(np.dot(T_P_M, X), T_N_P)
    zigzag = np.array([C[y + 1 - k, k] for y in range(P) for k in range(y, 0, -1)])
    return C, zigzag


def histogram(img, BIN=16) -> Tuple:
    M, N = img.shape
    top_hist = np.array([np.sum(np.array(img[: M // 2, :] >= b * (256 // BIN)) & np.array(img[: M // 2, :] <= (b + 1) * (256 // BIN) - 1)) for b in range(BIN)])
    bottom_hist = np.array([np.sum(np.array(img[M // 2 :, :] >= b * (256 // BIN)) & np.array(img[M // 2 :, :] <= (b + 1) * (256 // BIN) - 1)) for b in range(BIN)])
    h = np.concatenate((top_hist, bottom_hist)) / (M * N)
    return (np.array(range(2 * BIN)), h), h


def gradient(img: np.array, window_width=16) -> Tuple:
    width, _ = img.shape
    _image = img.copy().astype(np.int32)
    grads = []
    for x in range(window_width, width - window_width):
        top = _image[x - window_width : x, :]
        bottom = np.flip(_image[x : x + window_width, :], axis=0)
        grads.append(dist(top, bottom))
    grads = np.array(grads)
    return (np.array(range(len(grads))), grads), grads


features = {
    "scale": scale,
    "histogram": histogram,
    "gradient": gradient,
    "dft": dft,
    "dct": dct,
}
