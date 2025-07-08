import json
import os
import getpass
import socket
from datetime import datetime
from .models import Event

# tamo` probando.

def emitter_event(base_path: str, type_event: str, detail: str, vm_name: str = None, user: str = None):
    vm_name = vm_name or socket.gethostname()
    user = user or getpass.getuser()

    now = datetime.now()
    file_date = now.strftime("Evento-%d-%m-%Y.json")
    destination_folder = os.path.join(base_path, vm_name, user)
    os.makedirs(destination_folder, exist_ok=True)

    file_path = os.path.join(destination_folder, file_date)

    event = Event(
        type_event=type_event,
        detail=detail,
        user=user,
        timestamp=now.isoformat()
    )

    data = []
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"[WARN] No se pudo leer el archivo existente: {e}")

    data.append(event.__dict__)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return file_path
