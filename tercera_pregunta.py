import re

def palabra_mas_frecuente(texto: str, lista_ignorar: list) -> list:
    """
    Devuelve una lista con la/s palabra/s más frecuente/s del texto dado respetando la lista de palabras a ignorar.

        parametros:
            texto -- texto a analizar.
            lista_ignorar -- lista de palabras a ignorar.

        return:
            list -- retorna una lista con las palabras más frecuentes.
    """
    # texto en lowercase y obtener lista con palabras (sin incluir puntuación, se hace mediante RegEx)
    texto = texto.lower()
    palabras = re.findall(r"\w+", texto)

    # eliminar palabras a ignorar
    palabras = [palabra for palabra in palabras if (palabra not in lista_ignorar)]

    diccionario_frecuencias = {}
    for palabra in palabras:
        # pagina para testear expresiones regulares: https://regex101.com/
        # ([\., ]|^)palabra([\., ]|$)
        patron =  rf"([\., ]|^){palabra}([\., ]|$)"
        frecuencia = len(re.findall(patron, texto))
        diccionario_frecuencias[palabra] = frecuencia

    # buscar palabra con mayor frecuencia
    valor_mas_frecuencia = max(diccionario_frecuencias.values())
    claves_diccionario = diccionario_frecuencias.keys()

    palablas_igual_frecuencia = []
    for clave in claves_diccionario:
        valor = diccionario_frecuencias[clave]
        if valor_mas_frecuencia == valor:
            palablas_igual_frecuencia.append(clave)

    return palablas_igual_frecuencia
