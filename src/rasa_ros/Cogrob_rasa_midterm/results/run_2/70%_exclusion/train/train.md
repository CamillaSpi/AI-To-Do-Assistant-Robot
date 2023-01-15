## intent:bot_challenge
- Sto parlando con un bot?
- Sei un bot?

## intent:goodbye
- è stato un piacere
- ci si vede

## intent:help
- Non so cosa fare
- Cosa facciamo adesso?

## intent:greet
- Hey
- buona mattina
- ciao

## intent:affirm
- sisi
- indubbiamente

## intent:mood_great
- Super entusiasta
- Così perfetto
- Sto per salvare il mondo

## intent:ask_name
- dimmi il mio nome
- mi hai riconosciuto?
- qual è il mio nome?

## intent:mood_unhappy
- Super triste
- Non mi sento molto bene
- La mia giornata è stata orribile

## intent:deny
- n
- non mi va
- no
- negativo

## intent:clean_activities
- cancella tutte le mie attività completate
- rimuovi le attività
- elimina le attività

## intent:view_categories
- fammi vedere tutte le mie categorie
- mostrami tutte le categorie create
- mostrami le mie categorie
- quali sono le categorie create?

## intent:remind_me_of
- non posso dimenticare di fare l'attività [andare alla posta](activity) nella categoria [commissioni](category) lunedi prossimo
- imposta un promemoria per l'attività [chiamare il dottore](activity) nella categoria [visite mediche](category) nella prossima mattina
- non posso dimenticare di fare l'attività [parlare con il professore](activity) nella categoria [progetto](category) per domenica prossima
- ricordami [l'esame](activity) domani mattina
- imposta un promemoria
- aiutami a ricordare di [andare al compleanno](activity) il 12/18/2022
- aiutami a non dimenticare l'attività [ascoltare la registrazione della lezione](activity) nella categoria [università](category) per domani
- ricordami l'attività [lezione di chitarra](activity) domani mattina
- aiutami a ricordare un'attività

## intent:view_activities
- voglio vedere tutte le mie attività
- voglio vedere tutte le mie attività [incomplete](activity_status)
- mostra le attività [completate](activity_status)
- mostrami attività [eseguite](activity_status) nella categoria [scuola](category)
- cosa ho da fare?
- fammi vedere le attività per mercoledì sera
- voglio vedere tutte le mie attività [completate](activity_status)
- quali sono le mie attività?
- mostra attività nella categoria [palestra](category) per questa sera

## intent:modify_category
- sostituire la categoria [banca]{"entity": "category", "role": "old"} nella categoria [finanza]{"entity": "category", "role": "new"}
- per favore, cambiare la categoria [cura della persona]{"entity": "category", "role": "old"} con la categoria [università]{"entity": "category", "role": "new"}
- variare il nome della categoria [personale]{"entity": "category", "role": "old"} con il nome [sport]{"entity": "category", "role": "new"}
- variare la categoria [famiglia]{"entity": "category", "role": "old"} con [giornaliero/settimanale]{"entity": "category", "role": "new"}
- per favore, variare la categoria [finanza]{"entity": "category", "role": "old"} nella categoria [banca]{"entity": "category", "role": "new"}
- convertire la categoria [genitori]{"entity": "category", "role": "old"} con [casa]{"entity": "category", "role": "new"}
- voglio alterare la categoria [annuale]{"entity": "category", "role": "old"} a [estate]{"entity": "category", "role": "new"}
- trasformare la categoria [vacanza]{"entity": "category", "role": "old"} in [banca]{"entity": "category", "role": "new"}
- cambiare il nome della categoria [divertimento]{"entity": "category", "role": "old"} con il nome [cura personale]{"entity": "category", "role": "new"}
- cambiare la categoria [università]{"entity": "category", "role": "old"} con la categoria [cura della persona]{"entity": "category", "role": "new"}

## intent:add_category
- voglio aggiungere una categoria [pagamenti](category)
- inserisci [tempo libero](category) categoria
- voglio aggiungere la categoria [università](category)
- metti [sport](category) categoria
- voglio aggiungere una categoria
- la categoria da aggiungere è [università](category)
- metti la categoria [ingegneria](category)
- inserisci [vacanze](category) categoria
- ciao, voglio inserire una nuova categoria [ricerca](category)
- ciao, voglio inserire la categoria [quotidiana](category)
- ciao, inserisci la seguente categoria [spesa](category)
- inserisci [amici](category)
- nuova categoria: [lavoro](category)

## intent:modify_activity_deadline
- modifica la scadenza dell'attività [piscina](activity) con mercoledì
- modifica il termine dell'attività [revisione del progetto](activity) nella categoria [università](category)
- altera la scadenza dell'attività [cantare](activity) in domenica
- altera la deadline dell'attività [pagare il supermercato](activity) nella categoria [pagamenti](category) in domenica
- voglio modificare la deadline dell'attività [suonare la chitarra](activity) nella categoria [musica](category) in domani alle 18:00
- nella categoria [assistenza sanitaria](category) modificare la scadenza dell'attività [prenotare visita medica](activity) da 22 settembre a 25 settembre
- sostituisci la scadenza dell'attività [torneo di calcio](activity)
- altera la deadline dell'attività [pagare le bollette](activity) da domenica a mercoledì
- alterare la scadenza
- voglio cambiare il termine dell'attività [ascoltare il podcast](activity) nella categoria [musica](category) con 27 settembre 1998
- altera la scadenza dell'attività [cena di Natale](activity) nella categoria [eventi](category)
- nella categoria [famiglia](category) sostituisci il termine dell'attività [accompagnare mio figlio](activity)
- altera la scadenza dell'attività [aiutare il nonno](activity) alle 22:00
- per l'attività [studiare in biblioteca](activity) nella categoria [università](category) modifica il termine nel 22 ottobre 1922

## intent:remove_category
- voglio eliminare la categoria [sport](category)
- ciao, voglio eliminare la categoria [finanza](category)
- voglio togliere una categoria [tempo libero](category)
- ciao, voglio togliere la categoria [lavoro](category)
- non voglio usare la categoria [medico](category)
- ciao, per favore cestina la seguente categoria [finanza](category)
- rimuovi [sport](category) dalle mie categorie
- voglio rimuovere la categoria [impegni](category)
- categoria da togliere: [cura personale](category)
- voglio togliere la categoria [settimanale](category)
- ciao, voglio rimuovere una categoria [cura personale](category)
- ciao, voglio togliere la categoria [assistenza sanitaria](category)
- voglio eliminare la categoria [progetti](category)
- voglio eliminare la categoria [giornaliera](category)
- togliere la categoria [svago](category)

## intent:set_status_activity
- imposta come [fatta](activity_status) [leggere](activity)
- ciao, voglio porre come [eseguito](activity_status) [ripetizioni](activity) nella categoria [laurea](category)
- imposta [sviluppata](activity_status) l'attività [suona la chitarra](activity) nella categoria [musica](category)
- imposta [incompleto](activity_status) [ripetere la presentazione](activity) nella categoria [progetti](category)
- ciao, voglio porre come [non eseguita](activity_status) [ripetizioni](activity) nella categoria [laurea](category)
- imposta [non sviluppata](activity_status) l'attività [suona la chitarra](activity) nella categoria [musica](category)
- ciao, metti [completa](activity_status) l'attività [jogging](activity) in [salute fisica](category)
- poni [completata](activity_status) [suonare la chitarra](activity)
- imposta come [non sviluppata](activity_status) [giocare a carte](activity)
- imposta [fatta](activity_status) l'attività [vai in farmacia](activity) nella categoria [benessere](category)
- imposta [fatto](activity_status) [powerpoint](activity) nella categoria [programmi](category)
- imposta [incompleta](activity_status) [spegni il forno](activity) in [casa](category)
- poni come [completata](activity_status) l'attività [suonare il pianoforte](activity) in [musica](category)
- imposta [incompleta](activity_status) [ascoltare musica](activity) in [personale](category)
- ciao, voglio impostare [non completata](activity_status) l'attività [taekwondo](activity) nella categoria [arti marziali](category)
- voglio impostare [non completata](activity_status) l'attività [postare selfie](activity) in [sociale](category)
- imposta come [non conclusa](activity_status) [giardinaggio](activity) nella categoria [giardino](category)
- imposta [non fatto](activity_status) [ripeti matematica](activity) nella categoria [scuola](category)
- ciao, poni [non fatto](activity_status) [pulisci il bagno](activity) in [casa](category)

## intent:modify_activity_category
- per l'attività [partecipare alla conferenza](activity) trasforma la categoria [cultura]{"entity": "category", "role": "old"} in [lavoro]{"entity": "category", "role": "new"}
- modificare la categoria [pranzo]{"entity": "category", "role": "old"} dell'attività [pranzo di lavoro](activity) in [lavoro]{"entity": "category", "role": "new"}
- transformare la categoria [progetto]{"entity": "category", "role": "old"} dell'attività [prepare il powerpoint](activity) in categoria [university]{"entity": "category", "role": "new"}
- per l'attività [ritirare il pacco](activity) aggiornare la categoria [commissioni]{"entity": "category", "role": "old"} in [imminente]{"entity": "category", "role": "new"}
- trasforma la categoria [progetti]{"entity": "category", "role": "old"} dell'attività [studiare](activity) in categoria [università]{"entity": "category", "role": "new"}
- sostituire la categoria [Natale]{"entity": "category", "role": "old"} dell'attività [fare i regali](activity) con la categoria [tempo libero]{"entity": "category", "role": "new"}
- modifica la categoria [tempo libero]{"entity": "category", "role": "old"} di [camminare all'aperto](activity) in [dieta]{"entity": "category", "role": "new"}
- trasforma la categoria [studio]{"entity": "category", "role": "old"} dell'attività [preparare l'esame](activity) in categoria [università]{"entity": "category", "role": "new"}
- cambia la categoria [cura della persona]{"entity": "category", "role": "old"} dell'attività [correre](activity)
- modifica la categoria [dieta]{"entity": "category", "role": "old"} di [camminare all'aperto](activity) in [tempo libero]{"entity": "category", "role": "new"}
- modifica la categoria [dieta]{"entity": "category", "role": "old"} dell'attività [camminare all'aperto](activity)
- per l'attività [riposare](activity) modificare la categoria [stile di vita]{"entity": "category", "role": "old"} in [dieta]{"entity": "category", "role": "new"}
- trasforma la categoria [università]{"entity": "category", "role": "old"} dell'attività [preparare il powerpoint](activity) in categoria [progetto]{"entity": "category", "role": "new"}
- modifica la categoria [svago]{"entity": "category", "role": "old"} dell'attività [andare al mare](activity) in [vacanze]{"entity": "category", "role": "new"}
- per l'attività [andare in farmacia](activity) modificare la categoria [salute personale]{"entity": "category", "role": "old"} in [salute]{"entity": "category", "role": "new"}
- per l'attività [andare al mercato](activity) aggiorna la categoria [spesa]{"entity": "category", "role": "old"} in [impegni domestici]{"entity": "category", "role": "new"}
- convertire la categoria [giornaliero/settimanale]{"entity": "category", "role": "old"} dell'attività [yoga](activity) con [sport]{"entity": "category", "role": "new"}
- per l'attività [giocare a pallone](activity) trasforma la categoria [sport]{"entity": "category", "role": "old"} in [svago]{"entity": "category", "role": "new"}
- voglio cambiare la categoria [viaggio]{"entity": "category", "role": "old"} dell'attività [prenotare l'hotel](activity) in [desideri]{"entity": "category", "role": "new"}
- per l'attività [pulire la casa](activity) nella categoria [faccende domestiche]{"entity": "category", "role": "old"} sostituire la categoria con [quotidiano]{"entity": "category", "role": "new"}
- sostituisci la categoria [faccende domestiche]{"entity": "category", "role": "old"} dell'attività [preparare la colazione](activity)

## intent:modify_activity_name
- modifica il nome dell'attività [pulire la casa]{"entity": "activity", "role": "old"} nella categoria [faccende domestiche](category)
- per l'attività [andare a giocare a calcio]{"entity": "activity", "role": "old"} nella categoria [tempo libero](category) modifica il nome con [suonare la chitarra]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [boxe]{"entity": "activity", "role": "old"} nella categoria [sport](category) con il nome [nuoto]{"entity": "activity", "role": "new"}
- per l'attività [andare al cinema]{"entity": "activity", "role": "old"} trasforma il nome con [andare a teatro]{"entity": "activity", "role": "new"}
- nella categoria [università](category) cambiare il nome dell'attività [studio]{"entity": "activity", "role": "old"}  con nome [esame]{"entity": "activity", "role": "new"}
- nella categoria [università](category) cambiare il nome dell'attività [esame]{"entity": "activity", "role": "old"}  con nome [studio]{"entity": "activity", "role": "new"}
- per l'attività [parrucchiere]{"entity": "activity", "role": "old"} nella categoria [cura personale](category) modifica il nome con [yoga]{"entity": "activity", "role": "new"}
- per l'attività [suonare la chitarra]{"entity": "activity", "role": "old"} nella categoria [tempo libero](category) modifica il nome con [andare a giocare a calcio]{"entity": "activity", "role": "new"}
- per l'attività [prendere l'autobus]{"entity": "activity", "role": "old"} in [viaggio](category) trasforma il nome con [prendere il treno]{"entity": "activity", "role": "new"}
- modifica il nome di una attività
- per l'attività [completare il powerpoint]{"entity": "activity", "role": "old"} modifica il nome con [completare la relazione]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [andare a nuotare]{"entity": "activity", "role": "old"} con [andare al parco]{"entity": "activity", "role": "new"}
- per l'attività [scrivere un articolo]{"entity": "activity", "role": "old"} trasforma il nome con [leggere un giornale]{"entity": "activity", "role": "new"}
- sostituisci il nome dell'attività [scrivere l'articolo]{"entity": "activity", "role": "old"}  con il nome [pubblicare l'articolo]{"entity": "activity", "role": "new"}
- nella categoria [eventi](category) cambia il nome dell'attività [tagliare i capelli]{"entity": "activity", "role": "old"}
- sostituisci il nome dell'attività [camminare]{"entity": "activity", "role": "old"}  con il nome [imparare l'inglese]{"entity": "activity", "role": "new"}
- per l'attività [andare a teatro]{"entity": "activity", "role": "old"} trasforma il nome con [andare al cinema]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [andare al parco]{"entity": "activity", "role": "old"} con [andare a nuotare]{"entity": "activity", "role": "new"}
- nella categoria [scuola](category) sostituisci il nome dell'attività [compito di matematica]{"entity": "activity", "role": "old"}  con il nome [interrogazione di matematica]{"entity": "activity", "role": "new"}
- per l'attività [completare la relazione]{"entity": "activity", "role": "old"} modifica il nome con [completare il powerpoint]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [andare dal dentista]{"entity": "activity", "role": "old"} con il nome [andare dal dottore]{"entity": "activity", "role": "new"}
- nella categoria [eventi](category) cambia il nome dell'attività [tagliare i capelli]{"entity": "activity", "role": "old"}  con il nome [andare dal parrucchiere]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [yoga]{"entity": "activity", "role": "old"} con il nome [pilates]{"entity": "activity", "role": "new"}
- per l'attività [andare al teatro]{"entity": "activity", "role": "old"} modifica il nome con [andare a un concerto]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [prenotare l'aereo]{"entity": "activity", "role": "old"} con [prenotare il treno]{"entity": "activity", "role": "new"}

## intent:remove_item
- voglio cancellare un'attività nella categoria [generi alimentari](category) alle 9:40
- cancella [passeggiata](activity) nella categoria [giornaliera](category) alle 7:00
- cancella [studiare](activity) nella categoria [scuola](category) alle 19:00
- ciao, voglio cancellare un'attività nella categoria [marketing](category) alle 18:30
- elimina l'attività [giocare](activity) nella categoria [intrattenimento](category)
- rimuovi l'attività [leggere il giornale](activity) nella categoria [cultura](category)
- ciao, voglio cancellare un'attività nella categoria [stile di vita](category) alle 16:00
- elimina [shampoo](activity) nella categoria [quotidiana](category)
- elimina [alzarsi](activity)
- elimina [riposo](activity) nella categoria [salute](category)
- ciao, voglio eliminare un'attività dall'elenco [genitori](category)
- rimuovi l'attività [boxe](activity) nella categoria [settimanale](category)
- ciao, voglio cancellare un'attività nella categoria [cura](category) alle 3:29
- cancellare l'attività [correggere i compiti](activity) nella categoria [lavoro](category)
- cancella [arrampicata](activity) nella categoria [estate](category) alle 18:30
- cancella [windsurf](activity) alle 01:45
- voglio rimuovere un'attività da un elenco
- rimuovi [videoconferenza](activity) nella categoria [teamwork](category)
- cancella [andare in chiesa](activity) nella categoria [personale](category) alle 19:41
- cancella [camminare](activity) nella categoria [salute personale](category) alle 6:30
- cancella [aiutare mia madre](activity) alle 01:45
- rimuovi [uscire](activity) nella categoria [società](category) alle 17:30
- ciao, voglio cancellare un'attività dall'elenco [pianificazioni](category)
- rimuovi [annaffiare le piante](activity) nella categoria [faccende domestiche](category) alle 13:29
- cancellare l'attività [fare jogging](activity) nella categoria [cura personale](category)
- voglio eliminare un'attività dall'elenco [documenti](category)

## intent:presentation
- [gerry](name)
- [kikka](name)
- ciao il mio nome è [Kevin](name)
- [teresa](name)
- [diodato](name)
- [giustino](name)
- [gianni](name)
- [natascia](name)
- [pino](name)
- [adele](name)
- ciao, sono [matteo](name)
- [azzurra](name)
- [Foca](name)
- [aristide](name)
- [francesca](name)
- [raffaella](name)
- [donatello](name)
- [rametta](name)
- [ursola](name)
- impostare un utente
- [valerio](name)
- [anacleto](name)
- [giorgina](name)
- ciao, sono [pierfrancesco](name)
- ciao, sono [marco](name)
- [giusy](name)
- sono [carolina](name)
- [guendalina](name)
- sono [antonio](name)
- [violeta](name)
- [cinzia](name)
- il mio nome è [Ugo](name)
- sono [giulio](name)
- [betti](name)
- [jhon](name)
- [edvige](name)
- fammi iscrivere
- [nik](name)
- [peppe](name)
- [speranza](name)
- [andrew](name)
- voglio iscrivermi
- [amadeo](name)
- [stefano](name)

## intent:inform
- [compiti](category)
- [nuotare](activity)
- [carrello](category)
- [prendere appunti](activity)
- [cucinare](activity)
- [analisi](activity)
- [andare in biblioteca](activity)
- [viaggio in Brasile](activity)
- [rata casa](activity)
- [scuola](category)
- [lavori](category)
- [andare a fare shopping](activity)
- [prenotare il ristorante](activity)
- [corda](activity)
- [andare nello studio](activity)
- [aggiustare la porta](activity)
- [fare shopping](activity)
- [escursione](activity)
- [partitella](activity)
- [viaggio in spagna](activity)
- [volontariato](category)
- [suonare](activity)
- [quotidiano](category)
- 26 minuti e 30 secondi
- [to do](category)
- [uscire in barca](activity)
- [aggiustare orologio](activity)
- [cose da fare oggi](category)
- [armadietto](category)
- [fare un ripasso di matematica](activity)
- [laboratorio](category)
- [tempo libero](category)
- [macchine](category)
- [musica](category)
- [correre](activity)
- [obiettivi](category)
- [dipingere](activity)
- [biblioteca](category)
- il prossimo venerdì
- [film da vedere](category)
- [calendario](category)
- [ritirare stipendio](activity)
- [porto](category)
- [esame patente](activity)
- [allenamenti](category)
- [ristorante](category)
- [fare il rifornimento](activity)
- [da comprare](category)
- oggi
- [saldare prestito](activity)
- [multa](activity)
- 14 settembre 2022
- [inviare un'e-mail al capo](activity)

## intent:add_item
- nella categoria [vacanze](category), voglio inserire un'attività [cena di Natale](activity)
- inserisci l'attività [annaffiare le piante](activity) nella categoria [casa](category)
- ciao, vorrei inserire un'attività in un elenco [spesa](category) alle 21:10
- ciao, vorrei inserire un'attività nella mia lista alle 18:14
- inserire [prenotare le vacanze](activity) nella categoria [vacanza](category) alle 4:25
- ciao, vorrei inserire un'attività nella lista [cultura](category) alle 16:00
- voglio inserire un'attività nell'elenco [documentazione](category)
- ciao, inserisci [guardare lo spettacolo](activity) nella categoria [interesse](category)
- metti [preparare la presentazione](activity) in [progetti](category)
- ciao, voglio inserire un'attività [webcall](activity) nella categoria [lavoro](category)
- aggiungi [suonare il pianoforte](activity) in [musica](category)
- inserisci [prendere la pillola](activity) alle 9:30
- ciao, inserisci l'attività [riparare l'auto](activity) nella categoria [impegni](category)
- ciao, voglio aggiungere un'attività [parrucchiere](activity) nella categoria [benessere](category)
- ciao, inserisci [andare a cantare](activity) nella categoria [tempo libero](category)
- ciao, vorrei inserire l'attività nell'elenco [imminente](category) alle 16:30
- aggiungi [organizzare la cucina](activity) nella categoria [casa](category)
- ciao, voglio inserire un'attività in un elenco
- ciao, voglio inserire una nuova attività [cena con gli amici](activity) nella categoria [amicizia](category)
- vorrei mettere una nuova attività [fare shopping](activity) in [personale](category)
- inserire [studiare per interrogazione](activity) nella categoria [scuola](category) alle 19:00
- nella categoria [salute](category) inserisci un'attività [andare dal medico](activity)
- ciao, vorrei inserire un'attività nell'elenco [coaching](category) alle 19:00
- ciao, vorrei inserire un'attività nell'elenco [marketing](category) alle 17:30
- voglio creare un'attività nella mia lista
- ciao, aggiungi [cucinare la cena](activity) nella categoria [casa](category)
- ciao, voglio inserire una nuova attività nella categoria [autunno](category)
- inserisci [il compleanno del mio amico](activity) in [eventi](category) alle 14:50
- ciao, voglio inserire un'attività [pagare le bollette](activity) nella categoria [finanza](category)
- metti attività [pizza](activity) in [amici](category) alle 7:00
- aggiungi l'attività [inviare il codice](activity) in [impegni](category)
- ciao, voglio inserire un'attività [imparare lo spagnolo](activity) nella categoria [cultura](category)
- ciao, vorrei inserire un'attività in un elenco alle 13:39
- aggiungi [fare le pulizie](activity) in [settimanale](category)
- aggiungi [correre](activity)
- inserire [chiamare mia madre](activity) nella categoria [famiglia](category) alle 19:00
- ciao, voglio creare l'attività [giardinaggio](activity) nell'elenco [giardino](category)
- ciao, inserisci [scrittura](activity) nella categoria [hobby](category)
- ciao, vorrei aggiungere un'attività nella lista [teatro](category) alle 18:30
- aggiungere [robotica](activity) nella categoria [università](category) alle 8:00
- inserire [andare al supermercato](activity) nella categoria [cibo](category) alle 6:30
- ciao, inserisci l'attività [andare a teatro](activity) nella categoria [arte](category)
- aggiungi attività [gioca a pallavolo](activity) in categoria [sport](category) alle 5:12
- vorrei creare un'attività nella categoria [pianificazioni](category) alle 6:30
- ciao, inserisci l'attività [giocare a carte](activity) nella categoria [divertimento](category)
- vorrei mettere l'attività [pagare le bollette](activity) alla categoria [banca](category)
- voglio inserire una nuova attività in una categoria alle 13:39
- ciao, voglio inserire un'attività nell'elenco [priorità](category)
- aggiungere [cucinare per cena](activity) alle 20:45
- metti l'attività [ricerca](activity) in [aggiornamenti](category) alle 18:30
- inserisci [nuotare](activity) in [sport](category)
- voglio inserire una nuova attività nell'elenco [spettacolo](category)
- ciao, crea [chiamata di gruppo](activity) nella categoria [studio](category)
- ciao, nella categoria [creatività](category) inserisci [dipingere](activity)
- ciao, vorrei aggiungere un'attività all'elenco [spesa](category) alle 6:30
- aggiungere l'attività [spegnere la luce](activity) nella categoria [necessari](category) alle 3:29
- nella categoria [corso](category) inserire [incontro](activity) alle 20:30
- aggiungi [prenota il volo](activity) in categoria [viaggio](category) alle 16:30
- inserisci l'attività [leggere](activity) nella categoria [cultura](category)
- vorrei inserire un'attività alla categoria [cura della mente](category)
- vorrei inserire una nuova attività [manicure](activity) all'elenco [estetica](category)
- voglio aggiungere un'attività nell'elenco [leadership](category)
- ciao, voglio inserire un'attività nell'elenco [imminenti](category)
- ciao, voglio inserire un'attività nell'elenco [business](category)
- aggiungi nuova attività [andare al teatro](activity) in [cultura](category) alle 12:35
- aggiungi un'attività in [musica](category)
- ciao, vorrei inserire un'attività nell'elenco [stile di vita](category) alle 14:50

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
