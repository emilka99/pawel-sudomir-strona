#!/usr/bin/env python3
"""Generuje statyczne strony HTML (strona główna + podstrony usług).

Uruchom z katalogu głównego repozytorium:  python3 tools/build.py
Edytuj treści w słownikach poniżej, a potem przebuduj strony.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

R = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
L = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>'
D = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg>'

SITE_URL = "https://przewodnikzawodowy.pl"   # podmień na docelową domenę
PHONE = "518 941 857"
PHONE_HREF = "+48518941857"
EMAIL = "pawel@przewodnikzawodowy.pl"
LINKEDIN = "https://pl.linkedin.com/in/pawel-sudomir"

SERVICES = [
    dict(slug="coaching", about="Coaching to przestrzeń, w której lider może zatrzymać się na chwilę i spojrzeć na swoją sytuację z dystansu. Pracujemy na realnych wyzwaniach: decyzjach, relacjach w zespole, presji wyników i własnej energii. Nie daję gotowych odpowiedzi, tylko pomagam dojść do rozwiązań, które naprawdę pasują do Ciebie i Twojej organizacji. Efektem są konkretne zmiany w sposobie działania, a nie chwilowa inspiracja.", desc="Indywidualna praca z liderem nad decyzjami, komunikacją i działaniem pod presją.", no="01", title="Coaching", photo="coaching.jpg", pos="45% 40%",
         lead="Indywidualny proces dla liderów i managerów, którzy chcą podejmować decyzje z większą jasnością i spokojem.",
         who=["Członkowie zarządów i dyrektorzy", "Managerowie średniego szczebla", "Liderzy w nowej roli lub w zmianie", "Osoby w transformacji zawodowej"],
         items_title="Trzy formy coachingu",
         items=["Executive coaching", "Business coaching", "Career & Life coaching", "Extended DISC®"],
         facts=[("6–10", "sesji w procesie"), ("90 min", "każda sesja"), ("EMCC", "kodeks etyczny i pełna poufność"), ("1:1", "indywidualna praca z liderem")]),
    dict(slug="mentoring", about="Dobrze zaprojektowany program mentoringowy to jeden z najskuteczniejszych sposobów na rozwój talentów i zatrzymanie w firmie najlepszych ludzi. Razem z działem HR projektuję cały proces: od celów i doboru par, przez przygotowanie mentorów, po wsparcie w trakcie i podsumowanie efektów. Dzięki temu wiedza i doświadczenie liderów nie zostają w ich głowach, tylko realnie pracują na rozwój organizacji.", desc="Programy, w których doświadczenie liderów realnie przechodzi na kolejnych managerów.", no="02", title="Programy mentoringowe", photo="sala.jpg", pos="50% 50%",
         lead="Projektuję i prowadzę programy, w których doświadczenie liderów realnie przechodzi na kolejnych managerów.",
         who=["Działy HR i L&D", "Organizacje rozwijające talenty i następców", "Firmy wprowadzające nowych managerów", "Zespoły po fuzjach i reorganizacjach"],
         items_title="Co obejmuje program",
         items=["Diagnoza i cele", "Dobór par mentor – mentee", "Przygotowanie mentorów", "Wsparcie i ewaluacja"],
         facts=[("3–9 mies.", "typowy czas programu"), ("1:1", "pary mentor – mentee"), ("HR", "stały partner po stronie firmy"), ("Raport", "podsumowanie efektów")]),
    dict(slug="warsztaty", about="Każdy warsztat zaczynam od rozmowy o tym, co ma się zmienić w codziennej pracy uczestników. Łączę wiedzę z zakresu przywództwa i komunikacji z doświadczeniem biznesowym, dlatego zajęcia opieram na realnych sytuacjach, a nie na teorii z podręcznika. Uczestnicy ćwiczą, testują i wychodzą z narzędziami, które mogą zastosować od razu.", desc="Praktyczne warsztaty z przywództwa, komunikacji i pracy pod presją. Mniej teorii, więcej ćwiczeń.", no="03", title="Warsztaty i szkolenia", photo="warsztaty.jpg", pos="50% 55%",
         lead="Praktyczne warsztaty z przywództwa, komunikacji i pracy pod presją. Mniej teorii, więcej ćwiczeń i decyzji.",
         who=["Kadra menedżerska", "Nowo awansowani managerowie", "Zespoły projektowe i sprzedażowe", "Działy HR i People & Culture"],
         items_title="Przykładowe tematy",
         items=["Przywództwo w praktyce", "Komunikacja pod presją", "Delegowanie i samodzielność zespołu", "Lider bez wypalenia", "Extended DISC® w zespole", "Program szyty na miarę"],
         facts=[("1–2 dni", "lub cykl modułów"), ("8–20", "osób w grupie"), ("Na miejscu", "lub online"), ("Praktyka", "ćwiczenia na realnych case’ach")]),
    dict(slug="facylitacja", about="Jako facylitator dbam o to, żeby zespół mógł skupić się na treści, a nie na procesie. Prowadzę spotkania strategiczne, warsztaty zarządu i trudne rozmowy tak, by każdy głos został usłyszany, a spotkanie zakończyło się konkretnymi decyzjami. W coachingu zespołowym pracujemy nad tym, jak zespół współpracuje, komunikuje się i bierze odpowiedzialność za wspólne cele.", desc="Spotkania, na których zarządy i zespoły dochodzą do decyzji, oraz praca nad współpracą w zespole.", no="04", title="Facylitacja i coaching zespołowy", photo="facylitacja.jpg", pos="40% 50%",
         lead="Prowadzę spotkania, na których zespoły i zarządy dochodzą do decyzji — i pracuję z zespołem nad współpracą.",
         who=["Zarządy i zespoły kierownicze", "Zespoły po zmianach lub w konflikcie", "Nowo tworzone zespoły", "Organizacje planujące strategię"],
         items_title="Jak mogę pomóc",
         items=["Spotkania strategiczne", "Retrospektywy i trudne rozmowy", "Coaching zespołowy", "Profil zespołu Extended DISC®"],
         facts=[("Neutralność", "prowadzę proces, nie narzucam treści"), ("Cel", "konkretne decyzje i ustalenia"), ("4–15", "osób w zespole"), ("Follow-up", "podsumowanie i plan działań")]),
]

REVIEWS = [  # (imię, rola, cytat, inicjały, styl) — źródło: przewodnikzawodowy.pl/coaching
    ("Sandra Samson-Muszyńska", "Senior Business Developer", "Miałam okazję współpracować z Pawłem w obszarze coachingu. Otrzymałam konkretne wsparcie, wskazówki i narzędzia. Polecam każdemu, kto szuka profesjonalnej współpracy i doświadczenia. Paweł posiada odpowiednie kompetencje i wiedzę, którymi się dzieli i umiejętnie kieruje, tak aby wypracować najlepsze rozwiązania. Właśnie takie podejście pomogło mi wybrać kierunek działania, ustalić priorytety oraz zaplanować kolejne kroki. Bardzo polecam!", "SS", ""),
    ("Barbara Kozłowska-Jakóbik", "International Leasing Manager", "Nie jestem osobą, która przesadnie wierzyła w coaching. Ale jestem wdzięczna, że się zdecydowałam na pracę z Pawłem.\nPaweł to coach uważny, skrupulatny. Przygotowany na każdą kolejną sesję. Tworzy atmosferę zaufania i komfortu – co nie jest łatwe, szczególnie rozmawiając online! Co szczególnie do mnie trafiło to to, że za każdym razem wiedziałam, że mogę przyjść z tym, czego akurat potrzebuję, a Paweł podąży za mną – bo ma do tego narzędzia i przygotowanie.\nWypracowałam z jego pomocą narzędzia, z których korzystam codziennie i naprawdę ułatwiają mi życie.\nGdy szukasz zmiany, potrzebujesz się przeprofilować, coś Cię uwiera – szczególnie w życiu profesjonalnym – Paweł to Twój człowiek!\nPowodzenia Paweł i jeszcze raz wielkie dzięki!", "BK", "dark"),
    ("Aleksandra Ryńska", "Leader @ Semantive, People & Culture", "Praca z Pawłem to nie był po prostu „proces coachingowy” – to była dobra, ludzka rozmowa, którą Paweł potrafił dobrze prowadzić. Paweł tworzy przestrzeń, w której naprawdę mogłam się zatrzymać, pomyśleć, powiedzieć coś na głos bez obaw. Słucha uważnie, z ciekawością i bez presji. Dzięki niemu poukładałam kilka ważnych dla siebie spraw ale i wzmocniłam siebie. Bardzo polecam każdemu, kto szuka nie tylko coacha, ale też uważnego towarzysza w zmianie. Dzięki Paweł!", "AR", ""),
    ("Iryna Siwiak", "Executive Assistant for CEO, FoodWell Sp. z o.o.", "Miałam coaching z Pawłem 🙂 Nie wiedziałam, czego się spodziewać, a wyszłam z konkretnymi narzędziami i nową energią – dziękuję! Dzięki Tobie poukładałam sobie w głowie więcej niż przez ostatnie miesiące. Przez cały czas czułam wsparcie i przestrzeń do przemyśleń. Trafne spostrzeżenia i różnorodne pytania pomogły mi skupić się na tym, co naprawdę ważne, dzięki czemu dość szybko osiągnęłam cel. Gorąco polecam! 🙂", "IS", ""),
    ("Paulina Skowron", "Communication & PR Manager, SAIC Motor Poland (MG)", "Sesje coachingowe z Pawłem, to kilka tygodni pełne emocji i refleksji. Pokazały mi szerszą perspektywę patrzenia na świat, na problemy i wyzwania – dotyczy to zarówno sfery prywatnej jak i służbowej. Nie wiedziałam czego się spodziewać po sesjach, ale Paweł świetnie poprowadził mnie za rękę.\nOkazało się, że „się da”, że jest rozwiązanie, że mam zasoby i muszę (i chcę!) po nie sięgnąć. Paweł jest bardzo uważny, ma doskonałe wyczucie sytuacji i daje przestrzeń na to, aby przemyśleć i przeanalizować.\nNabrałam pewności siebie (która mnie mocno ograniczała), zaczęłam doceniać sama siebie, okazało się, że mogę więcej i że mogę realizować moje cele.\nSesje coachingowe z Pawłem to podróż w głąb siebie i absolutnie polecam każdemu, kto choć przez chwilę wątpi w siebie i myśli, że „się nie da”!\nPaweł: dziękuję Ci za tę fantastyczną przygodę, którą na pewno będziemy jeszcze wspólnie kontynuować.", "PS", "ink"),
]

LOGOS = [  # (plik w assets/img/logos, nazwa, kolor tła kafelka = tło logo) — źródło: przewodnikzawodowy.pl
    ("stylowy-biznes.webp", "Stylowy Biznes", "#BFB5A4"), ("katalog-marzen.webp", "Katalog Marzeń", "#FFFFFF"),
    ("okam.webp", "OKAM", "#BC3B37"), ("fundacja-nowy-staw.webp", "Fundacja Nowy Staw", "#FFFFFF"),
    ("strefa-kadr-i-plac.webp", "Strefa Kadr i Płac", "#13152B"), ("sport-evolution.webp", "Sport Evolution", "#FFFFFF"),
    ("polka.webp", "PolKa — Polska Kaucja", "#FFFFFF"), ("res-energy.webp", "res energy", "#FFFFFF"),
    ("coi.webp", "Centralny Ośrodek Informatyki", "#111B3F"),
]


def head(r, title, desc, canonical):
    return f'''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE_URL}{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE_URL}/assets/img/hero.jpg">
<meta name="theme-color" content="#E2E1E0">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{r}assets/fonts/space-grotesk-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}assets/css/style.css">
<script defer src="{r}assets/js/main.js"></script>
</head>'''


def header(r, home, solid=False):
    h = "" if home else f"{r}index.html"
    cls = "header is-solid" if solid else "header"
    return f'''<body{' class="home"' if home else ''}>
<a class="skip" href="#main">Przejdź do treści</a>
<header class="{cls}" data-solid="{'1' if solid else '0'}">
  <div class="container">
    <a class="brand" href="{h or '#top'}" aria-label="Paweł Sudomir — strona główna"><b>Paweł Sudomir</b><small>Executive &amp; Leadership Coach</small></a>
    <nav class="nav" aria-label="Główna nawigacja">
      <a href="{h}#uslugi">Usługi</a>
      <a href="{h}#o-mnie">O mnie</a>
      <a href="{h}#opinie">Opinie</a>
      <a class="btn" href="#kontakt">Kontakt <span class="ic">{R}</span></a>
    </nav>
    <button class="burger" aria-label="Otwórz menu" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span></button>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu" aria-hidden="true">
  <nav aria-label="Menu mobilne">
    <a href="{h}#uslugi">Usługi</a>
    <a href="{h}#o-mnie">O mnie</a>
    <a href="{h}#opinie">Opinie</a>
    <a href="#kontakt">Kontakt</a>
  </nav>
  <div class="mm-contact"><a href="tel:{PHONE_HREF}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
</div>'''


def contact():
    rows = [("Telefon", PHONE, f"tel:{PHONE_HREF}", ""), ("E-mail", EMAIL, f"mailto:{EMAIL}", ""), ("LinkedIn", "in/pawel-sudomir", LINKEDIN, ' target="_blank" rel="noopener"')]
    rr = "\n".join(f'        <a class="c-row" href="{h}"{x}><small>{l}</small><span>{v}</span><i>{R}</i></a>' for l, v, h, x in rows)
    return f'''<section class="contact-wrap container" id="kontakt" aria-labelledby="kontakt-h">
    <div class="contact rv">
      <div class="blob" aria-hidden="true"></div>
      <div>
        <p class="kicker">Kontakt</p>
        <h2 id="kontakt-h">Porozmawiajmy<span>.</span></h2>
        <p class="note">Podczas konsultacji opowiem, jak mogę Ci pomóc.</p>
      </div>
      <div class="c-rows">
{rr}
      </div>
    </div>
  </section>'''


def footer(r):
    links = "".join(f'<a href="{r}uslugi/{s["slug"]}.html">{s["title"].split(" ")[0] if s["slug"]!="mentoring" else "Mentoring"}</a>' for s in SERVICES)
    return f'''<footer class="footer">
  <div class="container">
    <span>© <span data-year>2026</span> Paweł Sudomir · Przewodnik Zawodowy</span>
    <nav aria-label="Stopka">{links}<a href="{r}polityka-prywatnosci.html">Polityka prywatności</a></nav>
  </div>
</footer>
</body>
</html>
'''


def home():
    r = ""
    cards = "\n".join(f'''      <a class="svc rv{' rv-d1' if i % 2 else ''}" href="uslugi/{s['slug']}.html">
        <span class="nr">({s['no']})</span>
        <span class="arrow" aria-hidden="true">{R}</span>
        <span class="bottom"><h3>{s['title']}</h3><span class="desc"><span>{s['desc']}</span></span><span class="more">Więcej</span></span>
      </a>''' for i, s in enumerate(SERVICES))
    reviews = "\n".join(f'''      <figure class="review {st}">
        <div><div class="q" aria-hidden="true">“</div><blockquote>{"".join(f"<p>{x}</p>" for x in q.split(chr(10)))}</blockquote><button type="button" class="read-more" data-read>Czytaj całość</button></div>
        <figcaption><img class="av" src="assets/img/opinie/{ini.lower()}.jpg" alt="" width="46" height="46"><span><b>{n}</b><small>{ro}</small></span></figcaption>
      </figure>''' for n, ro, q, ini, st in REVIEWS)
    logos = "".join(f'<span class="logo" style="background:{bg}"><img src="assets/img/logos/{f}" alt="{n}" height="100"></span>' for f, n, bg in LOGOS)
    stmt = 'Biznes i ludzie <br>w <strong>jednym procesie</strong>'
    body = f'''{head(r, "Paweł Sudomir — Executive & Leadership Coach", "Executive & Leadership Coach z akredytacją EMCC. Coaching, programy mentoringowe, warsztaty i szkolenia, facylitacja i coaching zespołowy.", "/")}
{header(r, True)}
<main id="main">
  <section class="hero" id="top" aria-label="Wprowadzenie">
    <div class="hero-media" data-parallax="0.18"><img src="assets/img/hero.jpg" alt="Paweł Sudomir podczas wystąpienia" width="1672" height="941" fetchpriority="high"></div>
    <div class="hero-inner container">
      <span class="hero-tag fade-in">Executive &amp; Leadership Coach · EMCC</span>
      <h1><span class="line"><span>Paweł</span></span><span class="line"><span>Sudomir</span></span></h1>
      <p class="lead fade-in d1">Wspieram w podejmowaniu decyzji i skutecznym działaniu w wymagającym środowisku</p>
      <div class="hero-actions fade-in d2">
        <a class="btn btn-cream" href="#kontakt">Porozmawiajmy</a>
        <a class="btn btn-glass" href="#uslugi">Obszary współpracy <span class="ic">{D}</span></a>
      </div>
    </div>
  </section>

  <section class="container" aria-label="W liczbach">
    <div class="stats">
      <div class="stat rv"><div class="num"><span data-count="15">15</span><sup>+</sup></div><p>lat doświadczenia</p></div>
      <div class="stat rv rv-d1"><div class="num"><span data-count="300">300</span><sup>+</sup></div><p>godzin sesji</p></div>
      <div class="stat rv rv-d2"><div class="num"><span data-count="50">50</span><sup>+</sup></div><p>procesów coachingowych</p></div>
      <div class="stat rv rv-d3"><div class="num">EMCC</div><p>akredytacja</p></div>
    </div>
  </section>

  <section class="section container" id="uslugi" aria-labelledby="uslugi-h">
    <div class="sec-head rv"><p class="kicker">Obszary współpracy</p><h2 class="h-xl" id="uslugi-h">W czym pomagam</h2></div>
    <div class="services">
{cards}
    </div>
  </section>

  <section class="statement container" aria-label="Motto"><p data-words>{stmt}</p></section>

  <section class="about" id="o-mnie" aria-labelledby="o-mnie-h">
    <div class="gallery" data-gallery>
      <figure class="g1 rv" data-float="-0.04"><img src="assets/img/sala.jpg" alt="Warsztat prowadzony przez Pawła Sudomira" loading="lazy" width="1000" height="750"></figure>
      <figure class="g2 rv rv-d1">
        <div class="ph"><img src="assets/img/coaching.jpg" alt="Paweł Sudomir podczas sesji coachingowej" loading="lazy" width="900" height="1038"></div>
        <div class="badges"><img src="assets/img/akredytacje.png" alt="Akredytacje: ICF ACC, EMCC Global Individual Accreditation, AoEC Practitioner Graduate" loading="lazy" width="906" height="252"></div>
      </figure>
      <figure class="g3 rv rv-d2" data-float="0.05"><img src="assets/img/warsztaty.jpg" alt="Uczestnicy warsztatu przy pracy" loading="lazy" width="900" height="1200"></figure>
    </div>
    <div class="about-text">
      <p class="kicker rv">O mnie</p>
      <h2 class="h-xl rv" id="o-mnie-h">Executive &amp; Leadership Coach</h2>
      <div class="body rv">
        <p>Łączę doświadczenie biznesowe zdobyte w międzynarodowych organizacjach z coachingiem transformacyjnym, szkoleniami i doradztwem. Dzięki temu rozumiem nie tylko wyzwania związane z rozwojem liderów, ale również presję odpowiedzialności za ludzi, realizację strategii i osiąganie wyników biznesowych.</p>
        <p>Jestem <strong>Executive &amp; Leadership Coachem</strong> z międzynarodową akredytacją <strong>EMCC</strong> oraz absolwentem programu <strong>Executive Coach AoEC (Academy of Executive Coaching)</strong> – potrójnie akredytowanego przez <strong>EMCC, ICF i Association for Coaching</strong>. Od ponad 15 lat współpracuję z liderami, zarządami i organizacjami, wspierając ich w rozwoju przywództwa, prowadzeniu zmian oraz budowaniu organizacji, które skutecznie realizują swoje cele biznesowe.</p>
      </div>
    </div>
  </section>

  <section class="passion" id="pasja" aria-labelledby="pasja-h">
    <div class="passion-media" data-parallax="0.12"><img src="assets/img/pasja.jpg" alt="Paweł Sudomir podczas biegu górskiego" loading="lazy" width="1440" height="960"></div>
    <div class="container">
      <div class="passion-box">
        <div class="rv"><p class="big" id="pasja-h"><span data-count="13">13</span> lat</p><p class="sub">ultramaratonów górskich</p></div>
        <p class="txt rv rv-d1">Góry uczą tego, czego uczę liderów. Konsekwencji, cierpliwości i zarządzania energią: umiejętności niezwykle potrzebnych w przywództwie.</p>
      </div>
    </div>
  </section>

  <section class="section" id="opinie" aria-labelledby="opinie-h">
    <div class="container reviews-head rv">
      <div class="sec-head" style="margin:0"><p class="kicker">Opinie</p><h2 class="h-xl" id="opinie-h">Co mówią klienci</h2></div>
      <div class="car-nav"><button type="button" data-prev aria-label="Poprzednia opinia">{L}</button><button type="button" data-next aria-label="Następna opinia">{R}</button></div>
    </div>
    <div class="track rv" data-track tabindex="0" aria-label="Opinie klientów (przewijane)">
{reviews}
    </div>
  </section>

  <dialog class="review-dialog" id="review-dialog" aria-label="Pełna opinia">
    <button type="button" class="rd-close" aria-label="Zamknij" data-close><span></span><span></span></button>
    <div class="rd-body"></div>
  </dialog>

  <section class="logos" aria-label="Firmy, z którymi współpracuję">
    <p>Zaufali mi m.in.</p>
    <div class="marquee"><div class="marquee-track"><div class="marquee-set">{logos}</div><div class="marquee-set" aria-hidden="true">{logos}</div></div></div>
  </section>

  {contact()}
</main>
{footer(r)}'''
    (ROOT / "index.html").write_text(body, encoding="utf-8")


def service(s):
    r = "../"
    others = "\n".join(f'''      <a class="o-row" href="{o['slug']}.html"><small>({o['no']})</small><span>{o['title']}</span><i>{R}</i></a>''' for o in SERVICES if o is not s)
    who = "".join(f'<li class="rv">{w}</li>' for w in s["who"])
    items = "".join(f'<li class="rv"><small>0{i+1}</small><span>{t}</span></li>' for i, t in enumerate(s["items"]))
    facts = "".join(f'<div class="stat rv"><div class="num">{a}</div><p>{b}</p></div>' for a, b in s["facts"])
    body = f'''{head(r, f"{s['title']} — Paweł Sudomir", s['lead'], f"/uslugi/{s['slug']}.html")}
{header(r, False, solid=True)}
<main id="main" class="page-top">
  <section class="sp-hero" aria-labelledby="h1">
    <div class="sp-text">
      <div class="blob" aria-hidden="true"></div>
      <nav class="crumbs fade-in" aria-label="Okruszki"><a href="../index.html">Strona główna</a><span>/</span><a href="../index.html#uslugi">Usługi</a><span>/</span><span aria-current="page">{s['title']}</span></nav>
      <div class="sp-main">
        <p class="nr fade-in">({s['no']})</p>
        <h1 id="h1" class="fade-in d1">{s['title']}</h1>
        <p class="lead fade-in d2">{s['lead']}</p>
        <a class="btn btn-cream fade-in d3" href="#kontakt">Zapytaj o współpracę</a>
      </div>
    </div>
    <div class="sp-photo"><img src="../assets/img/{s['photo']}" alt="{s['title']} — Paweł Sudomir" style="object-position:{s['pos']}"></div>
  </section>

  <div class="container">
    <section class="sp-intro" aria-label="Opis"><p class="kicker rv">O usłudze</p><p class="sp-intro-text rv">{s['about']}</p></section>
    <div class="sp-grid">
      <section aria-labelledby="kto"><p class="kicker rv">Dla kogo</p><h2 class="sp-h rv" id="kto">Z kim pracuję</h2><ul class="lines">{who}</ul></section>
      <section aria-labelledby="zakres"><p class="kicker rv">Zakres</p><h2 class="sp-h rv" id="zakres">{s['items_title']}</h2><ul class="lines numbered">{items}</ul></section>
    </div>
    <div class="stats sp-stats" aria-label="W skrócie">{facts}</div>
    <nav class="others" aria-labelledby="inne">
      <p class="kicker rv" id="inne">Inne obszary</p>
      <div class="o-rows">
{others}
      </div>
    </nav>
  </div>
  {contact()}
</main>
{footer(r)}'''
    (ROOT / "uslugi" / f"{s['slug']}.html").write_text(body, encoding="utf-8")


def privacy():
    r = ""
    body = f'''{head(r, "Polityka prywatności — Paweł Sudomir", "Polityka prywatności strony Pawła Sudomira.", "/polityka-prywatnosci.html")}
{header(r, False, solid=True)}
<main id="main" class="container legal">
  <h1>Polityka prywatności</h1>
  <p>[Do uzupełnienia: administrator danych, zakres i cel przetwarzania, pliki cookies, prawa użytkownika, kontakt w sprawie danych osobowych.]</p>
  <p><a class="link-more" href="index.html">Wróć na stronę główną</a></p>
</main>
{footer(r)}'''
    (ROOT / "polityka-prywatnosci.html").write_text(body.replace('href="#kontakt"', 'href="index.html#kontakt"'), encoding="utf-8")


if __name__ == "__main__":
    (ROOT / "uslugi").mkdir(exist_ok=True)
    home()
    for s in SERVICES:
        service(s)
    privacy()
    print("Gotowe: index.html, uslugi/*.html, polityka-prywatnosci.html")
