## intent:bot_challenge
- Sei un umano?

## intent:goodbye
- buona giornata
- è stato un piacere

## intent:help
- Non so cosa fare
- Aiuto

## intent:greet
- buona mattina
- buon giorno

## intent:affirm
- esatto
- si

## intent:mood_great
- Stupefacente
- Meraviglioso
- Così buono

## intent:mood_unhappy
- Non bene
- Super triste

## intent:ask_name
- sapresti dirmi chi sono?
- chi sono
- dimmi il mio nome

## intent:deny
- no mi dispiace
- negativo
- non mi piace

## intent:clean_activities
- rimuovi le attività
- rimuovi tutte le mie attività completate
- per favore, elimina tutte le mie attività completate

## intent:view_categories
- fammi vedere tutte le mie categorie
- Puoi mostrare le mie categorie?
- mostra le mie categorie

## intent:remind_me_of
- aiutami a ricordare un'attività
- ricordami di [mangiare frutta](activity)
- ricordami di [cucinare il pranzo](activity) nella categoria [casa](category) alle 8:30
- aiutami a non dimenticare l'attività [ascoltare la registrazione della lezione](activity) nella categoria [università](category) per domani
- non posso dimenticare di fare l'attività [nuoto](activity) nella categoria [salute fisica](category) per il prossimo lunedì
- imposta un promemoria per l'attività [chiamare la mia ragazza](activity) nella categoria [sociale](category) nella prossima mattina
- ricordami la [riunione di lavoro](activity) domani mattina

## intent:view_activities
- quali sono le mie attività [incomplete](activity_status)?
- voglio vedere tutte le mie attività aggiunte
- mostrami le mie attività [fatte](activity_status)
- mostrami attività [eseguite](activity_status) nella categoria [scuola](category)
- mostrami cosa devo fare oggi
- cosa ho da fare?
- voglio vedere tutte le attività create
- quali sono le mie attività aggiunte?

## intent:modify_category
- alterare la categoria [tempo libero]{"entity": "category", "role": "old"} con [palestra]{"entity": "category", "role": "new"}
- convertire la categoria [genitori]{"entity": "category", "role": "old"} con [casa]{"entity": "category", "role": "new"}
- cambiare la categoria [università]{"entity": "category", "role": "old"} in [esami]{"entity": "category", "role": "new"}
- sostituire la categoria [estate]{"entity": "category", "role": "old"} in [annuale]{"entity": "category", "role": "new"}
- sostituire la categoria [scuola]{"entity": "category", "role": "old"} con [eventi]{"entity": "category", "role": "new"}
- voglio sostituire la categoria [cultura]{"entity": "category", "role": "old"} in [teatro]{"entity": "category", "role": "new"}
- sostituire la categoria [faccende domestiche]{"entity": "category", "role": "old"} con [benessere]{"entity": "category", "role": "new"}
- trasformare la categoria [famiglia]{"entity": "category", "role": "old"} con [amicizia]{"entity": "category", "role": "new"}

## intent:add_category
- ciao, voglio inserire una nuova categoria [ricerca](category)
- categoria: [pagamenti](category)
- viao, voglio mettere la categoria [genitori](category)
- inserisci [tempo libero](category) categoria
- categoria: [scuola](category)
- ciao, voglio aggiungere una categoria [settimanale](category)
- voglio usare una nuova categoria [eventi](category)
- metti [sport](category) categoria
- voglio mettere la categoria [vacanza](category)
- metti la categoria [ingegneria](category)
- la categoria da aggiungere è [università](category)

## intent:modify_activity_deadline
- sostituisci la scadenza dell'attività [torneo di calcio](activity) al 25 novembre
- voglio cambiare la scadenza dell'attività [andare dal parrucchiere](activity) nella categoria [personale](category) da 25 settembre a 27 settembre 1998
- voglio cambiare la scadenza dell'attività [andare dal parrucchiere](activity) nella categoria [personale](category)
- modifica il termine dell'attività [revisione del progetto](activity) nella categoria [università](category) in domenica
- nella categoria [scuola](category) modificare il termine dell'attività [ripetere scienze](activity) dal 22 settembre al 25 settembre
- nella categoria [famiglia](category) sostituisci il termine dell'attività [accompagnare mio figlio](activity) dal 10/12/2022 al 12/13/2022
- nella categoria [cultura](category) sostituisci la scadenza dell'attività [mostra di pittura](activity) dal 22 settembre al 25 settembre
- modifica la scadenza dell'attività [esame della patente](activity) da venerdì a lunedi
- altera la scadenza dell'attività [aiutare il nonno](activity) alle 22:00
- sostituisci la scadenza dell'attività [torneo di calcio](activity)
- modifica il termine dell'attività [leggere il giornale](activity) nella categoria [cultura](category) con domenica
- altera il termine dell'attività [karaoke](activity) da 18:00 alle 20:00

## intent:remove_category
- voglio rimuovere una categoria
- voglio togliere la categoria [mensile](category)
- voglio eliminare la categoria [vacanza](category)
- togliere la vecchia categoria [dieta](category)
- rimuovi [università](category) tra le mie categorie
- ciao, voglio eliminare la categoria [genitori](category)
- ciao, per favore cestina la seguente categoria [finanza](category)
- la categoria da cancellare è [volontariato](category)
- voglio rimuovere la categoria [università](category)
- ciao, voglio eliminare la categoria [casa](category)
- ciao, voglio eliminare la categoria [finanza](category)
- ciao, voglio rimuovere la categoria [faccende domestiche](category)

## intent:set_status_activity
- ciao, metti [completato](activity_status) [andare dal parrucchiere](activity) nella categoria [benessere](category)
- ciao, imposta [completato](activity_status) [annaffia le piante](activity)
- imposta [sviluppata](activity_status) l'attività [suona la chitarra](activity) nella categoria [musica](category)
- voglio impostare [completata](activity_status) un'attività
- voglio impostare [incompleta](activity_status) un'attività
- poni [non completata](activity_status) [suonare la chitarra](activity)
- poni [completata](activity_status) [suonare la chitarra](activity)
- ciao, imposta [completato](activity_status) l'attività [aiuta mio nonno](activity) nella categoria [genitori](category)
- imposta [non finita](activity_status) [chiama il medico](activity)
- imposta [completato](activity_status) [andare a correre](activity)
- metti [completata](activity_status) l'attività [cena fuori](activity) nella categoria [svago](category)
- ciao, imposta [non terminata](activity_status) [annaffia le piante](activity)
- poni come [incompleta](activity_status) l'attività [suonare il pianoforte](activity) in [musica](category)
- imposta [completato](activity_status) [pulire la cucina](activity) nella categoria [casa](category)
- imposta come [sviluppata](activity_status) [giocare a carte](activity)
- imposta come [non fatta](activity_status) [leggere](activity)

## intent:modify_activity_category
- cambia la categoria [progetti]{"entity": "category", "role": "old"} dell'attività [studiare](activity) in categoria [esami]{"entity": "category", "role": "new"}
- per l'attività [giocare a carte](activity) cambiare la categoria [amici]{"entity": "category", "role": "old"} in [svago]{"entity": "category", "role": "new"}
- voglio cambiare la categoria dell'attività [boxe](activity)
- converti la categoria [urgente]{"entity": "category", "role": "old"} dell'attività [fare benzina](activity) con [importante]{"entity": "category", "role": "new"}
- convertire la categoria [commissioni]{"entity": "category", "role": "old"} dell'attività [lavare la macchina](activity) con [importante]{"entity": "category", "role": "new"}
- transformare la categoria [progetto]{"entity": "category", "role": "old"} dell'attività [prepare il powerpoint](activity) in categoria [university]{"entity": "category", "role": "new"}
- trasforma la categoria [università]{"entity": "category", "role": "old"} dell'attività [preparare il powerpoint](activity) in categoria [progetto]{"entity": "category", "role": "new"}
- trasforma la categoria [università]{"entity": "category", "role": "old"} dell'attività [preparare l'esame](activity) in categoria [studio]{"entity": "category", "role": "new"}
- per l'attività [mangiare sano](activity) modifica la categoria [dieta]{"entity": "category", "role": "old"} in [stile di vita]{"entity": "category", "role": "new"}
- converti la categoria [importante]{"entity": "category", "role": "old"} dell'attività [fare benzina](activity) con [urgente]{"entity": "category", "role": "new"}
- per l'attività [andare al mercato](activity) aggiorna la categoria [impegni domestici]{"entity": "category", "role": "old"} in [spesa]{"entity": "category", "role": "new"}
- per l'attività [pulire la casa](activity) nella categoria [faccende domestiche]{"entity": "category", "role": "old"} sostituire la categoria con [quotidiano]{"entity": "category", "role": "new"}
- per l'attività [mangiare sano](activity) modifica la categoria [stile di vita]{"entity": "category", "role": "old"} in [dieta]{"entity": "category", "role": "new"}
- modifica la categoria [svago]{"entity": "category", "role": "old"} dell'attività [andare al mare](activity) in [vacanze]{"entity": "category", "role": "new"}
- per l'attività [pulire la casa](activity) nella categoria [faccende domestiche]{"entity": "category", "role": "old"} sostituisci la categoria con [quotidiano]{"entity": "category", "role": "new"}
- sostituire la categoria [casa]{"entity": "category", "role": "old"} dell'attività [preparare il pranzo](activity) con la categoria [faccende domestiche]{"entity": "category", "role": "new"}
- cambia la categoria [cura della persona]{"entity": "category", "role": "old"} dell'attività [correre](activity)

## intent:modify_activity_name
- voglio cambiare l'attività con nome [andare in montagna]{"entity": "activity", "role": "old"} nella categoria [vacanza](category) con [andare a sciare]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [preparare la colazione]{"entity": "activity", "role": "old"} con il nome [pulire il giardino]{"entity": "activity", "role": "new"}
- nella categoria [università](category) cambiare il nome dell'attività [esame]{"entity": "activity", "role": "old"}  con nome [studio]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [jogging]{"entity": "activity", "role": "old"} nella categoria [sport](category)
- voglio cambiare il nome dell'attività [boxe]{"entity": "activity", "role": "old"} nella categoria [sport](category) con il nome [nuoto]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [rileggere]{"entity": "activity", "role": "old"} nella categoria [consegna](category) con il nome [revisione]{"entity": "activity", "role": "new"}
- per l'attività [completare il powerpoint]{"entity": "activity", "role": "old"} modifica il nome
- cambia il nome dell'attività [mostra d'arte]{"entity": "activity", "role": "old"} con nome [mostra di pittura]{"entity": "activity", "role": "new"}
- nella categoria [scuola](category) sostituire il nome dell'attività [interrogazione di latino]{"entity": "activity", "role": "old"}  con nome [compito di latino]{"entity": "activity", "role": "new"}
- sostituisci il nome dell'attività [pubblicare l'articolo]{"entity": "activity", "role": "old"}  con il nome [scrivere l'articolo]{"entity": "activity", "role": "new"}
- sostituisci il nome dell'attività [scrivere l'articolo]{"entity": "activity", "role": "old"}  con il nome [pubblicare l'articolo]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [prenotare l'aereo]{"entity": "activity", "role": "old"} con [prenotare il treno]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [cucinare la cena]{"entity": "activity", "role": "old"} nella categoria [casa](category)
- voglio cambiare il nome dell'attività [andare a fisioterapia]{"entity": "activity", "role": "old"}
- cambia il nome dell'attività [chiesa]{"entity": "activity", "role": "old"}  con il nome [meditazione]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [nuotare]{"entity": "activity", "role": "old"} nella categoria [attività fisica](category) con nome [jogging]{"entity": "activity", "role": "new"}
- sostituire il nome dell'attività [guardare il telegiornale]{"entity": "activity", "role": "old"}  with name [leggere il giornare]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [aiutare la zia]{"entity": "activity", "role": "old"} nella categoria [famiglia](category) con [aiutare la sorella]{"entity": "activity", "role": "new"}
- cambiare il nome dell'attività [chiesa]{"entity": "activity", "role": "old"}  con nome [meditazione]{"entity": "activity", "role": "new"}
- per l'attività [completare la relazione]{"entity": "activity", "role": "old"} modifica il nome con [completare il powerpoint]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [attività all'aperto]{"entity": "activity", "role": "old"} nella categoria [salute fisica](category)

## intent:remove_item
- elimina [riposo](activity) nella categoria [salute](category)
- ciao, voglio cancellare un'attività nella categoria [commissioni](category) alle 22:20
- ciao, voglio cancellare un'attività nella categoria [marketing](category) alle 18:30
- voglio eliminare un'attività dall'elenco [leadership](category)
- elimina [fare una presentazione](activity) nella categoria [società](category)
- voglio eliminare un'attività dall'elenco [piacere](category)
- ciao, voglio rimuovere un'attività dall'elenco [ricreazione](category)
- elimina [correre](activity) nella categoria [quotidiana](category)
- voglio eliminare un'attività
- cancella [passeggiata](activity) nella categoria [giornaliera](category) alle 7:00
- voglio cancellare un'attività nella categoria [generi alimentari](category) alle 9:40
- cancella [pagare mutuo](activity) nella categoria [finanza](category) alle 16:00
- rimuovi l'attività [studiare matematica](activity) nella categoria [università](category)
- rimuovi [correre](activity)
- elimina l'attività [andare in banca](activity) nella categoria [finanza](category)
- voglio cancellare un'attività nella categoria [imminente](category) alle 16:30
- voglio eliminare un'attività dall'elenco [scuola](category)
- cancella [andare in chiesa](activity) nella categoria [personale](category) alle 19:41
- elimina [alzarsi](activity)
- ciao, voglio rimuovi un'attività dall'elenco [politica](category)
- voglio eliminare un'attività dall'elenco [documenti](category)
- cancella [andare all'ufficio](activity) nella categoria [progetto](category) alle 16:00
- voglio cancellare un'attività nella categoria [comunicazione](category) alle 21:10

## intent:presentation
- [piero](name)
- [gerardo](name)
- [alberto](name)
- [lucia](name)
- [gerry](name)
- il mio nome è [alessia](name)
- [stefano](name)
- nuovo utente
- [rossana](name)
- [giberto](name)
- fammi creare un account
- [liliana](name)
- [natascia](name)
- voglio iscrivermi
- [violeta](name)
- ciao sono [marcello](name)
- [Foca](name)
- [kikka](name)
- ciao, sono [marco](name)
- [adele](name)
- ciao, sono [pierfrancesco](name)
- [amadeo](name)
- impostare un utente
- [anita](name)
- [paola](name)
- [peppe](name)
- [isolda](name)
- [antonella](name)
- [lucilla](name)
- [memo](name)
- [jhon](name)
- [lucio](name)
- [nik](name)
- [faustino](name)
- [vincenzo](name)
- ciao, sono [nando](name)

## intent:inform
- [scrivere una lettera](activity)
- [uscire](activity)
- lunedì prossimo
- [fare saldo annuale](activity)
- [giocare a carte](activity)
- [preparare la vasca](activity)
- [bolletta](activity)
- [pagare la bolletta](activity)
- [fare shopping](activity)
- [studio](activity)
- [ritirare il pacco](activity)
- [partecipare a una conferenza](activity)
- [progetti](category)
- [alzarsi](activity)
- domani mattina
- [esame patente](activity)
- [lezione](activity)
- [ascoltare musica](activity)
- [appuntamento romantico](activity)
- [nuoto](activity)
- [andare in biblioteca](activity)
- [faccende di casa](category)
- [carrello](category)
- [fare un ripasso di matematica](activity)
- [musica](category)
- [bambino](category)
- in 30 secondi
- [cena con i parenti](activity)
- [sport](category)
- venerdì
- [dottorato](category)
- [compiti](category)
- [andare al cinema](activity)
- 6:30
- 08/09/2025
- [fisioterapia](activity)
- [lavori](category)
- [carro](category)
- alle 18:00
- [ritirare stipendio](activity)
- [viaggio in Spagna](activity)
- ieri
- [studiare per l'esame](activity)
- [cucinare](activity)

## intent:add_item
- inserisci [dormire](activity) nella categoria [benessere](category)
- aggiungi [andare dall'estetista](activity)
- inserisci attività [controllare e-mail](activity) in [lavoro](category) alle 9:40
- ciao, aggiungi l'attività [regali](activity) nella categoria [natale](category)
- ciao, vorrei inserire un'attività in un elenco [spesa](category) alle 21:10
- inserisci l'attività [fare stretching](activity) in [palestra](category)
- voglio inserire una nuova attività nell'elenco [spettacolo](category)
- vorrei creare una nuova attività
- vorrei aggiungere un'attività alle 11:00
- voglio aggiungere un'attività alla lista [cura del corpo](category)
- ciao, voglio aggiungere l'attività [inviare un'email](activity) all'elenco [comunicazione](category)
- metti [preparare la presentazione](activity) in [progetti](category)
- ciao, vorrei aggiungere un'attività all'elenco [business](category) alle 18:30
- ciao, voglio inserire un'attività nell'elenco [business](category)
- nella categoria [corso](category) inserire [incontro](activity) alle 20:30
- metti l'attività [studiare](activity) in [scuola](category)
- aggiungi l'attività [cantare](activity)
- ciao, inserisci l'attività [e-commerce](activity) nella categoria [tecnologia](category)
- ciao, inserisci [andare a cantare](activity) nella categoria [tempo libero](category)
- inserisci [prendere la pillola](activity) alle 9:30
- ciao, vorrei aggiungere un'attività nella mia lista alle 18:14
- ciao, vorrei inserire un'attività nell'elenco [coaching](category) alle 19:00
- metti [fare una doccia](activity) in [cura personale](category) alle 4:25
- aggiungi attività [gioca a pallavolo](activity) in categoria [sport](category) alle 5:12
- ciao, voglio aggiungere un'attività nell'elenco [visite mediche](category)
- inserire [chiamare il medico](activity) nella categoria [salute](category) alle 22:20
- inserisci [portare fuori il cane](activity) alle 3:00
- aggiungi [andare a sciare](activity) in [hobby](category) alle 20:00
- inserire l'attività [ripetere](activity) nella categoria [esame](category) alle 22:20
- inserire [uscire](activity) alle 9:30
- nella categoria [benessere](category) aggiungere l'attività [andare dal parrucchiere](activity) alle 21:10
- ciao, vorrei inserire un'attività nella mia lista alle 12:37
- inserisci l'attività [fare esercizi di routine](activity) nella categoria [sport](category)
- voglio aggiungere un'attività alla lista [divertimento](category) alle 21:10
- ciao, voglio creare un'attività per la lista [primavera](category)
- vorrei inserire un'attività alla categoria [cura della mente](category)
- ciao, voglio aggiungere un'attività [parrucchiere](activity) nella categoria [benessere](category)
- aggiungere [risposare](activity) nella categoria [cura della mente](category) alle 2:55
- ciao, vorrei inserire un'attività nell'elenco [sociale](category) alle 3:29
- inserisci [fare stand up](activity)
- ciao, vorrei aggiungere una nuova attività all'elenco [comunicazione](category) alle 9:40
- ciao, nella categoria [personale](category) voglio inserire l'attività [parrucchiere](activity)
- aggiungi [fare una passeggiata all'aria aperta](activity) in [tempo libero](category) oggi alle 12
- aggiungere l'attività [uscire con gli amici](activity) nella categoria [società](category) alle 19:41
- inserisci l'attività [prenotare il pub](activity) in [amicizia](category) alle 19:41
- metti [fare jogging](activity) in [sport](category)
- aggiungi attività [junkfood](activity) in categoria [settimanale](category) alle 11:00
- inserisci l'attività [leggere](activity) nella categoria [cultura](category)
- ciao, crea [partecipare a un corso](activity) nella categoria [laurea](category)
- aggiungi [fare pilates](activity)
- ciao, vorrei inserire un'attività nella categoria [giustizia](category) alle 22:20
- inserisci l'attività [andare in farmacia](activity)
- vorrei aggiungere una nuova attività
- ciao, vorrei inserire un'attività nella lista [politica](category) alle 17:30
- inserire [andare al supermercato](activity) nella categoria [cibo](category) alle 6:30
- ciao, voglio creare l'attività [andare nel centro della città](activity) nell'elenco [commissioni](category)

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
