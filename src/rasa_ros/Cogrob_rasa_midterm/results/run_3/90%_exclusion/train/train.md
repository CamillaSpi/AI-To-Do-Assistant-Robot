## intent:bot_challenge
- tu chi sei?

## intent:goodbye
- buona giornata

## intent:help
- Per favore aiuto

## intent:greet
- Buon pomeriggio

## intent:affirm
- sisi

## intent:mood_great
- Sono grande

## intent:ask_name
- dici il mio nome

## intent:mood_unhappy
- Non molto bene

## intent:deny
- mai

## intent:clean_activities
- cancella tutte le mie attività completate

## intent:view_categories
- posso vedere quali sono i miei elenchi?

## intent:remind_me_of
- aiutami a non dimenticare l'attività [studio](activity) nella categoria [scuola](category) per domani
- ricordami di [fare la spesa](activity) nella categoria [immediata](category) alle 8:30
- aiutami a ricordare un'attività

## intent:view_activities
- quali sono le mie attività?
- mostra tutte le mie attività [sviluppate](activity_status) nella categoria [mensile](category)
- quali sono le mie attività [fatte](activity_status)?

## intent:modify_category
- alterare la categoria [cura personale]{"entity": "category", "role": "old"} in [divertimento]{"entity": "category", "role": "new"}
- trasformare la categoria [vacanza]{"entity": "category", "role": "old"} in [banca]{"entity": "category", "role": "new"}
- voglio trasformare la categoria [medicazioni]{"entity": "category", "role": "old"} in [intrattenimento]{"entity": "category", "role": "new"}

## intent:add_category
- nuova categoria: [volontariato](category)
- ciao, voglio inserire la categoria [quotidiana](category)
- voglio aggiungere la categoria [stile di vita](category)
- ciao, voglio mettere una nuova categoria [eventi](category)

## intent:modify_activity_deadline
- voglio modificare la scadenza dell'attività [disegnare un ritratto](activity) nella categoria [lavoro](category) a domani alle 18:00
- voglio cambiare il termine dell'attività [uscire con gli amici](activity) nella categoria [eventi](category) con 27 settembre 1998
- cambia la scadenza dell'attività [raccogliere fondi](activity)
- per l'attività [prenotare l'aereo](activity) nella categoria [vacanza](category) trasformare la deadline in lunedì
- alterare la scadenza

## intent:remove_category
- cancella la categoria [finanza](category)
- voglio cancellare una categoria
- ciao, voglio togliere la categoria [progetti](category)
- rimuovere la categoria [ingegneria](category)
- la categoria da eliminare è [impegni sociali](category)

## intent:set_status_activity
- imposta [non fatto](activity_status) [ripeti matematica](activity) nella categoria [scuola](category)
- imposta [completato](activity_status) [pulire la cucina](activity) nella categoria [casa](category)
- ciao, imposta [incompleto](activity_status) l'attività [aiuta mio nonno](activity) nella categoria [genitori](category)
- ciao, imposta come [completa](activity_status) l'attività [partita di pallone](activity) in [palestra](category)
- ciao, imposta un'attività [non completata](activity_status)
- poni come [non terminata](activity_status) [riposare](activity) in [salute](category)

## intent:modify_activity_category
- modificare la categoria [lavoro]{"entity": "category", "role": "old"} di [pranzo di lavoro](activity)
- voglio cambiare la categoria [desideri]{"entity": "category", "role": "old"} dell'attività [prenotare l'hotel](activity) in [viaggio]{"entity": "category", "role": "new"}
- per l'attività [giocare a carte](activity) cambiare la categoria [amici]{"entity": "category", "role": "old"} in [svago]{"entity": "category", "role": "new"}
- per l'attività [ritirare il pacco](activity) aggiornare la categoria [commissioni]{"entity": "category", "role": "old"} in [imminente]{"entity": "category", "role": "new"}
- trasforma la categoria [studio]{"entity": "category", "role": "old"} dell'attività [preparare l'esame](activity) in categoria [università]{"entity": "category", "role": "new"}
- convertire la categoria [sport]{"entity": "category", "role": "old"} dell'attività [yoga](activity) con [giornaliero/settimanale]{"entity": "category", "role": "new"}
- per l'attività [andare al mercato](activity) aggiorna la categoria [spesa]{"entity": "category", "role": "old"} in [impegni domestici]{"entity": "category", "role": "new"}

## intent:modify_activity_name
- modifica il nome dell'attività [andare dal dentista]{"entity": "activity", "role": "old"} con il nome [andare dal dottore]{"entity": "activity", "role": "new"}
- sostituire il nome dell'attività [guardare il telegiornale]{"entity": "activity", "role": "old"}  with name [leggere il giornare]{"entity": "activity", "role": "new"}
- per l'attività [leggere un libro]{"entity": "activity", "role": "old"} nella categoria [impegni](category) trasforma il nome con [leggere l'articolo]{"entity": "activity", "role": "new"}
- nella categoria [amicizia](category) sostituisci il nome dell'attività [andare al pub]{"entity": "activity", "role": "old"}  con il nome [andare a mangiare una pizza]{"entity": "activity", "role": "new"}
- cambiare il nome dell'attività [meditazione]{"entity": "activity", "role": "old"}  con nome [chiesa]{"entity": "activity", "role": "new"}
- nella categoria [eventi](category) cambia il nome dell'attività [andare dal parrucchiere]{"entity": "activity", "role": "old"}  con il nome [tagliare i capelli]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con nome [andare in montagna]{"entity": "activity", "role": "old"} nella categoria [vacanza](category) con [andare a sciare]{"entity": "activity", "role": "new"}
- modifica il nome di una attività
- nella categoria [università](category) cambiare il nome dell'attività [studio]{"entity": "activity", "role": "old"}  con nome [esame]{"entity": "activity", "role": "new"}

## intent:remove_item
- cancella [chiamare l'elettricista](activity) nella categoria [guasti](category) alle 21:10
- ciao, voglio cancellare un'attività nella categoria [stile di vita](category) alle 16:00
- cancella [andare a un incontro](activity) nella categoria [lavoro](category) alle 4:25
- cancella [partecipare alla lezione](activity) nella categoria [università](category) alle 5:12
- elimina l'attività [psicologo](activity) nella categoria [mente](category)
- cancella [consultare il blog](activity) nella categoria [hobby](category) alle 14:50
- elimina l'attività [andare a nuotare](activity) nella categoria [sport](category)
- cancella [giardinaggio](activity) nella categoria [giardino](category) alle 5:12

## intent:presentation
- [aristide](name)
- [lucilla](name)
- [anna](name)
- [amichela](name)
- sono [giorgio](name)
- [riccardino](name)
- [riziero](name)
- [teresa](name)
- [ernesto](name)
- [chiara](name)
- voglio iscrivermi
- [fabio](name)
- il mio nome è [ferdi](name)
- [cathrine](name)
- crea un utente

## intent:inform
- [giocare ai videogiochi](activity)
- 10:00
- [suonare](activity)
- [spese](category)
- [rata casa](activity)
- [comprare un giubbino](activity)
- [musica](category)
- oggi alle 21
- [uscire](activity)
- in 5 minuti
- [giocare a carte](activity)
- [bolletta](activity)
- 12/10/2022 alle 18:00
- [fare jogging](activity)
- [arredamento](category)
- [finanza](category)
- [prenotare le vacanze](activity)
- [riparazioni](category)

## intent:add_item
- inserire l'attività [bollette](activity) nella categoria [importante](category) alle 11:00
- inserisci [termine sprint](activity) in categoria [ingegneria](category) alle 8:00
- aggiungi [fare pilates](activity)
- ciao, aggiungi [cucinare la cena](activity) nella categoria [casa](category)
- aggiungere l'attività [cucinare](activity) nella categoria [casa](category) alle 21:10
- inserisci l'attività [prenotare il pub](activity) in [amicizia](category) alle 19:41
- vorrei inserire la nuova attività [giocare ai videogiochi](activity) alla categoria [svago](category)
- ciao, voglio inserire un'attività nell'elenco [imminenti](category)
- vorrei inserire una nuova attività [manicure](activity) all'elenco [estetica](category)
- ciao, nella categoria [salute](category) voglio inserire l'attività [andare dal dentista](activity)
- ciao, inserisci l'attività [e-commerce](activity) nella categoria [tecnologia](category)
- inserire [consultare il blog](activity) alle 3:00
- vorrei aggiungere un'attività all'elenco [deepwork](category)
- metti attività [autobus](activity) in categoria [quotidiano](category) alle 3:29
- ciao, inserisci [partecipare alla lezione](activity) nella categoria [corsi](category)
- vorrei inserire un'attività alla categoria [faccende](category)
- ciao, inserisci l'attività [shampoo](activity) nella categoria [quotidiana](category)
- inserire l'attività [ripetere](activity) nella categoria [esame](category) alle 22:20
- ciao, inserisci [cena con i nonni](activity)
- aggiungere [ordinare l'armadio](activity) alle 01:45
- ciao, crea [chiamata di gruppo](activity) nella categoria [studio](category)
- nella categoria [estate](category), voglio aggiungere l'attività [arrampicata](activity)

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
