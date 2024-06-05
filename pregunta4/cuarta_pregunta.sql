-- RESPUESTA A LA PREGUNTA 4
SELECT ev.nombre AS nombre_evento,
       COALESCE(SUM(en.costo), 0) AS recaudacion
FROM evento AS ev
LEFT JOIN entradas AS en ON ev.id = en.id_evento
GROUP BY ev.nombre
ORDER BY COALESCE(SUM(en.costo), 0) DESC;
