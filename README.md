Autor:
 RENE DORIAN DIAZ CRESPO

 Descriptción

 El proyecto se basa en la resolución del cubo de rubik desde un etsado incial hasta un estado final por medio de algoritmos de búsqueda para encontrar la cantidad de movimientos mínima para llegar al estado deseado.
 En este caso se tomó en cuenta la estructura del cubo como base funcdamental para el armado y la expansión de los diferentes estados que se pueden tern es por eso que se recomienda lo siguiente:

 Subir los valores del cubo de acuerdo a lo siguiente:

            1: 'yellow',        # Cara frontal
            2: 'white',         # Cara trasera
            3: 'green',         # Cara izquierda
            4: 'blue',          # Cara derecha
            5: 'red',           # Cara superior
            6: 'orange'         # Cara inferior

El orden también es fundamental porque está tomando en cuentala orientación de los centros.

Las acciones posibles son 12 en total agrupadas en 6 grupos, las cuales son R, L, U, D, F, B, cada uno de estos con moviemientos de acuerdo a las macillas del reloj (Horario y antihorario)


Trabajo Futuro:

Se recomeinda tomar más énfasis en la estructura del cubo ya que de moemento se hace la carga de acuerdo a las 54 piezas diferentes que se tiene, pero esto se puiede ver reduciso a 26 las cuales están desarrolladas en el archivo excel. Con una ubicación estratégica de los labels, el algoritmo sería más rápido y más "Inteligente" o complejo.
Así también para las heurísticas se recomienda tomar en cuenta las aristas, las esquinas y los centros, ya que no existe ninguno de estos iguales en cuanto a orientación o similotud. Así también los estados imposibles como esquinas torcidas, aristas torcidas y también tomar en cuenta que como es un cubo 3x3, los centrso solo tienen orientación ene el sentido en el que se agarre el cubo, no tienen orientación de fuguras como los cubos mirror o con otro tipo de etiquetas.