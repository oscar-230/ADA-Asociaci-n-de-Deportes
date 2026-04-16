# 🏅 Mini Proyecto - Asociación de Deportes  
**Curso:** Análisis y Diseño de Algoritmos I  
**🏫 Universidad del Valle**  
**👨‍🏫 Profesor:** Jesús Alexander Aranda Bueno  
**📋 Monitor:** Samuel Galindo Cuevas  
**📅 Fecha:** 17 de Mayo de 2024  

---

## 📚 Información General
- **🏢 Facultad:** Ingeniería  
- **🏢 Escuela:** Ingeniería de Sistemas y Computación  
- **📘 Asignatura:** Análisis y Diseño de Algoritmos I  
- **👨‍🏫 Profesor:** Jesús Alexander Aranda Bueno  
- **📋 Monitor:** Samuel Galindo Cuevas  

---

## 🌍 Descripción del Problema

La **Asociación de Deportes** requiere un análisis detallado de su organización para:  
- Identificar equipos y jugadores que recibirán más recursos.  
- Detectar aquellos que necesitan planes de mejora en su rendimiento.  
- Generar rankings de jugadores y equipos basados en métricas de rendimiento y edad.  

El problema considera:  
- **K sedes** distribuidas en el país.  
- Cada sede con **M equipos** asociados a un deporte.  
- Cada equipo con un número de jugadores entre **Nmin y Nmax**.  
- Cada jugador con atributos: **ID, nombre, edad y rendimiento (1–100)**.  

Se requiere ordenar:  
- **Jugadores dentro de cada equipo** por rendimiento ascendente (en caso de empate, mayor edad primero).  
- **Equipos dentro de cada sede** por rendimiento promedio (en caso de empate, más jugadores primero).  
- **Sedes** por rendimiento promedio de sus equipos (en caso de empate, más jugadores primero).  
- **Ranking global de jugadores** de todas las sedes por rendimiento ascendente.  

Además, se deben calcular métricas:  
- Equipo con mayor y menor rendimiento.  
- Jugador con mayor y menor rendimiento.  
- Jugador más joven y más veterano.  
- Promedio de edad y rendimiento de los jugadores.  

---

## 🛠️ Requerimientos del Proyecto

1. **Plantear dos soluciones distintas** al problema, cada una con diferentes estructuras de datos.  
2. **Explicar claramente** las ideas de cada solución: estructuras de datos, algoritmos utilizados y su complejidad teórica.  
3. Implementar manualmente algoritmos de ordenamiento (ej. Merge Sort, Quick Sort), sin usar librerías externas.  
4. **Realizar pruebas** con al menos 4 instancias diferentes del problema.  
5. Implementar la solución en **Java, C++ o Python**.  
6. Entregar un **informe PDF** con:  
   - Análisis de resultados.  
   - Comparación entre complejidad teórica y tiempos reales de ejecución.  
   - Gráficos de tamaño de entrada vs tiempo de salida.  
   - Comparación entre las dos soluciones propuestas.  
   - Conclusiones finales.  

---

## 📖 Ejemplo de Instancia

**Entrada:**  
- K = 2, M = 2, Nmin = 2, Nmax = 4  
- Jugadores: Sofia García (21, 66), Alejandro Torres (27, 24), …  

**Salida esperada:**  
- Ordenamiento de equipos y sedes.  
- Ranking global de jugadores.  
- Estadísticas: equipo/jugador con mayor y menor rendimiento, jugador más joven y más veterano, promedios.  

---

## 🚀 Tecnologías Utilizadas
- **Lenguaje:** Python (o Java / C++ según elección del grupo).  
- **Paradigma:** Programación estructurada y orientada a objetos.  
- **Algoritmos:**  
  - Merge Sort / Quick Sort para ordenamientos.  
  - Algoritmos propios para cálculo de métricas.  

---

---

## 📌 Conclusiones
Este proyecto permite aplicar los conceptos de **estructuras de datos y algoritmos** en un problema realista de gestión deportiva, reforzando la importancia de:  
- Elegir estructuras de datos adecuadas.  
- Implementar algoritmos eficientes.  
- Validar la teoría con pruebas experimentales.  


---
