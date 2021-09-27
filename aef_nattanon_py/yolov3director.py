from director import Director


class YoloV3Director(Director):

    def __init__(self):
        super().__init__('../files/coco.names', '../files/yolov3-tiny.cfg', '../files/yolov3-tiny.weights')
