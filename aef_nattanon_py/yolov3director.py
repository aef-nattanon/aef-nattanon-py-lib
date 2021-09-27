from aef_nattanon_py.director import Director
import os


class YoloV3Director(Director):

    def __init__(self):
        path_s = os.path.dirname(__file__)
        super().__init__(
            path_s+'/files/coco.names',
            path_s+'/files/yolov3-tiny.cfg',
            path_s+'/files/yolov3-tiny.weights'
        )
