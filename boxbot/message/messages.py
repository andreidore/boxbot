"""

Messages utils

"""

import numpy as np

from boxbot.message.image_message_pb2 import ImageMessage  # pylint: disable = no-name-in-module


def decode_image(message: bytes):
    """
        Decode an image message.
    """

    image_message = ImageMessage()
    image_message.ParseFromString(message)

    frame = np.frombuffer(image_message.image_bytes,  # pylint disable = c-extension-no-member
                          dtype=np.uint8)
    frame = frame.reshape(image_message.height, image_message.width, image_message.channels)

    return frame


def encode_image(image: np.ndarray):
    """
    Encode an image message.

    :param image:
    :return:
    """

    image_message = ImageMessage()
    image_message.image_bytes = image.tobytes()
    image_message.width = image.shape[1]
    image_message.height = image.shape[0]
    image_message.channels = image.shape[2]

    return image_message.SerializeToString()
