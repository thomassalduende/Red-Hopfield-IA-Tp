# README - Red de Hopfield

Este programa implementa una red de Hopfield para el almacenamiento y recuperación de patrones binarios. Fue desarrollado por el equipo compuesto por Thomas Salduende, Enzo Bua y Nazareno Blanchet como parte de un proyecto de inteligencia artificial.

## Requisitos

Para utilizar este programa, se requiere tener instalado Python en su computadora. El programa ha sido desarrollado y probado en Python 3.

## Instalación

No es necesario realizar ninguna instalación especial para ejecutar este programa, ya que utiliza bibliotecas estándar de Python. Solo se necesita clonar o descargar el código fuente desde el repositorio de GitHub.

## Uso

El programa se ejecuta desde la línea de comandos y se encarga de cargar un archivo CSV de datos, entrenar una red de Hopfield con esos datos y realizar consultas para recuperar patrones almacenados en la red.

Siga estos pasos para utilizar el programa:

1. Asegúrese de que los archivos CSV de datos que desea utilizar (llamados `datos1.csv`, `datos2.csv`, etc.) se encuentren en la misma carpeta que el programa.

2. Ejecute el programa de la siguiente manera: debe correr el comando "python Nnhopfield.py" en la consola sobre la carpeta donde esté tu programa.

3. Se le presentará un menú que le preguntará si desea ejecutar el programa con la red de Hopfield. Responda "si" o "no" según su elección.

4. Si selecciona "si", el programa le mostrará una lista de archivos CSV disponibles en la carpeta. Elija el número del archivo que desea analizar.

5. La red de Hopfield se entrenará con los datos del archivo CSV seleccionado y le permitirá realizar consultas.

6. Después de cada corrida, el resultado se guardará en el directorio `results` en archivos CSV llamados `salida.csv`.

## Presentación de la Red de Hopfield

La red de Hopfield es un modelo de red neuronal recurrente que se utiliza para almacenar y recuperar patrones binarios. Se entrena con un conjunto de patrones y es capaz de reconstruir estos patrones, incluso si se presentan patrones parciales o con ruido.

## Integrantes del Grupo

- Thomas Salduende
- Enzo Bua
- Nazareno Blanchet

## Contribuciones y Contacto

Este programa es una implementación simple de una red de Hopfield y puede ser mejorado y extendido en muchos aspectos. Si tienes alguna pregunta, comentario o sugerencia, no dudes en ponerte en contacto con los integrantes del grupo.


## Informe de Corridas y Evaluación de Resultados

### Corridas con Dataset 1

Ejecutamos el programa con el Dataset 1, que contiene datos binarios representados en el archivo `datos.csv`. Los resultados de las corridas incluyen:

- Después de entrenar la red de Hopfield con el Dataset 1, realizamos consultas con patrones de entrada y obtuvimos resultados satisfactorios. La red fue capaz de recuperar patrones almacenados incluso cuando se presentaron patrones parciales o con ruido.

- Observamos que la red de Hopfield es efectiva para recuperar patrones almacenados en condiciones ideales y con patrones de entrada similares a los patrones almacenados en el dataset.

### Corridas con Dataset 2

Repetimos el proceso anterior utilizando el Dataset 2, que contiene datos binarios representados en el archivo `datos2.csv`. Los resultados de las corridas incluyen:

- Al igual que con el Dataset 1, después de entrenar la red de Hopfield con el Dataset 2, obtuvimos resultados satisfactorios en las consultas. La red demostró su capacidad para recuperar patrones almacenados incluso en presencia de patrones parciales o con ruido.

- En comparación con el Dataset 1, observamos que la red de Hopfield sigue siendo eficaz en la recuperación de patrones con el Dataset 2, lo que demuestra su robustez.

### Evaluación de Resultados

En general, los resultados obtenidos con ambos datasets indican que la red de Hopfield es una herramienta eficaz para el almacenamiento y recuperación de patrones binarios. La red muestra una buena capacidad para recuperar patrones almacenados, incluso en condiciones desafiantes. Sin embargo, es importante tener en cuenta que su rendimiento puede depender de la calidad de los patrones almacenados y la similitud de los patrones de entrada.

---


