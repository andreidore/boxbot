from ultralytics import YOLO

from boxbot.vision.detector.detector import Detector


class YOLO8Detector(Detector):
    def __init__(self):
        super().__init__()
        print("Dev detector init")
        self.model = YOLO("yolov8s.pt")

    def detect(self, image):
        """
        Detects objects in an image.

        Args:
            image (np.ndarray): The image to detect objects in.

        Returns:
            List[Object]: The objects detected in the image.
        """

        results = self.model.predict(source=image, save=False, save_txt=False,verbose=False)  # save predictions as labels

        #print(results)

        return []
