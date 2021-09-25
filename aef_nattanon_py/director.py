import cv2
import numpy as np


class Director:

    def __init__(self, classes_file='', model_configuration='', model_weights=''):
        self.director_img = ''
        self.class_ids = []
        self.classes = []
        self.labels = []
        self.boxes = []
        self.modelConfiguration = model_configuration
        self.modelWeights = model_weights

        self.set_classes(classes_file)

    def set_classes(self, classes_file=''):
        with open(classes_file, "r") as f:
            self.classes = [line.strip() for line in f.readlines()]

    def direct_by_img_path(self, photo):
        self.direct_by_frame(cv2.imread(photo))

    def direct_by_frame(self, frame):
        # Load Yolo
        net = cv2.dnn.readNet(self.modelWeights, self.modelConfiguration)

        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(self.classes), 3))
        # Loading image
        height, width, channels = frame.shape
        # Detecting objects
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)
        # Showing informations on the screen
        self.class_ids = []
        confidences = []
        self.boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    self.boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    self.class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(self.boxes, confidences, 0.5, 0.4)

        font = cv2.FONT_HERSHEY_SIMPLEX
        self.labels = []
        for i in range(len(self.boxes)):
            if i in indexes:
                x, y, w, h = self.boxes[i]
                self.labels.append(str(self.classes[self.class_ids[i]]))
                color = colors[i]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 3)
                cv2.putText(frame, self.labels[i], (x, y-20), font, 2, color, 3)
        self.director_img = frame
        return self.director_img, self.labels, self.classes, self.class_ids, self.boxes
