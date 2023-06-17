from boxbot.vision.extractor.extractor import Extractor


class TensorRTExtractor(Extractor):

    def __init__(self):
        super().__init__()
        print("TensorRT extractor init")

    def extract(self, image):
        """
        Extracts features from an image.

        Args:
            image (np.ndarray): The image to extract features from.

        Returns:
            List[Object]: The objects detected in the image.
        """

        return []
