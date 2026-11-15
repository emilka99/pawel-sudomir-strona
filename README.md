# Paweł Sudomir — strona www

Statyczna strona (HTML, CSS, JavaScript) bez frameworków i bez procesu budowania. Działa na GitHub Pages, Netlify, Vercel i każdym zwykłym hostingu.

## Struktura

```
index.html                  strona główna
uslugi/*.html               podstrony usług (Coaching, Mentoring, Warsztaty, Facylitacja)
polityka-prywatnosci.html   do uzupełnienia
assets/css/style.css        style (kolory i rozmiary w :root)
assets/js/main.js           animacje i interakcje
assets/fonts/               Space Grotesk (OFL), serwowany lokalnie
assets/img/                 zdjęcia
tools/build.py              generator HTML (treści usług, opinie, kontakt)
```

## Edycja treści

Treści usług, opinie, dane kontaktowe i loga są w `tools/build.py`. Po zmianie przebuduj strony:

```bash
python3 tools/build.py
```

Możesz też edytować pliki `.html` bezpośrednio. Pamiętaj jednak, że ponowne uruchomienie skryptu nadpisze te zmiany.

## Podgląd lokalny

```bash
python3 -m http.server 8000
# otwórz http://localhost:8000
```

## Publikacja na GitHub Pages

1. Wypchnij repozytorium na GitHub.
2. Wejdź w **Settings → Pages**, wybierz **Deploy from a branch**, gałąź `main`, folder `/ (root)`.
3. Własna domena: dodaj plik `CNAME` z nazwą domeny i ustaw rekordy DNS.

## Do uzupełnienia

- Loga firm (pasek „Zaufali mi”): teraz to nazwy wpisane tekstem. Docelowo pliki SVG.
- Pełne teksty opinii.
- Polityka prywatności.
- `SITE_URL` w `tools/build.py` (docelowa domena, używana w meta tagach).
