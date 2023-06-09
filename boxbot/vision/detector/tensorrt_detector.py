from boxbot.vision.detector.detector import Detector


class TensorRTDetector(Detector):
    def __init__(self):
        super().__init__()
        print("TensorRT detector init")

    def detect(self, image):
        """
        Detects objects in an image.

        Args:
            image (np.ndarray): The image to detect objects in.

        Returns:
            List[Object]: The objects detected in the image.
        """
        return []
