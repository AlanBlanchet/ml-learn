import importlib
import os
import time
import traceback
from multiprocessing import Process

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class Reloader:
    def __init__(self, module) -> None:
        self.moduleName = module
        self.reloadCount = 0
        self.imported = None
        self.process = None

        class Handler(FileSystemEventHandler):
            def on_modified(_, event):
                s = event.src_path.split(".")
                if (
                    not event.is_directory
                    and "__pycache__" not in event.src_path
                    and s[-1] == "py"
                ):
                    self.restart(event)

        event_handler = Handler()
        observer = Observer()
        observer.schedule(event_handler, path="./", recursive=True)
        observer.start()
        self.restart()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
        pass

    def restart(self, event=None):
        os.system("clear")
        if event:
            print(
                f"\33[42m\33[37m[{self.reloadCount}] {event.event_type}: {event.src_path}\33[0m\n\n"
            )
        self.reloadCount += 1
        try:
            if self.process != None:
                self.process.terminate()
            self.process = Process(
                target=lambda: importlib.import_module(self.moduleName)
            )
            self.process.start()
        except Exception:
            print(f"\33[91m{traceback.format_exc()}\33[0m")

