### Readme - Ejercicio Guía del Mercader Galáctico ###

#### Diseño ####

   La aplicación fue diseñada en base a un módulo conversor básico para números arábigos y romanos. 
Este conversor fue pensado para recibir únicamente un dígito (ej: 5) o una sección de un número romano (ej: M). 
Los números romanos de mayor complejidad, es decir, aquellos que no pueden ser leídos literalmente (ej: IX), son
descompuestos y procesados en los módulos convertores específicos (human_prize_converter, galactic_prize_converter).
Ambos módulos están pensados para ir descomponiendo el número en cifras, enviarlos al conversor básico y posteriormente 
devolver el resultado completo a la entrada entregada. Además, existe otro módulo llamado products_manager que se 
encarga de almacenar en memoria los artículos que han sido agregados al programa junto con sus repectivos precios. 
Si alguno de estos precios no ha sido calculado, se obtiene automáticamente llamando al módulo conversor correspondiente.

   Finalmente, cabe mencionar que el módulo utils fue creado para validar números romanos mediante una expresión regular.
Dicha expresión fue obtenida desde la página de Hackerrank bajo el supuesto de que no es necesario reinventar la rueda.
El link desde el cual se extrajo el código es el siguiente: [Expresión regular para números romanos](https://www.hackerrank.com/rest/contests/python-hacks/challenges/validate-a-roman-number/hackers/harsh_beria93/download_solution)

Nota: Es necesario autenticarse en la página para poder visualizar el código.
   
   Por último, cabe señalar que, si bien se utilizó TDD en la construcción de la solución, no se fue suficientemente 
estricto con los tests unitarios aquí presentes, dado que no se utilizaron Mockups en la mayoría de los módulos que 
operan como dependencias de los módulos probados, lo cual impidió un aislamiento completo del módulo probado respecto de
la totalidad del proyecto. Esta decisión radica principalmente en la convicción de que desarrollar tests de esta 
naturaleza ha permitido ejecutar pruebas de integración parciales, las cuales nos otorgaron resultados más completos en 
la medida que se iba avanzando con el proyecto. No obstante, esto no quiere decir que se considere una buena práctica.
Muy por el contrario, lo adecuado habría sido aislar por completo cada módulo a probar y luego realizar unos pocos tests
de integración para visualizar el resultado final de diversas entradas al software.


#### Ejecución ####

   Para ejecutar el programa utilizando es preciso ejecutar el intérprete de Python sobre el archivo main.py ubicado 
en el directorio principal del proyecto.
Se han dispuesto las entradas de prueba en un archivo llamado test_entries.txt. Este archivo es el único tipo de entrada 
que tiene el programa, por lo cual si se requiere modificar la entrada será necesario modificar el archivo. 
   Tras mostrar los resultados en pantalla, el programa se cerrará al cabo de 10 segundos.
   La versión de Python utilizada para desarrollar este módulo es Python 3.7. Este proyecto no necesito de ninguna
librería externa, por lo cuál solo se requiere del intérprete de Python para su ejecución.
   
### Supuestos ###

   Para el archivo de entrada, se hacen los siguientes supuestos:
   
* Las preguntas se harán siempre con la frase `how many` cuando se consulta acerca de un producto o expresión con su moneda específica.
En caso de que el tipo de moneda no se proporcione, se asume que la pregunta se hará siempre con la frase `how much` y 
la respuesta será la traducción (en números romanos) de aquello que se pregunta.

* Las instrucciones y consultas se ingresan siempre con letras minúsculas.   

* Los nombres de productos comenzarán siempre con una letra mayúscula.

* Las frases y palabras alienígenas serán siempre con minúscula.

* Se asume que se habla de dinero humano cuando este está escrito con números arábigos y 
está acompañado por la palabra `Credits`

* Se asume asimismo que cuando no se hace referencia al tipo de moneda se está preguntando por dinero galáctico



