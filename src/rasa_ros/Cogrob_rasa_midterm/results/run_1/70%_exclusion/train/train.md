## intent:bot_challenge
- Sto parlando con un umano?
- Sei un umano?

## intent:goodbye
- alla prossima
- ciao ciao

## intent:help
- Cosa puoi fare?
- Ho bisogno di aiuto

## intent:greet
- buona mattina
- Salve
- Ehi

## intent:affirm
- esattamente
- indubbiamente

## intent:mood_great
- Grandioso
- Sto per salvare il mondo
- Sono grande

## intent:ask_name
- mi riconosci?
- mi hai già visto prima?
- dici il mio nome

## intent:mood_unhappy
- Molto triste
- Così triste
- Infelice

## intent:deny
- non mi va
- no
- n
- non proprio

## intent:clean_activities
- pulisci tutte le attività completate
- cancella tutte le mie attività completate
- rimuovi tutte le attività terminate

## intent:view_categories
- mostra tutte le mie categorie
- quali sono le categorie aggiunte?
- quali sono le categorie create?
- voglio guardare le categorie aggiunte

## intent:remind_me_of
- voglio impostare un promemoria per l'attività [prenotare l'aereo](activity)
- ricordami [l'esame](activity) domani mattina
- imposta un promemoria per l'attività [chiamare la mia ragazza](activity) nella categoria [sociale](category) nella prossima mattina
- ricordami di [cucinare il pranzo](activity) nella categoria [casa](category) alle 8:30
- imposta un promemoria per l'attività [andare al cinema](activity) nella categoria [cultura](category) per domani mattina
- ricordami di [fare shopping](activity) nella categoria [personale](category) alle 8:30
- ricordami la [riunione di lavoro](activity) domani mattina
- ricordami di [mangiare frutta](activity)
- imposta un promemoria per l'attività [chiamare il dottore](activity) nella categoria [visite mediche](category) nella prossima mattina

## intent:view_activities
- mostra le mie attività
- mostra le attività nella categoria [progetti](category)
- mostrami cosa devo fare oggi
- quali sono le mie attività per domani mattina?
- mostra le attività nella categoria [palestra](category)
- mostra le attività [completate](activity_status)
- voglio vedere tutte le attività create
- voglio vedere tutte le mie attività [completate](activity_status)
- quali sono le mie attività [terminate](activity_status)?

## intent:modify_category
- convertire la categoria [genitori]{"entity": "category", "role": "old"} con [casa]{"entity": "category", "role": "new"}
- per favore, voglio sostituire la categoria [cura]{"entity": "category", "role": "old"} a [stile di vita]{"entity": "category", "role": "new"}
- sostituire la categoria [scuola]{"entity": "category", "role": "old"} con [eventi]{"entity": "category", "role": "new"}
- variare la categoria [famiglia]{"entity": "category", "role": "old"} con [giornaliero/settimanale]{"entity": "category", "role": "new"}
- modificare la categoria [giornaliero/settimanale]{"entity": "category", "role": "old"} in [famiglia]{"entity": "category", "role": "new"}
- voglio alterare la categoria [annuale]{"entity": "category", "role": "old"} a [estate]{"entity": "category", "role": "new"}
- voglio variare la categoria [commissioni]{"entity": "category", "role": "old"} in [scadenze]{"entity": "category", "role": "new"}
- voglio modificare una categoria
- modificare la categoria [volontariato]{"entity": "category", "role": "old"} in [sociale]{"entity": "category", "role": "new"}
- variare il nome della categoria [personale]{"entity": "category", "role": "old"} con il nome [sport]{"entity": "category", "role": "new"}

## intent:add_category
- aggiungi [sport](category)
- voglio aggiungere la categoria [università](category)
- nuova categoria: [lavoro](category)
- nuova categoria: [volontariato](category)
- voglio usare una nuova categoria
- voglio usare una nuova categoria [eventi](category)
- crea una nuova categoria
- voglio inserire una categoria
- aggiungi la categoria [relazioni](category)
- nuova categoria: [scuola](category)
- voglio aggiungere la categoria [stile di vita](category)
- categoria: [scuola](category)
- ciao, voglio inserire la categoria [progetti](category)

## intent:modify_activity_deadline
- per l'attività [andare in chiesa](activity) nella categoria [personale](category) modificare la scadenza con 22 ottobre 1922
- per l'attività [prendere le medicine](activity) nella categoria [salute personale](category) trasformare la scadenza in lunedì
- altera la scadenza dell'attività [cena di Natale](activity) nella categoria [eventi](category) con lunedì
- voglio cambiare il termine dell'attività [ascoltare il podcast](activity) nella categoria [musica](category) con 27 settembre 1998
- altera il termine dell'attività [karaoke](activity) da 18:00 alle 20:00
- altera la deadline dell'attività [pagare le bollette](activity) da domenica a mercoledì
- per l'attività [pulire la mia camera da letto](activity) nella categoria [casa](category) trasformare la deadline in lunedì
- voglio modificare la deadline dell'attività [suonare la chitarra](activity) da domani alla prossima settimana
- sostituisci la scadenza dell'attività [torneo di calcio](activity) al 25 novembre
- per l'attività [bollette](activity) nella categoria [finanza](category) modificare la deadline dal 4 novembre al 22 ottobre 1922
- voglio modificare la scadenza di un'attività
- altera la deadline dell'attività [pagare il supermercato](activity) nella categoria [pagamenti](category) in domenica
- nella categoria [famiglia](category) sostituisci il termine dell'attività [accompagnare mio figlio](activity)
- voglio modificare la scadenza dell'attività [disegnare un ritratto](activity) nella categoria [lavoro](category) a domani alle 18:00

## intent:remove_category
- ciao, per favore annulla la seguente categoria [divertimento](category)
- rimuovi una categoria
- voglio togliere la categoria [settimanale](category)
- voglio eliminare la categoria [progetti](category)
- voglio eliminare la categoria [imminente](category)
- ciao, per favore rimuovi la seguente categoria [spesa](category)
- voglio rimuovere la categoria [impegni](category)
- voglio rimuovere una categoria
- ciao, voglio eliminare la categoria [finanza](category)
- eliminare la vecchia categoria [pagamenti](category)
- ciao, voglio eliminare la categoria [imminenti](category)
- categoria da togliere: [cura personale](category)
- ciao, voglio cancellare una categoria [ricerca](category)
- voglio togliere la categoria [palestra](category)
- ciao, voglio rimuovere una categoria [cura personale](category)

## intent:set_status_activity
- ciao, imposta come [completa](activity_status) l'attività [partita di pallone](activity) in [palestra](category)
- voglio impostare [completata](activity_status) l'attività [postare selfie](activity) in [sociale](category)
- metti [non terminata](activity_status) l'attività [acquistare una bicicletta](activity) in [negozio](category)
- imposta [non fatta](activity_status) l'attività [vai in farmacia](activity) nella categoria [benessere](category)
- ciao, voglio impostare [non completata](activity_status) l'attività [taekwondo](activity) nella categoria [arti marziali](category)
- ciao, imposta come [incompleta](activity_status) l'attività [partita di pallone](activity) in [palestra](category)
- poni [fatta](activity_status) l'attività [shampoo](activity) nella categoria [benessere personale](category)
- imposta come [completato](activity_status) [nuotare](activity)
- poni [non completata](activity_status) [suonare la chitarra](activity)
- imposta [incompleto](activity_status) [ripetere la presentazione](activity) nella categoria [progetti](category)
- poni come [incompleta](activity_status) l'attività [suonare il pianoforte](activity) in [musica](category)
- metti [fatta](activity_status) [guardare la partita](activity) in [intrattenimento](category)
- imposta un'attività [completata](activity_status)
- imposta [non finita](activity_status) [chiama il medico](activity)
- metti come [non terminato](activity_status) [nuotare](activity) in [sport](category)
- metti come [terminato](activity_status) [nuotare](activity) in [sport](category)
- imposta [terminato](activity_status) [cena con gli amici](activity)
- voglio impostare [incompleta](activity_status) un'attività
- ciao, imposta un'attività [non completata](activity_status)

## intent:modify_activity_category
- per l'attività [partecipare alla conferenza](activity) trasforma la categoria [lavoro]{"entity": "category", "role": "old"} in [cultura]{"entity": "category", "role": "new"}
- sostituire la categoria [tempo libero]{"entity": "category", "role": "old"} dell'attività [fare i regali](activity)
- converti la categoria [sport]{"entity": "category", "role": "old"} dell'attività [correre](activity) con [cura della persona]{"entity": "category", "role": "new"}
- sostituire la categoria [Natale]{"entity": "category", "role": "old"} dell'attività [fare i regali](activity) con la categoria [tempo libero]{"entity": "category", "role": "new"}
- transformare la categoria [progetto]{"entity": "category", "role": "old"} dell'attività [prepare il powerpoint](activity) in categoria [university]{"entity": "category", "role": "new"}
- sostituisci la categoria [faccende domestiche]{"entity": "category", "role": "old"} dell'attività [preparare la colazione](activity)
- cambia la categoria [progetti]{"entity": "category", "role": "old"} dell'attività [studiare](activity) in categoria [esami]{"entity": "category", "role": "new"}
- modificare la categoria [lavoro]{"entity": "category", "role": "old"} di [pranzo di lavoro](activity)
- modificare la categoria [pranzo]{"entity": "category", "role": "old"} dell'attività [pranzo di lavoro](activity) in [lavoro]{"entity": "category", "role": "new"}
- modifica la categoria [dieta]{"entity": "category", "role": "old"} dell'attività [camminare all'aperto](activity)
- per l'attività [giocare a carte](activity) cambiare la categoria [amici]{"entity": "category", "role": "old"} in [svago]{"entity": "category", "role": "new"}
- per l'attività [prenotare il treno](activity) aggiorna la categoria [imminente]{"entity": "category", "role": "old"} in [vacanza]{"entity": "category", "role": "new"}
- sostituire la categoria [faccende domestiche]{"entity": "category", "role": "old"} dell'attività [preparare il pranzo](activity) con la categoria [casa]{"entity": "category", "role": "new"}
- trasforma la categoria [università]{"entity": "category", "role": "old"} dell'attività [studiare](activity) in categoria [progetti]{"entity": "category", "role": "new"}
- per l'attività [giocare a pallone](activity) trasforma la categoria [svago]{"entity": "category", "role": "old"} in [sport]{"entity": "category", "role": "new"}
- modifica la categoria dell'attività [andare al mare](activity)
- voglio cambiare la categoria [palestra]{"entity": "category", "role": "old"} dell'attività [boxe](activity) con la categoria [sport]{"entity": "category", "role": "new"}
- per l'attività [andare al mercato](activity) aggiorna la categoria [impegni domestici]{"entity": "category", "role": "old"} in [spesa]{"entity": "category", "role": "new"}
- per l'attività [mangiare sano](activity) modifica la categoria [stile di vita]{"entity": "category", "role": "old"} in [dieta]{"entity": "category", "role": "new"}
- modifica la categoria [tempo libero]{"entity": "category", "role": "old"} di [camminare all'aperto](activity) in [dieta]{"entity": "category", "role": "new"}
- modifica la categoria [vacanze]{"entity": "category", "role": "old"} dell'attività [andare al mare](activity)

## intent:modify_activity_name
- cambia il nome dell'attività [jogging]{"entity": "activity", "role": "old"} nella categoria [attività fisica](category) con nome [nuotare]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [mostra d'arte]{"entity": "activity", "role": "old"} con nome [mostra di pittura]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [pulire la casa]{"entity": "activity", "role": "old"} nella categoria [faccende domestiche](category)
- voglio cambiare l'attività con nome [organizzare raccolta fondi]{"entity": "activity", "role": "old"} nella categoria [volontariato](category)
- per l'attività [leggere un libro]{"entity": "activity", "role": "old"} nella categoria [impegni](category) trasforma il nome con [leggere l'articolo]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [canto]{"entity": "activity", "role": "old"} con il nome [ballo]{"entity": "activity", "role": "new"}
- nella categoria [università](category) cambia l'attività [seguire la lezione]{"entity": "activity", "role": "old"}  con il nome [andare a ricevimento]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [chiamare il medico]{"entity": "activity", "role": "old"}
- voglio cambiare il nome dell'attività [esame]{"entity": "activity", "role": "old"} nella categoria [università](category) con il nome [studio]{"entity": "activity", "role": "new"}
- cambiare il nome dell'attività [chiesa]{"entity": "activity", "role": "old"}  con nome [meditazione]{"entity": "activity", "role": "new"}
- nella categoria [università](category) cambiare il nome dell'attività [esame]{"entity": "activity", "role": "old"}  con nome [studio]{"entity": "activity", "role": "new"}
- nella categoria [scuola](category) sostituisci il nome dell'attività [interrogazione di matematica]{"entity": "activity", "role": "old"}  con il nome [compito di matematica]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [prendere le medicine]{"entity": "activity", "role": "old"}
- voglio cambiare il nome dell'attività [esame]{"entity": "activity", "role": "old"} nella categoria [cultura](category) con nome [studio]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [ballo]{"entity": "activity", "role": "old"} con nome [canto]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [andare a sciare]{"entity": "activity", "role": "old"} nella categoria [vacanza](category) con [andare in montagna]{"entity": "activity", "role": "new"}
- per l'attività [completare la relazione]{"entity": "activity", "role": "old"} modifica il nome con [completare il powerpoint]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [boxe]{"entity": "activity", "role": "old"} nella categoria [sport](category) con il nome [nuoto]{"entity": "activity", "role": "new"}
- per l'attività [scrivere un articolo]{"entity": "activity", "role": "old"} trasforma il nome con [leggere un giornale]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [fare una presentazione]{"entity": "activity", "role": "old"}  con il nome [viaggiare per lavoro]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [yoga]{"entity": "activity", "role": "old"} con il nome [pilates]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [andare dal dentista]{"entity": "activity", "role": "old"} con il nome [andare dal dottore]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [nuotare]{"entity": "activity", "role": "old"} nella categoria [attività fisica](category) con nome [jogging]{"entity": "activity", "role": "new"}
- modificare il nome dell'attività [yoga]{"entity": "activity", "role": "old"} con nome [pilates]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [preparare la colazione]{"entity": "activity", "role": "old"} con il nome [pulire il giardino]{"entity": "activity", "role": "new"}

## intent:remove_item
- rimuovi [giocare a basket](activity) alle 3:00
- rimuovi [dipingere](activity) nella categoria [creatività](category) alle 9:40
- cancella [aiutare mia madre](activity) alle 01:45
- ciao, voglio cancellare un'attività nella categoria [cura](category) alle 3:29
- rimuovi [nuotare](activity) nella categoria [sport](category)
- voglio cancellare un'attività alle 11:00
- elimina l'attività [allenarsi](activity) nella categoria [benessere](category)
- cancella [giardinaggio](activity) nella categoria [giardino](category) alle 5:12
- cancellare l'attività [scrivere la relazione](activity) nella categoria [ricerca](category)
- cancellare [taekwondo](activity) nella categoria [hobby](category)
- elimina [finire il report](activity) nella categoria [lavoro](category)
- cancella [acquistare il pane](activity) nella categoria [cibo](category) alle 8:00
- rimuovi [andare al cinema](activity) alle 13:00
- elimina l'attività [andare in banca](activity) nella categoria [finanza](category)
- elimina [fare yoga](activity)
- cancellare l'attività [fare il powerpoint](activity) nella categoria [imminente](category)
- rimuovi [annaffiare le piante](activity) nella categoria [faccende domestiche](category) alle 13:29
- cancella [andare a un incontro](activity) nella categoria [lavoro](category) alle 4:25
- elimina [studiare](activity)
- rimuovi [andare all'ufficio postale](activity) nella categoria [pacchi](category) alle 17:30
- voglio cancellare un'attività in un elenco alle 13:39
- cancella [studiare il latino](activity) nella categoria [scuola](category) alle 2:55
- rimuovi [uscire](activity) nella categoria [società](category) alle 17:30
- elimina [fare i compiti](activity)
- voglio cancellare un'attività nella categoria [generi alimentari](category) alle 9:40
- rimuovi [fare shopping](activity) nella categoria [faccende domestiche](category)

## intent:presentation
- [tiziano](name)
- [eugenio](name)
- [ermanno](name)
- [cristina](name)
- [mimmo](name)
- [galatea](name)
- [aristide](name)
- sono [carolina](name)
- [amichela](name)
- [speranza](name)
- ciao, sono [michele](name)
- il mio nome [Dario](name)
- [lorenzo](name)
- [jhon](name)
- [peppe](name)
- [edmondo](name)
- [giovanni](name)
- [adele](name)
- [roberto](name)
- [federico](name)
- [christian](name)
- [ursola](name)
- [silviero](name)
- [cafiero](name)
- [Foca](name)
- [azzurra](name)
- [elga](name)
- il mio nome è [Xavier](name)
- il mio nome è [Ugo](name)
- [teresa](name)
- [vincenzo](name)
- crea un account
- [giuseppe](name)
- voglio registrarmi
- ciao il mio nome è [Kevin](name)
- [lucia](name)
- [michi](name)
- [laura](name)
- [giusy](name)
- [ornella](name)
- [lucilla](name)
- iscrizione
- ciao, sono [pierfrancesco](name)
- [ernesto](name)

## intent:inform
- [fumetti](category)
- [calendario](category)
- [fare shopping](activity)
- [studiare per l'esame](activity)
- [aggiustare la porta](activity)
- [partecipare a una conferenza](activity)
- [camprare lampadina](activity)
- [viaggio in brasile](activity)
- [ritirare stipendio](activity)
- [relax](activity)
- [serata alcolica](activity)
- [nuotare](activity)
- [fisioterapia](activity)
- [tempo libero](category)
- [dottorato](category)
- [affitto](activity)
- [intervento](activity)
- [serata libera](activity)
- alle 18:00
- 26 minuti e 30 secondi
- oggi alle 21
- [magistrale](category)
- [spese](category)
- [rata casa](activity)
- [preparare la vasca](activity)
- [andare in banca](activity)
- [fare saldo annuale](activity)
- [volontariato](category)
- alle 21
- [obiettivi](category)
- [riscuotere affitto](activity)
- [andare a pescare](activity)
- [frigo](category)
- [musica](category)
- [andare a fare shopping](activity)
- [cena con i parenti](activity)
- [progetti](category)
- [famiglia](category)
- [pagare affitto](activity)
- [pranzo](activity)
- [ristorante](category)
- [cercare](activity)
- [allenamenti](category)
- [giocare a carte](activity)
- [laboratorio](category)
- [bolletta](activity)
- 12/10/2022 alle 18:00
- tra 1 ora
- [fare meeting](activity)
- ieri
- [carro](category)
- 09/12/2030 alle 13:00
- domani

## intent:add_item
- ciao, vorrei aggiungere un'attività all'elenco [spesa](category) alle 6:30
- voglio inserire un'attività nell'elenco [documentazione](category)
- ciao, inserisci [scrivere](activity) nella categoria [hobby](category)
- inserire [videoconferenza](activity) nella categoria [progetto](category) alle 14:50
- aggiungi [suonare il pianoforte](activity) in [musica](category)
- nella categoria [casa](category) inserisci la nuova attività [pulire il bagno](activity)
- vorrei mettere una nuova attività [studiare per l'esame](activity) alla categoria [università](category)
- aggiungi [andare dai genitori](activity) in [famiglia](category) alle 20:00
- inserisci l'attività [fare stretching](activity) in [palestra](category)
- metti l'attività [andare dal dentista](activity)
- ciao, inserisci [preparare la borsa](activity) nella categoria [viaggio](category)
- vorrei creare l'attività [github](activity) all'elenco [progetti](category)
- metti l'attività [piscina](activity)
- ciao, crea [partecipare a un corso](activity) nella categoria [laurea](category)
- inserire [studiare per interrogazione](activity) nella categoria [scuola](category) alle 19:00
- inserisci l'attività [revisione](activity) in [impegni](category) alle 17:30
- ciao, voglio creare un'attività per la lista [primavera](category)
- ciao, vorrei inserire un'attività nella categoria [dieta](category) alle 14:50
- ciao, inserisci l'attività [mandare e-mail](activity) nella categoria [progetti](category)
- ciao, vorrei inserire l'attività nell'elenco [imminente](category) alle 16:30
- inserisci [pulizie](activity) nella categoria [giornaliera](category)
- ciao, voglio inserire una nuova attività nella categoria [autunno](category)
- voglio inserire un'attività nella lista [piacere](category) alle 9:40
- inserisci l'attività [lavorare](activity)
- inserisci [nuotare](activity) in [sport](category)
- ciao, inserisci [leggere](activity)
- ciao, voglio inserire un'attività [pagare le bollette](activity) nella categoria [finanza](category)
- nella categoria [benessere](category) aggiungere l'attività [andare dal parrucchiere](activity) alle 21:10
- ciao, voglio inserire un'attività nell'elenco [priorità](category)
- inserisci [laurea](activity) alle 00:00
- ciao, voglio inserire un'attività nell'elenco [faccende domestiche](category)
- aggiungi nuova attività [andare al teatro](activity) in [cultura](category) alle 12:35
- aggiungi attività [junkfood](activity) in categoria [settimanale](category) alle 11:00
- ciao, vorrei inserire un'attività nell'elenco [coaching](category) alle 19:00
- ciao, voglio inserire un'attività nella lista [urgente](category)
- inserire l'attività [preparare lo zaino](activity) nella categoria [organizzazione](category) alle 18:30
- aggiungi [correre](activity) in [palestra](category) alle 12
- ciao, inserisci [taekwondo](activity) nella categoria [arti marziali](category)
- voglio inserire una nuova attività in una categoria alle 13:39
- ciao, vorrei aggiungere un'attività all'elenco [business](category) alle 18:30
- aggiungere l'attività [uscire con gli amici](activity) nella categoria [società](category) alle 19:41
- ciao, voglio inserire un'attività nella mia lista
- inserisci attività [controllare e-mail](activity) in [lavoro](category) alle 9:40
- inserire l'attività [disegnare](activity) nella categoria [creatività](category) alle 5:12
- ciao, inserisci l'attività [shampoo](activity) nella categoria [quotidiana](category)
- creare l'attività [dentista](activity) nella categoria [mensile](category) alle 20:00
- ciao, voglio creare l'attività [andare nel centro della città](activity) nell'elenco [commissioni](category)
- aggiungere [cucinare per cena](activity) alle 20:45
- ciao, vorrei mettere un'attività nell'elenco [faccende](category) alle 7:00
- metti l'attività [acquistare un regalo di natale](activity) in categoria [imminente](category) alle 9:40
- ciao, inserisci [cena con i nonni](activity)
- ciao, vorrei aggiungere un'attività nella lista [hobby](category) alle 3:29
- inserisci [leggere un libro](activity) nella categoria [cultura](category)
- voglio aggiungere un'attività alla lista [cura del corpo](category)
- ciao, voglio inserire un'attività [imparare lo spagnolo](activity) nella categoria [cultura](category)
- crea l'attività [cena](activity) nella categoria [cucina](category)
- inserisci l'attività [fare yoga](activity) nella categoria [benessere](category)
- voglio aggiungere un'attività alla lista [divertimento](category) alle 21:10
- ciao, inserisci l'attività [riparare l'auto](activity) nella categoria [impegni](category)
- ciao, vorrei inserire un'attività nella lista [politica](category) alle 17:30
- ciao, vorrei aggiungere un'attività nella mia lista alle 18:14
- aggiungi un'attività in [musica](category)
- aggiungi [organizzare la cucina](activity) nella categoria [casa](category)
- vorrei creare l'attività [festa di compleanno](activity) all'elenco [eventi](category)
- ciao, nella categoria [personale](category) voglio inserire l'attività [parrucchiere](activity)
- inserisci [portare fuori il cane](activity) alle 3:00
- voglio aggiungere un'attività nell'elenco [necessari](category)

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
