from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
from shutil import which
import os

class Singleton:
    last_event_time = time.time()
    bssg_generate_cmd = "bssg-generate"

class WatcherEventHandler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return
        
        if time.time() - Singleton.last_event_time <= 1:
            return
        Singleton.last_event_time = time.time()

        print("Change detected, regenerating!")
        generate = subprocess.run(Singleton.bssg_generate_cmd, capture_output=True)
        if generate.returncode != 0:
            print("An error occured while the site was regenerating. The error was:")
            print(bytes.decode(generate.stderr))
        else:
            print("The site was regenerated successfully.")


def main():
    if not which("bssg-generate"):
        print("Couldn't find bssg-generate, attempting to find bssggenerate.py...")
        print("This usually means your installation is broken.")
        if os.path.exists("bssggenerate.py"):
            print("Found bssggenerate.py, using it!")
            Singleton.bssg_generate_cmd = "python bssggenerate.py"
        else:
            print("Couldn't find bssggenerate.py! Re-installing bSSG may fix this issue.")
            exit(1)

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