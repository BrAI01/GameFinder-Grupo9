# TP8 - Recorridos BFS y DFS



## GameFinder - Sistema de recomendación de videojuegos



**Grupo 9**



## Objetivo



Incorporar recorridos BFS (Breadth-First Search) y DFS (Depth-First Search) al grafo de videojuegos de GameFinder.



Estos algoritmos permiten explorar las relaciones entre videojuegos más allá de los vecinos directos.



## Implementación



Se incorporaron tres métodos en `estructuras/grafo.py`:



- `recorrido_bfs(titulo_inicio)`

- `recorrido_dfs(titulo_inicio)`

- `camino_mas_corto_bfs(titulo_inicio, titulo_destino)`



### BFS - Búsqueda en anchura



BFS recorre el grafo por niveles, visitando primero los vértices más cercanos al origen.



Utiliza una cola FIFO y un conjunto de visitados para evitar recorrer un mismo videojuego más de una vez.



**Caso de uso:** encontrar el camino con menor cantidad de relaciones entre dos videojuegos.



Ejemplo:



Minecraft → Terraria → Starbound



El resultado representa un camino de dos conexiones.



### DFS - Búsqueda en profundidad



DFS explora una rama del grafo hasta donde sea posible antes de retroceder y continuar por otra.



La implementación utiliza una pila y un conjunto de visitados.



**Caso de uso:** explorar todos los videojuegos que se pueden alcanzar desde un videojuego inicial.



Ejemplo de prueba: comenzar desde The Witcher 3 y explorar los videojuegos relacionados directa o indirectamente.



## Comparación de algoritmos



| Característica | BFS | DFS |

|---|---|---|

| Estructura auxiliar | Cola | Pila |

| Estrategia | Por niveles | En profundidad |

| Camino más corto sin pesos | Sí | No garantiza |

| Aplicación | Encontrar conexiones mínimas | Explorar relaciones |

| Complejidad temporal | O(V + E) | O(V + E) |

| Complejidad espacial | O(V) | O(V) |



Donde V representa la cantidad de vértices y E la cantidad de aristas.



Ambos algoritmos recorren cada vértice y cada arista como máximo una cantidad constante de veces.



## Integración en GameFinder



Se amplió la opción 11 del menú principal:



1. Ver videojuegos relacionados.

2. Verificar conexión directa.

3. Ver grafo completo.

4. Buscar camino más corto (BFS).

5. Explorar relaciones en profundidad (DFS).

0. Volver.



### Consulta BFS



Permite ingresar un videojuego de origen y otro de destino. El programa muestra el camino con menor cantidad de conexiones.



### Consulta DFS



Permite ingresar un videojuego inicial y muestra todos los videojuegos alcanzables mediante el recorrido en profundidad.



## Pruebas realizadas



El archivo `pruebas_grafo.py` incluye pruebas para:



- Recorrido BFS.

- Recorrido DFS.

- Camino más corto mediante BFS.

- Búsquedas con videojuegos inexistentes.

- Orden de recorrido esperado.



También se verificó la integración desde el menú principal.



Ejemplos comprobados:



- BFS: Minecraft → Terraria.

- DFS: recorrido desde The Witcher 3.

- BFS: Minecraft → Terraria → Starbound.



Las pruebas del grafo y del heap se ejecutaron correctamente.



## Conclusión



La incorporación de BFS y DFS amplía las posibilidades de exploración del grafo de GameFinder.



BFS permite encontrar caminos con la menor cantidad de conexiones cuando las aristas no tienen pesos, mientras que DFS permite explorar en profundidad todos los videojuegos alcanzables.



Ambos algoritmos tienen complejidad temporal O(V + E) y aprovechan la representación mediante listas de adyacencia.



**TP8 - Versión 6**


