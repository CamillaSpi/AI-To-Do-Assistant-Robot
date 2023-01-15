## intent:bot_challenge
- Sei un umano?
- tu chi sei?

## intent:goodbye
- buona giornata
- arrivederci

## intent:help
- Per favore aiutami
- Ho bisogno di aiuto

## intent:greet
- Buonasera
- Hey
- Salve

## intent:affirm
- si
- sì

## intent:mood_great
- Stupefacente
- Meraviglioso
- Così perfetto

## intent:ask_name
- mi hai riconosciuto?
- mi riconosci?
- dimmi il mio nome

## intent:mood_unhappy
- Sono deluso
- Molto triste
- Estremamente triste

## intent:deny
- negativo
- non credo
- no
- mai

## intent:clean_activities
- rimuovi tutte le attività
- per favore, rimuovi tutte le attività completate
- elimina tutte le attività

## intent:view_categories
- posso vedere quali sono le mie categorie?
- quali sono le categorie inserite?
- quali sono le mie categorie?
- mostrami le mie categorie

## intent:remind_me_of
- imposta un promemoria per l'attività [chiamare il dottore](activity) nella categoria [visite mediche](category) nella prossima mattina
- aiutami a non dimenticare l'attività [studio](activity) nella categoria [scuola](category) per domani
- non posso dimenticare di [fare gli esercizi](activity) alle 19:00
- ricordami il [pranzo di lavoro](activity)
- aiutami a ricordare il [pranzo di lavoro](activity) dopodomani alle 12
- ricordami [l'esame](activity) domani mattina
- ricordami di [mangiare frutta](activity)
- aiutami a non dimenticare l'attività [ripassare matematica](activity) nella categoria [scuola](category) per domani
- ricordami di [fare shopping](activity) nella categoria [personale](category) alle 8:30

## intent:view_activities
- mostra le mie attività [non sviluppate](activity_status)
- quali sono le mie attività create per domenica?
- voglio vedere tutte le mie attività
- quali sono le mie attività [fatte](activity_status)?
- quali sono le mie attività aggiunte per domani?
- quali sono le mie attività per domani mattina?
- mostrami attività [eseguite](activity_status) nella categoria [scuola](category)
- cosa ho da fare?
- mostra le attività nella categoria [palestra](category)

## intent:modify_category
- sostituire la categoria [banca]{"entity": "category", "role": "old"} nella categoria [finanza]{"entity": "category", "role": "new"}
- convertire la categoria [sport]{"entity": "category", "role": "old"} in [personale]{"entity": "category", "role": "new"}
- voglio trasformare la categoria [scadenze]{"entity": "category", "role": "old"} in [commissioni]{"entity": "category", "role": "new"}
- voglio modificare il nome di una categoria
- sostituire la categoria [banca]{"entity": "category", "role": "old"} con [vacanza]{"entity": "category", "role": "new"}
- modificare la categoria [volontariato]{"entity": "category", "role": "old"} in [sociale]{"entity": "category", "role": "new"}
- voglio variare la categoria [commissioni]{"entity": "category", "role": "old"} in [scadenze]{"entity": "category", "role": "new"}
- voglio alterare la categoria [annuale]{"entity": "category", "role": "old"} a [estate]{"entity": "category", "role": "new"}
- per favore, variare la categoria [eventi]{"entity": "category", "role": "old"} in [scuola]{"entity": "category", "role": "new"}
- variare il nome della categoria [personale]{"entity": "category", "role": "old"} con il nome [sport]{"entity": "category", "role": "new"}

## intent:add_category
- categoria: [pagamenti](category)
- aggiungi la nuova categoria [banca](category)
- categoria: [scuola](category)
- voglio mettere una nuova categoria [vacanza](category)
- ciao, voglio aggiungere la categoria [commissioni](category)
- voglio aggiungere la categoria [università](category)
- nuova categoria da aggiungere: [progetti](category)
- voglio mettere la categoria [vacanza](category)
- inserisci la categoria [farmaci](category)
- la categoria da inserire è [volontariato](category)
- nuova categoria: [volontariato](category)
- aggiungi [sport](category) categoria
- voglio aggiungere la categoria [stile di vita](category)

## intent:modify_activity_deadline
- voglio modificare la scadenza di un'attività
- per l'attività [prenotare l'aereo](activity) trasforma la scadenza in lunedì
- altera la scadenza dell'attività [aiutare il nonno](activity) alle 22:00
- voglio cambiare la scadenza dell'attività [andare dal parrucchiere](activity) nella categoria [personale](category)
- cambia la scadenza dell'attività [raccogliere fondi](activity)
- voglio cambiare il termine dell'attività [uscire con gli amici](activity) nella categoria [eventi](category) con 27 settembre 1998
- alterare la scadenza
- voglio modificare la deadline dell'attività [suonare la chitarra](activity) da domani alla prossima settimana
- altera la deadline dell'attività [andare al mare](activity) nella categoria [tempo libero](category) in domenica
- altera la deadline dell'attività [pagare il supermercato](activity) nella categoria [pagamenti](category) in domenica
- per l'attività [prenotare l'aereo](activity) nella categoria [vacanza](category) trasformare la deadline in lunedì
- altera la scadenza dell'attività [cantare](activity) in domenica
- modifica la scadenza dell'attività [cucinare per la famiglia](activity) nella categoria [casa](category) con domenica
- sostituisci il termine dell'attività [mostra d'arte](activity) da lunedì a venerdì

## intent:remove_category
- ciao, per favore rimuovi la seguente categoria [spesa](category)
- rimuovi [sport](category) dalle mie categorie
- rimuovere la vecchia categoria [cura personale](category)
- ciao, voglio togliere una categoria [eventi](category)
- voglio togliere la categoria [palestra](category)
- ciao, per favore annulla la seguente categoria [divertimento](category)
- ciao, voglio rimuovere la categoria [desideri](category)
- voglio eliminare la categoria [professione](category)
- rimuovi una categoria
- ciao, voglio togliere la categoria [assistenza sanitaria](category)
- non voglio usare la categoria [sport](category)
- eliminare la categoria [relazioni](category)
- ciao, voglio cancellare la categoria [annuale](category)
- rimuovi [università](category) tra le mie categorie
- voglio cancellare la categoria [università](category)

## intent:set_status_activity
- voglio impostare [non fatta](activity_status) un'attività in un elenco
- ciao, metti [completato](activity_status) [andare dal parrucchiere](activity) nella categoria [benessere](category)
- imposta come [non fatta](activity_status) [leggere](activity)
- imposta come [non completato](activity_status) [nuotare](activity)
- ciao, imposta [non terminata](activity_status) [annaffia le piante](activity)
- ciao, poni [non fatto](activity_status) [pulisci il bagno](activity) in [casa](category)
- imposta [non terminata](activity_status) [chiama mia madre](activity) in [settimanale](category)
- ciao, imposta un'attività [non completata](activity_status)
- imposta [non fatto](activity_status) [ripeti matematica](activity) nella categoria [scuola](category)
- ciao, metti [completa](activity_status) l'attività [jogging](activity) in [salute fisica](category)
- ciao, voglio porre come [non eseguita](activity_status) [ripetizioni](activity) nella categoria [laurea](category)
- imposta [sviluppata](activity_status) l'attività [suona la chitarra](activity) nella categoria [musica](category)
- imposta come [sviluppata](activity_status) [giocare a carte](activity)
- imposta [terminato](activity_status) [cena con gli amici](activity)
- metti [non terminata](activity_status) l'attività [acquistare una bicicletta](activity) in [negozio](category)
- imposta come [non sviluppata](activity_status) [giocare a carte](activity)
- imposta [fatta](activity_status) l'attività [vai in farmacia](activity) nella categoria [benessere](category)
- imposta [non sviluppata](activity_status) l'attività [suona la chitarra](activity) nella categoria [musica](category)
- metti come [non finita](activity_status) [alzati](activity) in [quotidiano](category)

## intent:modify_activity_category
- modificare la categoria [lavoro]{"entity": "category", "role": "old"} di [pranzo di lavoro](activity)
- sostituire la categoria [faccende domestiche]{"entity": "category", "role": "old"} dell'attività [preparare il pranzo](activity) con la categoria [casa]{"entity": "category", "role": "new"}
- per l'attività [prenotare il treno](activity) aggiorna la categoria [imminente]{"entity": "category", "role": "old"} in [vacanza]{"entity": "category", "role": "new"}
- modifica la categoria [vacanze]{"entity": "category", "role": "old"} dell'attività [andare al mare](activity) in [svago]{"entity": "category", "role": "new"}
- per l'attività [dormire](activity) modifica la categoria [salute]{"entity": "category", "role": "old"} in [riposo]{"entity": "category", "role": "new"}
- trasforma la categoria [progetti]{"entity": "category", "role": "old"} dell'attività [studiare](activity) in categoria [università]{"entity": "category", "role": "new"}
- cambia la categoria [cura della persona]{"entity": "category", "role": "old"} dell'attività [correre](activity)
- per l'attività [andare al mercato](activity) aggiorna la categoria [spesa]{"entity": "category", "role": "old"} in [impegni domestici]{"entity": "category", "role": "new"}
- sostituisci la categoria [Natale]{"entity": "category", "role": "old"} dell'attività [comprare i regali](activity) con la categoria [tempo libero]{"entity": "category", "role": "new"}
- sostituire la categoria [tempo libero]{"entity": "category", "role": "old"} dell'attività [fare i regali](activity) con la categoria [Natale]{"entity": "category", "role": "new"}
- sostituisci la categoria [faccende domestiche]{"entity": "category", "role": "old"} dell'attività [preparare la colazione](activity) con la categoria [famiglia]{"entity": "category", "role": "new"}
- modifica la categoria [dieta]{"entity": "category", "role": "old"} di [camminare all'aperto](activity) in [tempo libero]{"entity": "category", "role": "new"}
- voglio cambiare la categoria [viaggio]{"entity": "category", "role": "old"} dell'attività [prenotare l'hotel](activity) in [desideri]{"entity": "category", "role": "new"}
- per l'attività [pulire la casa](activity) nella categoria [faccende domestiche]{"entity": "category", "role": "old"} sostituisci la categoria con [quotidiano]{"entity": "category", "role": "new"}
- modifica la categoria [tempo libero]{"entity": "category", "role": "old"} di [camminare all'aperto](activity) in [dieta]{"entity": "category", "role": "new"}
- voglio cambiare la categoria [desideri]{"entity": "category", "role": "old"} dell'attività [prenotare l'hotel](activity) in [viaggio]{"entity": "category", "role": "new"}
- per l'attività [ritirare il pacco](activity) aggiornare la categoria [commissioni]{"entity": "category", "role": "old"} in [imminente]{"entity": "category", "role": "new"}
- per l'attività [partecipare alla conferenza](activity) trasforma la categoria [cultura]{"entity": "category", "role": "old"} in [lavoro]{"entity": "category", "role": "new"}
- per l'attività [pulire la casa](activity) nella categoria [quotidiano]{"entity": "category", "role": "old"} sostituire la categoria con [faccende domestiche]{"entity": "category", "role": "new"}
- trasforma la categoria [studio]{"entity": "category", "role": "old"} dell'attività [preparare l'esame](activity) in categoria [università]{"entity": "category", "role": "new"}
- voglio cambiare la categoria [sport]{"entity": "category", "role": "old"} dell'attività [yoga](activity) con la categoria [palestra]{"entity": "category", "role": "new"}

## intent:modify_activity_name
- per l'attività [prendere l'autobus]{"entity": "activity", "role": "old"} in [viaggio](category) trasforma il nome con [prendere il treno]{"entity": "activity", "role": "new"}
- per l'attività [leggere un giornale]{"entity": "activity", "role": "old"} trasforma il nome con [scrivere un articolo]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [modificare un video]{"entity": "activity", "role": "old"} con il nome [editare un video]{"entity": "activity", "role": "new"}
- nella categoria [università](category) cambia l'attività [andare a ricevimento]{"entity": "activity", "role": "old"}  con il nome [seguire la lezione]{"entity": "activity", "role": "new"}
- modificare il nome dell'attività [revisione]{"entity": "activity", "role": "old"} nella categoria [report](category) con nome [rileggere]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [andare a nuotare]{"entity": "activity", "role": "old"} con [andare al parco]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [aiutare la zia]{"entity": "activity", "role": "old"} nella categoria [famiglia](category) con [aiutare la sorella]{"entity": "activity", "role": "new"}
- nella categoria [scuola](category) sostituisci il nome dell'attività [interrogazione di matematica]{"entity": "activity", "role": "old"}  con il nome [compito di matematica]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [organizzare raccolta fondi]{"entity": "activity", "role": "old"} nella categoria [volontariato](category) con [fare beneficenza]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [jogging]{"entity": "activity", "role": "old"} nella categoria [sport](category)
- modificare il nome dell'attività [pilates]{"entity": "activity", "role": "old"} con nome [yoga]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [boxe]{"entity": "activity", "role": "old"} nella categoria [sport](category)
- nella categoria [università](category) cambiare il nome dell'attività [esame]{"entity": "activity", "role": "old"}  con nome [studio]{"entity": "activity", "role": "new"}
- per l'attività [andare al teatro]{"entity": "activity", "role": "old"} modifica il nome con [andare a un concerto]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con nome [fare beneficenza]{"entity": "activity", "role": "old"} nella categoria [impegni sociali](category)
- modifica il nome dell'attività [preparare la colazione]{"entity": "activity", "role": "old"} con il nome [pulire il giardino]{"entity": "activity", "role": "new"}
- per l'attività [completare la relazione]{"entity": "activity", "role": "old"} modifica il nome con [completare il powerpoint]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [pulire la casa]{"entity": "activity", "role": "old"} nella categoria [faccende domestiche](category)
- modifica il nome dell'attività [pulire il giardino]{"entity": "activity", "role": "old"} con il nome [preparare la colazione]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [aiutare la sorella]{"entity": "activity", "role": "old"} nella categoria [famiglia](category) con [aiutare la zia]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [portare fuori il cane]{"entity": "activity", "role": "old"} in [quotidiana](category)
- voglio cambiare l'attività con nome [leggere]{"entity": "activity", "role": "old"} con [leggere un libro]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [fare taekwondo]{"entity": "activity", "role": "old"} nella categoria [sport](category) con il nome [andare a nuotare]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [ballo]{"entity": "activity", "role": "old"} con il nome [canto]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [chiamare il medico]{"entity": "activity", "role": "old"}

## intent:remove_item
- rimuovi [videoconferenza](activity) nella categoria [teamwork](category)
- cancella [fare il pieno](activity) nella categoria [auto](category) alle 20:00
- ciao, voglio cancellare un'attività nella categoria [blog](category) alle 17:30
- rimuovi l'attività [leggere il giornale](activity) nella categoria [cultura](category)
- elimina l'attività [allenarsi](activity) nella categoria [benessere](category)
- elimina l'attività [inviare un'email](activity) nella categoria [scadenze](category)
- voglio cancellare un'attività nella categoria [commissioni](category) alle 19:00
- elimina [finire il report](activity) nella categoria [lavoro](category)
- rimuovi [rivisitare la presentazione](activity) nella categoria [scuola](category)
- ciao, voglio cancellare un'attività nella categoria [stile di vita](category) alle 16:00
- rimuovi [dipingere](activity) nella categoria [creatività](category) alle 9:40
- rimuovi [camminare nel giardino](activity)
- ciao, voglio eliminare un'attività dalla mia lista
- cancella [andare in chiesa](activity) nella categoria [personale](category) alle 19:41
- ciao, voglio cancellare un'attività nella categoria [marketing](category) alle 18:30
- cancella [pulizia](activity) nella categoria [casa](category) alle 20:30
- rimuovi [dentista](activity) nella categoria [assistenza sanitaria](category) alle 22:20
- cancella [andare a cantare](activity) alle 11:00
- elimina [fare i compiti](activity)
- voglio cancellare un'attività dall'elenco [computer](category)
- elimina l'attività [andare in banca](activity) nella categoria [finanza](category)
- voglio rimuovere un'attività da un elenco
- cancella [partecipare alla lezione](activity) nella categoria [università](category) alle 5:12
- elimina l'attività [nuotare](activity) nella categoria [divertimento](category)
- rimuovi l'attività [boxe](activity) nella categoria [settimanale](category)
- cancellare [andare in escursione](activity) nella categoria [tempo libero](category)

## intent:presentation
- voglio registrarmi
- [vito](name)
- impostare un account
- creare un account
- [olivia](name)
- [flaviano](name)
- [roberto](name)
- [marianna](name)
- hi, il mio nome è [Simonetta](name)
- [diodato](name)
- [annamaria](name)
- [liliana](name)
- [ermanno](name)
- nuovo account
- [orlando](name)
- [raffaella](name)
- sono [Nando](name)
- ciao, sono [michele](name)
- [laura](name)
- fammi creare un utente
- [paola](name)
- [clarissa](name)
- [riccardino](name)
- il mio nome è [matti](name)
- [filomena](name)
- [edvige](name)
- [erode](name)
- [ornella](name)
- [isolda](name)
- ciao sono [marcello](name)
- [cathrine](name)
- [andrew](name)
- impostare un utente
- [alberigo](name)
- [anna](name)
- [geppy](name)
- [galatea](name)
- crea un utente
- il mio nome è [ferdi](name)
- crea un account
- voglio creare un account
- [faustino](name)
- [christian](name)
- [riziero](name)

## intent:inform
- [esami](category)
- 14 settembre 2022
- [andare dai nonni](activity)
- [viaggio in Brasile](activity)
- [studiare](activity)
- [ritirare il pacco](activity)
- [divertimento](category)
- [chiamare mia madre](activity)
- [uscita con la famiglia](activity)
- [ritirare patente](activity)
- oggi alle 21
- [eventi](category)
- [scuola](category)
- [giocare](activity)
- lunedì prossimo
- [zaino](category)
- [fare fisioterapia](activity)
- [negozio](category)
- [ricerca](category)
- [andare nello studio](activity)
- [chiamare il medico](activity)
- [fare jogging](activity)
- [affitto](activity)
- [lavori](category)
- da oggi a domani
- [lezione](activity)
- [pagamenti](category)
- [comprare le scarpe](activity)
- [universita](category)
- [carro](category)
- [fare attività fisica](activity)
- [prendere appunti](activity)
- [palestra](category)
- [nuoto](activity)
- [comprare un giubbino](activity)
- [aggiustare la porta](activity)
- [giocare partita](activity)
- [pagare la multa](activity)
- [andare in biblioteca](activity)
- [studiare in biblioteca](activity)
- [disegnare](activity)
- [cinema](activity)
- oggi
- [volte](category)
- [borsa](category)
- [porto](category)
- 9:30
- [obiettivi](category)
- [bolletta](activity)
- [incontro genitori](activity)
- [serata libera](activity)
- 10:00
- [biblioteca](category)

## intent:add_item
- voglio inserire un'attività nella mia lista
- inserire l'attività [acquistare fiori](activity) nella categoria [spesa](category) alle 13:39
- inserisci l'attività [conferenza](activity) in [lavoro](category)
- inserire [windsurf](activity) nella categoria [estate](category) alle 20:30
- inserisci [termine sprint](activity) in categoria [ingegneria](category) alle 8:00
- inserisci l'attività [prenotare il pub](activity) in [amicizia](category) alle 19:41
- aggiungi [fare pilates](activity)
- aggiungi l'attività [dipingere](activity)
- aggiungi [boxe](activity) nella categoria [sport](category)
- inserisci [prendere la pillola](activity) alle 9:30
- inserisci [fare stand up](activity)
- ciao, aggiungi [scrivere un messaggio](activity)
- ciao, inserisci [partecipare alla lezione](activity) nella categoria [corsi](category)
- inserire l'attività [ripetere](activity) nella categoria [esame](category) alle 22:20
- aggiungi [organizzare la cucina](activity) nella categoria [casa](category)
- ciao, vorrei aggiungere un'attività nella lista [hobby](category) alle 3:29
- metti l'attività [piscina](activity)
- ciao, vorrei inserire un'attività nella categoria [dieta](category) alle 14:50
- ciao, vorrei mettere un'attività nell'elenco [blog](category) alle 22:20
- ciao, vorrei aggiungere un'attività all'elenco [spesa](category) alle 6:30
- ciao, voglio inserire un'attività nell'elenco [business](category)
- inserisci l'attività [annaffiare le piante](activity) nella categoria [casa](category)
- aggiungi attività [gioca a pallavolo](activity) in categoria [sport](category) alle 5:12
- ciao, inserisci [lezione di canto](activity) nella categoria [tempo libero](category)
- inserisci l'attività [ripetere il discorso](activity) nella categoria [università](category)
- vorrei mettere un'attività [esercizi](activity) in [sport](category)
- inserire l'attività [fare benzina](activity) nella categoria [auto](category) alle 16:00
- inserisci [yoga](activity)
- ciao, inserisci [andare al ristorante](activity) nella categoria [svago](category)
- ciao, inserisci l'attività [mandare e-mail](activity) nella categoria [progetti](category)
- ciao, vorrei inserire un'attività nella mia lista alle 18:14
- inserisci l'attività [leggere](activity) nella categoria [cultura](category)
- vorrei aggiungere la nuova attività [revisione](activity) alla categoria [progetti](category)
- nella categoria [vacanze](category), voglio inserire un'attività [cena di Natale](activity)
- ciao, vorrei aggiungere un'attività all'elenco [vita](category) alle 16:00
- inserisci [andare in palestra](activity)
- ciao, voglio inserire una nuova attività nella categoria [autunno](category)
- voglio aggiungere un'attività alla lista [divertimento](category) alle 19:00
- ciao, inserisci [scrittura](activity) nella categoria [hobby](category)
- aggiungi un'attività in [musica](category)
- vorrei inserire la nuova attività [giocare ai videogiochi](activity) alla categoria [svago](category)
- ciao, voglio aggiungere l'attività [inviare un'email](activity) all'elenco [comunicazione](category)
- creare l'attività [dentista](activity) nella categoria [mensile](category) alle 20:00
- inserisci l'attività [andare al concerto](activity) in [musica](category) alle 17:30
- inserisci [leggere un libro](activity) nella categoria [cultura](category)
- inserisci [gioca a pallavolo](activity) nella categoria [sport](category) alle 19:00
- vorrei aggiungere la nuova attività [andare in banca](activity) alla categoria [finanza](category)
- ciao, voglio inserire un'attività nell'elenco [imminenti](category)
- ciao, nella categoria [salute](category) voglio inserire l'attività [andare dal dentista](activity)
- inserisci [fare una passeggiata](activity) in [quotidiano](category)
- metti [fare shopping](activity)
- ciao, vorrei mettere un'attività nell'elenco [faccende](category) alle 7:00
- inserire [inviare una email](activity) nella categoria [lavoro](category) alle 16:00
- vorrei inserire una nuova attività [manicure](activity) all'elenco [estetica](category)
- ciao, voglio aggiungere un'attività nell'elenco [visite mediche](category)
- vorrei inserire un'attività [pagamenti](activity) alla categoria [finanza](category)
- metti attività [autobus](activity) in categoria [quotidiano](category) alle 3:29
- ciao, voglio inserire una nuova attività [leggere un paper](activity) nell'elenco [ricerca](category)
- voglio inserire un'attività nella categoria [ricreazione](category) alle 16:30
- ciao, aggiungi [cucinare la cena](activity) nella categoria [casa](category)
- inserire [ascoltare musica](activity) alle 3:00
- inserisci [organizzare l'armadio](activity) nella categoria [abbigliamento](category)
- vorrei inserire la nuova attività [discoteca](activity) alla categoria [divertimento](category)
- voglio inserire un'attività nella categoria [tempo libero](category)
- vorrei mettere un'attività [cena con gli amici](activity) in [amicizia](category)
- inserisci [nuotare](activity) in [sport](category)
- nella categoria [università](category) aggiungi l'attività [esame](activity)

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
