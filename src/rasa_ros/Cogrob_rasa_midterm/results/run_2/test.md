## intent:bot_challenge
- Sei un bot?

## intent:goodbye
- arrivederci
- è stato un piacere

## intent:help
- Ho bisogno di assistenza
- Aiutami

## intent:greet
- Buongiorno
- Salve

## intent:affirm
- affermativo
- si

## intent:mood_great
- Super entusiasta
- Mi sento molto bene
- Così perfetto

## intent:mood_unhappy
- Non molto bene
- Così triste

## intent:ask_name
- sai chi sono?
- mi hai già visto prima?
- puoi dire il mio nome?

## intent:deny
- non voglio
- non mi va
- no

## intent:clean_activities
- per favore, elimina tutte le mie attività completate
- rimuovi tutte le mie attività completate
- rimuovi le attività

## intent:view_categories
- voglio vedere tutte le mie categorie
- fammi vedere tutte le mie categorie
- quali sono le categorie create?

## intent:remind_me_of
- aiutami a ricordare un'attività
- non farmi dimenticare di [correre](activity) alle 19:00
- ricordami di [cucinare il pranzo](activity) nella categoria [casa](category) alle 8:30
- voglio impostare un promemoria
- ricordami di [prendere la pillola](activity) in [cura personale](category)
- ricordami l'attività [lezione di chitarra](activity) domani mattina
- ricordami [l'esame](activity) domani mattina

## intent:view_activities
- quali sono le mie attività create per domenica?
- voglio vedere tutte le mie attività
- quali sono le mie attività inserite?
- mostra le attività [completate](activity_status)
- quali sono le mie attività aggiunte per domani?
- mostra le attività nella categoria [progetti](category)
- mostra le attività [incompiute](activity_status) nella categoria [lavoro](category)
- mostra tutte le mie attività [sviluppate](activity_status) nella categoria [mensile](category)

## intent:modify_category
- voglio cambiare la categoria [lavoro]{"entity": "category", "role": "old"} con la categoria [impegni]{"entity": "category", "role": "new"}
- modificare la categoria [giornaliero/settimanale]{"entity": "category", "role": "old"} in [famiglia]{"entity": "category", "role": "new"}
- voglio modificare il nome della categoria [svago]{"entity": "category", "role": "old"} con il nome [divertimento]{"entity": "category", "role": "new"}
- alterare la categoria [tempo libero]{"entity": "category", "role": "old"} con [palestra]{"entity": "category", "role": "new"}
- sostituire la categoria [esami]{"entity": "category", "role": "old"} in [università]{"entity": "category", "role": "new"}
- cambiare il nome della categoria [divertimento]{"entity": "category", "role": "old"} con il nome [cura personale]{"entity": "category", "role": "new"}
- sostituire la categoria [banca]{"entity": "category", "role": "old"} con [vacanza]{"entity": "category", "role": "new"}
- voglio alterare la categoria [annuale]{"entity": "category", "role": "old"} a [estate]{"entity": "category", "role": "new"}

## intent:add_category
- voglio aggiungere la categoria [università](category)
- voglio aggiungere la categoria [stile di vita](category)
- aggiungi la categoria [relazioni](category)
- ciao, voglio inserire la categoria [quotidiana](category)
- metti [sport](category) categoria
- voglio aggiungere una nuova categoria [tempo libero](category)
- metti la categoria [ingegneria](category)
- voglio usare una nuova categoria [eventi](category)
- voglio aggiungere una categoria [pagamenti](category)
- la categoria da inserire è [volontariato](category)
- aggiungi [sport](category)

## intent:modify_activity_deadline
- cambia la scadenza dell'attività [raccogliere fondi](activity)
- per l'attività [prenotare l'aereo](activity) trasforma la scadenza in lunedì
- modifica il termine dell'attività [revisione del progetto](activity) nella categoria [università](category) in domenica
- modifica il termine dell'attività [leggere il giornale](activity) nella categoria [cultura](category) con domenica
- per l'attività [prenotare l'aereo](activity) nella categoria [vacanza](category) trasformare la deadline in lunedì
- voglio modificare la scadenza di un'attività
- altera la deadline dell'attività [pagare il supermercato](activity) nella categoria [pagamenti](category) in domenica
- voglio modificare la deadline dell'attività [scuolacalcio](activity) nella categoria [sport](category) per domani alle 18:00
- per l'attività [invito di compleanno](activity) nella categoria [amici](category) modifica la scadenza con il 22 ottobre 1922
- per l'attività [andare in chiesa](activity) nella categoria [personale](category) modificare la scadenza con 22 ottobre 1922
- modifica la scadenza dell'attività [leggere](activity) nella categoria [università](category) da venerdì a domenica
- per l'attività [studiare in biblioteca](activity) nella categoria [università](category) modifica il termine nel 22 ottobre 1922

## intent:remove_category
- ciao, voglio rimuovere una categoria [cura personale](category)
- categoria da cestinare: [commissioni](category)
- non voglio usare la categoria [eventi](category)
- ciao, per favore rimuovi la seguente categoria [spesa](category)
- voglio togliere la categoria [scuola](category)
- eliminare la vecchia categoria [pagamenti](category)
- ciao, voglio rimuovere la categoria [faccende domestiche](category)
- voglio eliminare la categoria [progetti](category)
- ciao, per favore annulla la seguente categoria [divertimento](category)
- categoria da cancellare: [finanze](category)
- eliminare la categoria [relazioni](category)
- ciao, voglio togliere la categoria [progetti](category)

## intent:set_status_activity
- poni [non fatta](activity_status) l'attività [shampoo](activity) nella categoria [quotidiano](category)
- metti come [non finita](activity_status) [alzati](activity) in [quotidiano](category)
- imposta [sviluppata](activity_status) l'attività [suona la chitarra](activity) nella categoria [musica](category)
- metti [non terminata](activity_status) l'attività [acquistare una bicicletta](activity) in [negozio](category)
- imposta [non fatta](activity_status) l'attività [vai in farmacia](activity) nella categoria [benessere](category)
- imposta [non finita](activity_status) [chiama il medico](activity)
- ciao, imposta come [completa](activity_status) l'attività [partita di pallone](activity) in [palestra](category)
- ciao, voglio porre come [non eseguita](activity_status) [ripetizioni](activity) nella categoria [laurea](category)
- poni come [completato](activity_status) [riposare](activity) in [salute](category)
- imposta come [non sviluppata](activity_status) [giocare a carte](activity)
- voglio impostare [non fatta](activity_status) un'attività in un elenco
- poni [completata](activity_status) [suonare la chitarra](activity)
- ciao, poni [non fatto](activity_status) [pulisci il bagno](activity) in [casa](category)
- imposta [non fatto](activity_status) [ripeti matematica](activity) nella categoria [scuola](category)
- poni come [incompleta](activity_status) l'attività [suonare il pianoforte](activity) in [musica](category)
- imposta [incompleto](activity_status) [andare al mare](activity) in [viaggio](category)

## intent:modify_activity_category
- per l'attività [giocare a pallone](activity) trasforma la categoria [svago]{"entity": "category", "role": "old"} in [sport]{"entity": "category", "role": "new"}
- per l'attività [partecipare alla conferenza](activity) trasforma la categoria [lavoro]{"entity": "category", "role": "old"} in [cultura]{"entity": "category", "role": "new"}
- voglio cambiare la categoria [viaggio]{"entity": "category", "role": "old"} dell'attività [prenotare l'hotel](activity) in [desideri]{"entity": "category", "role": "new"}
- voglio cambiare la categoria [palestra]{"entity": "category", "role": "old"} dell'attività [boxe](activity) con la categoria [sport]{"entity": "category", "role": "new"}
- per l'attività [giocare a carte](activity) cambiare la categoria [amici]{"entity": "category", "role": "old"} in [svago]{"entity": "category", "role": "new"}
- modifica la categoria [dieta]{"entity": "category", "role": "old"} dell'attività [camminare all'aperto](activity)
- voglio cambiare la categoria dell'attività [boxe](activity)
- modifica la categoria dell'attività [andare al mare](activity)
- transformare la categoria [progetto]{"entity": "category", "role": "old"} dell'attività [prepare il powerpoint](activity) in categoria [university]{"entity": "category", "role": "new"}
- per l'attività [uscita con la famiglia](activity) trasforma la categoria [svago]{"entity": "category", "role": "old"} in [tempo libero]{"entity": "category", "role": "new"}
- convertire la categoria [giornaliero/settimanale]{"entity": "category", "role": "old"} dell'attività [yoga](activity)
- trasforma la categoria [progetti]{"entity": "category", "role": "old"} dell'attività [studiare](activity) in categoria [università]{"entity": "category", "role": "new"}
- per l'attività [uscita con la famiglia](activity) trasforma la categoria [tempo libero]{"entity": "category", "role": "old"} in [svago]{"entity": "category", "role": "new"}
- cambia la categoria [esami]{"entity": "category", "role": "old"} dell'attività [studiare](activity) in categoria [progetti]{"entity": "category", "role": "new"}
- cambia la categoria [cura della persona]{"entity": "category", "role": "old"} dell'attività [correre](activity)
- modifica la categoria [vacanze]{"entity": "category", "role": "old"} dell'attività [andare al mare](activity)
- modifica la categoria [svago]{"entity": "category", "role": "old"} dell'attività [andare al mare](activity) in [vacanze]{"entity": "category", "role": "new"}

## intent:modify_activity_name
- voglio cambiare l'attività con il nome [uscire con mia madre]{"entity": "activity", "role": "old"} in [famiglia](category)
- per l'attività [andare a un concerto]{"entity": "activity", "role": "old"} modifica il nome con [andare al teatro]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [nuoto]{"entity": "activity", "role": "old"} nella categoria [sport](category) con il nome [boxe]{"entity": "activity", "role": "new"}
- per l'attività [suonare la chitarra]{"entity": "activity", "role": "old"} nella categoria [tempo libero](category) modifica il nome con [andare a giocare a calcio]{"entity": "activity", "role": "new"}
- modificare il nome dell'attività [yoga]{"entity": "activity", "role": "old"} con nome [pilates]{"entity": "activity", "role": "new"}
- per l'attività [andare a giocare a calcio]{"entity": "activity", "role": "old"} nella categoria [tempo libero](category) modifica il nome con [suonare la chitarra]{"entity": "activity", "role": "new"}
- per l'attività [leggere un giornale]{"entity": "activity", "role": "old"} trasforma il nome con [scrivere un articolo]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [prenotare il treno]{"entity": "activity", "role": "old"} con [prenotare l'aereo]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [andare in montagna]{"entity": "activity", "role": "old"} nella categoria [vacanza](category) con [andare a sciare]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [andare a sciare]{"entity": "activity", "role": "old"} nella categoria [vacanza](category) con [andare in montagna]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [jogging]{"entity": "activity", "role": "old"} nella categoria [sport](category)
- cambia il nome dell'attività [attività all'aperto]{"entity": "activity", "role": "old"} nella categoria [salute fisica](category)
- voglio cambiare il nome dell'attività [editare un video]{"entity": "activity", "role": "old"} con il nome [modificare un video]{"entity": "activity", "role": "new"}
- per l'attività [prendere l'autobus]{"entity": "activity", "role": "old"} in [viaggio](category) trasforma il nome con [prendere il treno]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [yoga]{"entity": "activity", "role": "old"} con il nome [pilates]{"entity": "activity", "role": "new"}
- nella categoria [amicizia](category) sostituisci il nome dell'attività [andare a mangiare una pizza]{"entity": "activity", "role": "old"}
- per l'attività [parrucchiere]{"entity": "activity", "role": "old"} nella categoria [cura personale](category) modifica il nome con [yoga]{"entity": "activity", "role": "new"}
- nella categoria [università](category) cambiare il nome dell'attività [studio]{"entity": "activity", "role": "old"}  con nome [esame]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [pulire il giardino]{"entity": "activity", "role": "old"} con il nome [preparare la colazione]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [modificare un video]{"entity": "activity", "role": "old"} con il nome [editare un video]{"entity": "activity", "role": "new"}
- per l'attività [prendere il treno]{"entity": "activity", "role": "old"} in [viaggio](category) trasforma il nome con [prendere l'autobus]{"entity": "activity", "role": "new"}

## intent:remove_item
- rimuovi [andare all'ufficio postale](activity) nella categoria [pacchi](category) alle 17:30
- elimina l'attività [inviare un'email](activity) nella categoria [scadenze](category)
- cancella [pulire la casa](activity) nella categoria [faccende domestiche](category) alle 19:00
- rimuovi [revisione del progetto](activity) nella categoria [lavoro](category) alle 10:25
- cancella [andare a cantare](activity) alle 11:00
- elimina l'attività [suonare il pianoforte](activity) nella categoria [musica](category)
- ciao, voglio eliminare un'attività dall'elenco [genitori](category)
- ciao, voglio cancellare un'attività nella categoria [marketing](category) alle 18:30
- voglio cancellare un'attività nella categoria [generi alimentari](category) alle 9:40
- cancella [andare a un incontro](activity) nella categoria [lavoro](category) alle 4:25
- ciao, voglio cancellare un'attività nella categoria [sociale](category) alle 14:50
- ciao, voglio cancellare un'attività nella categoria [blog](category) alle 17:30
- cancella [parrucchiere](activity) nella categoria [benessere](category) alle 13:39
- voglio cancellare un'attività nella categoria [comunicazione](category) alle 21:10
- elimina l'attività [andare in banca](activity) nella categoria [finanza](category)
- elimina l'attività [allenarsi](activity) nella categoria [benessere](category)
- cancella [andare al mercato](activity) nella categoria [spesa](category) alle 21:10
- voglio rimuovere un'attività da un elenco
- ciao, voglio cancellare un'attività dall'elenco [pianificazioni](category)
- elimina l'attività [giocare](activity) nella categoria [intrattenimento](category)
- rimuovi [dentista](activity) nella categoria [assistenza sanitaria](category) alle 22:20
- elimina l'attività [psicologo](activity) nella categoria [mente](category)
- ciao, voglio cancellare un'attività nella mia lista alle 18:14

## intent:presentation
- [grazia](name)
- sono [antonio](name)
- il mio nome è [matti](name)
- [giusy](name)
- [tiziano](name)
- [vito](name)
- [marianna](name)
- [jhon](name)
- [riccardino](name)
- [andrew](name)
- [geppy](name)
- [elga](name)
- [betti](name)
- [sonia](name)
- [guendalina](name)
- sono [carla](name)
- [piero](name)
- [adele](name)
- [azzurra](name)
- [salvatore](name)
- [lorella](name)
- voglio creare un account
- sono [antonino](name)
- [galatea](name)
- [isa](name)
- [nik](name)
- sono [giulio](name)
- sono [simone](name)
- il mio nome è [ferdi](name)
- [fabiano](name)
- [andrea](name)
- [giovanni](name)
- [edvige](name)
- [alessandra](name)
- [olivia](name)
- [clerice](name)

## intent:inform
- [lavori](category)
- [da comprare](category)
- [studio](activity)
- [quotidiano](category)
- tra 4 ore
- [mensile](category)
- [farmaci](category)
- [saldare prestito](activity)
- [viaggi](category)
- [cose da fare oggi](category)
- [rata casa](activity)
- [giocare ai videogiochi](activity)
- 09/12/2030 alle 13:00
- [eventi](category)
- [carrello](category)
- [vacanza](category)
- [carro](category)
- [università](category)
- [laboratorio](category)
- [nuotare](activity)
- [tempo libero](category)
- [correre](activity)
- [presentare domanda](activity)
- [giocare partita](activity)
- [corda](activity)
- [fare patente](activity)
- 26 minuti e 30 secondi
- [fisioterapia](activity)
- [cercare](activity)
- [nuoto](activity)
- [accompagnare mio figlio](activity)
- lunedì prossimo
- [palestra](category)
- [guardare mio figlio](activity)
- [cena con i parenti](activity)
- alle 18:00
- [sfizi](category)
- da oggi a domani
- [relax](activity)
- [volontariato](category)
- [famiglia](category)
- [riscuotere affitto](activity)
- [borsa](category)
- [vacanze](category)

## intent:add_item
- inserisci l'attività [andare in farmacia](activity)
- ciao, voglio inserire un'attività nell'elenco [priorità](category)
- inserisci [andare in palestra](activity)
- inserisci [portare fuori il cane](activity) alle 3:00
- inserire [prenotazione](activity) alle 00:00
- metti [preparare la presentazione](activity) in [progetti](category)
- voglio inserire un'attività nella lista [piacere](category) alle 9:40
- ciao, voglio creare l'attività [andare nel centro della città](activity) nell'elenco [commissioni](category)
- inserire l'attività [ripetere](activity) nella categoria [esame](category) alle 22:20
- inserisci l'attività [fare yoga](activity) nella categoria [benessere](category)
- ciao, vorrei inserire un'attività nella lista [politica](category) alle 17:30
- ciao, voglio creare un'attività per la lista [primavera](category)
- ciao, voglio inserire un'attività [ripetizioni](activity) nella categoria [laurea](category)
- inserisci [push del codice](activity) in [informatica](category) alle 22:20
- voglio aggiungere un'attività nell'elenco [leadership](category)
- aggiungi [pulire la casa](activity) nella categoria [casa](category)
- ciao, vorrei inserire un'attività nell'elenco [coaching](category) alle 19:00
- ciao, aggiungi [psicologo](activity) nella categoria [mente](category)
- ciao, inserisci [scrittura](activity) nella categoria [hobby](category)
- ciao, voglio inserire un'attività nella lista [impegni](category)
- ciao, aggiungi [cucinare la cena](activity) nella categoria [casa](category)
- voglio aggiungere un'attività nell'elenco [necessari](category)
- ciao, voglio inserire una nuova attività [leggere un paper](activity) nell'elenco [ricerca](category)
- inserire [chiamare mia madre](activity) nella categoria [famiglia](category) alle 19:00
- aggiungi l'attività [cantare](activity)
- inserisci [yoga](activity)
- ciao, vorrei inserire un'attività in un elenco [spesa](category) alle 21:10
- inserire [chiamare il medico](activity) nella categoria [salute](category) alle 22:20
- inserisci una nuova attività [giardinaggio](activity)
- nella categoria [vacanze](category), voglio inserire un'attività [cena di Natale](activity)
- inserisci l'attività [giocare a basket](activity)
- metti attività [autobus](activity) in categoria [quotidiano](category) alle 3:29
- vorrei creare una nuova attività
- voglio aggiungere un'attività alla lista [divertimento](category) alle 21:10
- aggiungi [fare una passeggiata all'aria aperta](activity) in [tempo libero](category) oggi alle 12
- ciao, inserisci [leggere](activity)
- inserire l'attività [acquistare fiori](activity) nella categoria [spesa](category) alle 13:39
- ciao, inserisci l'attività [fare un ripasso di scienze](activity) nella categoria [scuola](category)
- ciao, inserisci [taekwondo](activity) nella categoria [arti marziali](category)
- vorrei aggiungere un'attività
- inserire l'attività [preparare lo zaino](activity) nella categoria [organizzazione](category) alle 18:30
- aggiungi [fare selfie](activity) alle 01:45
- ciao, inserisci [cena con i nonni](activity)
- ciao, voglio inserire un'attività nell'elenco [faccende domestiche](category)
- ciao, vorrei inserire un'attività nella categoria [giustizia](category) alle 22:20
- inserire [prenotare il treno](activity) nella categoria [viaggio](category) alle 6:30
- ciao, voglio inserire un'attività nell'elenco [business](category)
- voglio inserire un'attività nell'elenco [documentazione](category)
- ciao, inserisci l'attività [riparare l'auto](activity) nella categoria [impegni](category)
- aggiungi l'attività [pulire](activity) in [casa](category)
- metti attività [pizza](activity) in [amici](category) alle 7:00
- voglio aggiungere un'attività alla lista [cura del corpo](category)
- vorrei creare l'attività [github](activity) all'elenco [progetti](category)
- vorrei mettere l'attività [pagare le bollette](activity) alla categoria [banca](category)
- ciao, inserisci l'attività [mandare e-mail](activity) nella categoria [progetti](category)
- inserisci [organizzare l'armadio](activity) nella categoria [abbigliamento](category)

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
