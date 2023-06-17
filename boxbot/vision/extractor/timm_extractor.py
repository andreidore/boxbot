import timm

from boxbot.vision.extractor.extractor import Extractor


class TimmExtractor(Extractor):

    def __init__(self):
        super().__init__()
        print("Timm extractor init")

        self.model = timm.create_model('mobilenetv2_100', pretrained=True, num_classes=0)

    def extract(self, image):
        """
        Extracts features from an image.

        Args:
            image (np.ndarray): The image to extract features from.

        Returns:
        """

        return []
