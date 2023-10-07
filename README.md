# Guía Generador de historias interactivas

## Juan Camilo Bernal
## Juan Duque
## Cristian Perafan

Siga estos pasos para configurar y utilizar el proyecto del generador de historias interactivas:

1. **Configuración Inicial**

   - Asegúrese de tener Python 3.x instalado en su sistema.

2. **Clonar el Repositorio**

   ``` 
   git clone https://github.com/BernalCamilo/Tarea-Integradora-1.git 
   ```

3. **Configurar un Entorno Virtual (Opcional, pero recomendado)**

   - Abra una terminal en la raíz del proyecto y ejecute el siguiente comando para crear un entorno virtual:
   
     ```
     python -m venv venv
     ```

   - Luego, active el entorno virtual ejecutando el siguiente comando:

     - En Windows:

       ```
       .\venv\Scripts\activate
       ```

     - En macOS y Linux:

       ```
       source venv/bin/activate
       ```

4. **Instalar Dependencias**

   - Asegúrese de estar en el entorno virtual (de ser necesario) y en la raíz del proyecto. Luego, instale las dependencias ejecutando:

     ```
     pip install -r requirements.txt
     ```

5. **Ejecutar el Proyecto**

   - Una vez que todas las dependencias estén instaladas correctamente, puede ejecutar el proyecto. Utilice el siguiente comando:

     ```
     python main.py
     ```

6. **Interactuar con el Proyecto**

   - Siga las instrucciones proporcionadas por la interfaz de usuario por consola para interactuar con el generador de historias interactivas.


7. **Desactivar el Entorno Virtual (Opcional)**

   - Si ha utilizado un entorno virtual, puede desactivarlo ejecutando el siguiente comando:

     - En Windows:

       ```
       deactivate
       ```

     - En macOS y Linux:

       ```
       deactivate
       ```

Ahora está listo para utilizar el generador de historias interactivas en Python. Siga las instrucciones proporcionadas por el programa y disfrute de su experiencia de narración de historias interactivas. ¡Diviértase!


**Ejecutar las Pruebas:**

Para ejecutar las pruebas del proyecto, utilice el siguiente comando:
  ```
  python -m unittest tests/test_implementation.py
  ```
Para obtener detalles adicionales sobre la ejecución de las pruebas, puede utilizar el siguiente comando detallado:

  ```
  python -m unittest -v tests/test_implementation.py
  ```
 **Implementación con GUI**

 La implementación con GUI ofrece una alternativa visual para aquellos que prefieren una experiencia más amigable desde el punto de vista gráfico. En esta versión, los usuarios pueden interactuar con elementos de la historia a través de una interfaz gráfica intuitiva. Sin embargo, es importante destacar que la implementación con GUI le falta la integración del módulo de logros (GIC), esta implementación esta completa en la UI por consola.

 Para ejecutar las GUI, utilice el siguiente comando:
  ```
  python gui.py
  ```