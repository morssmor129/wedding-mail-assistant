# Pochodzenie i granice
Wersja 1.3.0 aktualizuje wersję 1.2.0 na podstawie zatwierdzonych uwag autora: stały formularz, granice profili, podpis i automatyczny przykład. Master Sample v3.0 pozostaje bez zmiany bajtów. Master Brain zachowuje metodologię; zmieniono zatwierdzone granice konfiguracji i podpisu.

## Dokumentacja platformy
Odnośnik z dokumentacji pierwotnego wdrożenia 1.2.0 (nie sprawdzano ponownie interfejsu platformy w aktualizacji 1.3):
https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex
OpenAI opisuje wybór ChatGPT > Work w aplikacji desktopowej, otwieranie lokalnego folderu i zależność od uprawnień. Wiadomości oraz kontekst mogą być przechowywane w chmurze mimo pracy lokalnej.

Schemat narzedzie/profil, rewizje, kopie i odczyt kontrolny są procedurą Wedding Mail Assistant, nie wbudowaną bazą danych ChatGPT. Nie wykonano tu testu na komputerze klienta. Nie obiecuj automatycznego odczytu AGENTS.md ani bezwarunkowej instalacji natywnych Skills.

Repozytorium prywatne wymaga dostępu. Nie zmieniaj jego widoczności bez wyraźnego polecenia właściciela. Do repozytorium nie trafiają wypełnione profile i dane par.

## marketingskills
https://github.com/coreyhaines31/marketingskills
Autor: Corey Haines. Wskazane źródło inspiracji dotyczące copywritingu, korzyści i redakcji. Pakiet nie zawiera kopii pełnych modułów upstream i nie pobiera ich podczas pisania maila. Nie opisuj ich jako zainstalowanej zależności. Zasady branżowe, workflow i sample wynikają z uzgodnień Jester Ads.

## Update scheduling, verified 2026-10-23
https://developers.openai.com/codex/app/automations
Redirects to https://learn.chatgpt.com/docs/automations?surface=app .
The official guide says skills can create/update real scheduled tasks. Desktop local tasks need
an available local workspace, computer on and app running; permissions still apply.
https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt
Availability and task limits depend on the account/app. Web tasks are not proof of local-folder
access. Do not rely on project uploads in cloud tasks; use a self-contained repository watch prompt.
The morning policy, stable-release manifest, backup and confirmation rules are WMA design decisions,
not a promise of a built-in auto-update service provided by OpenAI.
