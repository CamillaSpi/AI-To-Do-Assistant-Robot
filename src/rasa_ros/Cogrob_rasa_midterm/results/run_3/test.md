## intent:bot_challenge
- Sto parlando con un bot?

## intent:goodbye
- alla prossima
- buona notte

## intent:help
- Cosa puoi fare?
- Ho bisogno di assistenza

## intent:greet
- ciao
- Ciao

## intent:affirm
- indubbiamente
- corretto

## intent:mood_great
- Mi sento molto bene
- Sto per salvare il mondo
- Così buono

## intent:mood_unhappy
- Non mi sento molto bene
- Sono triste

## intent:ask_name
- chi sono
- sai chi sono?
- sapresti dirmi chi sono?

## intent:deny
- assolutamente no
- non mi piace
- no mi dispiace

## intent:clean_activities
- rimuovi tutte le attività terminate
- per favore, rimuovi tutte le mie attività completate
- per favore, elimina tutte le mie attività completate

## intent:view_categories
- quali sono le categorie aggiunte?
- voglio vedere tutte le mie categorie
- fammi vedere tutte le mie categorie

## intent:remind_me_of
- non posso dimenticare di fare l'attività [nuoto](activity) nella categoria [salute fisica](category) per il prossimo lunedì
- ricordami l'attività [lezione di chitarra](activity) domani mattina
- aiutami a non dimenticare l'attività [ascoltare la registrazione della lezione](activity) nella categoria [università](category) per domani
- imposta un promemoria per l'attività [andare al cinema](activity) nella categoria [cultura](category) per domani mattina
- ricordami la [riunione di lavoro](activity) domani mattina
- non posso dimenticare di fare l'attività [parlare con il professore](activity) nella categoria [progetto](category) per domenica prossima
- non posso dimenticare di [andare dal veterinario](activity) alle 19:00

## intent:view_activities
- voglio vedere tutte le attività create
- mostra la mia attività [non fatta](activity_status) nella categoria [impegni](category)
- voglio vedere tutte le mie attività aggiunte
- quali sono le mie attività aggiunte?
- mostra le mie attività
- quali sono le mie attività inserite?
- mostra attività
- voglio vedere tutte le mie attività [completate](activity_status)

## intent:modify_category
- per favore, variare la categoria [finanza]{"entity": "category", "role": "old"} nella categoria [banca]{"entity": "category", "role": "new"}
- cambiare la categoria [università]{"entity": "category", "role": "old"} in [esami]{"entity": "category", "role": "new"}
- modificare la categoria [amicizia]{"entity": "category", "role": "old"} in [famiglia]{"entity": "category", "role": "new"}
- per favore, voglio sostituire la categoria [cura]{"entity": "category", "role": "old"} a [stile di vita]{"entity": "category", "role": "new"}
- alterare la categoria [sociale]{"entity": "category", "role": "old"} in [volontariato]{"entity": "category", "role": "new"}
- convertire la categoria [benessere]{"entity": "category", "role": "old"} in [faccende domestiche]{"entity": "category", "role": "new"}
- voglio cambiare la categoria [lavoro]{"entity": "category", "role": "old"} con la categoria [impegni]{"entity": "category", "role": "new"}
- trasformare la categoria [famiglia]{"entity": "category", "role": "old"} con [amicizia]{"entity": "category", "role": "new"}

## intent:add_category
- voglio usare una nuova categoria [eventi](category)
- viao, voglio mettere la categoria [genitori](category)
- ciao, voglio inserire una nuova categoria [ricerca](category)
- voglio aggiungere una categoria
- voglio usare una nuova categoria [medico](category)
- aggiungi la categoria [studio](category)
- categoria: [bollette](category)
- aggiungi la categoria [relazioni](category)
- ciao, inserisci la seguente [divertimento](category)
- voglio inserire la categoria [professione](category)
- metti [sport](category) categoria

## intent:modify_activity_deadline
- nella categoria [scuola](category) modificare il termine dell'attività [ripetere scienze](activity) dal 22 settembre al 25 settembre
- nella categoria [creatività](category) sostituisci la deadline dell'attività [disegnare](activity) da 22 settembre a 25 settembre
- nella categoria [famiglia](category) sostituisci il termine dell'attività [accompagnare mio figlio](activity) dal 10/12/2022 al 12/13/2022
- per l'attività [andare in chiesa](activity) nella categoria [personale](category) modificare la scadenza con 22 ottobre 1922
- modifica la scadenza dell'attività [leggere](activity) nella categoria [università](category) da venerdì a domenica
- voglio cambiare il termine dell'attività [ascoltare il podcast](activity) nella categoria [musica](category) con 27 settembre 1998
- altera la scadenza dell'attività [viaggio con la mamma](activity) nella categoria [vacanza](category) dal 07/11/2022 a domenica
- per l'attività [studiare in biblioteca](activity) nella categoria [università](category) modifica il termine nel 22 ottobre 1922
- modifica il termine dell'attività [leggere il giornale](activity) nella categoria [cultura](category) con domenica
- modifica la scadenza dell'attività [giro in barca](activity) al prossimo mese
- altera il termine dell'attività [karaoke](activity) da 18:00 alle 20:00
- modifica il termine dell'attività [revisione del progetto](activity) nella categoria [università](category)

## intent:remove_category
- voglio eliminare la categoria [progetti](category)
- ciao, voglio eliminare la categoria [finanza](category)
- voglio togliere la categoria [mensile](category)
- non voglio usare la categoria [eventi](category)
- eliminare la vecchia categoria [pagamenti](category)
- categoria da togliere: [cura personale](category)
- voglio rimuovere la categoria [impegni](category)
- ciao, voglio cancellare una categoria [ricerca](category)
- ciao, per favore elimina la seguente categoria [medica](category)
- ciao, voglio togliere la categoria [lavoro](category)
- voglio togliere la categoria [settimanale](category)
- ciao, voglio rimuovere la categoria [famiglia](category)

## intent:set_status_activity
- imposta un'attività [completata](activity_status)
- imposta un'attività [incompleta](activity_status)
- imposta [incompleto](activity_status) [andare al mare](activity) in [viaggio](category)
- imposta [non fatta](activity_status) l'attività [vai in farmacia](activity) nella categoria [benessere](category)
- metti [non completata](activity_status) l'attività [cena fuori](activity) nella categoria [svago](category)
- ciao, metti [non completato](activity_status) [andare dal parrucchiere](activity) nella categoria [benessere](category)
- imposta [completata](activity_status) [chiama il medico](activity)
- ciao, imposta come [incompleta](activity_status) l'attività [partita di pallone](activity) in [palestra](category)
- imposta come [completato](activity_status) [nuotare](activity)
- metti come [non terminato](activity_status) [nuotare](activity) in [sport](category)
- imposta come [fatta](activity_status) [leggere](activity)
- imposta [incompiuta](activity_status) [andare a correre](activity)
- imposta come [concluso](activity_status) [giardinaggio](activity) nella categoria [giardino](category)
- imposta [fatto](activity_status) [powerpoint](activity) nella categoria [programmi](category)
- imposta [non completato](activity_status) [pulire la cucina](activity) nella categoria [casa](category)
- imposta [non terminato](activity_status) [cena con gli amici](activity)

## intent:modify_activity_category
- cambia la categoria [esami]{"entity": "category", "role": "old"} dell'attività [studiare](activity) in categoria [progetti]{"entity": "category", "role": "new"}
- converti la categoria [urgente]{"entity": "category", "role": "old"} dell'attività [fare benzina](activity) con [importante]{"entity": "category", "role": "new"}
- per l'attività [mangiare sano](activity) modifica la categoria [dieta]{"entity": "category", "role": "old"} in [stile di vita]{"entity": "category", "role": "new"}
- modifica la categoria [vacanze]{"entity": "category", "role": "old"} dell'attività [andare al mare](activity)
- voglio cambiare la categoria [palestra]{"entity": "category", "role": "old"} dell'attività [boxe](activity) con la categoria [sport]{"entity": "category", "role": "new"}
- per l'attività [giocare a pallone](activity) trasforma la categoria [svago]{"entity": "category", "role": "old"} in [sport]{"entity": "category", "role": "new"}
- cambia la categoria [esami]{"entity": "category", "role": "old"} dell'attività [studiare](activity)
- per l'attività [andare al mercato](activity) aggiorna la categoria [impegni domestici]{"entity": "category", "role": "old"} in [spesa]{"entity": "category", "role": "new"}
- per l'attività [disegnare](activity) nella categoria [arte]{"entity": "category", "role": "old"} sostituire la categoria con [creatività]{"entity": "category", "role": "new"}
- modifica la categoria [svago]{"entity": "category", "role": "old"} dell'attività [andare al mare](activity) in [vacanze]{"entity": "category", "role": "new"}
- sostituisci la categoria [famiglia]{"entity": "category", "role": "old"} dell'attività [preparare la colazione](activity) con la categoria [faccende domestiche]{"entity": "category", "role": "new"}
- per l'attività [giocare a carte](activity) cambiare la categoria [svago]{"entity": "category", "role": "old"} in [amici]{"entity": "category", "role": "new"}
- per l'attività [guardare il match](activity) trasformare la categoria [famiglia]{"entity": "category", "role": "old"} in [tempo libero]{"entity": "category", "role": "new"}
- per l'attività [andare in farmacia](activity) modificare la categoria [salute personale]{"entity": "category", "role": "old"} in [salute]{"entity": "category", "role": "new"}
- per l'attività [dormire](activity) modifica la categoria [riposo]{"entity": "category", "role": "old"} in [salute]{"entity": "category", "role": "new"}
- per l'attività [uscita con la famiglia](activity) trasforma la categoria [svago]{"entity": "category", "role": "old"} in [tempo libero]{"entity": "category", "role": "new"}
- transformare la categoria [progetto]{"entity": "category", "role": "old"} dell'attività [prepare il powerpoint](activity) in categoria [university]{"entity": "category", "role": "new"}

## intent:modify_activity_name
- modifica il nome dell'attività [yoga]{"entity": "activity", "role": "old"} con il nome [pilates]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [andare a fisioterapia]{"entity": "activity", "role": "old"}
- voglio cambiare il nome dell'attività [ballo]{"entity": "activity", "role": "old"} con nome [canto]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [pittura]{"entity": "activity", "role": "old"} con il nome [mostra d'arte]{"entity": "activity", "role": "new"}
- per l'attività [andare al cinema]{"entity": "activity", "role": "old"} trasforma il nome con [andare a teatro]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [esame]{"entity": "activity", "role": "old"} nella categoria [università](category) con il nome [studio]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [esame]{"entity": "activity", "role": "old"} nella categoria [cultura](category) con nome [studio]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [mostra d'arte]{"entity": "activity", "role": "old"} con nome [mostra di pittura]{"entity": "activity", "role": "new"}
- nella categoria [università](category) cambia l'attività [seguire la lezione]{"entity": "activity", "role": "old"}  con il nome [andare a ricevimento]{"entity": "activity", "role": "new"}
- nella categoria [scuola](category) sostituisci il nome dell'attività [compito di matematica]{"entity": "activity", "role": "old"}  con il nome [interrogazione di matematica]{"entity": "activity", "role": "new"}
- per l'attività [andare a un concerto]{"entity": "activity", "role": "old"} modifica il nome con [andare al teatro]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [nuotare]{"entity": "activity", "role": "old"} nella categoria [attività fisica](category) con nome [jogging]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [andare dal dottore]{"entity": "activity", "role": "old"} con il nome [andare dal dentista]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [chiesa]{"entity": "activity", "role": "old"}  con il nome [meditazione]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [cucinare la cena]{"entity": "activity", "role": "old"} nella categoria [casa](category)
- cambia il nome dell'attività [jogging]{"entity": "activity", "role": "old"} nella categoria [attività fisica](category) con nome [nuotare]{"entity": "activity", "role": "new"}
- sostituire il nome dell'attività [leggere il giornare]{"entity": "activity", "role": "old"}  con nome [guardare il telegiornale]{"entity": "activity", "role": "new"}
- per l'attività [andare a giocare a calcio]{"entity": "activity", "role": "old"} nella categoria [tempo libero](category) modifica il nome con [suonare la chitarra]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [editare un video]{"entity": "activity", "role": "old"} con il nome [modificare un video]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [nuoto]{"entity": "activity", "role": "old"} nella categoria [sport](category) con il nome [boxe]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con nome [leggere un libro]{"entity": "activity", "role": "old"} con [leggere]{"entity": "activity", "role": "new"}

## intent:remove_item
- voglio rimuovere un'attività dall'elenco [spettacolo](category)
- rimuovi [giocare a basket](activity) alle 3:00
- elimina [riposo](activity) nella categoria [salute](category)
- ciao, voglio cancellare un'attività nella mia lista alle 18:14
- cancellare l'attività [scrivere la relazione](activity) nella categoria [ricerca](category)
- cancellare [compilare il modulo](activity) nella categoria [impegni](category)
- ciao, voglio cancellare un'attività nella categoria [sociale](category) alle 14:50
- cancella [inviare e-mail](activity) alle 9:30
- elimina l'attività [suonare il pianoforte](activity) nella categoria [musica](category)
- cancella [controllare le e-mail](activity) alle 00:00
- rimuovi [fare shopping](activity) nella categoria [faccende domestiche](category)
- cancellare l'attività [correggere i compiti](activity) nella categoria [lavoro](category)
- elimina [alzarsi](activity)
- voglio eliminare un'attività dall'elenco [leadership](category)
- voglio eliminare un'attività dall'elenco [scuola](category)
- rimuovi [revisione del progetto](activity) nella categoria [lavoro](category) alle 10:25
- rimuovi [riordinare l'armadio](activity) nella categoria [faccende domestiche](category) alle 10:25
- rimuovi [correre](activity)
- ciao, voglio rimuovere un'attività dall'elenco [ricreazione](category)
- voglio cancellare un'attività nella categoria [generi alimentari](category) alle 9:40
- cancella [pulire la casa](activity) nella categoria [faccende domestiche](category) alle 19:00
- rimuovi l'attività [studiare matematica](activity) nella categoria [università](category)
- elimina [fare una presentazione](activity) nella categoria [società](category)

## intent:presentation
- sono [giorgia](name)
- [gizio](name)
- nuovo utente
- [edoardo](name)
- [Foca](name)
- [edmondo](name)
- fammi iscrivere
- il mio nome è [alessia](name)
- [michelle](name)
- [rossana](name)
- [pino](name)
- [ercole](name)
- hi bot, il mio nome è [Gianluca](name)
- [nerone](name)
- [elga](name)
- creare un utente
- ciao, sono [nando](name)
- [mimmo](name)
- sono [simone](name)
- [isabella](name)
- [lucio](name)
- [ursola](name)
- sono [antonino](name)
- [pierluigi](name)
- sono [simo](name)
- [andrea](name)
- [cinzia](name)
- [michi](name)
- [venturino](name)
- [fabiano](name)
- [benedetto](name)
- [tina](name)
- il mio nome [Dario](name)
- [raimondo](name)
- [romi](name)
- [gianni](name)

## intent:inform
- [triennale](category)
- [barca](category)
- [fare la valigia](activity)
- [cercare](activity)
- [fare il rifornimento](activity)
- [andare a fare shopping](activity)
- [andare a pescare](activity)
- [uscire con gli amici](activity)
- [farmaci](category)
- [casa](category)
- [controllare il mercato](activity)
- ieri
- [viaggio in spagna](activity)
- [famiglia](category)
- 26 minuti e 30 secondi
- [riscuotere affitto](activity)
- [banca](category)
- [studiare per l'esame](activity)
- [laboratorio](category)
- [tempo libero](category)
- [esame patente](activity)
- [fare bilancio](activity)
- [cuocere biscotti](activity)
- [dottorato](category)
- [viaggiare](activity)
- [alzarsi](activity)
- [ascoltare musica](activity)
- [medico](category)
- [aggiustare orologio](activity)
- [cucinare per cena](activity)
- [presentare domanda](activity)
- [impegni](category)
- [ritirare stipendio](activity)
- [to do](category)
- [suonare la chitarra](activity)
- [armadietto](category)
- [studio](activity)
- [fare meeting](activity)
- [ristorante](category)
- il prossimo venerdì
- [personale](category)
- [dieta](category)
- [vacanze](category)
- [mensile](category)

## intent:add_item
- aggiungi [andare dai genitori](activity) in [famiglia](category) alle 20:00
- nella categoria [benessere](category) aggiungere l'attività [andare dal parrucchiere](activity) alle 21:10
- inserire l'attività [suonare il violino](activity) nella categoria [musica](category) alle 17:30
- creare [partecipare a una conferenza](activity) nella categoria [lavoro](category) alle 20:00
- voglio inserire un'attività nell'elenco [documentazione](category)
- aggiungi [prenota il volo](activity) in categoria [viaggio](category) alle 16:30
- ciao, vorrei aggiungere un'attività nella mia lista alle 18:14
- ciao, vorrei inserire un'attività nella mia lista alle 12:37
- inserire [festa](activity) nella categoria [intrattenimento](category) alle 10:25
- ciao, voglio aggiungere un'attività [parrucchiere](activity) nella categoria [benessere](category)
- aggiungi [chiamare mia madre](activity) alle 13:00
- vorrei inserire un'attività alla categoria [cura della mente](category)
- inserisci [dormire](activity) nella categoria [benessere](category)
- crea l'attività [cena](activity) nella categoria [cucina](category)
- inserisci [andare all'ufficio postale](activity) in [essenziali](category) per domani
- vorrei aggiungere un'attività [passeggiata](activity) alla categoria [quotidiano](category)
- metti l'attività [acquistare un regalo di natale](activity) in categoria [imminente](category) alle 9:40
- inserisci l'attività [nuotare](activity) nella categoria [sport](category)
- ciao, voglio inserire un'attività [sci](activity) nell'elenco [inverno](category)
- inserisci [giocare](activity) nella categoria [divertimento](category)
- metti [fare jogging](activity) in [sport](category)
- vorrei inserire un'attività [andare al cinema](activity) all'elenco [amicizia](category)
- ciao, voglio inserire un'attività nell'elenco [priorità](category)
- inserisci attività [controllare e-mail](activity) in [lavoro](category) alle 9:40
- aggiungi [partita](activity) alle 11:00
- inserire [guardare un film](activity) alle 11:00
- inserire [videoconferenza](activity) nella categoria [progetto](category) alle 14:50
- ciao, aggiungi l'attività [e-reading](activity) nella categoria [università](category)
- voglio inserire un'attività nell'elenco [computer](category)
- inserisci l'attività [fare stretching](activity) in [palestra](category)
- metti l'attività [studiare](activity) in [scuola](category)
- aggiungi [pulire la casa](activity) nella categoria [casa](category)
- aggiungere l'attività [spegnere la luce](activity) nella categoria [necessari](category) alle 3:29
- inserire [chiamare il medico](activity) nella categoria [salute](category) alle 22:20
- vorrei mettere l'attività [suonare](activity) in [settimanale](category)
- inserire [uscire](activity) alle 9:30
- vorrei inserire un'attività in un elenco
- ciao, aggiungi [psicologo](activity) nella categoria [mente](category)
- inserisci l'attività [fare giardinaggio](activity) in [casa](category)
- ciao, inserisci [taekwondo](activity) nella categoria [arti marziali](category)
- ciao, voglio inserire un'attività in un elenco
- ciao, voglio inserire un'attività nell'elenco [scadenze](category)
- inserisci una nuova attività [giardinaggio](activity)
- ciao, voglio inserire un'attività [ripetizioni](activity) nella categoria [laurea](category)
- ciao, voglio inserire una nuova attività [cena con gli amici](activity) nella categoria [amicizia](category)
- ciao, vorrei inserire un'attività in un elenco [spesa](category) alle 21:10
- ciao, aggiungi [comprare cibo](activity) nella categoria [dieta](category)
- metti l'attività [fare un bagno](activity) in [cura personale](category)
- ciao, vorrei inserire un'attività nella lista [politica](category) alle 17:30
- ciao, vorrei inserire un'attività nell'elenco [marketing](category) alle 17:30
- vorrei creare l'attività [festa di compleanno](activity) all'elenco [eventi](category)
- inserisci [prendere la medicina](activity) in categoria [salute](category) alle 20:30
- aggiungi l'attività [cantare](activity)
- ciao, voglio creare un'attività per la lista [primavera](category)
- inserisci [portare fuori il cane](activity) alle 3:00
- inserire [prenotazione](activity) alle 00:00

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
