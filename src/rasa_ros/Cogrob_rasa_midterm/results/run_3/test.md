## intent:bot_challenge
- Sto parlando con un umano?

## intent:goodbye
- ci si vede
- arrivederci

## intent:help
- Non so cosa fare
- Aiuto

## intent:greet
- Salve
- buona mattina

## intent:affirm
- si
- affermativo

## intent:mood_great
- Così perfetto
- Sono grande
- Sto per salvare il mondo

## intent:mood_unhappy
- Così triste
- Super triste

## intent:ask_name
- dici il mio nome
- puoi dire il mio nome?
- mi riconosci?

## intent:deny
- assolutamente no
- non mi va
- mai

## intent:clean_activities
- per favore, elimina tutte le mie attività completate
- elimina le attività
- pulisci tutte le attività completate

## intent:view_categories
- mostra le categorie
- Puoi mostrare le mie categorie?
- quali sono le categorie create?

## intent:remind_me_of
- non posso dimenticare di [fare gli esercizi](activity) alle 19:00
- ricordami [cena](activity)
- non posso dimenticare di fare l'attività [andare alla posta](activity) nella categoria [commissioni](category) lunedi prossimo
- ricordami la [riunione di lavoro](activity) domani mattina
- aiutami a non dimenticare l'attività [ripassare matematica](activity) nella categoria [scuola](category) per domani
- ricordami di [mangiare frutta](activity)
- aiutami a ricordare il [pranzo di lavoro](activity) dopodomani alle 12

## intent:view_activities
- quali sono le mie attività per domani mattina?
- quali sono le mie attività aggiunte per domani?
- mostra le attività nella categoria [palestra](category)
- mostra la mia attività [non fatta](activity_status) nella categoria [impegni](category)
- voglio vedere tutte le mie attività
- quali sono le mie attività [fatte](activity_status)?
- fammi vedere le attività per mercoledì sera
- quali sono le mie attività [terminate](activity_status)?

## intent:modify_category
- trasformare la categoria [vacanza]{"entity": "category", "role": "old"} in [banca]{"entity": "category", "role": "new"}
- alterare la categoria [cura personale]{"entity": "category", "role": "old"} in [divertimento]{"entity": "category", "role": "new"}
- sostituire la categoria [estate]{"entity": "category", "role": "old"} in [annuale]{"entity": "category", "role": "new"}
- voglio modificare il nome di una categoria
- voglio convertire la categoria [casa]{"entity": "category", "role": "old"} in [genitori]{"entity": "category", "role": "new"}
- voglio sostituire una categoria
- voglio sostituire la categoria [impegni]{"entity": "category", "role": "old"} con la categoria [lavoro]{"entity": "category", "role": "new"}
- per favore, voglio sostituire la categoria [cura]{"entity": "category", "role": "old"} a [stile di vita]{"entity": "category", "role": "new"}

## intent:add_category
- voglio mettere la categoria [vacanza](category)
- voglio usare una nuova categoria [eventi](category)
- la categoria da inserire è [volontariato](category)
- inserisci [amici](category)
- voglio aggiungere una nuova categoria [tempo libero](category)
- aggiungi la categoria [relazioni](category)
- metti [sport](category)
- aggiungi la categoria [studio](category)
- voglio usare una nuova categoria
- aggiungi la nuova categoria [banca](category)
- metti [sport](category) categoria

## intent:modify_activity_deadline
- per l'attività [andare in chiesa](activity) nella categoria [personale](category) modificare la scadenza con 22 ottobre 1922
- modifica la scadenza dell'attività [leggere](activity) nella categoria [università](category) da venerdì a domenica
- modifica il termine dell'attività [revisione del progetto](activity) nella categoria [università](category) in domenica
- per l'attività [bollette](activity) nella categoria [finanza](category) modificare la deadline dal 4 novembre al 22 ottobre 1922
- altera la deadline dell'attività [andare al mare](activity) nella categoria [tempo libero](category) in domenica
- per l'attività [prenotare l'aereo](activity) nella categoria [vacanza](category) trasformare la deadline in lunedì
- modifica la scadenza di un'attività
- sostituisci la scadenza dell'attività [torneo di calcio](activity) al 25 novembre
- altera la scadenza dell'attività [cantare](activity) in domenica
- voglio cambiare la scadenza dell'attività [pub](activity) nella categoria [svago](category) al 27 settembre 1998
- nella categoria [salute fisica](category) sostituisci la scadenza dell'attività [fisioterapia](activity) dal 22 settembre al 25 settembre
- voglio modificare la scadenza dell'attività [disegnare un ritratto](activity) nella categoria [lavoro](category) a domani alle 18:00

## intent:remove_category
- voglio eliminare la categoria [vacanza](category)
- voglio cancellare la categoria [università](category)
- voglio togliere la categoria [palestra](category)
- voglio togliere la categoria [settimanale](category)
- rimuovi [università](category) tra le mie categorie
- ciao, voglio togliere una categoria [eventi](category)
- rimuovere la categoria [ingegneria](category)
- voglio cancellare una categoria
- fai scomparire [spesa](category) dalle mie categorie
- voglio eliminare la categoria [progetti](category)
- voglio eliminare la categoria [sport](category)
- voglio eliminare la categoria [professione](category)

## intent:set_status_activity
- imposta come [concluso](activity_status) [giardinaggio](activity) nella categoria [giardino](category)
- imposta [fatto](activity_status) [powerpoint](activity) nella categoria [programmi](category)
- imposta come [non completato](activity_status) [nuotare](activity)
- imposta come [sviluppata](activity_status) [giocare a carte](activity)
- ciao, imposta un'attività [non completata](activity_status)
- imposta [non completato](activity_status) [pulire la cucina](activity) nella categoria [casa](category)
- ciao, imposta come [completa](activity_status) l'attività [partita di pallone](activity) in [palestra](category)
- poni come [completata](activity_status) l'attività [suonare il pianoforte](activity) in [musica](category)
- imposta [non fatto](activity_status) [ripeti matematica](activity) nella categoria [scuola](category)
- metti come [non finita](activity_status) [alzati](activity) in [quotidiano](category)
- imposta [completato](activity_status) [ripetere la presentazione](activity) nella categoria [progetti](category)
- imposta come [non fatta](activity_status) [leggere](activity)
- poni come [completato](activity_status) [riposare](activity) in [salute](category)
- imposta [sviluppata](activity_status) l'attività [suona la chitarra](activity) nella categoria [musica](category)
- poni [fatta](activity_status) l'attività [shampoo](activity) nella categoria [benessere personale](category)
- voglio impostare [fatta](activity_status) un'attività in un elenco

## intent:modify_activity_category
- convertire la categoria [giornaliero/settimanale]{"entity": "category", "role": "old"} dell'attività [yoga](activity)
- modifica la categoria [vacanze]{"entity": "category", "role": "old"} dell'attività [andare al mare](activity)
- trasforma la categoria [studio]{"entity": "category", "role": "old"} dell'attività [preparare l'esame](activity) in categoria [università]{"entity": "category", "role": "new"}
- per l'attività [andare in farmacia](activity) modificare la categoria [salute]{"entity": "category", "role": "old"} in [salute personale]{"entity": "category", "role": "new"}
- per l'attività [riposare](activity) modificare la categoria [stile di vita]{"entity": "category", "role": "old"} in [dieta]{"entity": "category", "role": "new"}
- per l'attività [uscita con la famiglia](activity) trasforma la categoria [tempo libero]{"entity": "category", "role": "old"} in [svago]{"entity": "category", "role": "new"}
- converti la categoria [urgente]{"entity": "category", "role": "old"} dell'attività [fare benzina](activity)
- modifica la categoria [svago]{"entity": "category", "role": "old"} dell'attività [andare al mare](activity) in [vacanze]{"entity": "category", "role": "new"}
- per l'attività [riposare](activity) modificare la categoria [dieta]{"entity": "category", "role": "old"} in [stile di vita]{"entity": "category", "role": "new"}
- per l'attività [giocare a carte](activity) cambiare la categoria [svago]{"entity": "category", "role": "old"} in [amici]{"entity": "category", "role": "new"}
- voglio cambiare la categoria [desideri]{"entity": "category", "role": "old"} dell'attività [prenotare l'hotel](activity) in [viaggio]{"entity": "category", "role": "new"}
- modifica la categoria dell'attività [andare al mare](activity)
- per l'attività [disegnare](activity) nella categoria [arte]{"entity": "category", "role": "old"} sostituire la categoria
- converti la categoria [importante]{"entity": "category", "role": "old"} dell'attività [fare benzina](activity) con [urgente]{"entity": "category", "role": "new"}
- per l'attività [pulire la casa](activity) nella categoria [quotidiano]{"entity": "category", "role": "old"} sostituire la categoria con [faccende domestiche]{"entity": "category", "role": "new"}
- converti la categoria [cura della persona]{"entity": "category", "role": "old"} dell'attività [correre](activity) con [sport]{"entity": "category", "role": "new"}
- per l'attività [partecipare alla conferenza](activity) trasforma la categoria [cultura]{"entity": "category", "role": "old"} in [lavoro]{"entity": "category", "role": "new"}

## intent:modify_activity_name
- sostituisci il nome dell'attività [camminare]{"entity": "activity", "role": "old"}  con il nome [imparare l'inglese]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [fare beneficenza]{"entity": "activity", "role": "old"} nella categoria [volontariato](category) con [organizzare raccolta fondi]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [viaggiare per lavoro]{"entity": "activity", "role": "old"}  con il nome [fare una presentazione]{"entity": "activity", "role": "new"}
- per l'attività [andare al teatro]{"entity": "activity", "role": "old"} modifica il nome con [andare a un concerto]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [andare a sciare]{"entity": "activity", "role": "old"} nella categoria [vacanza](category) con [andare in montagna]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [yoga]{"entity": "activity", "role": "old"} con il nome [pilates]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [ballo]{"entity": "activity", "role": "old"} con il nome [canto]{"entity": "activity", "role": "new"}
- nella categoria [eventi](category) cambia il nome dell'attività [andare dal parrucchiere]{"entity": "activity", "role": "old"}  con il nome [tagliare i capelli]{"entity": "activity", "role": "new"}
- cambia il nome dell'attività [meditazione]{"entity": "activity", "role": "old"}  con il nome [chiesa]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [organizzare raccolta fondi]{"entity": "activity", "role": "old"} nella categoria [volontariato](category) con [fare beneficenza]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [revisione]{"entity": "activity", "role": "old"} nella categoria [consegna](category) con il nome [rileggere]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con il nome [portare fuori il cane]{"entity": "activity", "role": "old"} in [quotidiana](category)
- per l'attività [prendere il treno]{"entity": "activity", "role": "old"} in [viaggio](category) trasforma il nome con [prendere l'autobus]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [editare un video]{"entity": "activity", "role": "old"} con il nome [modificare un video]{"entity": "activity", "role": "new"}
- voglio cambiare l'attività con nome [andare in montagna]{"entity": "activity", "role": "old"} nella categoria [vacanza](category) con [andare a sciare]{"entity": "activity", "role": "new"}
- sostituisci il nome dell'attività [pubblicare l'articolo]{"entity": "activity", "role": "old"}  con il nome [scrivere l'articolo]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [nuoto]{"entity": "activity", "role": "old"} nella categoria [sport](category) con il nome [boxe]{"entity": "activity", "role": "new"}
- nella categoria [scuola](category) sostituire il nome dell'attività [compito di latino]{"entity": "activity", "role": "old"}  con nome [interrogazione di latino]{"entity": "activity", "role": "new"}
- nella categoria [università](category) cambiare il nome dell'attività [esame]{"entity": "activity", "role": "old"}  con nome [studio]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [studio]{"entity": "activity", "role": "old"} nella categoria [cultura](category) con nome [esame]{"entity": "activity", "role": "new"}
- sostituisci il nome dell'attività [scrivere l'articolo]{"entity": "activity", "role": "old"}  con il nome [pubblicare l'articolo]{"entity": "activity", "role": "new"}

## intent:remove_item
- ciao, voglio cancellare un'attività nella categoria [commissioni](category) alle 22:20
- rimuovi [nuotare](activity) nella categoria [sport](category)
- elimina l'attività [giocare](activity) nella categoria [intrattenimento](category)
- voglio eliminare un'attività dall'elenco [documenti](category)
- cancellare [taekwondo](activity) nella categoria [hobby](category)
- rimuovi [revisione del progetto](activity) nella categoria [lavoro](category) alle 10:25
- voglio eliminare un'attività dall'elenco [scuola](category)
- elimina [shampoo](activity) nella categoria [quotidiana](category)
- cancella [parrucchiere](activity) nella categoria [benessere](category) alle 13:39
- elimina l'attività [psicologo](activity) nella categoria [mente](category)
- cancellare [compilare il modulo](activity) nella categoria [impegni](category)
- elimina [alzarsi](activity)
- cancella [andare a cantare](activity) alle 11:00
- cancella [studiare per l'esame](activity) nella categoria [università](category) alle 7:00
- cancella [andare a un incontro](activity) nella categoria [lavoro](category) alle 4:25
- ciao, voglio eliminare un'attività dall'elenco [divertimento](category)
- rimuovi [annaffiare le piante](activity) nella categoria [faccende domestiche](category) alle 13:29
- cancella [chiamare l'elettricista](activity) nella categoria [guasti](category) alle 21:10
- voglio eliminare un'attività dall'elenco [piacere](category)
- ciao, voglio cancellare un'attività dall'elenco [pianificazioni](category)
- rimuovi [lavare l'auto](activity) nella categoria [faccende domestiche](category) alle 22:20
- voglio cancellare un'attività nella categoria [imminente](category) alle 16:30
- cancellare l'attività [fare il powerpoint](activity) nella categoria [imminente](category)

## intent:presentation
- [andrea](name)
- sono [giorgia](name)
- [lilly](name)
- [anna](name)
- [fabiano](name)
- [valerio](name)
- [vito](name)
- [isabella](name)
- [marzia](name)
- [ernesto](name)
- [edoardo](name)
- [grazia](name)
- creare un utente
- sono [antonio](name)
- [riziero](name)
- [teresa](name)
- ciao sono [marcello](name)
- [stefano](name)
- [pino](name)
- [marta](name)
- iscrizione
- [guendalina](name)
- [aristide](name)
- [raimondo](name)
- hi bot, il mio nome è [Gianluca](name)
- [lorella](name)
- ciao, sono [marco](name)
- [chicca](name)
- voglio registrarmi
- [benedetto](name)
- [cathrine](name)
- [monia](name)
- ciao, sono [nando](name)
- [Foca](name)
- [clerice](name)
- [roberto](name)

## intent:inform
- [cinema](activity)
- prossima domenica
- [ritirare patente](activity)
- [andare alla banca](activity)
- [viaggio in Spagna](activity)
- [settimanale](category)
- [guardare un film](activity)
- [viaggi](category)
- [correre](activity)
- [allenamenti](category)
- [rata casa](activity)
- 19 ore
- [viaggio in brasile](activity)
- [arredamento](category)
- [casa](category)
- [esame patente](activity)
- [serata libera](activity)
- il prossimo venerdì
- [cuocere biscotti](activity)
- [studio](activity)
- [armadietto](category)
- [finanza](category)
- [affitto](activity)
- [ritirare stipendio](activity)
- [guardare mio figlio](activity)
- [dieta](category)
- [ritirare il pacco](activity)
- [prendere appunti](activity)
- [fare fisioterapia](activity)
- [tempo libero](category)
- [progetti](category)
- [palestra](category)
- [appuntamento romantico](activity)
- [alzarsi](activity)
- [saldare prestito](activity)
- [macchine](category)
- [fumetti](category)
- [carrello](category)
- [fare la valigia](activity)
- lunedì prossimo
- [corda](activity)
- [partecipare a una conferenza](activity)
- [escursioni](category)
- ieri

## intent:add_item
- ciao, aggiungi [acquistare una pizza](activity) nella categoria [mangiare](category)
- crea l'attività [cena](activity) nella categoria [cucina](category)
- aggiungere [ordinare l'armadio](activity) alle 01:45
- vorrei creare un'attività nella categoria [pianificazioni](category) alle 6:30
- inserire l'attività [suonare il violino](activity) nella categoria [musica](category) alle 17:30
- voglio inserire un'attività nell'elenco [computer](category)
- ciao, inserisci [ascoltare musica](activity)
- ciao, aggiungi una nuova attività [guardare il match](activity) nella categoria [interessi](category)
- ciao, inserisci l'attività [torneo di calcio](activity) nella categoria [sport](category)
- ciao, vorrei inserire un'attività nell'elenco [coaching](category) alle 19:00
- ciao, voglio inserire una nuova attività nella categoria [autunno](category)
- vorrei mettere l'attività [pagare le bollette](activity) alla categoria [banca](category)
- ciao, aggiungi [psicologo](activity) nella categoria [mente](category)
- nella categoria [corso](category) inserire [incontro](activity) alle 20:30
- aggiungi [correre](activity)
- ciao, vorrei aggiungere un'attività all'elenco [business](category) alle 18:30
- inserisci [yoga](activity)
- ciao, inserisci [vedere il match](activity) nella categoria [personale](category)
- ciao, voglio inserire un'attività [andare a boxe](activity) nella categoria [sport](category)
- ciao, aggiungi [scrivere un messaggio](activity)
- aggiungi [organizzare la cucina](activity) nella categoria [casa](category)
- ciao, nella categoria [salute](category) voglio inserire l'attività [andare dal dentista](activity)
- inserisci l'attività [fare stretching](activity) in [palestra](category)
- ciao, inserisci [andare a cantare](activity) nella categoria [tempo libero](category)
- inserire l'attività [preparare lo zaino](activity) nella categoria [organizzazione](category) alle 18:30
- inserisci [organizzare l'armadio](activity) nella categoria [abbigliamento](category)
- aggiungere [cucinare per cena](activity) alle 20:45
- ciao, voglio aggiungere un'attività [farmacia](activity) nella categoria [salute](category)
- aggiungere [risposare](activity) nella categoria [cura della mente](category) alle 2:55
- voglio inserire un'attività nella mia lista
- voglio inserire un'attività nella lista [piacere](category) alle 9:40
- aggiungi [boxe](activity) nella categoria [sport](category)
- aggiungere l'attività [uscire con gli amici](activity) nella categoria [società](category) alle 19:41
- aggiungere l'attività [cucinare](activity) nella categoria [casa](category) alle 21:10
- inserire l'attività [acquistare un libro](activity) nella categoria [apprendimento](category) alle 5:12
- voglio aggiungere un'attività nell'elenco [leadership](category)
- ciao, voglio aggiungere un'attività nell'elenco [vacanze di pasqua](category)
- inserire [consultare il blog](activity) alle 3:00
- ciao, vorrei inserire l'attività nell'elenco [imminente](category) alle 16:30
- nella categoria [benessere](category) aggiungere l'attività [andare dal parrucchiere](activity) alle 21:10
- aggiungi [partita](activity) alle 11:00
- metti l'attività [studiare](activity) in [scuola](category)
- aggiungi [fare le pulizie](activity) in [settimanale](category)
- inserisci una nuova attività [giardinaggio](activity)
- ciao, voglio aggiungere un'attività nell'elenco [visite mediche](category)
- inserisci [nuotare](activity) in [sport](category)
- inserisci l'attività [nuotare](activity) nella categoria [sport](category)
- ciao, inserisci [scrivere](activity) nella categoria [hobby](category)
- ciao, inserisci l'attività [e-commerce](activity) nella categoria [tecnologia](category)
- ciao, inserisci l'attività [giocare a carte](activity) nella categoria [divertimento](category)
- vorrei mettere l'attività all'elenco [apprendimento](category)
- ciao, voglio inserire una nuova attività [cena con gli amici](activity) nella categoria [amicizia](category)
- vorrei creare una nuova attività
- inserire l'attività [acquistare fiori](activity) nella categoria [spesa](category) alle 13:39
- ciao, inserisci [allenamento](activity)
- voglio inserire un'attività nell'elenco [documentazione](category)

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
