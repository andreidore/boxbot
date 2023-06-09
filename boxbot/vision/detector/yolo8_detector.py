from ultralytics import YOLO

from boxbot.vision.detector.detector import Detector


class YOLO8Detector(Detector):
    def __init__(self):
        super().__init__()
        print("Yolo8 detector init")
        self.model = YOLO("yolov8s.pt")

    def detect(self, image):
        """
        Detects objects in an image.

        Args:
            image (np.ndarray): The image to detect objects in.

        Returns:
            List[Object]: The objects detected in the image.
        """

        results = self.model.predict(source=image, save=False, save_txt=False,
                                     verbose=False)  # save predictions as labels

        if len(results) == 0:
            return {}

        result = results[0]
        detection_frame = result.plot()

        bbs = []

        for i, box in enumerate(result.boxes):

            # detect only persons
            if box.cls != 0:
                continue

            bbs.append(box.data[0])
            # print(box.data)

        detector_result = {"detection_frame": detection_frame,
                           "bbs": bbs}

        # print(boxes)

        # print(results)

        return detector_result
