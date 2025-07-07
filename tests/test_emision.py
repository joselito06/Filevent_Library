from filevent import emitter_event

if __name__ == "__main__":
    path = emitter_event(
        base_path="C:\\Users\\Admin\\Desktop\\Proyectos\\Proyectos Python\\PruebaEventos",
        type_event="proceso_iniciado",
        detail="Se comenzó el análisis de datos",
        vm_name="VM-002",
        user="Joselito Beriguete"
    )
    print(f"✅ Evento emitido en: {path}")