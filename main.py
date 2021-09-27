# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Import Multiplication from your library
import cv2
import aef_nattanon_py as aef

if __name__ == '__main__':
    # YoloV3Detector
    myDetector = aef.Detector(
        'aef_nattanon_py/files/coco.names',
        'aef_nattanon_py/files/yolov3-tiny.cfg',
        'aef_nattanon_py/files/yolov3-tiny.weights'
    )
    myDetector.detect_by_img_path('./my-photo.jpeg')
    cv2.imshow("Image", myDetector.detect_img)
    cv2.waitKey(0)

    # YoloV3Detector
    myDetector = aef.YoloV3Detector()
    myDetector.detect_by_img_path('./my-photo.jpeg')
    cv2.imshow("Image", myDetector.detect_img)
    cv2.waitKey(0)

    # Multiplication
    multiplication = aef.Multiplication(2)
    print(multiplication.multiply(5))
