# aef-nattanon-py-lib
## Install

```bash
$ pip install aef-nattanon-py
```

## Simple Demo

```python
# Import aef_nattanon_py from your library
import aef_nattanon_py as aef
import cv2

# Multiplication
multiplication = aef.Multiplication(2)
print(multiplication.multiply(5)) # 10

# direct_by_img_path
myDirector = aef.Director('coco.names', 'yolov3-tiny.cfg', 'yolov3-tiny.weights')
myDirector.direct_by_img_path('my-photo.jpeg')
cv2.imshow("Image", myDirector.director_img)
cv2.waitKey(100)

# direct_by_frame
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    myDirector.direct_by_frame(frame)
    cv2.imshow("Image", myDirector.director_img)
    cv2.waitKey(1)

cv2.destroyAllWindows()

```