from filevent import emitter_event
import os

if __name__ == "__main__":
    ruta_servidor = os.path.join(os.path.dirname(__file__),'..','tests','ruta_servidor')
    try:
        path = emitter_event(
            base_path=ruta_servidor,
            type_event="proceso_iniciado",
            detail="Se comenzó el análisis de datos",
            vm_name="VM-002",
            user="Joselito Beriguete"
        )
        print(f"✅ Evento emitido en: {path}")
    except Exception as e:
        print(f"[WARN] No se pudo emitir el evento existente: {e}")
