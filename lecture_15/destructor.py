class FileHandler:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = open(filename, mode)


    def read_data(self):
        return self.file.read()

    def __del__(self):
        self.file.close()
        print(f"File {self.filename} has been closed")


file_handler = FileHandler('example.txt')
data = file_handler.read_data()
print(data)
del file_handler

