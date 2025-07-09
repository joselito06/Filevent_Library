from filevent import emitter_event
import os

def test_emitter_creates_file():
    ruta_servidor = os.path.join(os.path.dirname(__file__), 'ruta_servidor')
    path = emitter_event(
        base_path=ruta_servidor,
        type_event="proceso_iniciado",
        detail="Se comenzó el análisis de datos",
        vm_name="VM-002",
        user="Joselito Beriguete"
    )
    assert os.path.exists(path)  # Verifica que el archivo realmente se creó

