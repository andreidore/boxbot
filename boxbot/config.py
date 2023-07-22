"""

Configuration file for boxbot

"""

__VERSION__ = "0.1.0"

ZMQ_HOST = "127.0.0.1"

# Services
COMMAND_ZMQ_PORT = "5003"

# Publishers
BOARD_ZMQ_PORT = "5001"

VISION_ZMQ_PORT = "5004"

# Subscribers
NAVIGATION_ZMQ_PORT = "5002"

# vision
VISION_ENDPOINT = f"tcp://{ZMQ_HOST}:5004"

VISION_IMAGE_TOPIC = f"tcp://{ZMQ_HOST}:5001"

# Board
BOARD_MOTOR_VELOCITY_SERVICE = f"tcp://{ZMQ_HOST}:5010"

# camera

CAMERA_URI = "v4l2:///dev/video0"
