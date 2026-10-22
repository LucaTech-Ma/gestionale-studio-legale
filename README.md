# Gestionale per piccoli studi legali · prototipo

Prototipo navigabile di un gestionale per piccoli studi legali. **Tutti i dati sono inventati**: pratiche, persone e società sono di esempio.

## Cosa mostra

**Pagine essenziali**
- **Recap**: in una frase e tre numeri, cosa c'è da fare oggi e nei prossimi giorni e quali compensi vanno sollecitati.
- **Pratiche**: numero di pratica e fascicolo, assistiti e controparti, autorità, responsabile, prossima udienza. Si aggiungono con "Nuova pratica". La scheda di ogni pratica permette di registrare ore e pagamenti e di aggiungere udienze e scadenze.
- **Udienze e scadenze**: un'agenda unica, divisa per settimana.
- **Clienti e controparti**: anagrafica con il controllo del conflitto di interessi.
- **Compensi e incassi**: concordato, pagato, residuo e solleciti.

**Pagine aggiuntive**
- **Preventivo**: fasi del giudizio e complessità. Gli importi per fase sono dimostrativi, non quelli del DM 147/2022.
- **Mandato**: si compila dal preventivo o dalla pratica. Il testo è di esempio, non un modello legale.
- **Margine e ROI**: guadagno e ore di ogni pratica, per capire quali rendono di più e quali di meno.
- **Mappa delle funzioni**: importanza, risparmio e problema risolto di ogni funzione.

Le pratiche, le ore e i pagamenti aggiunti restano solo nel browser di chi li inserisce.

## Come si apre

- **Online**: con GitHub Pages attivo, all'indirizzo `https://lucatech-ma.github.io/gestionale-studio-legale/`. La pagina chiede ai motori di ricerca di non indicizzarla.
- **In locale**: doppio clic su `index.html`. Serve la connessione a internet per i font.

## Come si aggiorna

La pagina nasce dalla bozza `2026-10-22_bozza_prototipo-gestionale.html`, nella cartella sopra questa. Dopo ogni modifica alla bozza:

```
python aggiorna.py
git add index.html
git commit -m "Descrizione della modifica"
git push
```
