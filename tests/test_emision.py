from filevent import emitter_event
import os

def test_emitter_creates_file():
    ruta_servidor = os.path.join(os.path.dirname(__file__), 'ruta_servidor')
    paths = emitter_event(
        base_path=ruta_servidor,
        type_event="proceso_cerrado",
        detail="Se comenzó el análisis de datos",
        vm_names=["VM-004"],
        source_id="btnClose",
        target_element="end_event",
        user="Joselito Beriguete"
    )
    for path in paths:
        assert os.path.exists(path), f"No se encontró el archivo: {path}"  # Verifica que el archivo realmente se creó

if __name__ == "__main__":
    test_emitter_creates_file()
    print("✅ Test ejecutado manualmente con éxito.")