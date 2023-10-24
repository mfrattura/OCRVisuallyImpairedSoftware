import cv2
from video.OCR_Processor import OCRProcessor


class VideoPlayer:
    def __init__(self, video_path):
        # Initialize video player with video file
        self.video_path = video_path
        self.video_capture = cv2.VideoCapture(self.video_path)
        self.ocr_processor = OCRProcessor()
        self.paused = False  # Add a paused flag
        cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Video', 800, 600)  # Adjust width and height as desired

    def play_video(self):
        # Start playing the video
        while True:
            if not self.paused:  # Check the paused flag
                ret, frame = self.video_capture.read()
                if not ret:
                    # Video has ended
                    break

                # Display the frame
                cv2.imshow('Video', frame)

                # Perform OCR and display text
                ocr_result = self.ocr_processor.perform_ocr(frame)  # Assuming you have a reference to OCRProcessor
                print(ocr_result)  # Print the extracted text

            key = cv2.waitKey(1)
            if key & 0xFF == ord('p'):
                self.toggle_pause()  # Toggle pause when the 'p' key is pressed

            if key & 0xFF == ord('q'):
                break  # Press 'q' to quit

        # Release the video capture object and close the OpenCV window
        self.video_capture.release()
        cv2.destroyAllWindows()

    def toggle_pause(self):
        self.paused = not self.paused

    def capture_frame(self):
        # Capture the current frame
        ret, frame = self.video_capture.read()
        return frame
