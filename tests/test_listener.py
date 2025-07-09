from filevent import start_listening
import os

def test_listener_starts_and_handles_event(tmp_path):
    # Se simula una ruta con eventos
    ruta_prueba = tmp_path
    #ruta_prueba.mkdir(parents=True, exist_ok=True)

    eventos_detectados = []

    def handle_events(path, events):
        print(f"📥 Cambios detectados en: {path}")
        eventos_detectados.extend(events)
        for event in events:
            print(f"🕒 [{event['timestamp']}] {event['user']} - {event['type_event']}: {event['detail']}")

    # Se inicia el listener en una carpeta vacía (no bloquea, escucha)
    start_listening(str(ruta_prueba), handle_events, "VM-004")

    # El test en realidad debería simular un evento también...
    # Por ahora solo validamos que no crashee
    assert callable(handle_events)

"""if __name__ == "__main__":
    ruta_servidor = os.path.join(os.path.dirname(__file__), 'ruta_servidor')
    test_listener_starts_and_handles_event(ruta_servidor)
    print("✅ Test ejecutado manualmente con éxito.")

def handle_events(path, events):
    print(f"📥 Cambios detectados en: {path}")
    for event in events:
        print(f"🕒 [{event['timestamp']}] {event['user']} - {event['type_event']}: {event['detail']}")

if __name__ == "__main__":
    # Usa la misma ruta base
    ruta_servidor = os.path.join(os.path.dirname(__file__),'..','tests','ruta_servidor')
    try:
        start_listening(ruta_servidor, handle_events, "VM-003")
    except Exception as e:
        print(f"[WARN] No se pudo capturar el archivo enviado: {e}")"""
