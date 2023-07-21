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
VISION_ENDPOINT = "tcp://{}:5004".format(ZMQ_HOST)

VISION_IMAGE_TOPIC = "tcp://{}:5001".format(ZMQ_HOST)

# Board
BOARD_MOTOR_VELOCITY_SERVICE = "tcp://{}:5010".format(ZMQ_HOST)

## camera

CAMERA_URI = "v4l2:///dev/video0"
