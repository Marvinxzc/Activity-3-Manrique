import EV_Calc as ec
import Stat_Calc as sc

print('1. Stat Calc ')
print('2. EV Calc ')

pokemon_nature_attack = 1
pokemon_nature_defense = 1
pokemon_nature_SPattack = 1
pokemon_nature_SPdefense = 1
pokemon_nature_speed = 1

cho = int(input('Enter: '))


if cho == 1:
	print('Stats')
	
	pokemon = str(input('Enter pokemon: '))

pokemon_lev = int(input('Enter pokemon level: '))

pokemon_nature = str.lower(input('Enter Pokemon Nature: '))

pokemon_base = int(input('Enter pokemon base: '))

pokemon_IV = int(input('Enter pokemon IV: '))

pokemon_EV = int(input('enter pokemon_EV: '))
	
#NEUTRAL NATURE
if pokemon_nature in ['bashful','serious','quirky','docile','hardy']:
	pokemon_nature_attack = 1
	pokemon_nature_defense = 1 
	pokemon_nature_SPattack = 1
	pokemon_nature_SPdefense = 1
	pokemon_nature_speed = 1

#ATTACK NATURE
elif pokemon_nature in ['lonely','adamant','naughty','brave']:
    pokemon_nature_attack = 1.1
    if pokemon_nature in ['lonely']:
        pokemon_nature_defense = 0.9
    elif pokemon_nature in ['adamant']:
        pokemon_nature_SPattack = 0.9
    elif pokemon_nature in ['naughty']:
        pokemon_nature_SPdefense = 0.9
    elif pokemon_nature in ['brave']:
        pokemon_nature_speed = 0.9

#DEFENSE NATURE
elif pokemon_nature in ['bold','relaxed','impish','lax']:
	pokemon_nature_defense = 1.1
	if pokemon_nature in ['bold']:
		pokemon_nature_att = 0.9
	elif pokemon_nature in ['relaxed']:
		pokemon_nature_speed = 0.9
elif pokemon_nature in ['impish']:
        pokemon_nature_SPattack = 0.9
elif pokemon_nature in ['lax']:
        pokemon_nature_SPdefense = 0.9
	
#SPEED NATURE
elif pokemon_nature in ['timid','hasty','jolly','naive']:
    pokemon_nature_speed = 1.1
    if pokemon_nature in ['timid']:
        pokemon_nature_attack = 0.9
    elif pokemon_nature in ['hasty']:
        pokemon_nature_defense = 0.9
    elif pokemon_nature in ['jolly']:
        pokemon_nature_SPattack = 0.9
    elif pokemon_nature in ['naive']:
        pokemon_nature_SPdefense = 0.9
#SPEED ATTACK NATURE
elif pokemon_nature in ['modest', 'mild', 'rash','quiet']:
    pokemon_nature_SPattack = 1.1
    if pokemon_nature in ['modest']:
        pokemon_nature_attack = 0.9
    elif pokemon_nature in ['mild']:
         pokemon_nature_defense = 0.9
    elif pokemon_nature in ['rash']:
        pokemon_nature_SPdefense = 0.9
    elif pokemon_nature in ['quiet']:
        pokemon_nature_speed = 0.9
#SPEED DEFENSE NATURE
elif pokemon_nature in ['calm', 'hasty', 'jolly' , 'naive']:
    pokemon_nature_SPdefense = 1.1
    if pokemon_nature in ['calm']:
        pokemon_nature_attack = 0.9
    elif pokemon_nature_defense ['hasty']:
        pokemon_nature_defense = 0.9
    elif pokemon_nature in ['jolly']:
        pokemon_nature_SPattack = 0.9
    elif pokemon_nature in ['naive']:
        pokemon_nature_speed = 0.9

print("1. HP")        
print("2. Attack")
print("3. Defense")
print ("4. Special Attack")
print ("5. Special Defense")
print ("6. Speed")


opt = int(input("Enter: "))

if opt == 1:
    pokemon_base_hp = int(input("Enter base hp: "))
    pokemon_IV = int(input("Enter Pokemon IV: "))
    pokemon_EV = int(input("Enter Pokemon EV: "))
    print("TOTAL HP: ", sc.Stat_Calc.Stat_Calc_HP(pokemon_base_hp, pokemon_IV, pokemon_EV, pokemon_lev), "\n")
if opt == 2:
    pokemon_base_attack = int(input("Enter Base Attack: "))
    pokemon_IV = int(input("Enter Pokemon IV: "))
    print("TOTAL BASE ATTACK: ", sc.Stat_Calc.other_stat_att(pokemon_base_attack,pokemon_IV,pokemon_lev,pokemon_nature_att), "\n")
if opt == 3:
    pokemon_base_def = int(input("Enter Base Defense: "))
    pokemon_IV = int(input("Enter IV: "))
    print("TOTAL BASE DEFENSE: ", sc.Stat_Calc.other_stat_def(pokemon_base_def,pokemon_IV,pokemon_lev,pokemon_nature_defense), "\n")
if opt == 4:
    pokemon_base_SPAttack = int(input("Enter Base Special Attack: "))
    print_IV = int(input("Enter IV: "))
    print("TOTAL SPECIAL ATTACK: ", sc.Stat_Calc.other_stat_SPattack(pokemon_base_SPAttack,pokemon_IV,pokemon_lev,pokemon_nature_SPattack), "\n")
if opt == 5:
    pokemon_base_SPDefense = int(input("Enter Base Special Defense:"))
    print_IV = int (input("Enter IV: "))
    print("TOTAL SPECIAL DEFENSE: ",  sc.Stat_Calc.other_stat_SPdefense(pokemon_base_SPDefense,pokemon_IV,pokemon_lev,pokemon_nature_SPdefense), "\n")

if opt == 6:
    pokemon_base_speed = int(input("Enter Base Speed: "))
    print_IV = int (input("ENTER IV: "))
    print("Total Speed: ",  sc.Stat_Calc.other_stat_speed(pokemon_base_speed,pokemon_IV,pokemon_lev,pokemon_nature_speed), "\n")

flag = True
pokemon_lev = 0
Pokemon_Stat = ["HP" ,"Attack","Defense","Special Attack","Special Defense","Speed"]
pokemon_base = [6]
pokemon_IV = [6]
pokemon_EV = [6]

if cho == 2:
    print("Evs")

    while flag:
        pokemon_lev = int(input("Enter Pokemon Level: "))
        if pokemon_lev > 0 and pokemon_lev < 101:
            flag = False
    
    pokemon_nature = str.lower(input("Enter Pokemon's Nature: "))

    print("Enter Base Stats")
    for x in range (1, 6):
        pokemon_base.append(int(input("Enter " + Pokemon_Stat[x] + ": ")))

    print ("Enter IV on each Stat")
    i = 1
    while i < 7:
        pokemon_IV.append(int(input("Enter " + Pokemon_Stat [i] + " IV: ")))
        if (pokemon_IV[i] < 0 or pokemon_IV[i] > 31):
            i = i - 1
            print("Must be between 0 and 31")
        i = i + 1

    print("Enter EV on each Stat")
    j = 1
    while j < 7:
        pokemon_EV.append(int(input("Enter "+Pokemon_Stat[j]+" EV: ")))
        if (pokemon_EV[j] < 0 or pokemon_EV[j] > 255 ):
            j = j - 1
            print("Must be between 0 and 255")
        j = j + 1


    #Pokemon Neutral Nature
    if pokemon_nature in ['quirky' , 'bashful', 'serious','docile','hardy']:
        pokemon_nature_attack = 1
        pokemon_nature_defense = 1
        pokemon_nature_SPattack = 1
        pokemon_nature_SPdefense = 1
        pokemon_nature_speed = 1

    #Pokemon Attack Nature
    elif pokemon_nature in ['lonely','brave','adamant','naughty']:
        pokemon_nature_attack = 1.1
        if pokemon_nature in ['lonely']:
            pokemon_nature_defense = 0.9
        elif pokemon_nature in ['brave']:
            pokemon_nature_speed = 0.9
        elif pokemon_nature in ['adamant']:
            pokemon_nature_SPattack = 0.9
        elif pokemon_nature in ["naughty"]:
            pokemon_nature_SPdefense = 0.9
    
    #Pokemon Nature Defense
    elif pokemon_nature in ['bold','relaxed','impish','lax']:
        pokemon_nature_defense = 1.1
        if pokemon_nature in ['bold']:
            pokemon_nature_attack = 0.9
        elif pokemon_nature in ['relaxed']:
            pokemon_nature_speed = 0.9
        elif pokemon_nature in ['impish']:
            pokemon_nature_SPattack = 0.9
        elif pokemon_nature in ['lax']:
            pokemon_nature_SPdefense = 0.9
    
    #Pokemon Speed Nature
    elif pokemon_nature in ['timid','hasty','jolly','naive']:
        pokemon_nature_speed = 1.1
        if pokemon_nature in ['timid']:
            pokemon_nature_attack = 0.9
        elif pokemon_nature in ['hasty']:
            pokemon_nature_defense = 0.9
        elif pokemon_nature in ['jolly']:
            pokemon_nature_SPattack = 0.9
        elif pokemon_nature in ['naive']:
            pokemon_nature_SPdefense = 0.9
    
    #Pokemon Special Attack Nature
    elif pokemon_nature in ['modest','mild','quiet','rash']:
        pokemon_nature_SPattack = 1.1
        if pokemon_nature in ['modest']:
            pokemon_nature_attack = 0.9
        elif pokemon_nature in ['mild']:
            pokemon_nature_defense = 0.9
        elif pokemon_nature in ['quiet']:
            pokemon_nature_speed = 0.9
        elif pokemon_nature in ['rash']:
            pokemon_nature_SPdefense = 0.9
    
    #Pokemon Special Defense Nature
    elif pokemon_nature in ['calm','gentle','sassy','careful']:
        pokemon_nature_SPdefense = 1.1
        if pokemon_nature in ['calm']:
            pokemon_nature_attack = 0.9
        elif pokemon_nature in ['gently']:
            pokemon_nature_defense = 0.9
        elif pokemon_nature in ['sassy']:
            pokemon_nature_speed = 0.9
        elif pokemon_nature in ['careful']:
            pokemon_nature_SPattack = 0.9
    

    print("1. Attack")
    print("2. Defense")
    print("3. Special Attack")
    print("4. Special Defense")
    print("5. Speed")

    opt = int(input("Enter: "))

    if opt == 1:
        Modifier = pokemon_nature_attack
    if opt == 2:
        Modifier = pokemon_nature_defense
    if opt == 3:
        Modifier = pokemon_nature_SPattack
    if opt == 4:
        Modifier = pokemon_nature_SPdefense
    if opt == 5:
        Modifier = pokemon_nature_speed

    Desired_Increase = int(input("Enter Desired Increase: "))

    D = ec.EV_Calc.EV_Calc_D (pokemon_base[opt+1],pokemon_IV[opt+1],pokemon_EV[opt+1],pokemon_lev)

    EVs_needed = ec.EV_Calc.Ev_Calc_EV_Needed(Desired_Increase,Modifier,D,pokemon_lev)

    print("The total amount of needed EV for your pokemon is ", EVs_needed)


    


    


    