import os


class FileManager:
    def __init__(self, base_path="app/temp"):
        self.base_path = base_path

    def save(self, file, name):
        path = os.path.join(self.base_path, name)

        with open(path, "wb") as f:
            f.write(file)
            f.close()
            return path

    @staticmethod
    def remove(path):
        if os.path.exists(path):
            os.remove(path)
