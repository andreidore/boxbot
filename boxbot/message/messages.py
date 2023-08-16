"""

Messages utils

"""

import numpy as np

from boxbot.message.image_message_pb2 import ImageMessage  # pylint: disable = no-name-in-module


def get_image_from_message(image_message: ImageMessage) -> np.ndarray:
    """
    Get an image from an image message.

    :param image_message: The image message.
    :return: The image.
    """

    image = np.frombuffer(image_message.image_bytes, dtype=np.uint8).reshape(
        (image_message.height, image_message.width, image_message.channels))

    return image
