from pyformlang.cfg import CFG


cfg = CFG.from_text("""
    S -> beginning SF RF
    SF ->  saludaralforastero SFA | epsilon
    RF ->  mantenerdistancia  RFA  | epsilon
    RFA -> salvarforasterodezombies
    SFA -> preguntarsinecesitaayuda PA | epsilon
    PA ->  darcomida
""")





def validateachievement(consequence):
    return bool(cfg.contains(consequence))