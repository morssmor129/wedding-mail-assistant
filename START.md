# Wedding Mail Assistant by Jester Ads - START
Wersja: 1.2.0. Instrukcja dla asystenta, nie skrypt powłoki.
Repozytorium: https://github.com/morssmor129/wedding-mail-assistant

## Warunki uruchomienia
Uruchom narzędzie w lokalnym Work w aplikacji ChatGPT Desktop. Użytkownik raz wskazuje prywatny folder i udziela wymaganych uprawnień. Po tym asystent sam odczytuje i zapisuje profile. Nie obiecuj zerowej liczby zgód ani nie wyłączaj zabezpieczeń.

1. Ustal pełną ścieżkę wybranego folderu ROOT. Nie przeszukuj całego komputera.
2. Sprawdź rzeczywisty odczyt i zapis w ROOT: utwórz plik testowy o unikalnej nazwie, odczytaj jego treść, następnie usuń tylko własny plik testowy. Nie nadpisuj istniejących danych.
3. Sandbox i /mnt/data nie dowodzą dostępu do dysku klienta. Bez odpowiednich narzędzi zatrzymaj instalację i wskaż konieczność otwarcia folderu w lokalnym Work.
4. Sprawdź pełny odczyt repozytorium. Błąd 404 lub brak uprawnień zgłoś wprost. Nie proś o hasło ani token w czacie.

## Instalacja
Dla nowej przestrzeni umieść kompletną kopię narzędzia w ROOT/narzedzie. Użyj dostępnego pobierania lub git; nie wymagaj terminala od klienta. Nie uruchamiaj nieprzeczytanych skryptów internetowych. Nie wykonuj push ani nie zmieniaj widoczności repozytorium.

Jeżeli komplet narzędzia jest już lokalnie, odczytaj VERSION i nie instaluj drugiej kopii. Jeżeli ROOT jest bezpośrednio katalogiem narzędzia, użyj go bez zagnieżdżania; przestrzegaj .gitignore dla danych prywatnych.

Przeczytaj SKILL.md i moduły wskazane dla konfiguracji, profili, zapisu, metodologii, Master Sample, ofert, follow-upów, stylu i kontroli. Zanotuj rzeczywistą wersję, a SHA tylko gdy jest znane. Brak pełnej instrukcji oznacza instalację niekompletną.

W wariancie ROOT/narzedzie przygotuj w ROOT plik START.md z oznaczeniem "installation_mode: ready" i faktycznymi ścieżkami do narzedzie/SKILL.md, profil/company-profile.md i profil/user-style.md. Zapisz w nim: "Przy nowej sprawie odczytaj instrukcje i profile; nie instaluj narzędzia ponownie". Nie nadpisuj obcego START.md bez uzgodnienia.

Utwórz albo bezpiecznie uzupełnij ROOT/AGENTS.md o wskazanie tego START.md; zachowaj cudze instrukcje. Odczyt AGENTS.md zależy od aplikacji. Dlatego komenda w nowej rozmowie ma jawnie nakazywać odczyt START.md. Samo umieszczenie pliku na dysku nie gwarantuje jego automatycznego wczytania.

## Konfiguracja
Najpierw sprawdź profile. Jeżeli oba są zatwierdzone i kompletne, nie powtarzaj wywiadu. W przeciwnym razie wykonaj references/onboarding.md. Po akceptacji danych zapisz profile według references/local-workspace.md i wykonaj odczyt kontrolny. Nie kończ na "zapamiętałem".

Podaj rzeczywistą ścieżkę, nazwę firmy, wersję narzędzia i rewizje zapisanych profili. Jeżeli zapis jest częściowy, wyraźnie to powiedz. Nie każ pobierać i ponownie dodawać profili.

## Test i codzienna praca
Poproś o nową rozmowę Work z tym samym folderem i komendę: "Przeczytaj START.md z tego folderu. Sprawdź konfigurację Wedding Mail Assistant, odczytując oba profile z dysku". Nie deklaruj wykonania testu nowej sesji bez rzeczywistego testu.

Nowa oferta: "Przeczytaj START.md z tego folderu. Piszemy nowego maila". W już skonfigurowanej rozmowie wystarcza krótsze polecenie. Zawsze odczytaj aktualne profile przed nową sprawą.

## Aktualizacja narzędzia
Aktualizuj tylko ROOT/narzedzie. Sprawdź wersję, zmiany i zgodność schematu. Nie nadpisuj ROOT/profil, kopii ani plików klienta. Zachowaj poprzedni stan instrukcji przed aktualizacją. Brak dostępu do GitHuba nie blokuje pracy z kompletną lokalną kopią; model AI nadal może wymagać połączenia z dostawcą.
