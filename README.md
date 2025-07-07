# fileevent

`fileevent` es una librería ligera para comunicar múltiples aplicaciones o máquinas virtuales usando eventos escritos en archivos JSON. Está diseñada especialmente para entornos con restricciones de red, donde no es posible usar sockets o APIs.

## 📦 Instalación

```bash
pip install -e .
```

## ✨ Características

- Guarda eventos en archivos organizados por VM y usuario.
- Agrega múltiples eventos diarios en un solo archivo.
- Listener en tiempo real usando `watchdog`.
- Reintentos automáticos al detectar cambios.

## 🧰 Estructura de carpetas generada

```
RutaServidor/Evento/
└── VM-01/
    └── User1/
        └── Event-04-07-2025.json
```

## 🚀 Uso

### Emisión de evento
```python
from filevent import emitter_event

emitter_event(
    base_path="C:/RutaServidor/Evento",
    type_event="notificacion",
    detail="El proceso ha terminado",
    vm_name="VM-001",
    user="Tu_usuario"
)
```

### Escucha de eventos
```python
from filevent import start_listening

def handle_events(ruta, events):
    print(f"Archivo modificado: {ruta}")
    for event in events:
        print(f"[{event['timestamp']}] {event['user']} - {event['type_event']}: {event['detail']}")

start_listening("C:/RutaServidor/Evento/VM-01", handle_events, "VM-001")
```

## 📄 Licencia
MIT