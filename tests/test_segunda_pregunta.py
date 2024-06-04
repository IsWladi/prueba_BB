import pytest
from ..segunda_pregunta import Circulo_social

# test funcion "amigos"
datos_tests_segunda_pregunta_amigos = [([[1,2],[2,3],[1,4]],[1,2], True),
                                       ([[1,2],[2,3],[1,4]],[2,1], True),
                                       ([[1,2],[2,3],[1,4]],[2,4], False),
                                       ([[1,2],[2,3],[1,4],[9,25,12]],[9,12], True),
                                       ([[1,2],[2,3],[1,4],[9,25,12]],[9,12,8], False),
                                       ([[1,2],[2,3],[1,4],[9,25,12,8]],[9,12,8], True),
                                       ]
@pytest.mark.parametrize("relaciones,amigos_validar,respuesta_esperada", datos_tests_segunda_pregunta_amigos)
def test_segunda_pregunta_amigos(relaciones: list, amigos_validar: list, respuesta_esperada: bool):
    circulo_social = Circulo_social(relaciones)
    respuesta = circulo_social.amigos(amigos_validar)
    assert respuesta == respuesta_esperada

datos_tests_segunda_pregunta_amigos_errores = [([[1,2],[2,3],[1,4],[9,25,12,8]], [1,1]),
                                               ([[1,2],[2,3],[1,4],[9,25,12,8]], [2,3,2]),
                                               ]
@pytest.mark.parametrize("relaciones,amigos_validar", datos_tests_segunda_pregunta_amigos_errores)
def test_segunda_pregunta_amigos_errores_id_repetidos(relaciones: list, amigos_validar: list):
    with pytest.raises(Exception) as exc_info:
        circulo_social = Circulo_social(relaciones)
        respuesta = circulo_social.amigos(amigos_validar)
        assert exc_info.type is Exception

# tests funcion "comun"

datos_tests_segunda_pregunta_amigos = [([[1,2],[2,3],[1,4]], 1, 3, True),
                                       ([[1,2],[2,3],[1,4]], 4, 3, False),
                                       ([[1,2],[2,3],[1,4]], 1, 4, False),
                                       ([[1,2],[1,4], [5,3], [2,3]], 1, 3, True)
                                       ]
@pytest.mark.parametrize("relaciones,i,j,respuesta_esperada", datos_tests_segunda_pregunta_amigos)
def test_segunda_pregunta_comun(relaciones: list, i: int, j: int, respuesta_esperada: bool):
    circulo_social = Circulo_social(relaciones)
    respuesta = circulo_social.comun(i, j)
    assert respuesta == respuesta_esperada

def test_segunda_pregunta_comun_error_id_repetido():
    with pytest.raises(Exception) as exc_info:
        relaciones = [[1,2],[2,3],[1,4]]
        circulo_social = Circulo_social(relaciones)
        respuesta = circulo_social.comun(1, 1)
        assert exc_info.type is Exception
