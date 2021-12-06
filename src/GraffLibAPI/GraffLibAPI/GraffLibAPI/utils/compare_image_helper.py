from cv2 import cv2
import logging
logger = logging.getLogger()

# TODO: OpenCV SIFT is very slow now. We need to optimize performance, either by using another algorithm, using cache or by other means.
def compare_two_images(image_to_compare_file, image_to_compare_against_file):
    # Image imports
    # Features
    good = [1]

    # The main similarity status check, where len(good) defines matches
    return len(good)