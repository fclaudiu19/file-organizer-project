import pickle
import os

class History:
    def __init__(self, file="history.pkl"):
        self.file = file

    def save(self, moves):
        history = self._load_all()
        history.append(moves)
        with open(self.file, "wb") as f:
            pickle.dump(history, f)

    def load_last(self):
        history = self._load_all()
        if history:
            last = history.pop()
            with open(self.file, "wb") as f:
                pickle.dump(history, f)
            return last
        return []

    def _load_all(self):
        if os.path.exists(self.file):
            with open(self.file, "rb") as f:
                return pickle.load(f)
        return []