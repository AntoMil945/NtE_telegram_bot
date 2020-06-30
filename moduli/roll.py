from random import randint
from strutture.messaggio import Messaggio

## DICE ROLL MODULE

def roll(mittente, comando, chat, dati, speech):
    messaggi = []
    
    parametri = comando.lower().strip().split(" ")
    
    somma_dadi = 0
    somma_costanti = 0
    expected_value = 0
    
    stringa = "@"+str(mittente["username"])+"\n"
    for token in parametri:
        if (token.find("d")<0):
            somma_costanti += int(token)
        else:
            dice = token.split("d")
            dice_type = int(dice[1])
            dice_number = 1
            if (dice[0] != ""):
                dice_number = int(dice[0])
            stringa += "Tirando "+str(dice_number)+" volte un D"+str(dice_type)+" ho ottenuto:\n"
            for _ in range(dice_number):
                dice_roll = randint(1, dice_type)
                stringa += "- "+str(dice_roll)+"\n"
                somma_dadi += dice_roll
                expected_value += (1 + dice_type) / 2

    stringa += "Totale: "+str(somma_dadi)
    if (somma_costanti > 0):
        stringa += " + "+str(somma_costanti)+" -> "+str(somma_dadi + somma_costanti)
    stringa += "\n(Expected Value: "+str(expected_value + somma_costanti)+")"

    messaggi.append(Messaggio(stringa,chat["id"],speech))
    return messaggi