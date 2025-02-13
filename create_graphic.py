import cv2
from argparse import ArgumentParser
import os

MM = 0.5

parser = ArgumentParser()

parser.add_argument('-l', type=str, required=True, help='path to graphic')
parser.add_argument('-f', type=str, required=False, default=None, help='final size (mm) in format y,x, i.e. 5,4 for 5mm tall by 4mm wide')
parser.add_argument('-s', type=str, required=False, default=None, help='path to save location')

args = parser.parse_args()

graphic = cv2.imread(args.l)

if args.f is not None:
    y, x = args.f.split(',')
    graphic = cv2.resize(graphic, (y * MM, x * MM))

dest = args.s if args.s is not None else str(os.path.dirname(args.l)) + os.sep + 'graphic-' + str(os.path.split(args.l)[1])

cv2.imwrite(dest, graphic)
