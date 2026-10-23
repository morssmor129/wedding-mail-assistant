# Wedding Mail Assistant by Jester Ads - START
Wersja: 1.4.0. Instrukcja dla asystenta.
Repozytorium: https://github.com/morssmor129/wedding-mail-assistant

## Przygotowanie przestrzeni
Użyj folderu wskazanego przez klienta w agencie z rzeczywistym odczytem i zapisem. Nie zastępuj go sandboxem ani /mnt/data. Nie przeszukuj całego dysku. Wymagane zgody respektuj, nie obiecuj uruchomienia bez uprawnień.

Ustal ROOT wewnętrznie. Sprawdź odczyt i zapis przez unikalny plik testowy; usuń tylko własny plik po sprawdzeniu. Sprawdź dostęp do kompletnego repozytorium. Przy braku dostępu lub zapisu wyjaśnij problem prostym językiem, bez pozorowania zakończenia instalacji. Nie proś o hasło lub token w czacie.

## Instalacja
Umieść narzędzie w ROOT/narzedzie, chyba że ROOT już zawiera jego kompletną kopię. Nie instaluj duplikatu. Nie uruchamiaj nieprzeczytanych skryptów internetowych, nie wykonuj push ani zmiany widoczności repozytorium.

Przeczytaj SKILL.md, Master Brain, Master Sample oraz moduły onboardingu, profili, zapisu, ofert, stylu, podpisu, demo i kontroli. Wersję i rzeczywisty SHA zachowaj do diagnostyki, nie ogłaszaj ich klientowi przy zwykłej konfiguracji.

Jeżeli narzędzie jest w podfolderze, przygotuj w ROOT START.md wskazujący narzedzie/SKILL.md i oba prywatne profile, z oznaczeniem installation_mode: ready. Nie nadpisuj obcego pliku. Wskaż tam: "Przy nowej sprawie odczytaj instrukcje i profile. Nie instaluj ponownie. Nie pokazuj ścieżek ani rewizji. Po pierwszym zapisie uruchom demo-workflow". Bezpiecznie uzupełnij ROOT/AGENTS.md; zachowaj cudze instrukcje. Sam plik nie gwarantuje automatycznego odczytu przez każdą aplikację.

## Konfiguracja i pierwszy rezultat
Najpierw odczytaj istniejące profile. Nowy użytkownik: wykonaj wyłącznie kanoniczne Q01-Q16. Istniejący profil: wykorzystaj odpowiedzi, migruj schemat według company-profile.md i dopytaj tylko o istotne braki. Nie zeruj profili.

Pokaż podsumowanie firmy, wybranego języka i gotowego podpisu. Nie pokazuj reguł Master Brain ani technicznych parametrów. Po akceptacji zapisz i rzeczywiście odczytaj profile według local-workspace.md. Następnie automatycznie wykonaj demo-workflow.md z assets/demo-offer.json.

Nie kończ prośbą "przetestuj w nowej rozmowie". Klient otrzymuje komunikat gotowości oraz fikcyjny przykładowy mail. Nie pokazuj folderów, wersji profili, kart plików ani raportu testowego. Błędy wymagające działania klienta wyjaśnij krótko i uczciwie.

## Dalsza praca
"Piszemy nowego maila" i "Piszemy follow-up" uruchamiają odpowiednie workflow po odczycie aktualnych profili. W nowej sesji jawne polecenie odczytu START.md jest wariantem awaryjnym, gdy instrukcja nie została wczytana. Nie wymagaj nowej sesji jako testu po onboardingu. Przy każdym starcie sam sprawdzaj dostęp do zapisanych danych.

## Aktualizacje i poranny harmonogram
Wczytaj references/updates.md oraz assets/update-task.json. Po instalacji lub aktualizacji uruchom
rzeczywisty poranny harmonogram, gdy klient wyraził zgodę w poleceniu startowym; sprawdź istniejące
zadania i nie twórz duplikatów. Sam zapis pliku nie tworzy zadania. W razie braku narzędzia do
harmonogramu poinformuj o ograniczeniu, bez blokowania konfiguracji i demonstracji maila.

Harmonogram tylko sprawdza stabilne wydanie i pyta o aktualizację. Nie instaluje jej bez nowej
akceptacji konkretnej wersji. Aktualizuj tylko pliki narzędzia, z kopią poprzednich bajtów i kontrolą
odczytu. Nigdy nie modyfikuj profili ani instrukcji klienta poza katalogiem narzędzia. Ręczne zmiany
w masterze wymagają ostrzeżenia przed nadpisaniem. Migracja profili jest oddzielnym procesem,
nie częścią aktualizacji. Nie pokazuj klientowi raportów technicznych ani ścieżek.
