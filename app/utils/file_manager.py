import os


class FileManager:
    @staticmethod
    def save(file, name):
        path = os.path.join('app/tmp', name)

        with open(path, 'wb') as f:
            f.write(file)
            f.close()
            return path

    @staticmethod
    def remove(path):
        if os.path.exists(path):
            os.remove(path)
