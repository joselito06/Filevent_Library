from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from filevent.models import Event
import json, time, os, socket, threading

class EventHandler(FileSystemEventHandler):
    def __init__(self, on_events):
        self.on_events = on_events
        self.last_state = {}

    def on_modified(self, event):
        if event.is_directory or not event.src_path.endswith(".json"):
            return

        try:
            stat = os.stat(event.src_path)
            mod_time = stat.st_mtime
            if self.last_state.get(event.src_path) == mod_time:
                return
            self.last_state[event.src_path] = mod_time

            with open(event.src_path, "r", encoding="utf-8") as f:
                events = [Event.from_dict(e) for e in json.load(f)]

            unread_events = [e for e in events if not e.read]

            if unread_events:
                self.on_events(event.src_path, [e.to_dict() for e in unread_events])

                # Mark as read
                for e in events:
                    if not e.read:
                        e.read = True

                with open(event.src_path, "w", encoding="utf-8") as f:
                    json.dump([e.to_dict() for e in events], f, indent=4, ensure_ascii=False)

        except Exception as e:
            print(f"[ERROR] Procesando {event.src_path}: {e}")


def start_listening(path: str, on_events, vm_name: str = None, timeout: int = None):
    vm_name = vm_name or socket.gethostname()
    path_vm = os.path.join(path, vm_name)

    os.makedirs(path_vm, exist_ok=True)
    event_handler = EventHandler(on_events)

    observer = Observer()
    observer.schedule(event_handler, path_vm, recursive=True)
    observer.start()
    print(f"[LISTENER] Escuchando en: {path_vm}")

    if timeout is None:
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    else:
        def stop_observer():
            observer.stop()

        timer = threading.Timer(timeout, stop_observer)
        timer.start()

        observer.join()
        timer.cancel()