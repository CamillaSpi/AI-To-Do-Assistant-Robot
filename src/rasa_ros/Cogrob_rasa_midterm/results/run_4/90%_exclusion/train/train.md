## intent:bot_challenge
- Sto parlando con un bot?

## intent:goodbye
- buona notte

## intent:help
- Ho bisogno di assistenza

## intent:greet
- Ciao

## intent:affirm
- affermativo

## intent:mood_great
- Estremamente buono

## intent:ask_name
- mi hai già visto prima?

## intent:mood_unhappy
- Estremamente triste

## intent:deny
- mai

## intent:clean_activities
- per favore, cancella tutte le attività completate

## intent:view_categories
- quali sono le mie categorie?

## intent:remind_me_of
- non posso dimenticare di fare l'attività [boxe](activity) nella categoria [sport](category) il prossimo lunedì
- imposta un promemoria per l'attività [chiamare mia madre](activity) nella categoria [famiglia](category) per la prossima mattina
- aiutami a ricordare di [andare al compleanno](activity) il 12/18/2022

## intent:view_activities
- voglio vedere tutte le mie attività [completate](activity_status)
- quali sono le mie attività [fatte](activity_status)?
- voglio vedere tutte le mie attività per lunedì

## intent:modify_category
- sostituire la categoria [banca]{"entity": "category", "role": "old"} con [vacanza]{"entity": "category", "role": "new"}
- per favore, variare la categoria [finanza]{"entity": "category", "role": "old"} nella categoria [banca]{"entity": "category", "role": "new"}
- cambiare il nome della categoria [divertimento]{"entity": "category", "role": "old"} con il nome [cura personale]{"entity": "category", "role": "new"}

## intent:add_category
- nuova categoria da aggiungere: [progetti](category)
- voglio usare una nuova categoria [sport](category)
- ciao, inserisci la seguente categoria [cultura](category)
- nuova categoria da inserire: [finanze](category)

## intent:modify_activity_deadline
- per l'attività [prenotare l'aereo](activity) trasforma la scadenza in lunedì
- altera la deadline dell'attività [pagare il supermercato](activity) nella categoria [pagamenti](category) in domenica
- per l'attività [appunti](activity) nella categoria [scuola](category) trasformare la scadenza in lunedì
- altera la deadline dell'attività [andare al mare](activity) nella categoria [tempo libero](category) in domenica
- voglio modificare la scadenza dell'attività [partita con papà](activity) nella categoria [tempo libero](category) in domani alle 18:00

## intent:remove_category
- cancella una categoria
- non voglio usare la categoria [medico](category)
- ciao, voglio rimuovere la categoria [salute personale](category)
- fai scomparire [spesa](category) dalle mie categorie
- voglio eliminare la categoria [imminente](category)

## intent:set_status_activity
- imposta [non fatto](activity_status) [ripeti matematica](activity) nella categoria [scuola](category)
- ciao, voglio porre come [eseguito](activity_status) [ripetizioni](activity) nella categoria [laurea](category)
- poni [fatta](activity_status) l'attività [shampoo](activity) nella categoria [benessere personale](category)
- imposta come [non sviluppata](activity_status) [giocare a carte](activity)
- imposta come [concluso](activity_status) [giardinaggio](activity) nella categoria [giardino](category)
- metti come [finita](activity_status) [alzati](activity) in [quotidiano](category)

## intent:modify_activity_category
- per l'attività [giocare a pallone](activity) trasforma la categoria [svago]{"entity": "category", "role": "old"} in [sport]{"entity": "category", "role": "new"}
- modificare la categoria [tempo libero]{"entity": "category", "role": "old"} di [camminare all'aperto](activity) in [alimentazione]{"entity": "category", "role": "new"}
- voglio cambiare la categoria [vacanze]{"entity": "category", "role": "old"} dell'attività [yoga](activity)
- per l'attività [partecipare alla conferenza](activity) trasforma la categoria [cultura]{"entity": "category", "role": "old"} in [lavoro]{"entity": "category", "role": "new"}
- voglio cambiare la categoria [sport]{"entity": "category", "role": "old"} dell'attività [yoga](activity) con la categoria [palestra]{"entity": "category", "role": "new"}
- sostituisci la categoria [tempo libero]{"entity": "category", "role": "old"} dell'attività [comprare i regali](activity) con la categoria [Natale]{"entity": "category", "role": "new"}
- per l'attività [prenotare il treno](activity) aggiorna la categoria [imminente]{"entity": "category", "role": "old"} in [vacanza]{"entity": "category", "role": "new"}

## intent:modify_activity_name
- nella categoria [eventi](category) cambia il nome dell'attività [tagliare i capelli]{"entity": "activity", "role": "old"}
- voglio cambiare l'attività con nome [organizzare raccolta fondi]{"entity": "activity", "role": "old"} nella categoria [volontariato](category)
- modifica il nome dell'attività [yoga]{"entity": "activity", "role": "old"} con il nome [pilates]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con nome [leggere]{"entity": "activity", "role": "old"} con [leggere un libro]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [ballo]{"entity": "activity", "role": "old"} con nome [canto]{"entity": "activity", "role": "new"}
- per l'attività [yoga]{"entity": "activity", "role": "old"} nella categoria [cura personale](category) modifica il nome con [parrucchiere]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [canto]{"entity": "activity", "role": "old"} con il nome [ballo]{"entity": "activity", "role": "new"}
- per l'attività [leggere l'articolo]{"entity": "activity", "role": "old"} nella categoria [impegni](category) trasforma il nome con [leggere un libro]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con nome [fare beneficenza]{"entity": "activity", "role": "old"} nella categoria [impegni sociali](category)

## intent:remove_item
- elimina [fare yoga](activity)
- rimuovi [revisione del progetto](activity) nella categoria [lavoro](category) alle 10:25
- cancella [camminare](activity) nella categoria [salute personale](category) alle 6:30
- ciao, voglio eliminare un'attività dall'elenco [divertimento](category)
- elimina [imparare lo spagnolo](activity) nella categoria [lingue](category)
- cancellare l'attività [scrivere la relazione](activity) nella categoria [ricerca](category)
- ciao, voglio eliminare un'attività dalla mia lista
- elimina l'attività [allenarsi](activity) nella categoria [benessere](category)

## intent:presentation
- [edmondo](name)
- ciao sono [Luke](name)
- sono [carla](name)
- [gianni](name)
- [pierluigi](name)
- ciao il mio nome è [Kevin](name)
- creare un account
- [isa](name)
- [gisel](name)
- sono [carolina](name)
- [clarissa](name)
- [cinzia](name)
- [anacleto](name)
- [marianna](name)
- [laura](name)

## intent:inform
- [comprare le scarpe](activity)
- [film da vedere](category)
- [analisi](activity)
- [da comprare](category)
- [studiare in biblioteca](activity)
- [fare jogging](activity)
- oggi
- [palestra](category)
- [fare una doccia](activity)
- [suonare la chitarra](activity)
- [vacanze](category)
- [fare ripetizioni](activity)
- [cuocere biscotti](activity)
- dopodomani alle 15
- [negozio](category)
- [viaggiare](activity)
- [dieta](category)
- 26 minuti e 30 secondi

## intent:add_item
- aggiungi [andare dai genitori](activity) in [famiglia](category) alle 20:00
- ciao, inserisci [ascoltare musica](activity)
- ciao, voglio inserire un'attività [webcall](activity) nella categoria [lavoro](category)
- ciao, inserisci l'attività [andare a teatro](activity) nella categoria [arte](category)
- inserisci una nuova attività [guardare la partita](activity)
- vorrei aggiungere la nuova attività [revisione](activity) alla categoria [progetti](category)
- inserisci l'attività [nuotare](activity) nella categoria [sport](category)
- ciao, aggiungi [scrivere un messaggio](activity)
- ciao, inserisci [taekwondo](activity) nella categoria [arti marziali](category)
- inserisci [chiesa](activity) in [settimanale](category) alle 16:00
- inserisci l'attività [fare giardinaggio](activity) in [casa](category)
- inserisci [andare all'ufficio postale](activity) in [essenziali](category) per domani
- inserisci [nuotare](activity) in [sport](category)
- metti [fare shopping](activity)
- inserisci [organizzare l'armadio](activity) nella categoria [abbigliamento](category)
- vorrei mettere l'attività [suonare](activity) in [settimanale](category)
- inserisci l'attività [conferenza](activity) in [lavoro](category)
- vorrei inserire la nuova attività [giocare ai videogiochi](activity) alla categoria [svago](category)
- ciao, inserisci [andare al ristorante](activity) nella categoria [svago](category)
- inserisci [andare in palestra](activity)
- aggiungi [boxe](activity) nella categoria [sport](category)
- creare l'attività [fare shopping](activity) nella categoria [casa](category) alle 9:40

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
