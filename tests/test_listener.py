from filevent import start_listening

def handle_events(path, events):
    print(f"📥 Cambios detectados en: {path}")
    for event in events:
        print(f"🕒 [{event['timestamp']}] {event['user']} - {event['type_event']}: {event['detail']}")

if __name__ == "__main__":
    # Usa la misma ruta base
    try:
        start_listening("C:\\Users\\Admin\\Desktop\\Proyectos\\Proyectos Python\\PruebaEventos", handle_events, "VM-003")
    except Exception as e:
        print(f"[WARN] No se pudo capturar el archivo enviado: {e}")
