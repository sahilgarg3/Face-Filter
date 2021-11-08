## Face-Filter
###  Shape Predictor 68 Face Landmarks [Download Here](https://github.com/tzutalin/dlib-android/blob/master/data/shape_predictor_68_face_landmarks.dat)

Facial landmarks are used to localize and represent salient regions of the face, such as:
- Eyes (both left and right)
- Eyebrows (both left and right)
- Nose
- Mouth
- Jawline

Facial landmarks have been successfully applied to face alignment, head pose estimation, face swapping, locate facial parts,blink detection and much more.

Detecting facial landmarks is a subset of the shape prediction problem. Given an input image, a shape predictor attempts to localize key points of interest along the shape.
In the context of facial landmarks, our goal is detect important facial structures on the face using shape prediction methods.

Detecting facial landmarks is therefore a two step process:
- Step 1: Localize the face in the image.
- Step 2: Detect the key facial structures on the face

---

[**`Trackbars`**](https://blog.electroica.com/trackbar-in-opencv-python/) in OpenCV are helpful to tweak a variable value instantly without closing and relaunching the program.

To create a trackbar in OpenCV the OpenCV library provides `cv2.createTrackbar()` function, to read the current poisition of the trackbar slider you can use `cv2.getTrackbarPos()` function to change the position of trackbar use `cv2.setTrackbarPos()`.

`cv2.createTrackbar()` arguments
- Trackbar name
- Window name
- Default slider value
- Maximum value
- Callback function


`cv2.getTrackbarPos()` arguments
- Trackbar name
- Window name


`cv2.setTrackbarPos()` arguments
- Trackbar name
- Window name
- New Value
---

### Requirements
- OpenCV
- NumPy
- Dlib
- shape_predictor_68_face_landmarks.dat
---

We will use the [`dlib.get_frontal_face_detector()`](http://dlib.net/python/index.html#dlib.get_frontal_face_detector) function from the dlib module which we can use to detect faces

AND 
[`dlib.shape_predictor()`](http://dlib.net/python/index.html#dlib.shape_predictor) taken an image of a human face as input and are expected to identify the locations of important facial landmarks such as the corners of the mouth and eyes, tip of the nose, and so forth.

---
By using these we can find the location of the different facial parts and then using the trackbars to initialize the color or filtered color we would like to apply on our desired image. 

***Here,*** in this module I've filtered the lips of the person in the image, which one can change this to color any other part of the body too.
```
maskLips = bounding_box(image, all_points[48:61], masked=True, cropped=False)
```
Just, you need to get the **masked** image(Mask allows us to focus only on the portions of the image that interests us) of that particular part by giving the right landmarks. 

---

```
imgColorLips = cv.addWeighted(image, 1, imgColorLips, 0.6, 0)
# imgColorLips = cv.addWeighted(imgOriginalGray, 1, imgColorLips, 0.6, 0)
```
### Output:
![plot](https://github.com/sahilgarg3/Face-Filter/blob/main/Pictures/Face%20Filters%202.png)
---
```
# imgColorLips = cv.addWeighted(image, 1, imgColorLips, 0.6, 0)
imgColorLips = cv.addWeighted(imgOriginalGray, 1, imgColorLips, 0.6, 0)
```
### Output:
![plot](https://github.com/sahilgarg3/Face-Filter/blob/main/Pictures/Face%20Filters%201.png)
