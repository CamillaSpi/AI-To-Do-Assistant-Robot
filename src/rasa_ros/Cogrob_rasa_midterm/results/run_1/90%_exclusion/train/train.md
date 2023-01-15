## intent:bot_challenge
- Sto parlando con un bot?

## intent:goodbye
- buona notte

## intent:help
- Non so cosa fare

## intent:greet
- Buongiorno

## intent:affirm
- esatto

## intent:mood_great
- Perfetto

## intent:ask_name
- puoi dire il mio nome?

## intent:mood_unhappy
- Sono così triste

## intent:deny
- no

## intent:clean_activities
- per favore, elimina tutte le mie attività completate

## intent:view_categories
- posso vedere quali sono le mie categorie?

## intent:remind_me_of
- ricordami il [pranzo di lavoro](activity)
- ricordami di [mangiare frutta](activity)
- non farmi dimenticare di [correre](activity) alle 19:00

## intent:view_activities
- quali sono le mie attività [terminate](activity_status)?
- voglio vedere tutte le attività create
- mostra attività [completate](activity_status)

## intent:modify_category
- trasformare la categoria [vacanza]{"entity": "category", "role": "old"} in [banca]{"entity": "category", "role": "new"}
- voglio sostituire la categoria [divertimento]{"entity": "category", "role": "old"} con [svago]{"entity": "category", "role": "new"}
- modificare la categoria [amicizia]{"entity": "category", "role": "old"} in [famiglia]{"entity": "category", "role": "new"}

## intent:add_category
- aggiungi la nuova categoria [personale](category)
- crea una nuova categoria
- voglio mettere una nuova categoria [vacanza](category)
- voglio aggiungere la categoria [stile di vita](category)

## intent:modify_activity_deadline
- modifica il termine dell'attività [revisione del progetto](activity) nella categoria [università](category) in domenica
- altera il termine dell'attività [karaoke](activity) da 18:00 alle 20:00
- altera la scadenza dell'attività [cena di Natale](activity) nella categoria [eventi](category) con lunedì
- voglio modificare la deadline dell'attività [suonare la chitarra](activity) nella categoria [musica](category) in domani alle 18:00
- voglio modificare la deadline dell'attività [scuolacalcio](activity) nella categoria [sport](category) per domani alle 18:00

## intent:remove_category
- rimuovi [università](category) tra le mie categorie
- ciao, voglio rimuovere la categoria [faccende domestiche](category)
- ciao, voglio eliminare la categoria [casa](category)
- ciao, voglio rimuovere una categoria [cura personale](category)
- fai scomparire [spesa](category) dalle mie categorie

## intent:set_status_activity
- imposta un'attività [completata](activity_status)
- imposta [completata](activity_status) [chiama il medico](activity)
- ciao, metti [non completato](activity_status) [andare dal parrucchiere](activity) nella categoria [benessere](category)
- ciao, imposta [non terminata](activity_status) [annaffia le piante](activity)
- poni come [completata](activity_status) l'attività [suonare il pianoforte](activity) in [musica](category)
- voglio impostare [fatta](activity_status) un'attività in un elenco

## intent:modify_activity_category
- per l'attività [pulire la casa](activity) nella categoria [quotidiano]{"entity": "category", "role": "old"} sostituire la categoria con [faccende domestiche]{"entity": "category", "role": "new"}
- cambia la categoria [esami]{"entity": "category", "role": "old"} dell'attività [studiare](activity) in categoria [progetti]{"entity": "category", "role": "new"}
- modifica la categoria [dieta]{"entity": "category", "role": "old"} dell'attività [camminare all'aperto](activity)
- per l'attività [fare intervento](activity) modifica la categoria
- per l'attività [andare in farmacia](activity) modificare la categoria [salute]{"entity": "category", "role": "old"} in [salute personale]{"entity": "category", "role": "new"}
- voglio cambiare la categoria [palestra]{"entity": "category", "role": "old"} dell'attività [boxe](activity) con la categoria [sport]{"entity": "category", "role": "new"}
- per l'attività [giocare a carte](activity) cambiare la categoria [svago]{"entity": "category", "role": "old"} in [amici]{"entity": "category", "role": "new"}

## intent:modify_activity_name
- voglio cambiare il nome dell'attività [andare a fisioterapia]{"entity": "activity", "role": "old"}
- voglio cambiare l'attività con nome [organizzare raccolta fondi]{"entity": "activity", "role": "old"} nella categoria [volontariato](category)
- modifica il nome dell'attività [pilates]{"entity": "activity", "role": "old"} con il nome [yoga]{"entity": "activity", "role": "new"}
- voglio cambiare il nome dell'attività [studio]{"entity": "activity", "role": "old"} nella categoria [cultura](category) con nome [esame]{"entity": "activity", "role": "new"}
- nella categoria [università](category) cambiare il nome dell'attività [esame]{"entity": "activity", "role": "old"}  con nome [studio]{"entity": "activity", "role": "new"}
- modifica il nome dell'attività [yoga]{"entity": "activity", "role": "old"} con il nome [pilates]{"entity": "activity", "role": "new"}
- per l'attività [andare a teatro]{"entity": "activity", "role": "old"} trasforma il nome con [andare al cinema]{"entity": "activity", "role": "new"}
- cambiare il nome dell'attività [meditazione]{"entity": "activity", "role": "old"}  con nome [chiesa]{"entity": "activity", "role": "new"}
- nella categoria [eventi](category) cambia il nome dell'attività [andare dal parrucchiere]{"entity": "activity", "role": "old"}  con il nome [tagliare i capelli]{"entity": "activity", "role": "new"}

## intent:remove_item
- rimuovi [giocare a basket](activity) alle 3:00
- voglio rimuovere un'attività da un elenco
- voglio cancellare un'attività alle 11:00
- cancellare l'attività [scrivere la relazione](activity) nella categoria [ricerca](category)
- rimuovi l'attività [leggere](activity) nella categoria [cultura](category)
- voglio eliminare un'attività dall'elenco [piacere](category)
- cancellare l'attività [fare il powerpoint](activity) nella categoria [imminente](category)
- cancella [arrampicata](activity) nella categoria [estate](category) alle 18:30

## intent:presentation
- [raimondo](name)
- [michelle](name)
- il mio nome [Dario](name)
- [adele](name)
- [faustino](name)
- nuovo utente
- ciao, sono [matteo](name)
- [gisel](name)
- [teresa](name)
- [ercole](name)
- [peppe](name)
- [edvige](name)
- [edmondo](name)
- voglio iscrivermi
- [federico](name)

## intent:inform
- [uscire in barca](activity)
- [cose da fare oggi](category)
- [to do](category)
- [cuocere biscotti](activity)
- 26 minuti e 30 secondi
- [lavori](category)
- [corso](activity)
- [scrivere una lettera](activity)
- [fare il pieno](activity)
- alle 18:00
- [tempo libero](category)
- [cena con i parenti](activity)
- [spegnere il gas](activity)
- [frigo](category)
- [pagare affitto](activity)
- [intervento](activity)
- [carrello](category)
- [alzarsi](activity)

## intent:add_item
- ciao, vorrei inserire un'attività nella lista [cultura](category) alle 16:00
- inserire [festa](activity) nella categoria [intrattenimento](category) alle 10:25
- ciao, voglio aggiungere un'attività nell'elenco [vacanze di pasqua](category)
- inserisci [prendere la medicina](activity) in categoria [salute](category) alle 20:30
- vorrei aggiungere un'attività all'elenco [deepwork](category)
- nella categoria [salute](category) inserisci un'attività [andare dal medico](activity)
- metti [fare jogging](activity) in [sport](category)
- inserisci [fare una passeggiata](activity) in [quotidiano](category)
- voglio inserire un'attività nell'elenco [computer](category)
- metti [nuotare](activity)
- inserire [prenotare le vacanze](activity) nella categoria [vacanza](category) alle 4:25
- ciao, vorrei inserire un'attività nell'elenco [sociale](category) alle 3:29
- aggiungi l'attività [nuotare](activity)
- inserisci [dormire](activity) nella categoria [benessere](category)
- metti [preparare la presentazione](activity) in [progetti](category)
- ciao, inserisci l'attività [studiare la filosofia](activity) nella categoria [scuola](category)
- inserisci [pulizie](activity) nella categoria [giornaliera](category)
- crea l'attività [cena](activity) nella categoria [cucina](category)
- ciao, aggiungi [cucinare la cena](activity) nella categoria [casa](category)
- ciao, inserisci [cena con i nonni](activity)
- nella categoria [estate](category), voglio aggiungere l'attività [arrampicata](activity)
- inserisci l'attività [volontariato](activity) in categoria [beneficenza](category) alle 13:39

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
