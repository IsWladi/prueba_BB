import pytest
from ..primera_pregunta import Robot

datos_tests_primera_pregunta = [("IIIIDDDD", True), ("IDID", True), ("", True), ("DDD", False), ("IIID", False), ("DIDII", False)]
@pytest.mark.parametrize("movimientos,respuesta_esperada", datos_tests_primera_pregunta)
def test_primera_pregunta(movimientos: str, respuesta_esperada: bool):
    # instanciar objeto de Robot
    robot = Robot()
    respuesta = robot.vuelve(movimientos) # Por ejemplo: "IIIIDDDD"
    assert respuesta == respuesta_esperada


datos_invalidos_tests_primera_pregunta = [("string invalido"), ("IDTNDDDDD"), (5), (True)]
@pytest.mark.parametrize("movimientos", datos_invalidos_tests_primera_pregunta)
def test_primera_pregunta_valida_errores(movimientos):
    with pytest.raises(AssertionError) as exc_info:
        robot = Robot()
        robot.vuelve(movimientos) # Por ejemplo: "IIIIDDDD"
        assert exc_info.type is AssertionError
