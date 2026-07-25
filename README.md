# Fundamentos de Python

Proyecto individual para la evidencia **GA1-220501093-04-AA1-EV01**.

Este repositorio contiene ejercicios practicos de las secciones 1 a 4 de Fundamentos de Python. Cada script se puede ejecutar de forma independiente con Python 3.

## Estructura

```text
Fundamentos_Python/
|-- README.md
|-- seccion1/
|   |-- 01_hola_mundo.py
|   |-- 02_print_argumentos.py
|   `-- 03_formato_salida.py
|-- seccion2/
|   `-- 01_literales_cadenas.py
|-- seccion3/
|   `-- 01_operadores_matematicos.py
|-- seccion4/
|   |-- 01_variables.py
|   |-- 02_convertidor_temperatura.py
|   `-- 03_operadores_expresiones.py
`-- src/
    `-- puntaje_final_jugador.py
```

## Como ejecutar

1. Instala Python 3.
2. Clona el repositorio y abre una terminal en su carpeta.
3. Ejecuta un archivo, por ejemplo:

```bash
python seccion3/01_operadores_matematicos.py
python src/puntaje_final_jugador.py
```

En Windows tambien puedes usar `py` en lugar de `python`.

## Ejercicios de operadores matematicos

El archivo `seccion3/01_operadores_matematicos.py` trabaja con las variables `numero_1 = 10` y `numero_2 = 3`. La logica consiste en aplicar cada operador y mostrar su resultado.

| Operador | Operacion | Resultado | Uso |
|---|---:|---:|---|
| `+` | `10 + 3` | `13` | Suma |
| `-` | `10 - 3` | `7` | Resta |
| `*` | `10 * 3` | `30` | Multiplicacion |
| `/` | `10 / 3` | `3.3333333333333335` | Division decimal |
| `//` | `10 // 3` | `3` | Division entera |
| `%` | `10 % 3` | `1` | Residuo |
| `**` | `10 ** 3` | `1000` | Potencia |

El mismo programa tambien compara ambos valores con `>`, `<`, `==` y `!=`. Estas expresiones producen valores booleanos (`True` o `False`) y permiten tomar decisiones en un programa.

### Ejemplo de salida

```text
Numero 1: 10
Numero 2: 3
Suma: 13
Resta: 7
Multiplicacion: 30
Division: 3.3333333333333335
Division entera: 3
Modulo: 1
Potencia: 1000
10 es mayor que 3: True
10 es igual a 3: False
```

## Programa integrador

`src/puntaje_final_jugador.py` solicita el nombre de un jugador, su puntaje base, bonificacion y penalizacion. Luego calcula:

```text
puntaje_final = puntaje_base + bonificacion - penalizacion
```

Finalmente compara el resultado con 100 para informar si el jugador alcanzo la meta. Con este ejercicio se integran cadenas, entrada de datos, conversion a numeros, variables, operadores aritmeticos y operadores de comparacion.

## Conceptos aplicados

- Funcion `print()` y sus argumentos `sep` y `end`.
- Literales numericos, booleanos y de cadena.
- Concatenacion, repeticion, longitud y conversion de cadenas.
- Variables y asignacion de valores.
- Operadores aritmeticos y de comparacion.
- Expresiones y conversion de temperatura.
