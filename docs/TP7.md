# TP7 - Grafos

## GameFinder - Sistema de recomendación de videojuegos

**Grupo 9**

## Objetivo

Convertir las relaciones entre videojuegos en una red, para que GameFinder pueda recomendar títulos relacionados con uno que le gustó al usuario.

## Modelo del grafo

### Vértices

Cada vértice representa **un videojuego** del catálogo.

El grafo no crea copias: guarda referencias a los mismos objetos `Videojuego` que usan el catálogo, los árboles y la heap.

### Aristas

Dos videojuegos están conectados cuando **son similares**, es decir, cuando cumplen al menos una de estas condiciones:

- comparten **género** (por ejemplo, *The Witcher 3* y *Skyrim*, ambos RPG);
- comparten **desarrollador** (por ejemplo, *Elden Ring* y *Dark Souls III*, ambos de FromSoftware, aunque uno es RPG y el otro Acción).

El criterio está encapsulado en la función `son_similares()` y se recibe como parámetro en `construir_grafo()`. Así, si en el futuro se quiere cambiar la definición de "similar", no hace falta modificar la estructura del grafo.

### Tipo de grafo

- **No dirigido**: la similitud es una relación simétrica. Si *A* se parece a *B*, entonces *B* se parece a *A*. Por eso cada arista se guarda en ambos sentidos.
- **No pesado**: en esta etapa solo importa si dos videojuegos están relacionados o no. El costo de cada relación se incorporará en TP9, para los caminos mínimos.
- **Sin lazos ni aristas repetidas**: un videojuego no se conecta consigo mismo y cada par se conecta una sola vez.

### Representación: lista de adyacencia

Se utiliza una **representación por adyacencia**, implementada con un diccionario por vértice. El diccionario de vecinos conserva el orden de incorporación y permite verificar conexiones en tiempo O(1) promedio:

```text
clave  = título normalizado del videojuego
valor  = diccionario de vecinos (título -> objeto Videojuego)
```

Ejemplo con el catálogo actual:

```text
Minecraft      -> Terraria
Terraria       -> Minecraft
Elden Ring     -> The Witcher 3, Skyrim, Fallout 4, Cyberpunk 2077, Dark Souls III
Dark Souls III -> God of War, Elden Ring, God of War Ragnarök, The Last of Us
```

**¿Por qué lista y no matriz de adyacencia?**

Cada videojuego se relaciona solo con algunos otros: el grafo es **disperso**. Con el catálogo actual hay 14 vértices y 21 aristas, mientras que el máximo posible sería 14 · 13 / 2 = 91.

| Representación | Espacio | ¿Existe la arista u–v? | Conviene si... |
|---|---|---|---|
| Adyacencia con diccionarios | O(V + E) | O(1) promedio | el grafo es disperso |
| Matriz de adyacencia | O(V²) | O(1) | el grafo es denso |

Una matriz reservaría V² casillas, casi todas vacías. La lista guarda solamente las relaciones que existen y permite recorrer los vecinos de un videojuego directamente, que es la operación que más usa la recomendación (y la que usarán BFS y DFS en TP8).

## ¿Por qué un grafo y no otro árbol?

Las relaciones de similitud no son jerárquicas:

- un videojuego puede parecerse a varios otros;
- pueden formarse **ciclos** (*The Witcher 3* – *Skyrim* – *Fallout 4* – *The Witcher 3*);
- no existe una raíz natural.

Un árbol no permite ciclos ni que un nodo tenga varios "padres". El árbol general del TP5 sigue siendo adecuado para la jerarquía de categorías; el grafo resuelve otro problema: las relaciones entre videojuegos.

## Implementación

El archivo `estructuras/grafo.py` contiene:

- la clase `GrafoVideojuegos`;
- la función `son_similares(a, b)`, que define el criterio de arista;
- la función `construir_grafo(videojuegos, criterio)`, que arma el grafo a partir del catálogo.

Operaciones principales:

| Operación | Descripción | Complejidad |
|---|---|---|
| `agregar_vertice(videojuego)` | Agrega un videojuego como vértice | O(1) |
| `agregar_arista(a, b)` | Conecta dos videojuegos en ambos sentidos | O(1) promedio |
| `obtener_vertice(titulo)` | Devuelve el videojuego asociado al título | O(1) |
| `obtener_vecinos(titulo)` | Devuelve los videojuegos relacionados | O(grado) |
| `estan_conectados(a, b)` | Indica si existe una arista entre dos videojuegos | O(1) promedio |
| `lista_adyacencia()` | Devuelve el grafo completo | O(V + E) |
| `construir_grafo(...)` | Compara cada par de videojuegos | O(n²) |

La construcción es O(n²) porque, para decidir las aristas, se compara cada par de videojuegos una vez. Se hace una sola vez al iniciar el programa.

Los títulos se normalizan con `strip().lower()`, igual que en las búsquedas anteriores, para que la consulta no dependa de mayúsculas ni espacios.

## Datos de prueba

Para que el grafo tenga relaciones significativas se amplió `datos/videojuegos.json` de 5 a 14 videojuegos, manteniendo los cinco originales. Se agregaron títulos que comparten género o desarrollador con los existentes (por ejemplo, *Elden Ring*, *Fallout 4*, *Cyberpunk 2077*, *Dark Souls III*, *Terraria*).

## Integración en GameFinder

En `main.py` se agregó la opción:

```text
11. Explorar relaciones entre videojuegos
```

con tres consultas:

1. **Ver videojuegos relacionados**: muestra los vecinos de un videojuego como recomendación ("Si te gustó Minecraft, quizás te interesen: Terraria").
2. **Verificar si dos videojuegos están relacionados**: consulta si existe una arista entre ellos.
3. **Ver grafo completo**: muestra la cantidad de vértices y aristas y la lista de adyacencia.

El grafo se construye una vez en `cargar_catalogo()`, a partir del mismo catálogo que usan las demás estructuras.

## Ejemplos de consultas

```text
> 11 → 1
Ingrese el título: minecraft

Si te gustó Minecraft, quizás te interesen:
- Terraria (Sandbox, Re-Logic) - Rating: 8.9
```

```text
> 11 → 2
Primer videojuego: Elden Ring
Segundo videojuego: Dark Souls III

Sí, están relacionados (comparten género o desarrollador).
```

## Pruebas

El archivo `pruebas_grafo.py` verifica:

- el comportamiento de un grafo vacío;
- que no se dupliquen vértices ni aristas y que no se permitan lazos;
- que no se puedan conectar videojuegos inexistentes;
- que el grafo sea no dirigido (la relación vale en ambos sentidos);
- relaciones por mismo género, por mismo desarrollador y la ausencia de relación;
- la simetría de toda la lista de adyacencia construida desde el catálogo.

## Limitaciones y próximos pasos

- Las recomendaciones actuales solo muestran **vecinos directos** (distancia 1). En TP8 se incorporarán **BFS** y **DFS** para explorar relaciones más lejanas.
- Todas las relaciones valen lo mismo. En TP9 se podrá asignar un **costo** a cada arista para calcular caminos mínimos.
- La construcción O(n²) es aceptable para el tamaño del catálogo; con un catálogo muy grande convendría agrupar primero por género y desarrollador para comparar menos pares.

## Archivos del TP7

- `estructuras/grafo.py`
- `pruebas_grafo.py`
- `main.py`
- `datos/videojuegos.json`
- `docs/TP7.md`

## Ejecución

Para ejecutar GameFinder:

```bash
python main.py
```

Para ejecutar las pruebas del grafo:

```bash
python pruebas_grafo.py
```

El TP7 corresponde a la versión 5 de GameFinder.
