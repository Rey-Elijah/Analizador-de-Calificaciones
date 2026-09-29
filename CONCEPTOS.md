# Analizador funcional de calificaciones — Conceptos de la Unidad 2

**Problema:** cargar las calificaciones de un grupo (CSV) y analizarlas: promedios, aprobados (regla TecNM: todas las unidades ≥ 70), filtros, orden, búsqueda por rango de promedio e histograma.

**Idea central:** *núcleo funcional, cáscara imperativa*. Toda la lógica son funciones puras sin Qt (`model`, `analysis`, `criteria`, `tree`, `view`). Solo `reading.py` (lee el archivo) y `main.py` (pinta la ventana) tienen efectos secundarios.

```
CSV → read_students → tuple → build_tree → in_range → query (filter + sorted) → view → render
      (generador)    (inmutable) (reduce)   (árbol)     (predicados + key)       (puro) (Qt)
```

## Dónde está cada concepto

| Tema | Concepto | Archivo → función | Qué demuestra |
|---|---|---|---|
| — | Función pura | `analysis.py` (todas), `view.py` | Misma entrada, misma salida; no tocan nada externo. Se prueban con `print` sin abrir la ventana |
| 2.1 | Tipos e inmutabilidad | `model.py` → `Student(NamedTuple)` | Cada alumno es una tupla inmutable; `grades` también es tupla, así que es inmutable "hasta el fondo" |
| 2.1 | Desempaquetado | `model.py` → `row_to_student` | `controlN, name, group, *grades = row` |
| 2.2 | Funciones como valores | `criteria.py` → `FILTERS`, `SORT_KEYS` | Diccionarios de funciones; los combos de la GUI se llenan con sus llaves (sin `if/elif`) |
| 2.2 | Orden superior (recibe función) | `analysis.approved`, `criteria.query`, `main.connect_signals` | `filter(is_approved, …)`, `sorted(key=…)`, `signal.connect(self.refresh)` |
| 2.2 | Orden superior (regresa función) / closure | `criteria.py` → `in_group`, `average_at_least` | `in_group("7A")` regresa una lambda que "recuerda" `"7A"` |
| 2.2 | Combinadores | `criteria.py` → `both`, `negate` | "Reprobados" = `negate(is_approved)` sin escribir lógica nueva |
| 2.2 | lambda | `criteria.py`, `tree.build_tree` | Predicados cortos y acumuladores |
| 2.3 | Intervalos `range()` | `analysis.py` → `make_ranges`, `range_label`, `histogram` | Un range que genera ranges; `r.start`, `r[-1]`, `r.stop` exclusivo (por eso `range(90, 101)`) |
| 2.4 | Operadores como funciones | `criteria.SORT_KEYS` (`op.attrgetter`), `analysis.group_average` (`op.truediv`) | Operadores usados como funciones que se pasan a otras |
| 2.4 | Predicados | `analysis.is_approved` (`all(...)`), `criteria.FILTERS` | Funciones que regresan `True`/`False` |
| 2.5 | map | `reading.read_students`, `analysis.group_average`, `view.student_row` | Transformar cada elemento |
| 2.5 | filter | `analysis.approved`, `criteria.query` | Seleccionar elementos |
| 2.5 | reduce | `analysis.group_average`, `tree.build_tree` | Acumular: la suma de promedios y **construir el árbol completo** |
| 2.5 | Comprensiones | `analysis.failed_units`, `analysis.histogram` | `tuple(unit for unit, grade in enumerate(...) if grade < 70)` |
| 2.6 | Recursividad | `tree.py` → `insert`, `height`, `in_order`, `in_range` | Caso base `None` + llamadas sobre subárboles |
| 2.6 | Árboles | `tree.py` | Árbol binario de búsqueda por promedio, hecho con tuplas `(alumno, izq, der)` como en clase |
| 2.7 | Generadores / evaluación perezosa | `reading.read_students`, `tree.in_order`, `tree.in_range` | `yield` / `yield from`: los alumnos se producen conforme se piden |

## Puntos fuertes para explicar

1. **Árbol inmutable con *path copying*.** Al insertar solo se crean nuevos los nodos del camino raíz → hoja; el resto se **comparte**. El árbol viejo queda intacto (`t1[2] is t2[2]` → `True`).
2. **`in_order` ordena sin `sorted()`.** El recorrido izquierda-nodo-derecha de un ABB ya sale ordenado.
3. **`in_range` poda.** Si el promedio del nodo es menor que el mínimo, no visita la izquierda: no revisa a todos los alumnos.
4. **Los generadores se agotan.** Por eso el CSV se lee **una sola vez** y se guarda en una tupla (`load_path` en `main.py`).
5. **Un único estado.** `main.py` solo guarda `self.students` y `self.tree`, que se **reemplazan** completos al cargar otro archivo, nunca se modifican.
6. **Composición.** El resumen y el histograma se calculan sobre los alumnos ya filtrados, sin código extra.

## Preguntas probables del profe

- **¿Dónde está lo funcional si Qt es imperativo?** En la separación: Qt solo pinta (`render`); todo lo que decide qué pintar son funciones puras.
- **¿Por qué tupla y no lista?** Inmutabilidad: si una función recibiera una lista, podría alterar al alumno para todo el programa.
- **¿Por qué `max` y no `reduce` en `best_student`?** `max(key=average)` es más legible; la versión con `reduce` queda comentada para demostrar que la entiendo.
- **¿Qué es un closure?** Una función que conserva el entorno donde se creó (`in_group`).
- **¿De qué depende la altura del árbol?** Del orden de llegada de los datos. Con el CSV ordenado por promedio, la altura sube de 10 a 40 (se vuelve una lista).
- **¿Límites de Python?** No es funcional puro: sin optimización de recursión de cola, con miles de alumnos ordenados `insert` lanza `RecursionError` (límite ~1000 llamadas).

## Cómo ejecutar

```bash
.venv\Scripts\activate
python main.py
```
Carga `datos/calificaciones.csv` al abrir; con **Cargar Archivo** se puede abrir otro CSV con el mismo formato (`matricula,nombre,grupo,u1,u2,u3,u4`).
