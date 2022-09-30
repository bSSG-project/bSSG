from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

class Singleton:
    last_event_time = time.time()

class WatcherEventHandler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return
        
        if time.time() - Singleton.last_event_time <= 1:
            return
        Singleton.last_event_time = time.time()

        print("Change detected, regenerating!")
        os.system("bssg-generate")
        print("Regeneration finished.")


def main():
    print("Now watching content/ and templates/ for changes...")
    print("When a change is detected, bssg-generate will be executed.")

    path_content = "./content"
    path_templates = "./templates"

    observer = Observer()
    handler = WatcherEventHandler()

    observer.schedule(handler, path_content, recursive=True)
    observer.schedule(handler, path_templates, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()


if __name__ == "__main__":
    main()