# 02 - Casos de uso

## GameFinder

**Grupo 9**

## Actor principal

Usuario de GameFinder desde la terminal.

## CU01 - Buscar videojuego por título

**Objetivo:** encontrar un videojuego específico.

**Flujo principal:**
1. El usuario selecciona una opción de búsqueda.
2. Ingresa el título.
3. El sistema realiza la búsqueda con la estrategia elegida.
4. Si existe, muestra los datos del videojuego; si no, informa que no fue encontrado.

## CU02 - Listar catálogo

**Objetivo:** visualizar los videojuegos disponibles.

**Flujo principal:**
1. El usuario selecciona listar videojuegos.
2. El sistema recorre el catálogo.
3. Muestra los datos de cada videojuego.

## CU03 - Filtrar por género

**Objetivo:** consultar videojuegos de un género determinado.

**Flujo principal:**
1. El usuario selecciona filtrar por género.
2. Ingresa el género.
3. El sistema devuelve los videojuegos coincidentes.

## CU04 - Consultar mediante BST o AVL

**Objetivo:** utilizar árboles de búsqueda para consultar u ordenar videojuegos.

**Flujo principal:**
1. El usuario selecciona una opción BST o AVL.
2. Ingresa un título o solicita el listado ordenado.
3. El sistema realiza la operación sobre la estructura correspondiente.

## CU05 - Explorar categorías

**Objetivo:** recorrer la jerarquía de géneros y videojuegos.

**Flujo principal:**
1. El usuario selecciona `Explorar categorías`.
2. Puede visualizar la jerarquía, buscar una categoría o videojuego, o ejecutar el recorrido por niveles.
3. El sistema muestra el resultado correspondiente.

## CU06 - Consultar Top 5

**Objetivo:** obtener los videojuegos con mayor rating.

**Flujo principal:**
1. El usuario selecciona `Ver TOP 5 videojuegos por rating`.
2. El sistema carga los videojuegos en una max-heap.
3. Extrae hasta cinco elementos de mayor prioridad.
4. Muestra el ranking en orden descendente de rating.
