# M101
# Modulo per statistiche

# Import necessario al bot
from strutture.messaggio import Messaggio
from random import choice

# Import di funzionalità
import time
import math

# Comandi gestiti
# Questa variabile è usata dal main per capire quale modulo gestisce cosa
set_comandi = {"/aggiungi", "/estrai"}

# Funzione principale
# Questa funzione è chiamata dal main per permettere al modulo di gestire
# ogni suo comando
def gestisci_comando(comando,messaggio,mittente,chat,start_time,dati,voce):
    messaggi = list()

    if comando == "/aggiungi":
        testo = comando.lower().strip()

        parametri = []
        for line in testo:
            parametri.extend(line)

        global sacchetto
        sacchetto = []

        stringa = "@" + str(mittente["username"]) + "\n\n"

        for digit in parametri:
            if digit != 'b' and digit != 'n':
                stringa += "Sono stati inseriti token non consentiti: " + str(parametri) + "\n\n"
                stringa += "Si ricorda che sono consentiti solo token: \"b\" o \"n\""
                messaggi.append(Messaggio(stringa, chat["id"]))
                return messaggi
            sacchetto.append(digit)

        if len(sacchetto) <= 1:
            stringa += "Il sacchetto è vuoto o contiene un numero insufficente di token"
        else:
            stringa += ("Sacchetto creato!\n" + "Ci sono " + str(len(sacchetto)) + " token all'interno")

        messaggi.append(Messaggio(stringa, chat["id"]))

    elif comando == "/estrai" or comando == "/e":
    return messaggi


# Funzione di inserimento dei token
def aggiungi(comando, messaggio, mittente, chat, dati, speech):
    messaggi = []

    testo = comando.lower().strip()

    parametri = []
    for line in testo:
        parametri.extend(line)

    global sacchetto
    sacchetto = []

    stringa = "@" + str(mittente["username"]) + "\n\n"

    for digit in parametri:
        if digit != 'b' and digit != 'n':
            stringa += "Sono stati inseriti token non consentiti: " + str(parametri) + "\n\n"
            stringa += "Si ricorda che sono consentiti solo token: \"b\" o \"n\""
            messaggi.append(Messaggio(stringa, chat["id"], speech))
            return messaggi
        sacchetto.append(digit)

    if len(sacchetto) <= 1:
        stringa += "Il sacchetto è vuoto o contiene un numero insufficente di token"
    else:
        stringa += ("Sacchetto creato!\n" + "Ci sono " + str(len(sacchetto)) + " token all'interno")

    messaggi.append(Messaggio(stringa, chat["id"], speech))
    return messaggi



# Funzione di estrazione dei token
def estrai(mittente, comando, chat, dati, speech):
    messaggi = []
    estrazione = []
    emojy = {'b': '\U000026AA   ', 'n': '\U000026AB	'}

    parametri = comando.lower().strip().split(" ")

    stringa = "@" + str(mittente["username"]) + "\n"

    try:
        num_token = [int(s) for s in parametri if s.isdigit()][0]
        if num_token > 4:
            stringa += "Il numero di token da estrarre non è valido.\n\n" + \
                       "Ricorda che puoi estrarre fino ad un massimo di 4 token alla volta dal sacchetto"
            messaggi.append(Messaggio(stringa, chat["id"], speech))
            return messaggi

        elif num_token > len(sacchetto):
            stringa += "Il sacchetto contiene solo " + \
                       str(len(sacchetto)) + \
                       " token, non è possibile estrarne di più"
            messaggi.append(Messaggio(stringa, chat["id"], speech))
            return messaggi

        for _ in range(num_token):
            token_estratto = choice(sacchetto)
            try:
                sacchetto.remove(token_estratto)
            except NameError:
                stringa += "Il sacchetto non è ancora stato riempito!\n\n" + \
                           "Usa il comando /aggiungi per inserire i token nel sacchetto"
                messaggi.append(Messaggio(stringa, chat["id"], speech))
                return messaggi
            estrazione.append(token_estratto)

        stringa += "Sono stati estratti dal sacchetto " + str(num_token) + " token:\n\n     "
        for token in estrazione:
            stringa += emojy[token]

    except IndexError:
        stringa += "Non è stato indicato nessun numero di token da estrarre"

    messaggi.append(Messaggio(stringa, chat["id"], speech))
    return messaggi



# Funzione per popolare il comando help
def help():
    helpstr = "/stats - Mostra le statistiche correnti del bot"
    return helpstr
