## intent:bot_challenge
- tu chi sei?

## intent:goodbye
- buona notte
- arrivederci

## intent:help
- Per favore aiutami
- Aiuto

## intent:greet
- buon giorno
- Ehi

## intent:affirm
- certo
- si

## intent:mood_great
- Meraviglioso
- Così buono
- Stupefacente

## intent:mood_unhappy
- Sono triste
- Molto triste

## intent:ask_name
- mi riconosci?
- puoi dire il mio nome?
- puoi pronuniciare il mio nome?

## intent:deny
- assolutamente no
- no grazie
- nono

## intent:clean_activities
- per favore, rimuovi tutte le attività completate
- per favore, elimina tutte le mie attività completate
- rimuovi tutte le attività terminate

## intent:view_categories
- voglio guardare le categorie aggiunte
- posso vedere quali sono i miei elenchi?
- quali sono le mie categorie?

## intent:remind_me_of
- ricordami di [fare la spesa](activity) nella categoria [immediata](category) alle 8:30
- imposta un promemoria per l'attività [chiamare la mia ragazza](activity) nella categoria [sociale](category) nella prossima mattina
- ricordami la [riunione di lavoro](activity) domani mattina
- aiutami a non dimenticare l'attività [rivedere la relazione](activity) nella categoria [consegna progetto](category) per domani
- ricordami di [prendere la pillola](activity) in [cura personale](category)
- voglio impostare un promemoria
- aiutami a ricordare l'attività [compleanno](activity) il 12/18/2022

## intent:view_activities
- voglio vedere tutte le mie attività per lunedì
- voglio vedere tutte le attività inserite
- mostra attività
- cosa devo fare oggi?
- quali sono le mie attività inserite?
- mostra attività [completate](activity_status)
- quali sono le mie attività aggiunte?
- voglio vedere tutte le attività create

## intent:modify_category
- per favore, voglio cambiare la categoria [teatro]{"entity": "category", "role": "old"} in [cultura]{"entity": "category", "role": "new"}
- voglio modificare il nome della categoria [svago]{"entity": "category", "role": "old"} con il nome [divertimento]{"entity": "category", "role": "new"}
- per favore, voglio sostituire la categoria [cura]{"entity": "category", "role": "old"} a [stile di vita]{"entity": "category", "role": "new"}
- voglio modificare il nome di una categoria
- voglio trasformare la categoria [medicazioni]{"entity": "category", "role": "old"} in [intrattenimento]{"entity": "category", "role": "new"}
- modificare la categoria [volontariato]{"entity": "category", "role": "old"} in [sociale]{"entity": "category", "role": "new"}
- cambiare la categoria [università]{"entity": "category", "role": "old"} in [esami]{"entity": "category", "role": "new"}
- voglio convertire la categoria [casa]{"entity": "category", "role": "old"} in [genitori]{"entity": "category", "role": "new"}

## intent:add_category
- aggiungi [sport](category)
- viao, voglio mettere la categoria [genitori](category)
- voglio usare una nuova categoria [medico](category)
- voglio inserire una categoria
- nuova categoria da inserire: [finanze](category)
- inserisci [tempo libero](category)
- nuova categoria da aggiungere: [progetti](category)
- ciao, voglio aggiungere la categoria [commissioni](category)
- nuova categoria: [scuola](category)
- ciao, voglio inserire la categoria [progetti](category)
- voglio inserire la categoria [famiglia](category)

## intent:modify_activity_deadline
- per l'attività [prenotare l'aereo](activity) trasforma la scadenza in lunedì
- voglio modificare la scadenza dell'attività [partita con papà](activity) nella categoria [tempo libero](category) in domani alle 18:00
- nella categoria [salute fisica](category) sostituisci la scadenza dell'attività [fisioterapia](activity) dal 22 settembre al 25 settembre
- voglio modificare la deadline dell'attività [suonare la chitarra](activity) da domani alla prossima settimana
- altera la scadenza dell'attività [cena di Natale](activity) nella categoria [eventi](category) con lunedì
- modifica la scadenza dell'attività [cucinare per la famiglia](activity) nella categoria [casa](category) con domenica
- per l'attività [appunti](activity) nella categoria [scuola](category) trasformare la scadenza in lunedì
- per l'attività [pulire la mia camera da letto](activity) nella categoria [casa](category) trasformare la deadline in lunedì
- per l'attività [prenotare l'aereo](activity) nella categoria [vacanza](category) trasformare la deadline in lunedì
- modifica la scadenza di un'attività
- modifica la scadenza dell'attività [esame della patente](activity) da venerdì a lunedi
- voglio modificare la scadenza di un'attività

## intent:remove_category
- voglio togliere la categoria [vacanza](category)
- ciao, voglio togliere la categoria [progetti](category)
- categoria da cancellare: [finanze](category)
- voglio rimuovere la categoria [università](category)
- eliminare la vecchia categoria [pagamenti](category)
- rimuovi una categoria
- voglio eliminare la categoria [personale](category)
- ciao, voglio eliminare la categoria [genitori](category)
- voglio eliminare la categoria [professione](category)
- voglio rimuovere una categoria
- non voglio usare la categoria [sport](category)
- rimuovere la vecchia categoria [cura personale](category)

## intent:set_status_activity
- imposta [incompleto](activity_status) [andare al mare](activity) in [viaggio](category)
- ciao, imposta [completato](activity_status) [annaffia le piante](activity)
- imposta [completato](activity_status) [andare a correre](activity)
- metti [non terminata](activity_status) l'attività [acquistare una bicicletta](activity) in [negozio](category)
- imposta un'attività [incompleta](activity_status)
- imposta [incompleto](activity_status) [chiamare il capo](activity) nella categoria [lavoro](category)
- metti [completata](activity_status) l'attività [cena fuori](activity) nella categoria [svago](category)
- imposta come [completato](activity_status) [nuotare](activity)
- metti [terminata](activity_status) l'attività [acquistare una bicicletta](activity) in [negozio](category)
- ciao, imposta un'attività [completata](activity_status)
- metti come [non terminato](activity_status) [nuotare](activity) in [sport](category)
- voglio impostare [incompleta](activity_status) un'attività
- metti [non completata](activity_status) l'attività [cena fuori](activity) nella categoria [svago](category)
- voglio impostare [fatta](activity_status) un'attività in un elenco
- imposta come [non completato](activity_status) [nuotare](activity)
- imposta [non fatta](activity_status) [guardare la partita](activity) in [intrattenimento](category)

## intent:modify_activity_category
- cambia la categoria [progetti]{"entity": "category", "role": "old"} dell'attività [studiare](activity) in categoria [esami]{"entity": "category", "role": "new"}
- modificare la categoria [lavoro]{"entity": "category", "role": "old"} di [pranzo di lavoro](activity)
- per l'attività [pulire la casa](activity) nella categoria [quotidiano]{"entity": "category", "role": "old"} sostituire la categoria con [faccende domestiche]{"entity": "category", "role": "new"}
- per l'attività [andare al mercato](activity) aggiorna la categoria [impegni domestici]{"entity": "category", "role": "old"} in [spesa]{"entity": "category", "role": "new"}
- per l'attività [prenotare il treno](activity) aggiorna la categoria [vacanza]{"entity": "category", "role": "old"} in [imminente]{"entity": "category", "role": "new"}
- per l'attività [partecipare alla conferenza](activity) trasforma la categoria [lavoro]{"entity": "category", "role": "old"} in [cultura]{"entity": "category", "role": "new"}
- per l'attività [mangiare sano](activity) modifica la categoria [dieta]{"entity": "category", "role": "old"} in [stile di vita]{"entity": "category", "role": "new"}
- cambia la categoria [esami]{"entity": "category", "role": "old"} dell'attività [studiare](activity)
- modificare la categoria [tempo libero]{"entity": "category", "role": "old"} di [camminare all'aperto](activity) in [alimentazione]{"entity": "category", "role": "new"}
- converti la categoria [importante]{"entity": "category", "role": "old"} dell'attività [fare benzina](activity) con [urgente]{"entity": "category", "role": "new"}
- per l'attività [uscita con la famiglia](activity) trasforma la categoria [tempo libero]{"entity": "category", "role": "old"} in [svago]{"entity": "category", "role": "new"}
- per l'attività [pulire la casa](activity) nella categoria [quotidiano]{"entity": "category", "role": "old"} sostituisci la categoria con [faccende domestiche]{"entity": "category", "role": "new"}
- convertire la categoria [giornaliero/settimanale]{"entity": "category", "role": "old"} dell'attività [yoga](activity)
- sostituire la categoria [tempo libero]{"entity": "category", "role": "old"} dell'attività [fare i regali](activity) con la categoria [Natale]{"entity": "category", "role": "new"}
- per l'attività [disegnare](activity) nella categoria [arte]{"entity": "category", "role": "old"} sostituire la categoria
- voglio cambiare la categoria dell'attività [boxe](activity)
- sostituire la categoria [faccende domestiche]{"entity": "category", "role": "old"} dell'attività [preparare il pranzo](activity) con la categoria [casa]{"entity": "category", "role": "new"}

## intent:modify_activity_name
- voglio cambiare l'attività con nome [leggere un libro]{"entity": "activity", "role": "old"} con [leggere]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [modificare un video]{"entity": "activity", "role": "old"} con il nome [editare un video]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [ballo]{"entity": "activity", "role": "old"} con nome [canto]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [studio]{"entity": "activity", "role": "old"} nella categoria [università](category) con il nome [esame]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [camminare all'aperto]{"entity": "activity", "role": "old"} in [personale](category) con il nome [andare fuori con il cane]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [canto]{"entity": "activity", "role": "old"} con il nome [ballo]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [andare a nuotare]{"entity": "activity", "role": "old"} nella categoria [sport](category) con il nome [fare taekwondo]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [viaggiare per lavoro]{"entity": "activity", "role": "old"}  con il nome [fare una presentazione]{"entity": "activity", "role": "new"}
- modificare il nome dell'attività [yoga]{"entity": "activity", "role": "old"} con nome [pilates]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [aiutare la zia]{"entity": "activity", "role": "old"} nella categoria [famiglia](category) con [aiutare la sorella]{"entity": "activity", "role": "new"}
- modificare il nome dell'attività [pilates]{"entity": "activity", "role": "old"} con nome [yoga]{"entity": "activity", "role": "new"}
- per l'attività [andare a un concerto]{"entity": "activity", "role": "old"} modifica il nome con [andare al teatro]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [mostra d'arte]{"entity": "activity", "role": "old"} con nome [mostra di pittura]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [meditazione]{"entity": "activity", "role": "old"}  con il nome [chiesa]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [prendere le medicine]{"entity": "activity", "role": "old"}
- voglio cambiare il nome dell'attività [andare fuori con il cane]{"entity": "activity", "role": "old"} in [personale](category) con il nome [camminare all'aperto]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [mostra di pittura]{"entity": "activity", "role": "old"} con nome [mostra d'arte]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [prenotare il treno]{"entity": "activity", "role": "old"} con [prenotare l'aereo]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [chiamare il medico]{"entity": "activity", "role": "old"}
- modifica il nome dell'attività [revisione]{"entity": "activity", "role": "old"} nella categoria [consegna](category) con il nome [rileggere]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [pittura]{"entity": "activity", "role": "old"} con il nome [mostra d'arte]{"entity": "activity", "role": "new"}

## intent:remove_item
- cancellare [taekwondo](activity) nella categoria [hobby](category)
- cancella [chiamare l'elettricista](activity) nella categoria [guasti](category) alle 21:10
- cancellare [fare la spesa](activity) nella categoria [quotidiana](category)
- ciao, voglio cancellare un'attività nella categoria [blog](category) alle 17:30
- cancella [partecipare alla lezione](activity) nella categoria [università](category) alle 5:12
- voglio cancellare un'attività dall'elenco [computer](category)
- rimuovi [nuotare](activity) nella categoria [sport](category)
- elimina [fare i compiti](activity)
- cancella [andare a un incontro](activity) nella categoria [lavoro](category) alle 4:25
- elimina l'attività [allenarsi](activity) nella categoria [benessere](category)
- elimina [finire il report](activity) nella categoria [lavoro](category)
- voglio cancellare un'attività alle 11:00
- cancella [fare l'intervista](activity) nella categoria [società](category) alle 11:00
- elimina l'attività [inviare un'email](activity) nella categoria [scadenze](category)
- cancella [acquistare il pane](activity) nella categoria [cibo](category) alle 8:00
- ciao, voglio rimuovi un'attività dall'elenco [politica](category)
- ciao, voglio cancellare un'attività nella categoria [sociale](category) alle 14:50
- cancella [giardinaggio](activity) nella categoria [giardino](category) alle 5:12
- rimuovi [riordinare l'armadio](activity) nella categoria [faccende domestiche](category) alle 10:25
- elimina [studiare](activity)
- elimina l'attività [suonare il pianoforte](activity) nella categoria [musica](category)
- cancella [andare all'ufficio](activity) nella categoria [progetto](category) alle 16:00
- rimuovi [dipingere](activity) nella categoria [creatività](category) alle 9:40

## intent:presentation
- ciao sono [cami](name)
- [paola](name)
- [pierluigi](name)
- [tiziano](name)
- ciao sono [Luke](name)
- [chicca](name)
- [riccardino](name)
- [benedetto](name)
- [ermanno](name)
- ciao, sono [michele](name)
- [paolo](name)
- [sonia](name)
- [memo](name)
- [ale](name)
- [lilly](name)
- [chiara](name)
- voglio creare un account
- ciao, sono [camilla](name)
- ciao sono [alex](name)
- [liliana](name)
- [orlando](name)
- [cristina](name)
- crea un account
- [ercole](name)
- hi bot, il mio nome è [Gianluca](name)
- [marta](name)
- ciao, sono [ferdinando](name)
- [gizio](name)
- [erode](name)
- [molly](name)
- [clarissa](name)
- [giovanni](name)
- [giberto](name)
- [vincenzo](name)
- sono [simone](name)
- il mio nome è [matti](name)

## intent:inform
- lunedì
- [disegnare](activity)
- [giocare ai videogiochi](activity)
- prossima domenica
- [ritirare il pacco](activity)
- [pagare la multa](activity)
- [incontro genitori](activity)
- da oggi a domani
- [controllare il mercato](activity)
- [ritirare patente](activity)
- [serata libera](activity)
- [preparare la vasca](activity)
- dopodomani alle 15
- [fare attività fisica](activity)
- [viaggio in brasile](activity)
- [camminare](activity)
- [escursioni](category)
- [studiare](activity)
- [cinema](activity)
- [chiamare il medico](activity)
- [casa](category)
- [finanza](category)
- [cucinare per cena](activity)
- [fare fisioterapia](activity)
- [studio](activity)
- [fare una doccia](activity)
- [appuntamento romantico](activity)
- [conto in banca](category)
- 08/09/2025
- [desideri](category)
- [scrivere una lettera](activity)
- [università](category)
- [chiamare mia madre](activity)
- [universita](category)
- [lezione](activity)
- [vacanza](category)
- [prenotare le vacanze](activity)
- [pagare affitto](activity)
- [pranzo](activity)
- 10:00
- domani mattina
- [bambini](category)
- [mensile](category)
- [andare in barca](activity)

## intent:add_item
- inserisci l'attività [revisione](activity) in [impegni](category) alle 17:30
- nella categoria [benessere](category) aggiungere l'attività [andare dal parrucchiere](activity) alle 21:10
- inserire l'attività [e-mail](activity) nella categoria [consegne](category) alle 9:40
- ciao, inserisci [cena con i nonni](activity)
- ciao, inserisci [andare a correre](activity)
- vorrei aggiungere un'attività
- inserire l'attività [test](activity) nella categoria [compito](category) alle 17:30
- vorrei aggiungere un'attività alle 11:00
- inserisci [pulizie](activity) nella categoria [giornaliera](category)
- aggiungi [fare il bagaglio](activity) in [viaggio](category)
- aggiungi [fare pilates](activity)
- ciao, inserisci [scrivere](activity) nella categoria [hobby](category)
- inserisci l'attività [lavorare](activity)
- ciao, vorrei inserire un'attività nell'elenco [sociale](category) alle 3:29
- aggiungere [fare un ripasso di matematica](activity) nella categoria [lezioni](category) alle 16:30
- metti [fare shopping](activity)
- metti l'attività [piscina](activity)
- ciao, inserisci l'attività [fare un ripasso di scienze](activity) nella categoria [scuola](category)
- ciao, inserisci l'attività [caffè](activity) nella categoria [amicizia](category)
- ciao, inserisci l'attività [shampoo](activity) nella categoria [quotidiana](category)
- voglio aggiungere un'attività nell'elenco [necessari](category)
- ciao, voglio inserire un'attività [ripetizioni](activity) nella categoria [laurea](category)
- inserisci [andare all'ufficio postale](activity) in [essenziali](category) per domani
- voglio inserire un'attività nella mia lista
- inserisci l'attività [prenotare il pub](activity) in [amicizia](category) alle 19:41
- aggiungi l'attività [cantare](activity)
- aggiungi [compiti](activity) in categoria [scuola](category) alle 6:30
- ciao, vorrei aggiungere un'attività
- ciao, voglio aggiungere l'attività [inviare un'email](activity) all'elenco [comunicazione](category)
- ciao, voglio aggiungere un'attività nell'elenco [visite mediche](category)
- ciao, inserisci l'attività [e-commerce](activity) nella categoria [tecnologia](category)
- nella categoria [casa](category) inserisci la nuova attività [pulire il bagno](activity)
- ciao, inserisci [medicine](activity) nella categoria [settimanale](category)
- metti l'attività [fare un bagno](activity) in [cura personale](category)
- aggiungi [correre](activity) in [palestra](category) alle 12
- inserire [uscire](activity) alle 9:30
- ciao, voglio aggiungere un'attività nell'elenco [vacanze di pasqua](category)
- ciao, inserisci [leggere](activity)
- inserisci l'attività [nuotare](activity) nella categoria [sport](category)
- inserisci [organizzare l'armadio](activity) nella categoria [abbigliamento](category)
- vorrei creare una nuova attività
- vorrei mettere una nuova attività [studiare per l'esame](activity) alla categoria [università](category)
- ciao, vorrei aggiungere un'attività all'elenco [vita](category) alle 16:00
- inserire l'attività [suonare il violino](activity) nella categoria [musica](category) alle 17:30
- inserisci [portare fuori il cane](activity) alle 3:00
- ciao, voglio inserire una nuova attività [leggere un paper](activity) nell'elenco [ricerca](category)
- inserisci una nuova attività [giardinaggio](activity)
- crea l'attività [fare volontariato](activity) in [carità](category)
- inserisci l'attività [fare esercizi di routine](activity) nella categoria [sport](category)
- ciao, voglio creare un'attività per la lista [primavera](category)
- ciao, voglio creare l'attività [andare nel centro della città](activity) nell'elenco [commissioni](category)
- inserire [chiamare il medico](activity) nella categoria [salute](category) alle 22:20
- ciao, inserisci [powerpoint](activity)
- metti l'attività [acquistare un regalo di natale](activity) in categoria [imminente](category) alle 9:40
- vorrei inserire un'attività alla categoria [faccende](category)
- inserire [festa](activity) nella categoria [intrattenimento](category) alle 10:25

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
