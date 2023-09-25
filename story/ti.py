history = []
#0
history.append("Llegaste cansad@ del trabajo, y solo quieres descansar, prendes la televisión y ves que están presentando algo sobre zombies, ¿qué haces?")
#1
history.append("Empiezas a llamar a todos tus conocidos para verificar si lo que esta pasando es real ")
#2
history.append("Te das cuenta que lo que esta pasando es real por lo que vas al supermercado a tomar proviciones ")
#3
history.append("Sales de tu casa con un bate de baisbol ")
#4
history.append("En el camino te encuentras un zombie, decides esconderte ")
#5
history.append("Hiciste bien, solo alcanzabas a ver un zombie pero detrás de el habia una docena, luego de pasar los zombies, decides entrar al supermercado ")
#6
history.append("Adentro se encuentra solo un zombie, por lo que intentas matarlo para poder tener proviciones ")
#7
history.append("Lo lograste matar, mientras veías alimentos para llevarte a casa, encontraste una radio ")
#8
history.append("Empiezas a escuchar a un grupo hablar por la radio, asi que decides pedir ayuda  ")
#9
history.append("El grupo escucho tu ayuda asi que fueron a rescatarte, ahora haces parte de un grupo TE SALVASTE ")
#10
history.append("Empiezas a escuchar a un grupo hablar por la radio, pero decides ignorarlos porque podria ser una trampa  ")
#11
history.append("Los zombies que estaban en la zona eran muchos, por lo que pudieron destruir la puerta y entrar ESTAS MUERTO ")
#12
history.append("Lo lograste matar, mientras veías alimentos para llevarte a casa, encontraste tu comida favorita ")
#13
history.append("Decides abrirla para comer, ya que piensas que puede ser tu ultima comida ")
#14
history.append("Si fue tu ultima comida, al abrir la comida hiciste ruido, alertando a los zombies a tu alrededor ESTAS MUERTO ")
#15
history.append("Decides guardarla para una ocasión especial")
#16
history.append("Un grupo de personas pasaron matando zombies justo afuera de donde estas, decides esconderte ")
#17
history.append("Un grupo de personas pasaron matando zombies justo afuera de donde estas, decides pedir ayuda ")
#18
history.append("Adentro se encuentra solo un zombie, por lo que decides devolverte a casa ")
#19
history.append("Al devolverte a casa te encuentras con que tu vecino necesita ayuda, decides acompañarlo")
#20
history.append("El tenia comida guardada para mucho tiempo, por lo que te quedas Viviendo con el, TE SALVASTE")
#21
history.append("Al devolverte a casa te encuentras con que tu vecino necesita ayuda, decides ignorarlo ")
#22
history.append("Alcanzaste a regresar  a tu casa, pero te das cuenta que tus proviciones no duraran mas de una semana, MORISTE ")
#23
history.append("Hiciste bien, solo alcanzabas a ver un zombie pero detrás de el habia una docena, luego de pasar los zombies, decides devolverte a tu casa ")
#24
history.append("Al volver a casa, decides advertir a todos tus vecinos de lo que esta pasando")
#25
history.append("Logran crear una comunidad exitosa, y autosustentable ")
#26
history.append("Al volver a casa, decides intentar robar a uno de tus vecinos que esta en avanzada edad")
#27
history.append("No conocías la historia de tu vecino, el era parte de las fuerzas armadas, por lo que apenas entraste te disparo, MORISTE ")
#28
history.append("Logras acabar con el, pero habían muchos mas zombies de donde salio este, sales corriendo ")
#29
history.append("Te perdiste en un túnel subterráneo de la ciudad, jamás lograste salir, MORISTE ")
#30
history.append("En el camino te encuentras un zombie, decides atacarlo ")
#31
history.append("Logras acabar con el, pero habían muchos mas zombies de donde salio este, intentas acabar con todos ")
#32
history.append("Decides colgarte para no ser un problema para nadie, MORISTE ")
#33
history.append("Lograste acabsr con todos pero uno de ellos te alcanzo a morder, por lo que decides cortarte la pierna")
#34
history.append("No pudiste detener la hemorragia, ESTAS MUERTO ")
#35
history.append("Sales de tu casa con una pistola ")
#36
history.append("En el camino te encuentras un zombie, decides esconderte ")
#37
history.append("Al intentar esconderte te encuentras con grupo, y al ver el arma te disparan primero, ESTAS MUERTO ")
#38
history.append("En el camino te encuentras un zombie, decides atacarlo ")
#39
history.append("Hiciste much ruido, alertaste a los zombies, ESTAS MUERTO ")
#40
history.append("Te quedas sentado pensando que es una pelicula")
#41
history.append("Decides pedir una pizza por domicilio como cena ")
#42
history.append("Llego la pizza, abriste la puerta para recibirla, y resulto ser un zombie ESTAS MUERTO  ")
#43
history.append("Se te hace raro que la Pelicula siga siendo mas una noticia que entrentenimiento ")
#44
history.append("Lo ignoras y empiezas a preparar tu cena, escuchas un ruido afuera ")
#45
history.append("Decides tomar precaucion, pero aun asi los zombies te logran atrapar, ESTAS MUERTO   ")
#46
history.append("Ellos fuera matar los zombies, tambien estaban quemando todo para evitar que el virus se propagara, MORISTE QUEMADO ")
#47
history.append("Ellos escucharon tu llamado y se dieron cuenta que eres una buena persona ya que compartiste tu comida favorita con ellos, TE SALVASTE, AHORA PERTENECES A UN GRUPO ")



#conexiones
from pyformlang.finite_automaton import NondeterministicFiniteAutomaton

nfa = NondeterministicFiniteAutomaton()
#0
nfa.add_transition('q0','0','q1')
nfa.add_transition('q0','1','q40')

#1
nfa.add_transition('q1','0','q2')

#2
nfa.add_transition('q2','1','q3')
nfa.add_transition('q2','0','q35')

#3
nfa.add_transition('q3','1','q4')
nfa.add_transition('q3','0','q30')

#4
nfa.add_transition('q4','1','q5')
nfa.add_transition('q4','0','q23')

#5
nfa.add_transition('q5','1','q6')
nfa.add_transition('q5','0','q18')

#6
nfa.add_transition('q6','1','q7')
nfa.add_transition('q6','0','q12')

#7
nfa.add_transition('q7','1','q8')
nfa.add_transition('q7','0','q10')

#8
nfa.add_transition('q8','0','q9')

#9 = Estado final de aceptacion

#10
nfa.add_transition('q10','0','q11')

#11 = Estado final, Muere

#12
nfa.add_transition('q12','1','q13')
nfa.add_transition('q12','0','q15')

#13
nfa.add_transition('q13','0','q14')

#14 = Estado final, Muere

#15
nfa.add_transition('q15','1','q16')
nfa.add_transition('q15','0','q17')

#16
nfa.add_transition('q16','0','q46')

#17
nfa.add_transition('q17','0','q47')

#18
nfa.add_transition('q18','1','q19')
nfa.add_transition('q18','0','q21')

#19
nfa.add_transition('q19','0','q20')

#20 = Estado final, Te salvas

#21
nfa.add_transition('q21','1','q22')

#22 = Estado final, Muere

#23
nfa.add_transition('q23','1','q24')
nfa.add_transition('q23','0','q26')

#24
nfa.add_transition('q24','0','q25')

#25 = Estado final, Te salvas

#26
nfa.add_transition('q26','0','q27')

#27 = Estado final, Muere

#28
nfa.add_transition('q28','0','q29')

#29 = Estado final, Muere

#30
nfa.add_transition('q30','1','q28')
nfa.add_transition('q30','0','q31')

#31
nfa.add_transition('q31','1','q32')

#32 = Estado final, Muere

#33
nfa.add_transition('q33','0','q34')

#34 = Estado final, Muere

#35
nfa.add_transition('q35','1','q36')

#36
nfa.add_transition('q36','0','q37')

#37 = Estado final, Muere

#38
nfa.add_transition('q38','0','q39')

#39 = Estado final, Muere

#40
nfa.add_transition('q40','1','q41')
nfa.add_transition('q40','0','q43')

#41
nfa.add_transition('q41','0','q42')

#42 = Estado final, Muere

#43
nfa.add_transition('q43','1','q44')
nfa.add_transition('q43','0','q1')

#44
nfa.add_transition('q44','0','q45')

#45 = Estado final, Muere

#46 = Estado final, Muere

#47 = Estado final, Te salvas

nfa.add_start_state('q0')
nfa.add_final_state('q9')
nfa.add_final_state('q20')
nfa.add_final_state('q25')
nfa.add_final_state('q47')


print(nfa.accepts('ab'))
