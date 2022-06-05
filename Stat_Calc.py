class Stat_Calc():
    def Stat_Calc_HP(pokemon_base_hp, pokemon_IV, pokemon_EV, pokemon_lev):
        HP = (((2 * pokemon_base_hp + pokemon_IV + (pokemon_EV/4)) * pokemon_lev)/100) + pokemon_lev + 10
        return HP
    
    def other_stat_att(pokemon_base_att, pokemon_IV, pokemon_EV, pokemon_lev, pokemon_nature):
        stat_att = ((((2 * pokemon_base_att + pokemon_IV + (pokemon_EV/4)) * pokemon_lev)/100) + 5) * (((2 * pokemon_base_att + pokemon_IV + (pokemon_EV/4)) * pokemon_lev)/100) + pokemon_nature
        return stat_att
    
    def other_stat_def(pokemon_base_def, pokemon_IV, pokemon_EV, pokemon_lev,pokemon_nature):
        stat_def = ((((2 * pokemon_base_def + pokemon_IV + (pokemon_EV/4)) * pokemon_lev)/100) + 5) * (((2 * pokemon_base_def + pokemon_IV + (pokemon_EV/4)) * pokemon_lev)/100) + pokemon_nature
        return stat_def
    
    def other_stat_SPatt(pokemon_base_Spatt, pokemon_IV, pokemon_EV, pokemon_lev,pokemon_nature):
        stat_SPatt = ((((2 * pokemon_base_Spatt + pokemon_IV + (pokemon_EV/4)) * pokemon_lev)/100) + 5) * (((2 * pokemon_base_Spatt + pokemon_IV + (pokemon_EV/4)) * pokemon_lev)/100) + pokemon_nature
        return stat_SPatt
    
    def other_stat_SPdefense(pokemon_base_SPdefense, pokemon_IV, pokemon_EV, pokemon_lev,pokemon_nature):
        stat_SPdefense = ((((2 * pokemon_base_SPdefense + pokemon_IV + (pokemon_EV/4)) * pokemon_lev)/100) + 5) * (((2 * pokemon_base_SPdefense + pokemon_IV + (pokemon_EV/4)) * pokemon_lev)/100) + pokemon_nature
        return stat_SPdefense
    
    def other_stat_speed(pokemon_base_speed, pokemon_IV, pokemon_EV, pokemon_lev,pokemon_nature):
        stat_speed = ((((2 * pokemon_base_speed + pokemon_IV + (pokemon_EV/4)) * pokemon_lev)/100) + 5) * (((2 * pokemon_base_speed + pokemon_IV + (pokemon_EV/4)) * pokemon_lev)/100) + pokemon_nature
        return stat_speed
