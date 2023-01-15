## intent:bot_challenge
- Sto parlando con un umano?

## intent:goodbye
- ci vediamo in giro

## intent:help
- Per favore aiuto

## intent:greet
- Salve

## intent:affirm
- esatto

## intent:mood_great
- Così perfetto

## intent:ask_name
- chi sono?

## intent:mood_unhappy
- Così triste

## intent:deny
- niente da fare

## intent:clean_activities
- rimuovi tutte le attività

## intent:view_categories
- fammi vedere tutte le mie categorie

## intent:remind_me_of
- voglio impostare un promemoria per l'attività [prenotare l'aereo](activity)
- aiutami a ricordare di [andare al compleanno](activity) il 12/18/2022
- non farmi dimenticare di [correre](activity) alle 19:00

## intent:view_activities
- mostra le attività [incompiute](activity_status) nella categoria [lavoro](category)
- mostrami attività [eseguite](activity_status) nella categoria [scuola](category)
- mostra attività nella categoria [palestra](category) per questa sera

## intent:modify_category
- voglio cambiare la categoria [lavoro]{"entity": "category", "role": "old"} con la categoria [impegni]{"entity": "category", "role": "new"}
- voglio sostituire la categoria [cultura]{"entity": "category", "role": "old"} in [teatro]{"entity": "category", "role": "new"}
- cambiare il nome della categoria [divertimento]{"entity": "category", "role": "old"} con il nome [cura personale]{"entity": "category", "role": "new"}

## intent:add_category
- inserisci [vacanze](category) categoria
- ciao, voglio mettere una nuova categoria [eventi](category)
- categoria: [bollette](category)
- voglio usare una nuova categoria [eventi](category)

## intent:modify_activity_deadline
- per l'attività [andare in chiesa](activity) nella categoria [personale](category) modificare la scadenza con 22 ottobre 1922
- alterare la scadenza
- modifica il termine dell'attività [revisione del progetto](activity) nella categoria [università](category)
- per l'attività [prendere le medicine](activity) nella categoria [salute personale](category) trasformare la scadenza in lunedì
- nella categoria [creatività](category) sostituisci la deadline dell'attività [disegnare](activity) da 22 settembre a 25 settembre

## intent:remove_category
- voglio eliminare la categoria [vacanza](category)
- rimuovere la categoria [visite mediche](category)
- ciao, voglio cancellare la categoria [annuale](category)
- ciao, voglio rimuovere la categoria [famiglia](category)
- ciao, per favore elimina la seguente categoria [medica](category)

## intent:set_status_activity
- imposta [fatto](activity_status) [powerpoint](activity) nella categoria [programmi](category)
- imposta [completata](activity_status) [chiama il medico](activity)
- imposta come [fatta](activity_status) [leggere](activity)
- metti [fatta](activity_status) [guardare la partita](activity) in [intrattenimento](category)
- imposta [fatto](activity_status) [ripeti matematica](activity) nella categoria [scuola](category)
- ciao, imposta come [incompleta](activity_status) l'attività [partita di pallone](activity) in [palestra](category)

## intent:modify_activity_category
- converti la categoria [urgente]{"entity": "category", "role": "old"} dell'attività [fare benzina](activity) con [importante]{"entity": "category", "role": "new"}
- trasforma la categoria [studio]{"entity": "category", "role": "old"} dell'attività [preparare l'esame](activity) in categoria [università]{"entity": "category", "role": "new"}
- per l'attività [disegnare](activity) nella categoria [creatività]{"entity": "category", "role": "old"} sostituire la categoria con [arte]{"entity": "category", "role": "new"}
- per l'attività [preparare i biscotti](activity) modifica la categoria [casa]{"entity": "category", "role": "old"} in [dieta]{"entity": "category", "role": "new"}
- modifica la categoria [vacanze]{"entity": "category", "role": "old"} dell'attività [andare al mare](activity) in [svago]{"entity": "category", "role": "new"}
- per l'attività [guardare il match](activity) trasformare la categoria [famiglia]{"entity": "category", "role": "old"} in [tempo libero]{"entity": "category", "role": "new"}
- sostituire la categoria [casa]{"entity": "category", "role": "old"} dell'attività [preparare il pranzo](activity) con la categoria [faccende domestiche]{"entity": "category", "role": "new"}

## intent:modify_activity_name
- voglio cambiare l'attività con il nome [uscire con mia madre]{"entity": "activity", "role": "old"} in [famiglia](category)
- voglio cambiare l'attività con il nome [fare beneficenza]{"entity": "activity", "role": "old"} nella categoria [volontariato](category) con [organizzare raccolta fondi]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [attività all'aperto]{"entity": "activity", "role": "old"} nella categoria [salute fisica](category)
- modifica il nome dell'attività [pulire il giardino]{"entity": "activity", "role": "old"} con il nome [preparare la colazione]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [nuoto]{"entity": "activity", "role": "old"} nella categoria [sport](category) con il nome [boxe]{"entity": "activity", "role": "new"}
- per l'attività [completare la relazione]{"entity": "activity", "role": "old"} modifica il nome con [completare il powerpoint]{"entity": "activity", "role": "new"}
- sostituisci il nome dell'attività [scrivere l'articolo]{"entity": "activity", "role": "old"}  con il nome [pubblicare l'articolo]{"entity": "activity", "role": "new"}
- per l'attività [suonare la chitarra]{"entity": "activity", "role": "old"} nella categoria [tempo libero](category) modifica il nome con [andare a giocare a calcio]{"entity": "activity", "role": "new"}
- cambiare il nome dell'attività [chiesa]{"entity": "activity", "role": "old"}  con nome [meditazione]{"entity": "activity", "role": "new"}

## intent:remove_item
- cancella [studiare](activity) nella categoria [scuola](category) alle 19:00
- cancella [pagare mutuo](activity) nella categoria [finanza](category) alle 16:00
- cancella [unghie](activity) nella categoria [estetica](category) alle 9:40
- rimuovi l'attività [leggere](activity) nella categoria [cultura](category)
- rimuovi [camminare nel giardino](activity)
- ciao, voglio eliminare un'attività dall'elenco [divertimento](category)
- elimina l'attività [andare a nuotare](activity) nella categoria [sport](category)
- cancella [parrucchiere](activity) nella categoria [benessere](category) alle 13:39

## intent:presentation
- [jhon](name)
- ciao sono [marcello](name)
- il mio nome è [Ugo](name)
- [fiordalise](name)
- [vinci](name)
- [clerice](name)
- [grazia](name)
- [mirella](name)
- sono [Nando](name)
- [marzia](name)
- sono [carla](name)
- [gerardo](name)
- [alberigo](name)
- [geppy](name)
- sono [antonino](name)

## intent:inform
- [personale](category)
- [viaggio in Spagna](activity)
- 19 ore
- [affitto](activity)
- [biblioteca](category)
- venerdì
- [bollette](category)
- [andare nello studio](activity)
- [studiare in biblioteca](activity)
- [fare patente](activity)
- [fare ripetizioni](activity)
- in 5 secondi
- [prenotare il ristorante](activity)
- [salute](category)
- [multa](activity)
- [uscita con la famiglia](activity)
- [farmaci](category)
- [viaggiare](activity)

## intent:add_item
- inserisci [fare esperimenti](activity) nella categoria [scienze](category) alle 10:25
- ciao, voglio inserire un'attività in un elenco
- vorrei inserire un'attività [pagamenti](activity) alla categoria [finanza](category)
- inserisci l'attività [giocare a basket](activity)
- inserisci l'attività [volontariato](activity) in categoria [beneficenza](category) alle 13:39
- ciao, vorrei inserire l'attività nell'elenco [imminente](category) alle 16:30
- vorrei mettere l'attività [pagare le bollette](activity) alla categoria [banca](category)
- metti [trello](activity) in [teamwork](category) alle 2:55
- ciao, aggiungi [acquistare una pizza](activity) nella categoria [mangiare](category)
- inserire [consultare il blog](activity) alle 3:00
- vorrei creare l'attività [festa di compleanno](activity) all'elenco [eventi](category)
- inserisci una nuova attività [guardare la partita](activity)
- metti l'attività [ricerca](activity) in [aggiornamenti](category) alle 18:30
- ciao, voglio inserire un'attività [sci](activity) nell'elenco [inverno](category)
- creare [partecipare a una conferenza](activity) nella categoria [lavoro](category) alle 20:00
- inserisci [termine sprint](activity) in categoria [ingegneria](category) alle 8:00
- vorrei aggiungere la nuova attività [andare in banca](activity) alla categoria [finanza](category)
- aggiungi un'attività in [musica](category)
- metti attività [pizza](activity) in [amici](category) alle 7:00
- ciao, voglio aggiungere un'attività alla categoria [educazione](category)
- ciao, vorrei inserire un'attività nell'elenco [marketing](category) alle 17:30
- inserisci l'attività [fare la spesa](activity) in [quotidiano](category)

## synonym:completata
- terminata
- completata
- completato
- completo
- concluse
- fatta
- fatto
- fatte
- finita
- finito
- eseguita
- eseguite
- sviluppata
- sviluppate
- conclusa
- completa
- terminato
- terminate
- completate

## synonym:incompleta
- ineseguita
- non eseguita
- incompleto
- incomplete
- non sviluppate
- non conclusa
- non completo
- incompleta
- non completato
- non sviluppata
- non finita
- non fatta
- non fatto
- non finito
- non terminata
- non terminato
- incompiuta
- incompiute
- non completata
- non completa
