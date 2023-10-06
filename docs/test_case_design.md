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
| test_valid_username | "Juan Perez" | True |
| test_valid_username | "Maria Smith" | True |
| test_valid_username | "John Doe" | True |
| test_valid_username | "Juan Duque" | True |
| test_valid_username | "John" | True |
| test_valid_username | "Alice Monet" | True |

| test_invalid_username | "123" | False |
| test_invalid_username | "user_name" | False |
| test_invalid_username | "Alice123" | False |
| test_invalid_username | "Alice_Doe" | False |
| test_invalid_username | "Alice@Doe" | False |
| test_invalid_username | "Alice 8" | False |
| test_invalid_username | "Alice@8" | False |

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


# **Módulo Autómata Finito No Determinista**

## **Caso de Prueba #003**

| **ID de Caso de Prueba** | 003                                                      |
|-------------------------|----------------------------------------------------------|
| **Descripción de la Prueba** | Verificar si un autómata finito no determinista (NFA) acepta o no acepta diversas cadenas de entrada. |
| **Supuestos y Condiciones Previas** | Se asume que el módulo `non_deterministic_automata` está correctamente implementado y disponible para las pruebas. |
| **Datos de Prueba** | Se proporcionan diferentes cadenas de entrada para evaluar si el NFA las acepta o no. |
| **Resultado Esperado** | Se espera que el NFA acepte las cadenas de entrada para las cuales se ha afirmado que se aceptarán (True), y que no acepte las cadenas de entrada para las cuales se ha afirmado que no se aceptarán (False). |
| **Resultado Real y Condiciones Posteriores** | Los resultados reales de la prueba se compararán con los resultados esperados para determinar si el NFA funciona correctamente. |

| **Pruebas** | **Cadena de Entrada** | **Resultado Esperado** |
|-------------|-----------------------|------------------------|
| test_accepts | "001111110" | True |
| test_accepts | "00111010" | True |
| test_accepts | "0011010" | True |
| test_accepts | "0011110000" | True |

| test_no_accepts | "0" | False |
| test_no_accepts | "00111111" | False |
| test_no_accepts | "001111001" | False |
| test_no_accepts | "00111100001" | False |

# **Módulo Transductor de Estado Finito**

## **Caso de Prueba #004**

| **ID de Caso de Prueba | 004                                                        |
|------------------------|------------------------------------------------------------|
| **Descripción de la Prueba** | Verificar si el transductor hace el cambio de nombre o no, recibiendo diversas cadenas de entrada |
| **Supuestos y Condiciones Previas** | Se asume que el módulo `finite_state_transducer` está correctamente implementado y disponible para las pruebas. |
| **Datos de Prueba** | Se proporcionan diferentes cadenas de entrada para evaluar si el FST cambia el nombre en la historia. |
| **Resultado Esperado** | Se espera que el FST cambie el nombre del usuario al iniciar o en la mitad de la historia si las cadenas ingresadas son confirmadas como válidas (True), o se rechaza las cadenas de entrada confirmadas como inválidas (False). |
| **Resultado Real y Condiciones Posteriores** | Los resultados reales de la prueba se compararán con los resultados esperados para determinar si el FST funciona correctamente. |

| **Pruebas** | **Cadena de Entrada** | **Resultado Esperado** |
|-------------|-----------------------|------------------------|
| test_accepts | "Juan Perez" | True |
| test_accepts | "Juan Duque" | True |
| test_accepts | "Gabriel" | True |

| test_no_accepts | "Alice_Doe" | False |
| test_no_accepts | "user_name 123" | False |
| test_no_accepts | "MarieCurie 9" | False |