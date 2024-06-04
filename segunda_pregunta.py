class Circulo_social():
    def __init__(self, relaciones_personas: list):
        self.relaciones_personas = relaciones_personas

    def amigos(self, lista_personas) -> bool:
        """
        Valida si la lista de personas son amigos.

            parametros:
                lista_personas -- lista de personal a validar representados con numeros, ejemplo; [1,2] o [1,3,6]

            return:
                True -- si son amigos
                False -- si no son amigos

            errores:
                Exception -- no se permiten personas duplicadas, por ejemplo; [1, 1] o [2, 3, 2] son invalidos.
        """
        cantidad_amigos = len(lista_personas)
        validar_amigos = set(lista_personas)
        if cantidad_amigos != len(validar_amigos):
            raise Exception("Error: no se permiten identificadores duplicados")
        existe = any([(validar_amigos == set(relacion)) or (validar_amigos.issubset(set(relacion))) for relacion in self.relaciones_personas])
        if existe:
            return True
        return False

    def obtener_amigos(self, id: int) -> list:
        """
        Obtiene los amigos que tiene la persona

            parametros:
                persona_id -- numero que representa a la persona

            return:
                list -- retorna una lista de listas con sus amigos y relaciones.
        """
        amigos_de_persona_id = []
        for amigos in self.relaciones_personas:
            if id in amigos:
                amigos.remove(id)
                amigos_de_persona_id.append(amigos)
        return amigos_de_persona_id



    def comun(self, i: int, j: int) -> bool:
        # validar errores
        if i == j:
            raise Exception("Error: 'i' y 'j' no pueden ser iguales")
        # obtener amigos y relaciones de i y j
        amigos_i = self.obtener_amigos(i)
        amigos_j = self.obtener_amigos(j)

        # buscar amigos comunes
        tienen_amigos_comun = False

        for amigos in  amigos_i:
            for amigo in amigos:
                for relaciones_j in amigos_j:
                    if amigo in relaciones_j:
                        return True # si tienen al menos un amigo en comun retornar True

        return False

