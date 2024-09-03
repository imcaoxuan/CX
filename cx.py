import argparse

import cv2
import numpy as np

parser = argparse.ArgumentParser(
    prog='CX',
    description='My avatar.',
    epilog='help')
parser.add_argument('-n', type=int, default=512, help='length')
parser.add_argument('-opacity', type=int, metavar='[0-255]', default=255, help='opacity')
args = parser.parse_args()
n = args.n
opacity = args.opacity
array = np.ones((n, n, 4), np.uint8)
array *= opacity
thickness = max(1, n // 128)
cv2.ellipse(array, (n // 2, n // 2), (n // 2, n // 2), 0, 90, 270, (0, 0, 0), thickness)
cv2.line(array, (n, 0), (n // 2, n), (0, 0, 0), thickness)
cv2.line(array, (n // 2, 0), (n, n), (0, 0, 0), thickness)
cv2.imwrite(f'CX{n}.png', array)
cv2.imshow(f'CX{n}.png', array)
cv2.waitKey(0)
