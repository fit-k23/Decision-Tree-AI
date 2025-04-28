import sys

class Tee:
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()

    def flush(self):
        for f in self.files:
            f.flush()

# Usage
with open('logfile.txt', 'w') as log:
    original_stdout = sys.stdout
    sys.stdout = Tee(sys.stdout, log)

    try:
        print("Max Depth: \nActual Depth: \nAccuracy:")
        # ... any other print statements will go to both screen and log ...
    finally:
        sys.stdout = original_stdout  # restore original stdout
