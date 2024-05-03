from src.Device import Device
import shutil
import tempfile


class DeviceBirdRaspberry(Device):
    def get_image(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        shutil.copy2('data/capture_test.jpg', file.name)
        return file

    def get_video(self, duration):
        file = tempfile.NamedTemporaryFile(delete=False)
        shutil.copy2('data/video_test.mp4', file.name)
        return file