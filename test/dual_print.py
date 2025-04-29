import sys

def tee_print(message, file):
    original_stdout = sys.stdout
    class _DualWriter:
        def __init__(self, *targets): self.targets = targets
        def write(self, msg): [t.write(msg) for t in self.targets if not t.closed]; self.flush()
        def flush(self): [t.flush() for t in self.targets if not t.closed]
    sys.stdout = _DualWriter(original_stdout, file)
    print(message)
    sys.stdout = original_stdout  # restore to avoid flush errors

with open("dual_print.txt", "w") as f:
    tee_print("hello world", f)
    tee_print("hello me", f)

print("LOL, WTF")
tee_print("LMAO", open("dual_print.txt", "a"))