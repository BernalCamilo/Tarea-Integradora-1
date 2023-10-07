# **Módulo Expresiones Regulares**

## **Caso de Prueba #001**

| **ID de Caso de Prueba** | 001                                                     |
|-------------------------|----------------------------------------------------------|
| **Descripción de la Prueba** | Verificar la validez de varios nombres de usuario utilizando expresiones regulares. |
| **Supuestos y Condiciones Previas** | Se asume que el módulo `regular_expressions` está correctamente implementado y disponible para las pruebas. |
| **Datos de Prueba** | Los nombres de usuario que se van a validar incluyen ejemplos válidos e inválidos. |
| **Resultado Esperado** | Se espera que los nombres de usuario válidos sean confirmados como válidos (True) y los nombres de usuario inválidos sean confirmados como inválidos (False). |

Aquí tienes la tabla llenada con los casos de prueba proporcionados:

| **Pruebas**         | **Nombre de Usuario**  | **Resultado Esperado** | **Tipo de Caso**   |
|---------------------|-------------------------|------------------------|--------------------|
| test_standard_cases | "Juan Perez"            | True                   | Caso estándar      |
| test_standard_cases | "Maria Smith"           | True                   | Caso estándar      |
| test_standard_cases | "John Doe"              | True                   | Caso estándar      |
| test_limit_cases    | "J P"                   | True                   | Caso límite        |
| test_limit_cases    | "user_name 123"         | False                  | Caso límite        |
| test_limit_cases    | "Alice123 doe"          | False                  | Caso límite        |
| test_limit_cases    | "Alice_Doe"             | False                  | Caso límite        |
| test_limit_cases    | "Alice@Doe"            | False                  | Caso límite        |
| test_interesting_cases | "Alice@Doe"          | False                  | Caso interesante   |
| test_interesting_cases | "Alice Doe"          | True                   | Caso interesante   |
| test_interesting_cases | "User-Name"          | False                  | Caso interesante   |
| test_interesting_cases | "user123"            | False                  | Caso interesante   |
| test_interesting_cases | "A P"                | True                   | Caso interesante   |


# **Módulo Gramática Libre de Contexto**

## **Caso de Prueba #002**

| **ID de Caso de Prueba** | 002                                                   |
|-------------------------|----------------------------------------------------------|
| **Descripción de la Prueba** | Verificar la validez de secuencias utilizando una gramática libre de contexto. |
| **Supuestos y Condiciones Previas** | Se asume que el módulo `context_free_grammar` está correctamente implementado y disponible para las pruebas. |
| **Datos de Prueba** | Las secuencias que se van a validar incluyen ejemplos válidos e inválidos según la gramática libre de contexto. |
| **Resultado Esperado** | Se espera que las secuencias válidas sean confirmadas como válidas (True) y las secuencias inválidas sean confirmadas como inválidas (False) según la gramática. |

Aquí tienes la tabla llenada con los casos de prueba proporcionados para la clase `TestFreeContextGrammar`:

| **Pruebas**         | **Input**                                      | **Resultado Esperado** | **Tipo de Caso**   |
|---------------------|-----------------------------------------------|------------------------|--------------------|
| test_standard_cases | ["beginning", "saludaralforastero", "preguntarsinecesitaayuda", "darcomida"] | True                   | Caso estándar      |
| test_limit_cases    | ["saludaralforastero", "mantenerdistancia", "salvarforasterodezombies"] | False                  | Caso límite        |
| test_limit_cases    | ["befinning", "saludaralforastero", "preguntarsinecesitaayuda", "darcomida"] | False                  | Caso límite        |
| test_interesting_cases | ["beginning", "mantenerdistancia", "salvarforasterodezombies"] | True                   | Caso interesante   |

# **Módulo Autómata Finito No Determinista**

## **Caso de Prueba #003**

| **ID de Caso de Prueba** | 003                                                      |
|-------------------------|----------------------------------------------------------|
| **Descripción de la Prueba** | Verificar si un autómata finito no determinista (NFA) acepta o no acepta diversas cadenas de entrada. |
| **Supuestos y Condiciones Previas** | Se asume que el módulo `non_deterministic_automata` está correctamente implementado y disponible para las pruebas. |
| **Datos de Prueba** | Se proporcionan diferentes cadenas de entrada para evaluar si el NFA las acepta o no. |
| **Resultado Esperado** | Se espera que el NFA acepte las cadenas de entrada para las cuales se ha afirmado que se aceptarán (True), y que no acepte las cadenas de entrada para las cuales se ha afirmado que no se aceptarán (False). |
| **Resultado Real y Condiciones Posteriores** | Los resultados reales de la prueba se compararán con los resultados esperados para determinar si el NFA funciona correctamente. |

| **Pruebas**         | **Input**   | **Resultado Esperado** | **Tipo de Caso**   |
|---------------------|-------------|------------------------|--------------------|
| test_standard_cases | "0011010"   | True                   | Caso estándar      |
| test_standard_cases | "0011110000" | True                   | Caso estándar      |
| test_standard_cases | "001111110"  | True                   | Caso estándar      |
| test_limit_cases    | "0"         | False                  | Caso límite        |
| test_limit_cases    | "00111010"  | True                   | Caso límite        |
| test_limit_cases    | "00111100001" | False                  | Caso límite        |
| test_interesting_cases | "00111111" | False                  | Caso interesante   |
| test_interesting_cases | "001111001" | False                  | Caso interesante   |

# **Módulo Transductor de Estado Finito**

## **Caso de Prueba #004**

| **ID de Caso de Prueba | 004                                                        |
|------------------------|------------------------------------------------------------|
| **Descripción de la Prueba** | Verificar si el transductor hace el cambio de nombre o no, recibiendo diversas cadenas de entrada |
| **Supuestos y Condiciones Previas** | Se asume que el módulo `finite_state_transducer` está correctamente implementado y disponible para las pruebas. |
| **Datos de Prueba** | Se proporcionan diferentes cadenas de entrada para evaluar si el FST cambia el nombre en la historia. |
| **Resultado Esperado** | Se espera que el FST cambie el nombre del usuario al iniciar o en la mitad de la historia si las cadenas ingresadas son confirmadas como válidas (True), o se rechaza las cadenas de entrada confirmadas como inválidas (False). |
| **Resultado Real y Condiciones Posteriores** | Los resultados reales de la prueba se compararán con los resultados esperados para determinar si el FST funciona correctamente. |


| **Pruebas**                          | **Input**           | **Resultado Esperado**                                      | **Tipo de Caso**           |
|-------------------------------------|---------------------|-------------------------------------------------------------|----------------------------|
| `test_translates_accept`            | "Juan Perez"        | "En el camino se encuentra un zombie, Juan Perez decide esconderse." | Caso de Aceptación         |
| `test_translates_accept`                                | "C"                 | "En el camino se encuentra un zombie, C decide esconderse."     | Caso de Aceptación         |
|  `test_translates_accept`                                  | "Maria Rodriguez"   | "En el camino se encuentra un zombie, Maria Rodriguez decide esconderse." | Caso de Aceptación         |
| `test_translates_no_accepts`        | ""                  | No igual a "En el camino se encuentra un zombie, ---- decide esconderse." | Caso de No Aceptación      |
|  `test_translates_accept`                                     | "Maria Rodriguez"   | No igual a "En el camino se encuentra un zombie, ---- decide esconderse." | Caso de No Aceptación      |

