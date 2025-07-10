# filevent

`filevent` es una librería ligera para comunicar múltiples aplicaciones o máquinas virtuales mediante eventos escritos en archivos `.json`. Está diseñada para entornos con **restricciones de red o permisos**, donde no es posible usar sockets, APIs o conexiones entre servicios.

Ideal para:
- Máquinas virtuales aisladas
- Aplicaciones que comparten solo carpetas
- Comunicación de procesos sin red

---

## 📦 Instalación

```bash
pip install -e .
```

## ✨ Características

- Guarda eventos estructurados en archivos .json.
- Soporta múltiples máquinas virtuales (vm_name) a la vez.
- Organiza eventos por máquina virtual, usuario, y fecha.
- Acumula múltiples eventos diarios en un solo archivo.
- Usa watchdog para escuchar en tiempo real los cambios.
- Marca los eventos como leídos automáticamente.
- Puede procesar eventos pendientes (read: false) al iniciar.
- Compatible con pytest para pruebas automatizadas.

## 🧰 Estructura de carpetas generada

```
RutaServidor/
└── VM-01/
    └── User1/
        └── Event-04-07-2025.json
```

## 🚀 Uso

### Emisión de evento
```python
from filevent import emitter_event

emitter_event(
    base_path="C:/RutaServidor",
    type_event="notificacion",
    detail="El proceso ha terminado",
    vm_name=["VM-001","VM-002","VM-003"],
    user="Tu_usuario",
    source_id="btn-inicio",
    target_element="ServicioAnalisis"
)
```

Esto genera (o actualiza) un archivo .json con el siguiente formato:

```json
[
  {
    "timestamp": "2025-07-09T23:55:03",
    "type_event": "proceso_iniciado",
    "detail": "Se comenzó el análisis de datos",
    "user": "Joselito Beriguete",
    "source_id": "btn-inicio",
    "target_element": "ServicioAnalisis",
    "read": false
  }
]
```

### Escucha de eventos (listener)
```python
from filevent import start_listening

def handle_events(ruta, events):
    print(f"Archivo modificado: {ruta}")
    for event in events:
        print(f"[{event['timestamp']}] {event['user']} - {event['type_event']}: {event['detail']}")

start_listening(
  path="C:/RutaServidor/VM-01", 
  on_events=handle_events, 
  vm_name="VM-001",
  process_unread_on_start=True  # Procesa eventos pendientes al iniciar
  )
```
🔁 Solo los eventos marcados como "read": false serán procesados.
Una vez leídos, se marcan como "read": true.

🔁 Cuando process_unread_on_start=True, el listener leerá eventos read=false antes de empezar a escuchar nuevos cambios.

✅ Pruebas locales

Puedes crear pruebas dentro de tests/:

```python
from filevent import emitter_event
import os

def test_emitter_creates_file():
    base = os.path.join(os.path.dirname(__file__), "ruta_servidor")
    result = emitter_event(
        base_path=base,
        type_event="proceso_iniciado",
        detail="Test event",
        vm_name="VM-Test",
        user="TestUser",
        source_id="btn-test",
        target_element="ServiceTest"
    )
    assert os.path.exists(result[0])
```

## 📄 Licencia
MIT