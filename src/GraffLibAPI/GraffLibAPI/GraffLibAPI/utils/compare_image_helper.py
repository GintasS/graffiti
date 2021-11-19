from cv2 import cv2
import time
start_time = time.time()

def compare(image1,image2):

    #Image imports
    img1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE)     #QueryImage
    img2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE)     #ChallengeImage

    #Features
    sift = cv2.SIFT_create()

    #Find the keypoints and descriptors with SIFT
    kp1, desc1 = sift.detectAndCompute(img1, None)
    kp2, desc2 = sift.detectAndCompute(img2, None)

    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(desc1, desc2, k=2)

    # Apply ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.55 * n.distance:
            good.append([m])

    #The main similarity status check, where len(good) defines matches
    if len(good) >= 70:
        status = True
    else:
        status = False

    return status

    ### TESTING ###
'''
    # cv.drawMatchesKnn expects list of lists as matches.
    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # Show the image
    cv2.imshow('Matched Features', img3)
    cv2.waitKey(0)
    cv2.destroyWindow('Matched Features')
'''
st = compare("/Users/user/Desktop/Sample1.jpg","/Users/user/Desktop/Sample2.jpg")
print(st)

print("--- %0.6s seconds ---" % (time.time() - start_time))