import os
import re


class FileFinder:
    def __init__(self, path, pattern):
        self.path = path
        self.pattern = pattern

    def find_files(self):
        file_list = []
        for root, dirs, files in os.walk(self.path):
            for name in files:
                if re.search(self.pattern, name):
                    file_list.append(os.path.join(root, name))
        return file_list
