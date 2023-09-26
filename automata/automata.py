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
nfa.add_transition('q35','0','q38')

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

