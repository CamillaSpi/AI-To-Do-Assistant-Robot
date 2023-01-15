## intent:bot_challenge
- tu chi sei?

## intent:goodbye
- ci vediamo in giro
- buona notte

## intent:help
- Aiuto
- Aiutami

## intent:greet
- ciao
- Salve

## intent:affirm
- yes
- certo

## intent:mood_great
- Grandioso
- Sono grande
- Così buono

## intent:mood_unhappy
- Triste
- Estremamente triste

## intent:ask_name
- puoi pronuniciare il mio nome?
- mi hai già visto prima?
- dimmi il mio nome

## intent:deny
- non mi va
- non mi piace
- no mi dispiace

## intent:clean_activities
- pulisci tutte le attività completate
- per favore, elimina le attività
- elimina tutte le attività

## intent:view_categories
- posso vedere quali sono le mie categorie?
- quali sono le categorie create?
- Puoi mostrare le mie categorie?

## intent:remind_me_of
- aiutami a non dimenticare l'attività [rivedere la relazione](activity) nella categoria [consegna progetto](category) per domani
- non posso dimenticare di fare l'attività [parlare con il professore](activity) nella categoria [progetto](category) per domenica prossima
- ricordami di [prendere la pillola](activity) in [cura personale](category)
- ricordami l'attività [lezione di chitarra](activity) domani mattina
- aiutami a non dimenticare l'attività [ascoltare la registrazione della lezione](activity) nella categoria [università](category) per domani
- non farmi dimenticare di [correre](activity) alle 19:00
- aiutami a ricordare un'attività

## intent:view_activities
- mostra le attività nella categoria [progetti](category)
- quali sono le mie attività create per domenica?
- cosa ho da fare?
- mostrami cosa devo fare oggi
- mostra tutte le mie attività [sviluppate](activity_status) nella categoria [mensile](category)
- quali sono le mie attività [terminate](activity_status)?
- fammi vedere le attività per mercoledì sera
- mostra le attività nella categoria [palestra](category)

## intent:modify_category
- voglio modificare una categoria
- voglio convertire la categoria [casa]{"entity": "category", "role": "old"} in [genitori]{"entity": "category", "role": "new"}
- voglio trasformare la categoria [scadenze]{"entity": "category", "role": "old"} in [commissioni]{"entity": "category", "role": "new"}
- convertire la categoria [sport]{"entity": "category", "role": "old"} in [personale]{"entity": "category", "role": "new"}
- variare la categoria [famiglia]{"entity": "category", "role": "old"} con [giornaliero/settimanale]{"entity": "category", "role": "new"}
- cambiare il nome della categoria [divertimento]{"entity": "category", "role": "old"} con il nome [cura personale]{"entity": "category", "role": "new"}
- sostituire la categoria [faccende domestiche]{"entity": "category", "role": "old"} con [benessere]{"entity": "category", "role": "new"}
- convertire la categoria [benessere]{"entity": "category", "role": "old"} in [faccende domestiche]{"entity": "category", "role": "new"}

## intent:add_category
- ciao, inserisci la seguente categoria [cultura](category)
- voglio aggiungere una categoria
- ciao, voglio inserire una nuova categoria [ricerca](category)
- ciao, voglio inserire la categoria [progetti](category)
- voglio aggiungere una categoria [pagamenti](category)
- voglio usare una nuova categoria
- aggiungi la nuova categoria [banca](category)
- categoria: [bollette](category)
- metti la categoria [ingegneria](category)
- aggiungi la nuova categoria [personale](category)
- aggiungi la categoria [relazioni](category)

## intent:modify_activity_deadline
- sostituisci la scadenza dell'attività [torneo di calcio](activity)
- voglio modificare la deadline dell'attività [scuolacalcio](activity) nella categoria [sport](category) per domani alle 18:00
- sostituisci il termine dell'attività [mostra d'arte](activity) da lunedì a venerdì
- voglio cambiare il termine dell'attività [chiamare mia madre](activity) al 27 settembre 1998
- cambia la deadline dell'attività [aiutare la nonna](activity) nella categoria [famiglia](category) con lunedì
- altera la scadenza dell'attività [uscire con gli amici](activity) nella categoria [svago](category) a domenica
- voglio modificare la deadline dell'attività [suonare la chitarra](activity) da domani alla prossima settimana
- voglio modificare la scadenza dell'attività [partita con papà](activity) nella categoria [tempo libero](category) in domani alle 18:00
- modifica la scadenza dell'attività [esame della patente](activity) da venerdì a lunedi
- cambia la scadenza dell'attività [raccogliere fondi](activity) nella categoria [volontariato](category) a lunedì
- voglio cambiare la scadenza dell'attività [compito di matematica](activity) dal 25 settembre al 27 settembre 1998
- voglio cambiare il termine dell'attività [uscire con gli amici](activity) nella categoria [eventi](category) con 27 settembre 1998

## intent:remove_category
- voglio togliere la categoria [settimanale](category)
- ciao, per favore cestina la seguente categoria [finanza](category)
- rimuovi [università](category) tra le mie categorie
- rimuovere la categoria [ingegneria](category)
- ciao, voglio rimuovere la categoria [famiglia](category)
- categoria da cancellare: [finanze](category)
- non voglio usare la categoria [sport](category)
- ciao, per favore annulla la seguente categoria [divertimento](category)
- rimuovi una categoria
- voglio togliere una categoria [tempo libero](category)
- ciao, voglio togliere la categoria [assistenza sanitaria](category)
- la categoria da eliminare è [impegni sociali](category)

## intent:set_status_activity
- imposta come [non conclusa](activity_status) [giardinaggio](activity) nella categoria [giardino](category)
- imposta come [fatta](activity_status) [leggere](activity)
- metti come [non finita](activity_status) [alzati](activity) in [quotidiano](category)
- poni [fatta](activity_status) l'attività [shampoo](activity) nella categoria [benessere personale](category)
- imposta [incompleta](activity_status) [ascoltare musica](activity) in [personale](category)
- ciao, poni [fatto](activity_status) [pulisci il bagno](activity) in [casa](category)
- ciao, metti [completato](activity_status) [andare dal parrucchiere](activity) nella categoria [benessere](category)
- poni come [incompleta](activity_status) l'attività [suonare il pianoforte](activity) in [musica](category)
- imposta [incompleta](activity_status) [spegni il forno](activity) in [casa](category)
- imposta [fatto](activity_status) [ripeti matematica](activity) nella categoria [scuola](category)
- imposta [completato](activity_status) [ripetere la presentazione](activity) nella categoria [progetti](category)
- voglio impostare [non fatta](activity_status) un'attività in un elenco
- imposta [fatto](activity_status) l'attività [cucina la pizza](activity) in [casa](category)
- ciao, imposta [completato](activity_status) [annaffia le piante](activity)
- ciao, metti [incompiuta](activity_status) l'attività [jogging](activity) in [salute fisica](category)
- ciao, imposta [incompleto](activity_status) l'attività [aiuta mio nonno](activity) nella categoria [genitori](category)

## intent:modify_activity_category
- modifica la categoria [vacanze]{"entity": "category", "role": "old"} dell'attività [andare al mare](activity) in [svago]{"entity": "category", "role": "new"}
- per l'attività [disegnare](activity) nella categoria [arte]{"entity": "category", "role": "old"} sostituire la categoria con [creatività]{"entity": "category", "role": "new"}
- sostituisci la categoria [faccende domestiche]{"entity": "category", "role": "old"} dell'attività [preparare la colazione](activity) con la categoria [famiglia]{"entity": "category", "role": "new"}
- per l'attività [andare in farmacia](activity) modificare la categoria [salute personale]{"entity": "category", "role": "old"} in [salute]{"entity": "category", "role": "new"}
- per l'attività [andare al mercato](activity) aggiorna la categoria [impegni domestici]{"entity": "category", "role": "old"} in [spesa]{"entity": "category", "role": "new"}
- sostituisci la categoria [famiglia]{"entity": "category", "role": "old"} dell'attività [preparare la colazione](activity) con la categoria [faccende domestiche]{"entity": "category", "role": "new"}
- cambia la categoria [progetti]{"entity": "category", "role": "old"} dell'attività [studiare](activity) in categoria [esami]{"entity": "category", "role": "new"}
- convertire la categoria [sport]{"entity": "category", "role": "old"} dell'attività [yoga](activity) con [giornaliero/settimanale]{"entity": "category", "role": "new"}
- modifica la categoria [vacanze]{"entity": "category", "role": "old"} dell'attività [andare al mare](activity)
- converti la categoria [cura della persona]{"entity": "category", "role": "old"} dell'attività [correre](activity) con [sport]{"entity": "category", "role": "new"}
- modificare la categoria [alimentazione]{"entity": "category", "role": "old"} di [camminare all'aperto](activity) in [tempo libero]{"entity": "category", "role": "new"}
- modifica la categoria [tempo libero]{"entity": "category", "role": "old"} di [camminare all'aperto](activity) in [dieta]{"entity": "category", "role": "new"}
- trasforma la categoria [studio]{"entity": "category", "role": "old"} dell'attività [preparare l'esame](activity) in categoria [università]{"entity": "category", "role": "new"}
- convertire la categoria [giornaliero/settimanale]{"entity": "category", "role": "old"} dell'attività [yoga](activity)
- per l'attività [prenotare il treno](activity) aggiorna la categoria [vacanza]{"entity": "category", "role": "old"} in [imminente]{"entity": "category", "role": "new"}
- voglio cambiare la categoria [vacanze]{"entity": "category", "role": "old"} dell'attività [yoga](activity)
- per l'attività [guardare il match](activity) trasformare la categoria [tempo libero]{"entity": "category", "role": "old"} in [famiglia]{"entity": "category", "role": "new"}

## intent:modify_activity_name
- per l'attività [prendere l'autobus]{"entity": "activity", "role": "old"} in [viaggio](category) trasforma il nome con [prendere il treno]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [editare un video]{"entity": "activity", "role": "old"} con il nome [modificare un video]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [organizzare raccolta fondi]{"entity": "activity", "role": "old"} nella categoria [volontariato](category) con [fare beneficenza]{"entity": "activity", "role": "new"}
- sostituisci il nome dell'attività [scrivere l'articolo]{"entity": "activity", "role": "old"}  con il nome [pubblicare l'articolo]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con nome [organizzare raccolta fondi]{"entity": "activity", "role": "old"} nella categoria [volontariato](category)
- per l'attività [andare a teatro]{"entity": "activity", "role": "old"} trasforma il nome con [andare al cinema]{"entity": "activity", "role": "new"}
- per l'attività [andare a giocare a calcio]{"entity": "activity", "role": "old"} nella categoria [tempo libero](category) modifica il nome con [suonare la chitarra]{"entity": "activity", "role": "new"}
- per l'attività [andare a un concerto]{"entity": "activity", "role": "old"} modifica il nome con [andare al teatro]{"entity": "activity", "role": "new"}
- nella categoria [università](category) cambia l'attività [andare a ricevimento]{"entity": "activity", "role": "old"}  con il nome [seguire la lezione]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [rileggere]{"entity": "activity", "role": "old"} nella categoria [consegna](category) con il nome [revisione]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [pilates]{"entity": "activity", "role": "old"} con il nome [yoga]{"entity": "activity", "role": "new"}
- nella categoria [università](category) cambia l'attività [seguire la lezione]{"entity": "activity", "role": "old"}  con il nome [andare a ricevimento]{"entity": "activity", "role": "new"}
- nella categoria [scuola](category) sostituire il nome dell'attività [compito di latino]{"entity": "activity", "role": "old"}  con nome [interrogazione di latino]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [nuotare]{"entity": "activity", "role": "old"} nella categoria [attività fisica](category) con nome [jogging]{"entity": "activity", "role": "new"}
- sostituire il nome dell'attività [leggere il giornare]{"entity": "activity", "role": "old"}  con nome [guardare il telegiornale]{"entity": "activity", "role": "new"}
- per l'attività [suonare la chitarra]{"entity": "activity", "role": "old"} nella categoria [tempo libero](category) modifica il nome con [andare a giocare a calcio]{"entity": "activity", "role": "new"}
- nella categoria [scuola](category) sostituisci il nome dell'attività [interrogazione di matematica]{"entity": "activity", "role": "old"}  con il nome [compito di matematica]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [andare a fisioterapia]{"entity": "activity", "role": "old"}
- cambia il nome dell'attività [jogging]{"entity": "activity", "role": "old"} nella categoria [attività fisica](category) con nome [nuotare]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [prenotare l'aereo]{"entity": "activity", "role": "old"} con [prenotare il treno]{"entity": "activity", "role": "new"}
- modificare il nome dell'attività [yoga]{"entity": "activity", "role": "old"} con nome [pilates]{"entity": "activity", "role": "new"}

## intent:remove_item
- cancellare l'attività [correggere i compiti](activity) nella categoria [lavoro](category)
- cancellare l'attività [fare il powerpoint](activity) nella categoria [imminente](category)
- rimuovi [lavare l'auto](activity) nella categoria [faccende domestiche](category) alle 22:20
- cancella [pulizia](activity) nella categoria [casa](category) alle 20:30
- cancella [pagare mutuo](activity) nella categoria [finanza](category) alle 16:00
- cancellare [compilare il modulo](activity) nella categoria [impegni](category)
- cancella [aiutare mia madre](activity) alle 01:45
- rimuovi [camminare nel giardino](activity)
- voglio eliminare un'attività dall'elenco [documenti](category)
- voglio cancellare un'attività nella categoria [generi alimentari](category) alle 9:40
- cancella [unghie](activity) nella categoria [estetica](category) alle 9:40
- cancella [giardinaggio](activity) nella categoria [giardino](category) alle 5:12
- voglio eliminare un'attività
- cancellare [andare in escursione](activity) nella categoria [tempo libero](category)
- rimuovi [rivisitare la presentazione](activity) nella categoria [scuola](category)
- ciao, voglio cancellare un'attività dall'elenco [pianificazioni](category)
- cancella [camminare](activity) nella categoria [salute personale](category) alle 6:30
- elimina l'attività [andare a nuotare](activity) nella categoria [sport](category)
- cancella [fare shopping](activity) alle 00:00
- elimina [shampoo](activity) nella categoria [quotidiana](category)
- rimuovi [nuotare](activity) nella categoria [sport](category)
- cancella [chiamare l'elettricista](activity) nella categoria [guasti](category) alle 21:10
- cancella [ascoltare un podcast](activity) nella categoria [intrattenimento](category) alle 12:35

## intent:presentation
- [teresa](name)
- il mio nome è [ferdi](name)
- utente
- ciao, sono [camilla](name)
- ciao sono [alex](name)
- [kikka](name)
- [annamaria](name)
- ciao sono [ferdi](name)
- [ale](name)
- [michelle](name)
- [laura](name)
- [nino](name)
- impostare un utente
- fammi creare un account
- [roberto](name)
- [pierino](name)
- [elza](name)
- il mio nome è [alessia](name)
- [clarissa](name)
- sono [giorgino](name)
- [tina](name)
- nuovo account
- [nerone](name)
- hi, il mio nome è [Simonetta](name)
- il mio nome è [Ugo](name)
- [elga](name)
- [michi](name)
- [adele](name)
- [gianni](name)
- creare un account
- nuovo utente
- [piero](name)
- [grazia](name)
- [nik](name)
- [raimondo](name)
- [christian](name)

## intent:inform
- [viaggio in spagna](activity)
- [studiare per l'esame](activity)
- [presentare domanda](activity)
- [affitto](activity)
- [aggiustare la porta](activity)
- [porto](category)
- [andare in biblioteca](activity)
- [giocare a carte](activity)
- alle 18:00
- [musica](category)
- [cena con gli amici](activity)
- [giocare](activity)
- tra 26 minuti
- [materie](category)
- da oggi a domani
- [carrello](category)
- [famiglia](category)
- [andare in banca](activity)
- [andare in barca](activity)
- venerdì
- [odierne](category)
- [corda](activity)
- [eventi](category)
- [fare bilancio](activity)
- [bollette](category)
- [andare al cinema](activity)
- [appuntamento romantico](activity)
- [studio](activity)
- alle 21
- [viaggio in brasile](activity)
- [spese](category)
- [volontariato](category)
- [sport](category)
- [ricerca](category)
- [spegnere il gas](activity)
- [rapidamente](category)
- [progetti](category)
- [to do](category)
- [personale](category)
- [farmaci](category)
- [medico](category)
- [andare a fare shopping](activity)
- [pagare la bolletta](activity)
- oggi alle 21

## intent:add_item
- ciao, voglio aggiungere l'attività [inviare un'email](activity) all'elenco [comunicazione](category)
- vorrei mettere una nuova attività [fare shopping](activity) in [personale](category)
- ciao, crea [partecipare a un corso](activity) nella categoria [laurea](category)
- inserire l'attività [acquistare un libro](activity) nella categoria [apprendimento](category) alle 5:12
- inserisci [dormire](activity) nella categoria [benessere](category)
- inserisci [portare fuori il cane](activity) alle 3:00
- inserire l'attività [denti](activity) nella categoria [salute](category) alle 12:35
- ciao, aggiungi [formazione](activity)
- ciao, inserisci l'attività [caffè](activity) nella categoria [amicizia](category)
- inserisci [fare una passeggiata](activity) in [quotidiano](category)
- aggiungi [correre](activity) in [palestra](category) alle 12
- inserisci [termine sprint](activity) in categoria [ingegneria](category) alle 8:00
- inserisci l'attività [conferenza](activity) in [lavoro](category)
- vorrei mettere un'attività [cena con gli amici](activity) in [amicizia](category)
- ciao, voglio inserire una nuova attività [leggere un paper](activity) nell'elenco [ricerca](category)
- ciao, vorrei inserire un'attività nell'elenco [stile di vita](category) alle 14:50
- inserire [uscire](activity) alle 9:30
- creare [partecipare a una conferenza](activity) nella categoria [lavoro](category) alle 20:00
- inserire [windsurf](activity) nella categoria [estate](category) alle 20:30
- voglio creare un'attività nella mia lista
- inserisci l'attività [revisione](activity) in [impegni](category) alle 17:30
- metti [fare shopping](activity)
- ciao, inserisci [lezione di canto](activity) nella categoria [tempo libero](category)
- voglio inserire un'attività nella categoria [ricreazione](category) alle 16:30
- inserisci [leggere un libro](activity) nella categoria [cultura](category)
- aggiungi l'attività [inviare il codice](activity) in [impegni](category)
- vorrei inserire un'attività [pagamenti](activity) alla categoria [finanza](category)
- ciao, vorrei inserire un'attività nell'elenco [marketing](category) alle 17:30
- aggiungi attività [gioca a pallavolo](activity) in categoria [sport](category) alle 5:12
- ciao, vorrei aggiungere un'attività nella lista [hobby](category) alle 3:29
- aggiungi [andare dai genitori](activity) in [famiglia](category) alle 20:00
- inserire [ascoltare musica](activity) alle 3:00
- inserisci attività [apportare correzioni](activity) in categoria [lavoro](category) alle 13:39
- aggiungi [organizzare la cucina](activity) nella categoria [casa](category)
- inserire [prenotare le vacanze](activity) nella categoria [vacanza](category) alle 4:25
- inserisci l'attività [prenotare il pub](activity) in [amicizia](category) alle 19:41
- vorrei inserire la nuova attività [discoteca](activity) alla categoria [divertimento](category)
- aggiungere [fare un ripasso di matematica](activity) nella categoria [lezioni](category) alle 16:30
- ciao, voglio aggiungere un'attività [parrucchiere](activity) nella categoria [benessere](category)
- inserire [chiamare il medico](activity) nella categoria [salute](category) alle 22:20
- inserisci [organizzare l'armadio](activity) nella categoria [abbigliamento](category)
- inserisci [fare jogging](activity)
- ciao, aggiungi [psicologo](activity) nella categoria [mente](category)
- ciao, voglio inserire un'attività nell'elenco [business](category)
- aggiungi un'attività in [musica](category)
- ciao, voglio inserire un'attività nell'elenco [faccende domestiche](category)
- inserisci attività [controllare e-mail](activity) in [lavoro](category) alle 9:40
- inserisci una nuova attività [guardare la partita](activity)
- nella categoria [benessere](category) aggiungere l'attività [andare dal parrucchiere](activity) alle 21:10
- ciao, nella categoria [creatività](category) inserisci [dipingere](activity)
- inserire [chiamare mia madre](activity) nella categoria [famiglia](category) alle 19:00
- metti l'attività [fare un bagno](activity) in [cura personale](category)
- ciao, aggiungi [cucinare la cena](activity) nella categoria [casa](category)
- vorrei creare l'attività [festa di compleanno](activity) all'elenco [eventi](category)
- inserire l'attività [e-mail](activity) nella categoria [consegne](category) alle 9:40
- inserisci [il compleanno del mio amico](activity) in [eventi](category) alle 14:50

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
