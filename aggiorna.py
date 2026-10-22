"""Rigenera index.html dalla bozza del prototipo.

La bozza (../2026-10-22_bozza_prototipo-gestionale.html) è scritta per gli artefatti di Claude,
che aggiungono da soli l'intestazione HTML. Questo script la trasforma in una pagina completa
per GitHub Pages.

Uso, dalla cartella gestionale-github:
    python aggiorna.py
"""
from pathlib import Path

QUI = Path(__file__).resolve().parent
BOZZA = QUI.parent / "2026-10-22_bozza_prototipo-gestionale.html"
USCITA = QUI / "index.html"

testo = BOZZA.read_text(encoding="utf-8")
punto = testo.index('<div class="app">')
testa, corpo = testo[:punto].strip(), testo[punto:].strip()

pagina = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex">
<style>body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{testa}
</head>
<body>
{corpo}
</body>
</html>
"""
USCITA.write_text(pagina, encoding="utf-8")
print(f"Scritto {USCITA.name} ({len(pagina):,} caratteri)")
