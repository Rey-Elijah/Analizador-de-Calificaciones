# Analizador Funcional de Calificaciones

Aplicación de escritorio en **Python + PySide6 (Qt)** que carga las calificaciones de un grupo desde un archivo CSV y las analiza: promedios, alumnos aprobados y reprobados, filtros, ordenamiento, búsqueda por rango de promedio e histograma.

Proyecto de la **Unidad 2 — Modelo de Programación Funcional** de la materia *Programación Lógica y Funcional* (7.º semestre, Ingeniería en Sistemas Computacionales). El objetivo es resolver un problema real aplicando los conceptos de la unidad: funciones puras, inmutabilidad, funciones de orden superior, `lambda`, `map`/`filter`/`reduce`, comprensiones, `range()`, recursividad, árboles y generadores.

---

## Características

- **Carga de CSV**: al abrir la app se carga `datos/calificaciones.csv` automáticamente; con **Cargar Archivo** se puede abrir otro.
- **Tabla de alumnos**: matrícula, nombre, grupo, calificaciones por unidad, promedio, estado y unidades reprobadas.
- **Regla de aprobación TecNM**: un alumno aprueba solo si **todas** sus unidades son ≥ 70.
- **Filtros**: Todos, Aprobados, Reprobados, por grupo.
- **Ordenamiento** por nombre, promedio, matrícula o grupo, ascendente o descendente.
- **Búsqueda por rango de promedio** (mín / máx) usando un **árbol binario de búsqueda inmutable**.
- **Resumen**: total de alumnos, aprobados, promedio general y mejor alumno.
- **Histograma** por rangos de promedio (0-59, 60-69, 70-79, 80-89, 90-100).

Todos los controles se actualizan al instante: el resumen y el histograma siempre corresponden a los alumnos filtrados.

---

## Requisitos

- **Python 3.12 o superior** (probado con Python 3.14)
- **PySide6** (probado con la versión 6.11.2)

---

## Instalación y ejecución

Desde una terminal, dentro de la carpeta `analizador_calificaciones`:

### Windows

```bash
# 1. Crear el entorno virtual (solo la primera vez)
py -m venv .venv

# 2. Activarlo
.venv\Scripts\activate

# 3. Instalar las dependencias (solo la primera vez)
pip install -r requirements.txt

# 4. Ejecutar la aplicación
python main.py
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Editar la interfaz (opcional)

La ventana se diseñó en **Qt Designer** (`ui/window.ui`). Después de modificarla hay que regenerar el código de Python:

```bash
pyside6-designer                                  # abre Qt Designer
pyside6-uic ui/window.ui -o ui_window.py          # regenera la interfaz
```

> No edites `ui_window.py` a mano: se sobreescribe cada vez que se regenera.

---

## Formato del CSV

Primera fila de encabezados; una fila por alumno con 4 calificaciones de unidad (enteros de 0 a 100). Codificación **UTF-8**.

```csv
matricula,nombre,grupo,u1,u2,u3,u4
22130100,Ana López Díaz,7A,64,72,80,61
22130101,Luis Hernández López,7B,78,61,76,66
```

---

## Estructura del proyecto

```
analizador_calificaciones/
├── main.py           # Punto de entrada. Ventana y eventos (única parte con efectos en la GUI)
├── view.py           # Funciones puras que convierten alumnos en textos para la tabla, resumen e histograma
├── model.py          # Student (NamedTuple inmutable) y conversión de filas del CSV
├── reading.py        # Lectura del CSV con un generador (yield)
├── analysis.py       # Promedios, aprobados, mejor alumno, rangos e histograma
├── criteria.py       # Filtros y criterios de orden como funciones (FILTERS, SORT_KEYS)
├── tree.py           # Árbol binario de búsqueda inmutable por promedio
├── ui/window.ui      # Diseño de la ventana (Qt Designer)
├── ui_window.py      # Interfaz generada con pyside6-uic
├── datos/calificaciones.csv   # Datos de ejemplo (40 alumnos, grupos 7A y 7B)
├── CONCEPTOS.md      # Dónde se aplica cada concepto de la Unidad 2
└── requirements.txt
```

---

## Arquitectura: núcleo funcional, cáscara imperativa

Toda la lógica está en **funciones puras** que no dependen de Qt (`model`, `analysis`, `criteria`, `tree`, `view`). Solo dos archivos tienen efectos secundarios:

- `reading.py`: lee el archivo (la frontera con el exterior).
- `main.py`: pinta la ventana.

Cada cambio en un control ejecuta el mismo pipeline:

```
CSV → read_students → tuple → build_tree → in_range → query (filter + sorted) → view → render
      (generador)    (inmutable) (reduce)   (árbol)      (predicados + key)      (puro)  (Qt)
```

El detalle de qué concepto de la unidad se aplica en cada archivo y función está en [`CONCEPTOS.md`](CONCEPTOS.md).

---

## Autor

**Rey Elijah Morales Pérez**
Programación Lógica y Funcional · Unidad 2 · 7.º semestre
