## intent:bot_challenge
- Sei un bot?

## intent:goodbye
- ci vediamo più tardi
- buona giornata

## intent:help
- Cosa facciamo adesso?
- Per favore aiutami

## intent:greet
- Buon pomeriggio
- buon giorno

## intent:affirm
- sisi
- affermativo

## intent:mood_great
- Estremamente buono
- Così buono
- Sono stupefacente

## intent:mood_unhappy
- La mia giornata è stata orribile
- Non bene

## intent:ask_name
- sapresti dirmi chi sono?
- puoi pronuniciare il mio nome?
- dimmi il mio nome

## intent:deny
- no grazie
- non credo
- assolutamente no

## intent:clean_activities
- rimuovi tutte le attività
- cancella le mie attività
- per favore, elimina le attività

## intent:view_categories
- posso vedere le mie categorie?
- fammi vedere tutte le mie categorie
- quali sono le categorie inserite?

## intent:remind_me_of
- non posso dimenticare di [fare gli esercizi](activity) alle 19:00
- ricordami di [prendere la pillola](activity) in [cura personale](category)
- aiutami a non dimenticare l'attività [ripassare matematica](activity) nella categoria [scuola](category) per domani
- aiutami a ricordare un'attività
- ricordami [cena](activity)
- aiutami a non dimenticare l'attività [studio](activity) nella categoria [scuola](category) per domani
- imposta un promemoria

## intent:view_activities
- quali sono le mie attività create per domenica?
- mostrami le mie attività [fatte](activity_status)
- voglio vedere tutte le mie attività aggiunte
- fammi vedere le attività per mercoledì sera
- quali sono le mie attività [fatte](activity_status)?
- fammi vedere le mie attività per martedì pomeriggio
- mostra tutte le mie attività [sviluppate](activity_status) nella categoria [mensile](category)
- mostrami attività [eseguite](activity_status) nella categoria [scuola](category)

## intent:modify_category
- cambiare la categoria [università]{"entity": "category", "role": "old"} con la categoria [cura della persona]{"entity": "category", "role": "new"}
- trasformare la categoria [palestra]{"entity": "category", "role": "old"} in [tempo libero]{"entity": "category", "role": "new"}
- voglio modificare il nome di una categoria
- convertire la categoria [sport]{"entity": "category", "role": "old"} in [personale]{"entity": "category", "role": "new"}
- sostituire la categoria [estate]{"entity": "category", "role": "old"} in [annuale]{"entity": "category", "role": "new"}
- per favore, cambiare la categoria [cura della persona]{"entity": "category", "role": "old"} con la categoria [università]{"entity": "category", "role": "new"}
- sostituire la categoria [faccende domestiche]{"entity": "category", "role": "old"} con [benessere]{"entity": "category", "role": "new"}
- per favore, variare la categoria [finanza]{"entity": "category", "role": "old"} nella categoria [banca]{"entity": "category", "role": "new"}

## intent:add_category
- aggiungi [sport](category) categoria
- ciao, voglio inserire la categoria [quotidiana](category)
- inserisci la categoria [farmaci](category)
- voglio usare una nuova categoria [sport](category)
- categoria: [bollette](category)
- viao, voglio mettere la categoria [genitori](category)
- nuova categoria da aggiungere: [progetti](category)
- metti [sport](category)
- voglio inserire la categoria [professione](category)
- aggiungi la categoria [studio](category)
- ciao, inserisci la seguente [divertimento](category)

## intent:modify_activity_deadline
- altera la scadenza dell'attività [cena di Natale](activity) nella categoria [eventi](category)
- altera la deadline dell'attività [andare al mare](activity) nella categoria [tempo libero](category) in domenica
- voglio cambiare la scadenza dell'attività [andare dal parrucchiere](activity) nella categoria [personale](category) da 25 settembre a 27 settembre 1998
- voglio cambiare il termine dell'attività [uscire con gli amici](activity) nella categoria [eventi](category) con 27 settembre 1998
- modifica la deadline dell'attività [cena con i nonni](activity) dal 20 febbraio a 26 febbraio
- alterare la scadenza
- per l'attività [nuotare](activity) modifica la scadenza al 22 luglio 1922
- altera la scadenza dell'attività [viaggio con la mamma](activity) nella categoria [vacanza](category) dal 07/11/2022 a domenica
- modifica il termine dell'attività [revisione del progetto](activity) nella categoria [università](category)
- per l'attività [studiare in biblioteca](activity) nella categoria [università](category) modifica il termine nel 22 ottobre 1922
- modifica la scadenza dell'attività [esame della patente](activity) da venerdì a lunedi
- altera la scadenza dell'attività [uscire con gli amici](activity) nella categoria [svago](category) a domenica

## intent:remove_category
- rimuovere la categoria [visite mediche](category)
- ciao, voglio rimuovere la categoria [salute personale](category)
- ciao, voglio togliere la categoria [lavoro](category)
- ciao, voglio rimuovere la categoria [desideri](category)
- ciao, voglio togliere la categoria [progetti](category)
- voglio togliere la categoria [vacanza](category)
- voglio cancellare una categoria
- voglio rimuovere la categoria [università](category)
- ciao, voglio eliminare la categoria [genitori](category)
- ciao, per favore elimina la seguente categoria [medica](category)
- non voglio usare la categoria [eventi](category)
- non voglio usare la categoria [medico](category)

## intent:set_status_activity
- imposta [fatta](activity_status) l'attività [vai in farmacia](activity) nella categoria [benessere](category)
- metti come [finita](activity_status) [alzati](activity) in [quotidiano](category)
- imposta come [sviluppata](activity_status) [giocare a carte](activity)
- imposta [non completato](activity_status) [pulire la cucina](activity) nella categoria [casa](category)
- ciao, imposta [incompleto](activity_status) l'attività [aiuta mio nonno](activity) nella categoria [genitori](category)
- imposta [completato](activity_status) [spegni il forno](activity) in [casa](category)
- imposta [incompleto](activity_status) [chiamare il capo](activity) nella categoria [lavoro](category)
- imposta [non fatto](activity_status) [powerpoint](activity) nella categoria [programmi](category)
- voglio impostare [non fatta](activity_status) un'attività in un elenco
- metti [non completata](activity_status) l'attività [cena fuori](activity) nella categoria [svago](category)
- imposta [non fatta](activity_status) [guardare la partita](activity) in [intrattenimento](category)
- imposta un'attività [incompleta](activity_status)
- imposta [incompiuta](activity_status) [andare a correre](activity)
- ciao, voglio porre come [non eseguita](activity_status) [ripetizioni](activity) nella categoria [laurea](category)
- ciao, metti [incompiuta](activity_status) l'attività [jogging](activity) in [salute fisica](category)
- poni come [non terminata](activity_status) [riposare](activity) in [salute](category)

## intent:modify_activity_category
- sostituire la categoria [tempo libero]{"entity": "category", "role": "old"} dell'attività [fare i regali](activity) con la categoria [Natale]{"entity": "category", "role": "new"}
- per l'attività [preparare i biscotti](activity) modifica la categoria [dieta]{"entity": "category", "role": "old"} in [casa]{"entity": "category", "role": "new"}
- per l'attività [riposare](activity) modificare la categoria [stile di vita]{"entity": "category", "role": "old"} in [dieta]{"entity": "category", "role": "new"}
- per l'attività [prenotare il treno](activity) aggiorna la categoria [vacanza]{"entity": "category", "role": "old"} in [imminente]{"entity": "category", "role": "new"}
- per l'attività [andare in farmacia](activity) modificare la categoria [salute personale]{"entity": "category", "role": "old"} in [salute]{"entity": "category", "role": "new"}
- per l'attività [uscita con la famiglia](activity) trasforma la categoria [svago]{"entity": "category", "role": "old"} in [tempo libero]{"entity": "category", "role": "new"}
- converti la categoria [cura della persona]{"entity": "category", "role": "old"} dell'attività [correre](activity) con [sport]{"entity": "category", "role": "new"}
- converti la categoria [importante]{"entity": "category", "role": "old"} dell'attività [fare benzina](activity) con [urgente]{"entity": "category", "role": "new"}
- modificare la categoria [alimentazione]{"entity": "category", "role": "old"} di [camminare all'aperto](activity) in [tempo libero]{"entity": "category", "role": "new"}
- trasforma la categoria [studio]{"entity": "category", "role": "old"} dell'attività [preparare l'esame](activity) in categoria [università]{"entity": "category", "role": "new"}
- per l'attività [pulire la casa](activity) nella categoria [faccende domestiche]{"entity": "category", "role": "old"} sostituisci la categoria con [quotidiano]{"entity": "category", "role": "new"}
- modificare la categoria [tempo libero]{"entity": "category", "role": "old"} di [camminare all'aperto](activity) in [alimentazione]{"entity": "category", "role": "new"}
- sostituire la categoria [casa]{"entity": "category", "role": "old"} dell'attività [preparare il pranzo](activity) con la categoria [faccende domestiche]{"entity": "category", "role": "new"}
- sostituisci la categoria [tempo libero]{"entity": "category", "role": "old"} dell'attività [comprare i regali](activity) con la categoria [Natale]{"entity": "category", "role": "new"}
- cambia la categoria [esami]{"entity": "category", "role": "old"} dell'attività [studiare](activity)
- per l'attività [andare al mercato](activity) aggiorna la categoria [spesa]{"entity": "category", "role": "old"} in [impegni domestici]{"entity": "category", "role": "new"}
- sostituisci la categoria [Natale]{"entity": "category", "role": "old"} dell'attività [comprare i regali](activity) con la categoria [tempo libero]{"entity": "category", "role": "new"}

## intent:modify_activity_name
- voglio cambiare l'attività con il nome [prenotare il treno]{"entity": "activity", "role": "old"} con [prenotare l'aereo]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [portare fuori il cane]{"entity": "activity", "role": "old"} in [quotidiana](category)
- per l'attività [parrucchiere]{"entity": "activity", "role": "old"} nella categoria [cura personale](category) modifica il nome con [yoga]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [mostra d'arte]{"entity": "activity", "role": "old"} con il nome [pittura]{"entity": "activity", "role": "new"}
- nella categoria [università](category) cambiare il nome dell'attività [studio]{"entity": "activity", "role": "old"}  con nome [esame]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [andare a nuotare]{"entity": "activity", "role": "old"} con [andare al parco]{"entity": "activity", "role": "new"}
- nella categoria [amicizia](category) sostituisci il nome dell'attività [andare al pub]{"entity": "activity", "role": "old"}  con il nome [andare a mangiare una pizza]{"entity": "activity", "role": "new"}
- per l'attività [andare a giocare a calcio]{"entity": "activity", "role": "old"} nella categoria [tempo libero](category) modifica il nome con [suonare la chitarra]{"entity": "activity", "role": "new"}
- nella categoria [scuola](category) sostituire il nome dell'attività [interrogazione di latino]{"entity": "activity", "role": "old"}  con nome [compito di latino]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con nome [leggere un libro]{"entity": "activity", "role": "old"} con [leggere]{"entity": "activity", "role": "new"}
- modificare il nome dell'attività [revisione]{"entity": "activity", "role": "old"} nella categoria [report](category) con nome [rileggere]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [andare in montagna]{"entity": "activity", "role": "old"} nella categoria [vacanza](category) con [andare a sciare]{"entity": "activity", "role": "new"}
- sostituisci il nome dell'attività [camminare]{"entity": "activity", "role": "old"}  con il nome [imparare l'inglese]{"entity": "activity", "role": "new"}
- nella categoria [amicizia](category) sostituisci il nome dell'attività [andare a mangiare una pizza]{"entity": "activity", "role": "old"}
- modifica il nome dell'attività [revisione]{"entity": "activity", "role": "old"} nella categoria [consegna](category) con il nome [rileggere]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [nuoto]{"entity": "activity", "role": "old"} nella categoria [sport](category) con il nome [boxe]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [chiesa]{"entity": "activity", "role": "old"}  con il nome [meditazione]{"entity": "activity", "role": "new"}
- per l'attività [completare il powerpoint]{"entity": "activity", "role": "old"} modifica il nome con [completare la relazione]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [ballo]{"entity": "activity", "role": "old"} con il nome [canto]{"entity": "activity", "role": "new"}
- nella categoria [eventi](category) cambia il nome dell'attività [tagliare i capelli]{"entity": "activity", "role": "old"}
- voglio cambiare il nome dell'attività [camminare all'aperto]{"entity": "activity", "role": "old"} in [personale](category) con il nome [andare fuori con il cane]{"entity": "activity", "role": "new"}

## intent:remove_item
- cancella [preparare la colazione](activity) nella categoria [dieta](category) alle 7:30
- ciao, voglio cancellare un'attività dalla mia lista
- ciao, voglio cancellare un'attività dall'elenco [pianificazioni](category)
- cancella [camminare](activity) nella categoria [salute personale](category) alle 6:30
- rimuovi [revisione del progetto](activity) nella categoria [lavoro](category) alle 10:25
- cancella [acquistare il biglietto del treno](activity) nella categoria [viaggio](category) alle 20:00
- rimuovi l'attività [boxe](activity) nella categoria [settimanale](category)
- rimuovi [dentista](activity) nella categoria [assistenza sanitaria](category) alle 22:20
- elimina l'attività [inviare un'email](activity) nella categoria [scadenze](category)
- voglio cancellare un'attività dall'elenco [computer](category)
- ciao, voglio cancellare un'attività nella categoria [sociale](category) alle 14:50
- rimuovi [correre](activity) in [palestra](category) per domani
- elimina l'attività [giocare](activity) nella categoria [intrattenimento](category)
- cancella [controllare le e-mail](activity) alle 00:00
- elimina l'attività [andare a nuotare](activity) nella categoria [sport](category)
- cancella [unghie](activity) nella categoria [estetica](category) alle 9:40
- elimina [riposo](activity) nella categoria [salute](category)
- cancella [windsurf](activity) alle 01:45
- cancella [ascoltare un podcast](activity) nella categoria [intrattenimento](category) alle 12:35
- rimuovi l'attività [studiare matematica](activity) nella categoria [università](category)
- ciao, voglio rimuovere un'attività dall'elenco [ricreazione](category)
- voglio cancellare un'attività nella categoria [commissioni](category) alle 19:00
- cancella [pulizia](activity) nella categoria [casa](category) alle 20:30

## intent:presentation
- [antonella](name)
- [grazia](name)
- sono [antonino](name)
- [andrea](name)
- voglio creare un account
- impostare un account
- [isa](name)
- [nik](name)
- fammi creare un account
- [chiara](name)
- il mio nome è [matti](name)
- [alberto](name)
- voglio creare un utente
- [diodato](name)
- [alberigo](name)
- [isolda](name)
- il mio nome è [alessia](name)
- [piero](name)
- [arianna](name)
- [fabiano](name)
- [lilly](name)
- ciao, sono [ferdinando](name)
- [vinci](name)
- [giustino](name)
- [molly](name)
- [anita](name)
- [cathrine](name)
- [kikka](name)
- sono [simo](name)
- ciao sono [ferdi](name)
- [violeta](name)
- [nino](name)
- ciao sono [cami](name)
- [valerio](name)
- [pierino](name)
- [riziero](name)

## intent:inform
- [negozio](category)
- [medico](category)
- [viaggiare](activity)
- [finanza](category)
- [zaino](category)
- [partitella](activity)
- [corda](activity)
- [pagare le bollette](activity)
- [divertimento](category)
- [prenotare le vacanze](activity)
- [vacanze](category)
- [ritirare carta di indentità](activity)
- [pagare la bolletta](activity)
- [andare nello studio](activity)
- [andare alla banca](activity)
- [giocare a calcio](activity)
- in 30 secondi
- [viaggi](category)
- venerdì
- [studio](activity)
- in 5 minuti
- [uscire](activity)
- [investire](activity)
- 14:00
- [andare dai nonni](activity)
- [lavoro](category)
- [esame patente](activity)
- oggi
- [macchine](category)
- lunedì
- [azienda](category)
- [fare ripetizioni](activity)
- [universita](category)
- [analisi](activity)
- [arredamento](category)
- [sciare](activity)
- [andare al cinema](activity)
- [cucinare per cena](activity)
- 14 settembre 2022
- [lezione](activity)
- [triennale](category)
- [armadietto](category)
- 19 ore
- [uscire con gli amici](activity)

## intent:add_item
- inserire [uscire](activity) alle 9:30
- vorrei inserire una nuova attività [manicure](activity) all'elenco [estetica](category)
- nella categoria [corso](category) inserire [incontro](activity) alle 20:30
- vorrei inserire la nuova attività [giocare ai videogiochi](activity) alla categoria [svago](category)
- inserisci [yoga](activity)
- inserisci [il compleanno del mio amico](activity) in [eventi](category) alle 14:50
- aggiungi [chiamare mia madre](activity) alle 13:00
- ciao, vorrei mettere un'attività nella mia lista alle 12:37
- aggiungi l'attività [dipingere](activity)
- ciao, voglio inserire un'attività in un elenco
- ciao, voglio aggiungere un'attività [farmacia](activity) nella categoria [salute](category)
- aggiungi [fare selfie](activity) alle 01:45
- inserire [inviare una email](activity) nella categoria [lavoro](category) alle 16:00
- inserire [prenotazione](activity) alle 00:00
- inserisci l'attività [fare esercizi di routine](activity) nella categoria [sport](category)
- ciao, voglio inserire un'attività [andare a boxe](activity) nella categoria [sport](category)
- inserire l'attività [ripetere](activity) nella categoria [esame](category) alle 22:20
- vorrei aggiungere un'attività
- inserisci una nuova attività [guardare la partita](activity)
- inserire [andare al supermercato](activity) nella categoria [cibo](category) alle 6:30
- ciao, aggiungi l'attività [regali](activity) nella categoria [natale](category)
- ciao, inserisci [guardare lo spettacolo](activity) nella categoria [interesse](category)
- vorrei aggiungere la nuova attività [andare in banca](activity) alla categoria [finanza](category)
- ciao, inserisci l'attività [andare a teatro](activity) nella categoria [arte](category)
- ciao, inserisci l'attività [caffè](activity) nella categoria [amicizia](category)
- ciao, vorrei inserire un'attività in un elenco [spesa](category) alle 21:10
- vorrei inserire un'attività alla categoria [cura della mente](category)
- ciao, inserisci [imparare l'inglese](activity) nella categoria [lingue](category)
- ciao, inserisci [ripetere il discorso](activity) nella categoria [esame](category)
- aggiungi [partita](activity) alle 11:00
- inserisci [organizzare l'armadio](activity) nella categoria [abbigliamento](category)
- ciao, aggiungi [psicologo](activity) nella categoria [mente](category)
- vorrei mettere una nuova attività [fare shopping](activity) in [personale](category)
- ciao, vorrei aggiungere un'attività
- inserisci [fare esperimenti](activity) nella categoria [scienze](category) alle 10:25
- aggiungi attività [gioca a pallavolo](activity) in categoria [sport](category) alle 5:12
- ciao, aggiungi una nuova attività [guardare il match](activity) nella categoria [interessi](category)
- ciao, voglio aggiungere un'attività alla categoria [educazione](category)
- ciao, voglio inserire un'attività [sci](activity) nell'elenco [inverno](category)
- inserisci l'attività [ripetere il discorso](activity) nella categoria [università](category)
- aggiungere [ordinare l'armadio](activity) alle 01:45
- metti [studiare](activity) in [università](category)
- ciao, vorrei inserire un'attività nell'elenco [stile di vita](category) alle 14:50
- vorrei aggiungere una nuova attività
- inserisci [prendere la pillola](activity) alle 9:30
- metti [fare shopping](activity)
- vorrei aggiungere un'attività nella lista [parenti](category) per domani
- vorrei inserire un'attività [andare al cinema](activity) all'elenco [amicizia](category)
- inserisci [gioca a pallavolo](activity) nella categoria [sport](category) alle 19:00
- vorrei aggiungere un'attività alle 11:00
- metti [fare una doccia](activity) in [cura personale](category) alle 4:25
- inserisci l'attività [andare al concerto](activity) in [musica](category) alle 17:30
- ciao, inserisci [andare a correre](activity)
- inserire [guardare un film](activity) alle 11:00
- ciao, inserisci l'attività [torneo di calcio](activity) nella categoria [sport](category)
- ciao, voglio inserire un'attività nella lista [impegni](category)

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
