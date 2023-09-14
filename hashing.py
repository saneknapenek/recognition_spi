from pprint import pprint
import cv2
import numpy as np

from env import PATH1, PATH2



def pHash(file_path: str) -> np.ndarray:
    image = cv2.imread(file_path)
    resized = cv2.resize(image, (32,32), interpolation = cv2.INTER_AREA)
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    dct_conversion = cv2.dct(np.float32(gray_image))[:8, :8]
    mean_value = np.mean(dct_conversion[1:, 1:])
    thresholded_coefficients = np.where(dct_conversion > mean_value, 1, 0)
    return thresholded_coefficients

# def save(image):
#     for i in range(8):
#         for j in range(8):
#             if image[i][j] == 1:
#                 image[i][j] = 255
#             else:
#                 image[i][j] = -255
#     cv2.imwrite(OUTPUT_PATH, image)

def hamming_dist(hash1: np.ndarray, hash2: np.ndarray) -> int:
    sum = np.sum(hash1 != hash2)
    return sum

print(hamming_dist(
    hash1=pHash(PATH1),
    hash2=pHash(PATH2)
))
