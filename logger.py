from datetime import datetime

class Logger:
    def __init__(self, logfile):
        self.logfile = logfile

    def log_move(self, src, dst, undo=False):
        with open(self.logfile, "a") as f:
            action = "UNDO" if undo else "MOVE"
            f.write(f"{datetime.now()} | {action} | {src} -> {dst}\n")

    def log_error(self, message):
        with open(self.logfile, "a") as f:
            f.write(f"{datetime.now()} | ERROR | {message}\n")