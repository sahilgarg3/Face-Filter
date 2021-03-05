import cv2 as cv
import numpy as np
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


def nothing(a):
    pass


cv.namedWindow('BGR')
cv.resizeWindow('BGR', 720, 200)
cv.createTrackbar('Blue', 'BGR', 0, 255, nothing)
cv.createTrackbar('Green', 'BGR', 0, 255, nothing)
cv.createTrackbar('Red', 'BGR', 0, 255, nothing)


def bounding_box(img, points, scale=5, masked=False, cropped=True):
    if masked:
        mask = np.zeros_like(img)
        mask = cv.fillPoly(mask, [points], (255, 255, 255))
        img = cv.bitwise_and(img, mask)
        # cv.imshow('Mask', mask)
    if cropped:
        bbox = cv.boundingRect(points)
        x, y, w, h = bbox
        imgCrop = img[y:y+h, x:x+w]
        imgCrop = cv.resize(imgCrop, (0, 0), None, scale, scale)
        return imgCrop
    return mask


while True:
    image = cv.imread('4.jpg')
    image = cv.resize(image, (720, 580))
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    img_cp = image.copy()

    faces = detector(img_cp)

    for face in faces:
        x1, y1 = face.left(), face.top()
        x2, y2 = face.right(), face.bottom()
        cv.rectangle(img_cp, (x1, y1), (x2, y2), (0, 255, 0), 3)

        landmark = predictor(gray, face)

        all_points = []
        for i in range(68):
            x = landmark.part(i).x
            y = landmark.part(i).y
            all_points.append([x, y])
            cv.circle(img_cp, (x, y), 2, (44, 22, 104), -1)
            cv.putText(img_cp, str(i), (x, y-2), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.4, (0, 0, 0), 1)
            # {'lips': 48 to 60, 'left eye': 36 to 41, 'right eye': 42 to 47, 'nose': 27 to 35,
            # 'left eyebrow':17 to 21, 'right eyebrow':22 to 26}
        try:
            all_points = np.array(all_points)
            lips = bounding_box(image, all_points[48:61], scale=6)
            teeth = bounding_box(image, all_points[60:68], scale=6)
            LeftEyeBrow = bounding_box(image, all_points[17:22])
            RightEyeBrow = bounding_box(image, all_points[22:27])
            Nose = bounding_box(image, all_points[27:36])
            LeftEye = bounding_box(image, all_points[36:42])
            RightEye = bounding_box(image, all_points[42:48])

            maskLips = bounding_box(image, all_points[48:61], masked=True, cropped=False)

            imgColorLips = np.zeros_like(maskLips)

            b = cv.getTrackbarPos('Blue', 'BGR')
            g = cv.getTrackbarPos('Green', 'BGR')
            r = cv.getTrackbarPos('Red', 'BGR')
            imgColorLips[:] = b, g, r

            imgColorLips = cv.bitwise_and(maskLips, imgColorLips)
            imgColorLips = cv.GaussianBlur(imgColorLips, (7, 7), 10)

            imgOriginalGray = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

            # imgColorLips = cv.addWeighted(image, 1, imgColorLips, 0.6, 0)       # Original Image
            imgColorLips = cv.addWeighted(imgOriginalGray, 1, imgColorLips, 0.6, 0)     # For Gray Filter

            # cv.imshow('Original Image', image)
            # cv.imshow('Copy Image', img_cp)
            cv.imshow('BGR', imgColorLips)
        except:
            pass
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
