# La palabra with se usa en Python para gestionar un contexto, es así
# como se puede abrir un archivo usando with y no hay necesidad de
# cerrarlo, ya que el gestor se encarga de ello. Para crear un gestor de
# contexto se implemetan los métodos __enter__() y __exit__() para
# definir la entrada y salida respectivamente del contexto. Cree un clase
# llamada Timer, que aplicada a una iteración cualquiera mida el tiempo
# de ejecución de la iteración.
# Ayuda: debe importar el módulo time y usar el método time() para
# obtener el tiempo actual de la máquina. Además en la implemnetación
# del metodo __exit__() debe tener un mensaje que indique el tiempo
# transcurrido en segundos. Para probar la funcionalidad de su clase
# hágalo con el siguiente código:

import time

class Timer:


    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"Tiempo transcurrido: {elapsed_time:.2f} segundos")  


with Timer():
  # Bloque de código para medir el tiempo de ejecución
  for _ in range(1000000):
   pass
