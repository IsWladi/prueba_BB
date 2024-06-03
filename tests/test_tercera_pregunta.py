import pytest
from ..tercera_pregunta import palabra_mas_frecuente

datos_tests_tercera_pregunta = [
                                ("Vamos caminando por una villa llena de casas. Una a una visitamos las CASAS que encontramos",
                                 ["una"], ["casas"]),
                                ("Vamos caminando por una villa llena de casas. Una a una visitamos las CASAS que encontramos",
                                 ["casas"], ["una"]),
                                ("Vamos y vamos caminando por una villa llena de casas. Una a una visitamos las CASAS que encontramos",
                                 ["casas", "una"], ["vamos"]),]
@pytest.mark.parametrize("texto,lista_ignorar,respuesta_esperada", datos_tests_tercera_pregunta)
def test_tercera_pregunta(texto: str, lista_ignorar: list, respuesta_esperada: str):
    respuesta = palabra_mas_frecuente(texto, lista_ignorar)
    assert respuesta == respuesta_esperada


datos_no_ideales_tests_tercera_pregunta = [
                                ("terreno casa edificio casa edificio", # palabras con igual frecuencia
                                 ["condominio"], ["casa", "edificio"]),
                                ("terreno casa edificio, casa ", # lista de ignorar vacia
                                 [""], ["casa"])]
@pytest.mark.parametrize("texto,lista_ignorar,respuesta_esperada", datos_no_ideales_tests_tercera_pregunta)
def test_tercera_pregunta_no_ideales(texto: str, lista_ignorar: list, respuesta_esperada: str):
    respuesta = palabra_mas_frecuente(texto, lista_ignorar)
    assert respuesta == respuesta_esperada
