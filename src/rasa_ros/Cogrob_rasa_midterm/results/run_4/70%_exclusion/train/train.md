## intent:bot_challenge
- Sto parlando con un bot?
- tu chi sei?

## intent:goodbye
- ci si vede
- ci vediamo in giro

## intent:help
- Ho bisogno di assistenza
- Ho bisogno di aiuto

## intent:greet
- buona sera
- Buongiorno
- Salve

## intent:affirm
- indubbiamente
- yes

## intent:mood_great
- Estremamente buono
- Super entusiasta
- Sono grande

## intent:ask_name
- chi sono?
- puoi pronuniciare il mio nome?
- sai chi sono?

## intent:mood_unhappy
- Sono così triste
- Estremamente triste
- Sono triste

## intent:deny
- non voglio
- mai
- no
- no grazie

## intent:clean_activities
- elimina le attività
- per favore, rimuovi tutte le attività completate
- elimina tutte le attività

## intent:view_categories
- quali sono le mie categorie?
- mostrami tutte le categorie create
- mostrami le mie categorie
- posso vedere le mie categorie?

## intent:remind_me_of
- voglio impostare un promemoria
- aiutami a non dimenticare l'attività [rivedere la relazione](activity) nella categoria [consegna progetto](category) per domani
- imposta un promemoria
- non posso dimenticare di [andare dal veterinario](activity) alle 19:00
- aiutami a ricordare l'attività [compleanno](activity) il 12/18/2022
- aiutami a non dimenticare l'attività [studio](activity) nella categoria [scuola](category) per domani
- non posso dimenticare di fare l'attività [parlare con il professore](activity) nella categoria [progetto](category) per domenica prossima
- non posso dimenticare di fare l'attività [boxe](activity) nella categoria [sport](category) il prossimo lunedì
- ricordami [l'esame](activity) domani mattina

## intent:view_activities
- mostra le mie attività [non sviluppate](activity_status)
- mostra attività
- voglio vedere tutte le mie attività
- quali sono le mie attività create per domenica?
- fammi vedere le mie attività per martedì pomeriggio
- mostra le attività nella categoria [progetti](category)
- mostra la mia attività [non fatta](activity_status) nella categoria [impegni](category)
- mostra le attività [completate](activity_status)
- mostra le attività nella categoria [palestra](category)

## intent:modify_category
- modificare la categoria [volontariato]{"entity": "category", "role": "old"} in [sociale]{"entity": "category", "role": "new"}
- per favore, variare la categoria [finanza]{"entity": "category", "role": "old"} nella categoria [banca]{"entity": "category", "role": "new"}
- alterare la categoria [sociale]{"entity": "category", "role": "old"} in [volontariato]{"entity": "category", "role": "new"}
- sostituire la categoria [banca]{"entity": "category", "role": "old"} con [vacanza]{"entity": "category", "role": "new"}
- sostituire la categoria [esami]{"entity": "category", "role": "old"} in [università]{"entity": "category", "role": "new"}
- cambiare il nome della categoria [divertimento]{"entity": "category", "role": "old"} con il nome [cura personale]{"entity": "category", "role": "new"}
- voglio trasformare la categoria [scadenze]{"entity": "category", "role": "old"} in [commissioni]{"entity": "category", "role": "new"}
- voglio trasformare la categoria [medicazioni]{"entity": "category", "role": "old"} in [intrattenimento]{"entity": "category", "role": "new"}
- voglio sostituire la categoria [impegni]{"entity": "category", "role": "old"} con la categoria [lavoro]{"entity": "category", "role": "new"}
- trasformare la categoria [vacanza]{"entity": "category", "role": "old"} in [banca]{"entity": "category", "role": "new"}

## intent:add_category
- inserisci [tempo libero](category)
- aggiungi [sport](category) categoria
- nuova categoria: [scuola](category)
- aggiungi [sport](category)
- voglio aggiungere la categoria [università](category)
- voglio usare una nuova categoria [medico](category)
- voglio usare una nuova categoria [sport](category)
- crea una nuova categoria
- voglio aggiungere una categoria
- voglio aggiungere la categoria [stile di vita](category)
- ciao, inserisci la seguente categoria [spesa](category)
- ciao, voglio inserire la categoria [progetti](category)
- voglio mettere una nuova categoria [vacanza](category)

## intent:modify_activity_deadline
- voglio cambiare il termine dell'attività [chiamare mia madre](activity) al 27 settembre 1998
- per l'attività [bollette](activity) nella categoria [finanza](category) modificare la deadline dal 4 novembre al 22 ottobre 1922
- modifica la deadline dell'attività [cena con i nonni](activity) dal 20 febbraio a 26 febbraio
- modifica la scadenza di un'attività
- sostituisci il termine dell'attività [mostra d'arte](activity) da lunedì a venerdì
- altera la scadenza dell'attività [viaggio con la mamma](activity) nella categoria [vacanza](category) dal 07/11/2022 a domenica
- nella categoria [salute fisica](category) sostituisci la scadenza dell'attività [fisioterapia](activity) dal 22 settembre al 25 settembre
- altera la deadline dell'attività [pagare il supermercato](activity) nella categoria [pagamenti](category) in domenica
- modifica il termine dell'attività [revisione del progetto](activity) nella categoria [università](category)
- cambia la scadenza dell'attività [raccogliere fondi](activity) nella categoria [volontariato](category) a lunedì
- nella categoria [creatività](category) sostituisci la deadline dell'attività [disegnare](activity) da 22 settembre a 25 settembre
- cambia la scadenza dell'attività [raccogliere fondi](activity)
- voglio modificare la deadline dell'attività [suonare la chitarra](activity) nella categoria [musica](category) in domani alle 18:00
- per l'attività [prenotare l'aereo](activity) nella categoria [vacanza](category) trasformare la deadline in lunedì

## intent:remove_category
- ciao, voglio rimuovere la categoria [famiglia](category)
- eliminare la categoria [relazioni](category)
- voglio eliminare la categoria [imminente](category)
- ciao, voglio togliere la categoria [lavoro](category)
- voglio cancellare la categoria [università](category)
- ciao, per favore annulla la seguente categoria [divertimento](category)
- categoria da togliere: [cura personale](category)
- la categoria da eliminare è [casa](category)
- rimuovere la categoria [ingegneria](category)
- eliminare la vecchia categoria [pagamenti](category)
- ciao, per favore elimina la seguente categoria [medica](category)
- categoria da cestinare: [commissioni](category)
- elimina una categoria
- voglio eliminare la categoria [personale](category)
- rimuovere la vecchia categoria [cura personale](category)

## intent:set_status_activity
- imposta [incompleto](activity_status) [ripetere la presentazione](activity) nella categoria [progetti](category)
- poni come [non terminata](activity_status) [riposare](activity) in [salute](category)
- metti [terminata](activity_status) l'attività [acquistare una bicicletta](activity) in [negozio](category)
- imposta [non fatta](activity_status) [guardare la partita](activity) in [intrattenimento](category)
- imposta [incompleta](activity_status) [spegni il forno](activity) in [casa](category)
- voglio impostare [non completata](activity_status) l'attività [postare selfie](activity) in [sociale](category)
- ciao, metti [incompiuta](activity_status) l'attività [jogging](activity) in [salute fisica](category)
- ciao, voglio porre come [eseguito](activity_status) [ripetizioni](activity) nella categoria [laurea](category)
- imposta [completato](activity_status) [andare al mare](activity) in [viaggio](category)
- metti come [non terminato](activity_status) [nuotare](activity) in [sport](category)
- metti [non terminata](activity_status) l'attività [acquistare una bicicletta](activity) in [negozio](category)
- imposta come [fatta](activity_status) [leggere](activity)
- imposta un'attività [incompleta](activity_status)
- metti [fatta](activity_status) [guardare la partita](activity) in [intrattenimento](category)
- imposta [non fatto](activity_status) l'attività [cucina la pizza](activity) in [casa](category)
- imposta [terminata](activity_status) [chiama mia madre](activity) in [settimanale](category)
- imposta [non terminato](activity_status) [cena con gli amici](activity)
- ciao, poni [non fatto](activity_status) [pulisci il bagno](activity) in [casa](category)
- imposta [fatto](activity_status) l'attività [cucina la pizza](activity) in [casa](category)

## intent:modify_activity_category
- converti la categoria [urgente]{"entity": "category", "role": "old"} dell'attività [fare benzina](activity)
- per l'attività [pulire la casa](activity) nella categoria [quotidiano]{"entity": "category", "role": "old"} sostituire la categoria con [faccende domestiche]{"entity": "category", "role": "new"}
- per l'attività [partecipare alla conferenza](activity) trasforma la categoria [cultura]{"entity": "category", "role": "old"} in [lavoro]{"entity": "category", "role": "new"}
- voglio cambiare la categoria [desideri]{"entity": "category", "role": "old"} dell'attività [prenotare l'hotel](activity) in [viaggio]{"entity": "category", "role": "new"}
- sostituisci la categoria [faccende domestiche]{"entity": "category", "role": "old"} dell'attività [preparare la colazione](activity)
- per l'attività [riposare](activity) modificare la categoria [stile di vita]{"entity": "category", "role": "old"} in [dieta]{"entity": "category", "role": "new"}
- modificare la categoria [lavoro]{"entity": "category", "role": "old"} di [pranzo di lavoro](activity)
- modificare la categoria [lavoro]{"entity": "category", "role": "old"} dell'attività [pranzo di lavoro](activity) in [pranzo]{"entity": "category", "role": "new"}
- per l'attività [dormire](activity) modifica la categoria [riposo]{"entity": "category", "role": "old"} in [salute]{"entity": "category", "role": "new"}
- per l'attività [dormire](activity) modifica la categoria [salute]{"entity": "category", "role": "old"} in [riposo]{"entity": "category", "role": "new"}
- per l'attività [pulire la casa](activity) nella categoria [quotidiano]{"entity": "category", "role": "old"} sostituisci la categoria con [faccende domestiche]{"entity": "category", "role": "new"}
- per l'attività [guardare il match](activity) trasformare la categoria [famiglia]{"entity": "category", "role": "old"} in [tempo libero]{"entity": "category", "role": "new"}
- modifica la categoria [dieta]{"entity": "category", "role": "old"} di [camminare all'aperto](activity) in [tempo libero]{"entity": "category", "role": "new"}
- per l'attività [partecipare alla conferenza](activity) trasforma la categoria [lavoro]{"entity": "category", "role": "old"} in [cultura]{"entity": "category", "role": "new"}
- per l'attività [preparare i biscotti](activity) modifica la categoria [casa]{"entity": "category", "role": "old"} in [dieta]{"entity": "category", "role": "new"}
- per l'attività [prenotare il treno](activity) aggiorna la categoria [vacanza]{"entity": "category", "role": "old"} in [imminente]{"entity": "category", "role": "new"}
- sostituisci la categoria [famiglia]{"entity": "category", "role": "old"} dell'attività [preparare la colazione](activity) con la categoria [faccende domestiche]{"entity": "category", "role": "new"}
- per l'attività [giocare a pallone](activity) trasforma la categoria [sport]{"entity": "category", "role": "old"} in [svago]{"entity": "category", "role": "new"}
- per l'attività [ritirare il pacco](activity) aggiornare la categoria [commissioni]{"entity": "category", "role": "old"} in [imminente]{"entity": "category", "role": "new"}
- trasforma la categoria [università]{"entity": "category", "role": "old"} dell'attività [studiare](activity) in categoria [progetti]{"entity": "category", "role": "new"}
- converti la categoria [cura della persona]{"entity": "category", "role": "old"} dell'attività [correre](activity) con [sport]{"entity": "category", "role": "new"}

## intent:modify_activity_name
- per l'attività [andare a un concerto]{"entity": "activity", "role": "old"} modifica il nome con [andare al teatro]{"entity": "activity", "role": "new"}
- per l'attività [parrucchiere]{"entity": "activity", "role": "old"} nella categoria [cura personale](category) modifica il nome con [yoga]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [studio]{"entity": "activity", "role": "old"} nella categoria [università](category) con il nome [esame]{"entity": "activity", "role": "new"}
- per l'attività [completare il powerpoint]{"entity": "activity", "role": "old"} modifica il nome con [completare la relazione]{"entity": "activity", "role": "new"}
- nella categoria [eventi](category) cambia il nome dell'attività [tagliare i capelli]{"entity": "activity", "role": "old"}
- per l'attività [suonare la chitarra]{"entity": "activity", "role": "old"} nella categoria [tempo libero](category) modifica il nome con [andare a giocare a calcio]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [revisione]{"entity": "activity", "role": "old"} nella categoria [consegna](category) con il nome [rileggere]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [aiutare la sorella]{"entity": "activity", "role": "old"} nella categoria [famiglia](category) con [aiutare la zia]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [uscire con mia madre]{"entity": "activity", "role": "old"} in [famiglia](category)
- cambia il nome dell'attività [viaggiare per lavoro]{"entity": "activity", "role": "old"}  con il nome [fare una presentazione]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [andare dal dottore]{"entity": "activity", "role": "old"} con il nome [andare dal dentista]{"entity": "activity", "role": "new"}
- nella categoria [eventi](category) cambia il nome dell'attività [tagliare i capelli]{"entity": "activity", "role": "old"}  con il nome [andare dal parrucchiere]{"entity": "activity", "role": "new"}
- nella categoria [università](category) cambiare il nome dell'attività [studio]{"entity": "activity", "role": "old"}  con nome [esame]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [ballo]{"entity": "activity", "role": "old"} con nome [canto]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [pittura]{"entity": "activity", "role": "old"} con il nome [mostra d'arte]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [nuoto]{"entity": "activity", "role": "old"} nella categoria [tempo libero](category)
- voglio cambiare il nome dell'attività [esame]{"entity": "activity", "role": "old"} nella categoria [università](category) con il nome [studio]{"entity": "activity", "role": "new"}
- sostituisci il nome dell'attività [imparare l'inglese]{"entity": "activity", "role": "old"}  con il nome [camminare]{"entity": "activity", "role": "new"}
- cambiare il nome dell'attività [meditazione]{"entity": "activity", "role": "old"}  con nome [chiesa]{"entity": "activity", "role": "new"}
- per l'attività [leggere un giornale]{"entity": "activity", "role": "old"} trasforma il nome con [scrivere un articolo]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [organizzare raccolta fondi]{"entity": "activity", "role": "old"} nella categoria [volontariato](category) con [fare beneficenza]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [nuoto]{"entity": "activity", "role": "old"} nella categoria [sport](category) con il nome [boxe]{"entity": "activity", "role": "new"}
- per l'attività [andare a teatro]{"entity": "activity", "role": "old"} trasforma il nome con [andare al cinema]{"entity": "activity", "role": "new"}
- modificare il nome dell'attività [revisione]{"entity": "activity", "role": "old"} nella categoria [report](category) con nome [rileggere]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con nome [organizzare raccolta fondi]{"entity": "activity", "role": "old"} nella categoria [volontariato](category)

## intent:remove_item
- cancellare l'attività [fare il powerpoint](activity) nella categoria [imminente](category)
- cancella [giardinaggio](activity) nella categoria [giardino](category) alle 5:12
- elimina l'attività [andare a nuotare](activity) nella categoria [sport](category)
- rimuovi [andare al cinema](activity) alle 13:00
- rimuovi [giocare a basket](activity) alle 3:00
- elimina l'attività [giocare](activity) nella categoria [intrattenimento](category)
- elimina [shampoo](activity) nella categoria [quotidiana](category)
- elimina l'attività [suonare il pianoforte](activity) nella categoria [musica](category)
- rimuovi l'attività [leggere il giornale](activity) nella categoria [cultura](category)
- voglio cancellare un'attività nella categoria [commissioni](category) alle 19:00
- cancella [unghie](activity) nella categoria [estetica](category) alle 9:40
- voglio cancellare un'attività nella categoria [negozio](category) alle 7:00
- cancellare l'attività [fare jogging](activity) nella categoria [cura personale](category)
- elimina [fare i compiti](activity)
- rimuovi l'attività [leggere](activity) nella categoria [cultura](category)
- elimina l'attività [psicologo](activity) nella categoria [mente](category)
- elimina [imparare lo spagnolo](activity) nella categoria [lingue](category)
- voglio cancellare un'attività dall'elenco [computer](category)
- voglio cancellare un'attività alle 11:00
- ciao, voglio eliminare un'attività dall'elenco [genitori](category)
- cancella [camminare](activity) nella categoria [salute personale](category) alle 6:30
- ciao, voglio cancellare un'attività nella categoria [sociale](category) alle 14:50
- ciao, voglio cancellare un'attività nella categoria [cura](category) alle 3:29
- ciao, voglio eliminare un'attività dall'elenco [teatro](category)
- cancella [aiutare mia madre](activity) alle 01:45
- cancella [fare l'intervista](activity) nella categoria [società](category) alle 11:00

## intent:presentation
- [filomena](name)
- hi bot, il mio nome è [Gianluca](name)
- nuovo account
- sono [giorgia](name)
- [sonia](name)
- [christian](name)
- [salvatore](name)
- [diodato](name)
- sono [giorgino](name)
- [nerone](name)
- [federico](name)
- sono [giorgio](name)
- ciao, sono [camilla](name)
- il mio nome è [matti](name)
- [flaviano](name)
- [anacleto](name)
- ciao, sono [ferdinando](name)
- voglio creare un account
- [giovanni](name)
- il mio nome [Dario](name)
- [fabiano](name)
- sono [Nando](name)
- [ursola](name)
- [gisel](name)
- crea un utente
- [ernesto](name)
- [michi](name)
- [marta](name)
- [elga](name)
- ciao sono [Luke](name)
- voglio registrarmi
- [venturino](name)
- [edvige](name)
- account
- [cathrine](name)
- iscrizione
- [speranza](name)
- [monia](name)
- [fabio](name)
- [orlando](name)
- [astra](name)
- [isa](name)
- [alberigo](name)
- sono [giulio](name)

## intent:inform
- [medico](category)
- [viaggiare](activity)
- [escursione](activity)
- [escursioni](category)
- [azienda](category)
- [cuocere biscotti](activity)
- [zaino](category)
- [ricerca](category)
- [quotidiano](category)
- [spegnere il gas](activity)
- [desideri](category)
- [tempo libero](category)
- prossima domenica
- [leggere](activity)
- [armadietto](category)
- [bambini](category)
- [prendere appunti](activity)
- [inviare un'e-mail al capo](activity)
- [fare meeting](activity)
- [famiglia](category)
- [frigo](category)
- [allenamenti](category)
- 09/12/2030 alle 13:00
- [lista](category)
- [analisi](activity)
- [vacanze](category)
- [cinema](activity)
- [giocare](activity)
- [saldare prestito](activity)
- [nuotare](activity)
- [fare attività fisica](activity)
- [affitto](activity)
- [cucinare per cena](activity)
- [chiamare il medico](activity)
- [uscita con la famiglia](activity)
- [multa](activity)
- [investire](activity)
- [corda](activity)
- [riparazioni](category)
- [chiamare mia madre](activity)
- [dormire](activity)
- [salute](category)
- [fare la valigia](activity)
- [guardare un film](activity)
- [fare fisioterapia](activity)
- [eventi](category)
- [laboratorio](category)
- [compiti vacanze](category)
- [pagare le bollette](activity)
- dopodomani alle 15
- [suonare](activity)
- [andare al mare](activity)
- 14 settembre 2022

## intent:add_item
- ciao, voglio aggiungere un'attività alla categoria [educazione](category)
- inserisci l'attività [lavorare](activity)
- ciao, inserisci [partecipare alla lezione](activity) nella categoria [corsi](category)
- aggiungere [cucinare per cena](activity) alle 20:45
- voglio creare un'attività nella mia lista
- inserisci [fare una passeggiata](activity) in [quotidiano](category)
- ciao, vorrei mettere un'attività nell'elenco [faccende](category) alle 7:00
- aggiungi l'attività [nuotare](activity)
- ciao, voglio inserire un'attività [judo](activity) nella categoria [palestra](category)
- ciao, inserisci [cena con i nonni](activity)
- ciao, vorrei inserire un'attività nell'elenco [stile di vita](category) alle 14:50
- ciao, inserisci [andare a correre](activity)
- aggiungi [fare il bagaglio](activity) in [viaggio](category)
- ciao, voglio aggiungere l'attività [powerpoint](activity) all'elenco [programmi](category)
- metti l'attività [ricerca](activity) in [aggiornamenti](category) alle 18:30
- ciao, vorrei inserire un'attività nell'elenco [marketing](category) alle 17:30
- vorrei creare un'attività nella categoria [pianificazioni](category) alle 6:30
- aggiungi l'attività [inviare il codice](activity) in [impegni](category)
- inserire [festa](activity) nella categoria [intrattenimento](category) alle 10:25
- vorrei inserire un'attività [pagamenti](activity) alla categoria [finanza](category)
- inserisci l'attività [fare la spesa](activity) in [quotidiano](category)
- aggiungi [fare selfie](activity) alle 01:45
- inserire [prenotare le vacanze](activity) nella categoria [vacanza](category) alle 4:25
- ciao, inserisci [leggere](activity)
- ciao, vorrei mettere un'attività nella mia lista alle 12:37
- inserire l'attività [bollette](activity) nella categoria [importante](category) alle 11:00
- ciao, vorrei aggiungere un'attività all'elenco [vita](category) alle 16:00
- aggiungi [chiamare mia madre](activity) alle 13:00
- ciao, inserisci [powerpoint](activity)
- vorrei mettere una nuova attività [studiare per l'esame](activity) alla categoria [università](category)
- aggiungi [correre](activity)
- ciao, inserisci [guardare lo spettacolo](activity) nella categoria [interesse](category)
- vorrei mettere un'attività [esercizi](activity) in [sport](category)
- inserisci [il compleanno del mio amico](activity) in [eventi](category) alle 14:50
- aggiungi [boxe](activity) nella categoria [sport](category)
- aggiungi [andare dai genitori](activity) in [famiglia](category) alle 20:00
- metti attività [pizza](activity) in [amici](category) alle 7:00
- ciao, voglio inserire un'attività nella lista [urgente](category)
- ciao, aggiungi [psicologo](activity) nella categoria [mente](category)
- inserire l'attività [preparare lo zaino](activity) nella categoria [organizzazione](category) alle 18:30
- aggiungi [fare le pulizie](activity) in [settimanale](category)
- metti [fare shopping](activity)
- voglio aggiungere un'attività nell'elenco [necessari](category)
- inserisci [pulizie](activity) nella categoria [giornaliera](category)
- inserisci l'attività [volontariato](activity) in categoria [beneficenza](category) alle 13:39
- ciao, vorrei inserire un'attività nella mia lista alle 18:14
- vorrei inserire un'attività in un elenco
- ciao, inserisci l'attività [giocare a carte](activity) nella categoria [divertimento](category)
- inserisci [prendere la medicina](activity) in categoria [salute](category) alle 20:30
- voglio aggiungere un'attività nell'elenco [leadership](category)
- inserisci [giocare](activity) nella categoria [divertimento](category)
- aggiungi [correre](activity) in [palestra](category) alle 12
- inserire [studiare per interrogazione](activity) nella categoria [scuola](category) alle 19:00
- inserisci attività [apportare correzioni](activity) in categoria [lavoro](category) alle 13:39
- ciao, inserisci l'attività [riparare l'auto](activity) nella categoria [impegni](category)
- inserisci [organizzare l'armadio](activity) nella categoria [abbigliamento](category)
- inserisci [leggere un libro](activity) nella categoria [cultura](category)
- inserisci [andare all'ufficio postale](activity) in [essenziali](category) per domani
- creare l'attività [dentista](activity) nella categoria [mensile](category) alle 20:00
- ciao, inserisci [scrittura](activity) nella categoria [hobby](category)
- inserisci l'attività [giocare a basket](activity)
- ciao, voglio aggiungere un'attività [farmacia](activity) nella categoria [salute](category)
- voglio inserire un'attività nella categoria [ricreazione](category) alle 16:30
- ciao, vorrei inserire un'attività nella categoria [dieta](category) alle 14:50
- ciao, aggiungi l'attività [e-reading](activity) nella categoria [università](category)
- ciao, inserisci [scrivere](activity) nella categoria [hobby](category)
- ciao, voglio inserire un'attività nell'elenco [priorità](category)

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
