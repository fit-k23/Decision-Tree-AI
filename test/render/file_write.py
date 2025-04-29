import sys

class DualWriter:
    def __init__(self, *writers):
        self.writers = writers

    def write(self, message):
        for writer in self.writers:
            try:
                writer.write(message)
                writer.flush()
            except Exception:
                pass  # skip closed writers

    def flush(self):
        for writer in self.writers:
            try:
                writer.flush()
            except Exception:
                pass

original_stdout = sys.stdout

with open("output.txt", "w") as f:
    dual = DualWriter(original_stdout, f)
    sys.stdout = dual

    sys.stdout.write("This goes to console and file automatically.\n")
    sys.stdout.write("This goes to console and file sa.\n")

sys.stdout = original_stdout  # Always restore
