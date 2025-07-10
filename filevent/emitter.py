import json
import os
import getpass
import socket
from datetime import datetime
from .models import Event

# tamo` probando.

def emitter_event(base_path: str, type_event: str, detail: str, vm_names, user: str, source_id: str, target_element: str):
    #Validate if vm_name is a list
    if isinstance(vm_names, str):
        vm_names = [vm_names]

    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    event_data = {
        "timestamp": timestamp,
        "type_event": type_event,
        "detail": detail,
        "user": user,
        "source_id": source_id,
        "target_element": target_element,
        "read": False
    }

    paths = []
    for vm in vm_names:
        event_dir = os.path.join(base_path, vm, user)
        os.makedirs(event_dir, exist_ok=True)

        file_date = datetime.now().strftime("Evento-%d-%m-%Y.json")
        file_path = os.path.join(event_dir, file_date)

        events = []
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    events = json.load(f)

                for ev in events:
                    if(
                        ev["type_event"] == event_data["type_event"] and
                        ev["user"] == event_data["user"] and
                        ev["source_id"] == event_data["source_id"] and
                        ev["target_element"] == event_data["target_element"] and
                        not ev["read"]
                    ):
                        print("[INFO] Evento ya existe y no ha sido leído. No se volverá a agregar.")
                        return paths  # Salimos sin agregar el evento
                    
            except Exception as e:
                print(f"[WARN] No se pudo leer {file_path}: {e}")

        events.append(event_data)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(events, f, indent=4, ensure_ascii=False)

        paths.append(file_path)

    return paths  # Devuelve lista de rutas creadas

    """now = datetime.now()
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

    return file_path"""
