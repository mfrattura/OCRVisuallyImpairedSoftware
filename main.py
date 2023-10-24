import pytesseract
from video.video_player import VideoPlayer
from video.OCR_Processor import OCRProcessor
from video.text_to_speech import TextToSpeech
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\frattm\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


class VideoPlayerApp:
    def __init__(self, video_path):
        self.video_player = VideoPlayer(video_path)
        self.ocr_processor = OCRProcessor()
        self.tts = TextToSpeech()

    def run(self):
        self.video_player.play_video()

        while True:
            frame = self.video_player.capture_frame()
            text = self.ocr_processor.perform_ocr(frame)
            code = self.ocr_processor.identify_code_portions(text)
            formatted_code = self.ocr_processor.format_code(code)
            self.tts.speak_text(formatted_code)

            # Add logic to pause, resume, and exit the program


if __name__ == "__main__":
    video_path = "oop.mp4"  # Replace with the path to your video
    app = VideoPlayerApp(video_path)
    app.run()
