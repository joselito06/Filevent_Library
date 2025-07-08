from filevent import emitter_event

if __name__ == "__main__":
    try:
        path = emitter_event(
            base_path="C:\\Users\\Admin\\Desktop\\Proyectos\\Proyectos Python\\PruebaEventos",
            type_event="proceso_iniciado",
            detail="Se comenzó el análisis de datos",
            vm_name="VM-002",
            user="Joselito Beriguete"
        )
        print(f"✅ Evento emitido en: {path}")
    except Exception as e:
        print(f"[WARN] No se pudo emitir el evento existente: {e}")
