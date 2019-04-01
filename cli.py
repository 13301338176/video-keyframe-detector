import argparse

from keyframeDetector import keyframeDetection

parser = argparse.ArgumentParser()

parser.add_argument('-s','--source', help='source file', required=True)
parser.add_argument('-d', '--dest', help='destination folder', required=True)
parser.add_argument('-t','--Thres', help='Threshold of the image difference', default=0.3)

args = parser.parse_args()

keyframeDetection(args.source, args.dest, float(args.Thres))
