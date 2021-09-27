from aef_nattanon_py.detector import Detector
import os


class YoloV3Detector(Detector):

    def __init__(self):
        path_s = os.path.dirname(__file__)
        super().__init__(
            path_s+'/files/coco.names',
            path_s+'/files/yolov3-tiny.cfg',
            path_s+'/files/yolov3-tiny.weights'
        )
