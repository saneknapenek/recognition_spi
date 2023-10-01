import cv2
from cv2.typing import MatLike
import numpy as np



def pHash(frame: MatLike) -> np.ndarray:
    resized = cv2.resize(frame, (32,32), interpolation = cv2.INTER_AREA)
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    dct_conversion = cv2.dct(np.float32(gray_image))[:8, :8]
    mean_value = np.mean(dct_conversion[1:, 1:])
    thresholded_coefficients = np.where(dct_conversion > mean_value, 1, 0)
    return thresholded_coefficients

def hamming_dist(hash1: np.ndarray, hash2: np.ndarray) -> int:
    return np.sum(hash1 != hash2)
