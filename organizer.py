import os
import shutil
from datetime import datetime
from logger import Logger
from history import History

class FileOrganizer:
    def __init__(self, target_folder):
        self.target_folder = target_folder
        self.history = History()
        self.logger = Logger("file_mover.log")

    def organize(self):
        if not os.path.isdir(self.target_folder):
            raise NotADirectoryError(f"{self.target_folder} is not a valid folder.")

        moved = []
        for filename in os.listdir(self.target_folder):
            file_path = os.path.join(self.target_folder, filename)
            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1][1:].lower() or "others"
                dest_folder = os.path.join(self.target_folder, ext)

                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)

                dest_path = os.path.join(dest_folder, filename)
                dest_path = self._resolve_conflict(dest_path)

                try:
                    shutil.move(file_path, dest_path)
                    moved.append((file_path, dest_path, datetime.now()))
                    self.logger.log_move(file_path, dest_path)
                except Exception as e:
                    self.logger.log_error(f"Error moving {file_path}: {e}")

        self.history.save(moved)

    def _resolve_conflict(self, path):
        base, ext = os.path.splitext(path)
        counter = 1
        while os.path.exists(path):
            path = f"{base}_{counter}{ext}"
            counter += 1
        return path

    def undo(self):
        last_moved = self.history.load_last()
        for src, dst, _ in reversed(last_moved):
            try:
                shutil.move(dst, src)
                self.logger.log_move(dst, src, undo=True)
            except Exception as e:
                self.logger.log_error(f"Undo error moving {dst} back to {src}: {e}")