<h1 align="center">Lāčplēsis</h1>
<h4 align="center">Bots osu!Latvia discord serverim</h4>

## Projekta uzdevums

Izstrādāt lietotnes Discord botu, kurš:

- automātiski savieno osu! kontus ar discord kontiem, analizējot lietotāju discord "rich presence"
- automātiski piešķir lietotājiem discordā attiecīgo statusu atkarībā no to pozīcijas osu! valsts topā
- publicē spēlētāju jaunākos rezultātus

## Izmantotās bibliotēkas

*   `aiohttp`: HTTP klienta bibliotēka, tiek izmantota asinhronu API pieprasījumu veikšanai, galvenokārt uz osu! API.
*   `asyncpg`: PostgreSQL datu bāzes klienta bibliotēka, tiek izmantota, lai piekļūtu PostgreSQL datubāzei.
*   `discord.py`: Python bibliotēka Discord API izmantošanai. Šī ir galvenā bibliotēka, kas ļauj botam izveidot savienojumu ar Discord, klausīties notikumus, atbildēt uz komandām un pārvaldīt lomas.
*   `loguru`: Žurnalēšanas bibliotēka. Tā palīdz atkļūdot un uzraudzīt bota darbību un iespējamās kļūdas.
*   `python-dateutil`: Paplašinājumi `datetime` modulim. Tiek izmantota datumu un laiku parsēšanai, manipulēšanai un formatēšanai.
*   `python-dotenv`: Nolasa vides mainīgos no `.env` faila un padara tos pieejamus Python kodā.
*   `rosu-pp-py`: Bibliotēka, kas paredzēta osu! veiktspējas punktu (pp) aprēķināšanai. Ar to ir iespējams analizēt osu! rezultātus, lai publicētu jaunākos spēlētāju rezultātus.
*   `ruff`: Python linteris un formatētājs, kurš tiek izmantots, lai pārbaudītu kļūdas kodā un formatētu kodu.

## Datu struktūras

Projektā ir izveidots fails `src/custom_datastructures.py`, kurā tiek definētas paštaisītas datu struktūras.
Piemēram, ir implementēta `CustomSet` klase, kas demonstrē vienkāršu kopas (set) funkcionalitāti un tiek izmantota, lai pārbaudītu vai datubāzē nav dublikāti.

Tāpat ir implementēta `CustomHashTable` klase, kas nodrošina vienkāršu jaucējtabulas funkcionalitāti. Šī struktūra tiek izmantota konfigurācijas datu glabāšanai vai ātrai datu atrašanai pēc atslēgas, piemēram, konfigurācijas failos.

## Kā uzstādīt

1. Klonē repozitoriju
2. Uzstādi [uv](https://docs.astral.sh/uv/getting-started/installation/)
3. Palaid `uv sync`, lai uzinstalētu bibliotēkas
4. Izveido `.env` failu balstoties uz `.env.example` un modificē src/config.py ar savām vērtībām
5. Palaid `uv run src/app.py`, lai startētu botu

Alternatīvi, vari palaist ar docker-compose, izmantojot pieejamos `docker-compose.yaml` un `docker-compose-without-postgres.yaml` failus.
