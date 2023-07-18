import os
import pickle

import cv2
import zmq
#from deep_sort_realtime.deepsort_tracker import DeepSort


from jetson_inference import detectNet, depthNet
from jetson_utils import videoSource, videoOutput, cudaResize,  cudaToNumpy, cudaDeviceSynchronize, cudaOverlay, cudaConvertColor, cudaAllocMapped

from boxbot.config import VISION_ENDPOINT,CAMERA_URI

from boxbot.vision.depth_utils import depthBuffers



def convert_color(img, output_format):
	converted_img = cudaAllocMapped(width=img.width, height=img.height, format=output_format)
	cudaConvertColor(img, converted_img)
	return converted_img


def crop(img, crop_factor):
	crop_border = ((1.0 - crop_factor[0]) * 0.5 * img.width,
				(1.0 - crop_factor[1]) * 0.5 * img.height)

	crop_roi = (crop_border[0], crop_border[1], img.width - crop_border[0], img.height - crop_border[1])

	crop_img = cudaAllocMapped(width=img.width * crop_factor[0],
							   height=img.height * crop_factor[1],
							   format=img.format)

	cudaCrop(img, crop_img, crop_roi)
	return crop_img


# resize an image
def resize(img, resize_factor):
	resized_img = cudaAllocMapped(width=img.width * resize_factor[0],
								  height=img.height * resize_factor[1],
                                  format=img.format)

	cudaResize(img, resized_img)
	return resized_img



class Vision():
    CAMERA_IMAGE_SIZE = (1024, 768)
    IMAGE_SIZE = (640, 360)

    def __init__(self):
        print("Vision init")

        #self.tracker = DeepSort(max_age=5)


        self.publish_frame = True
        self.publish_detection_bbs = True
        self.publish_detection_frame = True

    def start(self):
        print("Vision start")
 
        try: 
            print(f"Publishing to {VISION_ENDPOINT}")
            self.context = zmq.Context()
            self.vision_socket = self.context.socket(zmq.PUB)
            self.vision_socket.bind(VISION_ENDPOINT)


            self.video_input=videoSource(CAMERA_URI,options={
                        'width': 640,
                        'height': 480,
                        'framerate': 30, 
                    })

            self.video_output_detect=videoOutput("webrtc://@:8554/detect")
            self.video_output_depth=videoOutput("webrtc://@:8554/depth")

            print("Load detection models")
            self.detections = detectNet("ssd-mobilenet-v2")

            print("Load depth models")
            self.depth=net = depthNet("fcn-mobilenet")
            self.buffers=depthBuffers()
            #self.depth_field_numpy=cudaToNumpy(self.depth_field)

        
            while True:
            
                frame = self.video_input.Capture(format="rgb8", timeout=1000)

                if frame is None:
                    print("No camera")
                    continue

                #print(frame) 

                self.buffers.Alloc(frame.shape,frame.format)

                self.depth.Process(frame,self.buffers.depth, "viridis-inverted", "linear")

                #depth=resize(self.depth_field,(640,480))

                #depth_gray=convert_color(self.depth_field, "rgb8")

                cudaOverlay(self.buffers.depth,self.buffers.composite,0,0)

                cudaDeviceSynchronize()
                #print(self.depth_field_numpy[0])


                self.video_output_depth.Render(self.buffers.composite)
                
                detections = self.detections.Detect(frame, overlay="box")

                #for detection in detections:
                #    print(detection)


                self.video_output_detect.Render(frame)

            

                #object_chips = self.chipper(frame, detection_bbs)
                #embeddings = self.embedder(object_chips)
                #vision_message["frame"] = bbs_frame[0]

                # print(detection_bbs)

                # TODO use a better serialization method
                #message_bytes = pickle.dumps(vision_message)

                #self.vision_socket.send(message_bytes)

        finally:
            print("Destroy vision")
            self.context.destroy()

    @staticmethod
    def chipper(frame, bbs):
        """
        Crop frame based on bbox values

        :param frame:
        :param bbs:
        :return:
        """
        chips = []
        for bb in bbs:
            x, y, w, h, p, c = bb
            x = int(x)
            y = int(y)
            w = int(w)
            h = int(h)
            chips.append(frame[y:y + h, x:x + w])
        return chips

    def embedder(self, chips):
        """
        Embeds chips using extractor

        :param chips:
        :return:
        """
        embeddings = []
        for chip in chips:
            embeddings.append(self.extractor.extract(chip))
        return embeddings


def main():
    vision = Vision()
    vision.start()


if __name__ == "__main__":
    main()
