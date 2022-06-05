class EV_Calc():
    def EV_Calc_D(pokemon_base,pokemon_IV,pokemon_EV,pokemon_lev):
        D = ((2*pokemon_base + pokemon_IV +(pokemon_EV/4))*pokemon_lev/100)
        return D
    def EV_Calc_EV_Needed(Desired_Increase, Modifier, D, pokemon_lev):
        EVs_needed = ((((Desired_Increase/Modifier)-(D))*400/pokemon_lev)/4)*4
        return EVs_needed