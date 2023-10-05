# **Módulo Expresiones Regulares**

## **Caso de Prueba #001**

| **ID de Caso de Prueba** | 001                                                     |
|-------------------------|----------------------------------------------------------|
| **Descripción de la Prueba** | Verificar la validez de varios nombres de usuario utilizando expresiones regulares. |
| **Supuestos y Condiciones Previas** | Se asume que el módulo `regular_expressions` está correctamente implementado y disponible para las pruebas. |
| **Datos de Prueba** | Los nombres de usuario que se van a validar incluyen ejemplos válidos e inválidos. |
| **Resultado Esperado** | Se espera que los nombres de usuario válidos sean confirmados como válidos (True) y los nombres de usuario inválidos sean confirmados como inválidos (False). |
| **Resultado Real y Condiciones Posteriores** | Los resultados reales de la prueba se compararán con los resultados esperados para determinar si la función `validate_username` funciona correctamente. |

| **Pruebas** | **Nombre de Usuario** | **Resultado Esperado** |
|-------------|-----------------------|------------------------|
| test_valid_username | "Alice" | True |
| test_valid_username | "Bob" | True |
| test_valid_username | "JohnDoe" | True |
| test_invalid_username | "123" | False |
| test_invalid_username | "user_name" | False |
| test_invalid_username | "Alice123" | False |
| test_invalid_username | "Alice_Doe" | False |
| test_invalid_username | "Alice@Doe" | False |

# **Módulo Gramática Libre de Contexto**

## **Caso de Prueba #002**

| **ID de Caso de Prueba** | 002                                                    |
|-------------------------|----------------------------------------------------------|
| **Descripción de la Prueba** | Verificar la validez de varias secuencias de entrada utilizando una gramática libre de contexto. |
| **Supuestos y Condiciones Previas** | Se asume que el módulo `context_free_grammar` está correctamente implementado y disponible para las pruebas. |
| **Datos de Prueba** | Las secuencias de entrada se comprobarán para determinar si son válidas según la gramática dada. |
| **Resultado Esperado** | Se espera que las secuencias de entrada válidas sean confirmadas como válidas (True) y las secuencias de entrada inválidas sean confirmadas como inválidas (False). |
| **Resultado Real y Condiciones Posteriores** | Los resultados reales de la prueba se compararán con los resultados esperados para determinar si la función `validateachievement` funciona correctamente. |

| **Pruebas** | **Secuencia de Entrada** | **Resultado Esperado** |
|-------------|-----------------------|------------------------|
| test_valid | ["beginning", "saludaralforastero", "preguntarsinecesitaayuda", "darcomida"] | True |
| test_valid | ["beginning", "mantenerdistancia", "salvarforasterodezombies"] | True |
| test_invalid | ["saludaralforastero", "mantenerdistancia", "salvarforasterodezombies"] | False |
| test_invalid | ["befinning","saludaralforastero", "preguntarsinecesitaayuda", "darcomida"] | False |
