# Trwały profil w lokalnej przestrzeni

ROOT oznacza wyłącznie prywatny folder wskazany przez klienta i dostępny do odczytu oraz zapisu. Sandbox, /mnt/data ani dostęp do GitHuba nie dowodzą dostępu do komputera klienta. Nie przeszukuj całego dysku. Jedna przestrzeń obsługuje jedną firmę.

Kopia narzędzia: zwykle ROOT/narzedzie. Dane prywatne: ROOT/profil/company-profile.md, ROOT/profil/user-style.md, ROOT/profil/profile-history.md oraz ROOT/profil/backups/. Nigdy nie publikuj tych danych. .gitignore nie jest szyfrowaniem.

## Odczyt
Odczytaj oba aktywne profile przed nową sprawą. Sprawdź profile_type, schema_version: 2, wspólny company_key, dodatni revision i approval: approved. TEMPLATE nie jest profilem. Starszy schemat migruj według company-profile.md bez ponownego całego onboardingu. Nie wybieraj kopii z backups jako aktywnej i nie łącz profili dwóch firm. Brak dostępu nie oznacza braku danych ani zgody na ich wyzerowanie.

## Zapis po akceptacji
1. Uzyskaj zatwierdzenie podsumowania. Jednoznaczna akceptacja jest zgodą na zapis, nie proś o ponowne kliknięcie ani komendę.
2. Przygotuj kompletne profile schematu 2 według wzorów; pierwszy revision to 1, tool_version to 1.3.0. Zachowaj dane już zatwierdzone. Nie twórz nowej firmy na podstawie demo.
3. Jeżeli pliki istnieją, przejdź do aktualizacji. Nigdy nie zastępuj pełnego profilu pustym wzorem.
4. Zapisz UTF-8 w ROOT/profil, najlepiej do unikalnych plików tymczasowych. Odczytaj je, porównaj z zatwierdzoną treścią, następnie bezpiecznie zastąp docelowe pliki. Ponownie odczytaj oba pliki docelowe. Kontroluj treść, wspólny klucz, zatwierdzenie i rewizję.
5. Przy częściowym błędzie nie ogłaszaj gotowości. Nie ukrywaj błędu za pokazem maila. Powiedz np. "Nie udało się zapisać wszystkich ustawień. Sprawdź dostęp do zapisu".
6. Dopisz datę i operację do prywatnej historii, bez treści maili i danych par. Szczegóły kontroli zachowaj do diagnostyki.
7. Po udanym zapisie uruchom demo-workflow, nie instrukcję samodzielnego testu dla klienta. Nie wyświetlaj ścieżek, rewizji ani kart plików.

## Aktualizacja i konflikt
Odczytaj cały profil, zachowaj company_key i niezmienione pola. "Od teraz zawsze" to stała zmiana; "w tym mailu" jest lokalna. Przed zapisem ponownie sprawdź skrót lub rewizję. Przy zmianie z innej sesji uzgodnij konflikt zamiast nadpisywać. Zapisz poprzednie bajty w nowej kopii backups, zwiększ revision, uzupełnij change_note i datę, zapisz cały plik oraz odczytaj go kontrolnie. Przywracaj kopie tylko na polecenie. Nie aktualizuj Core ani innych firm.

## Komunikacja
Zwykły wynik: "Ustawienia zapisane" lub po pierwszym zapisie komunikat i przykład z demo-workflow. "Sprawdź konfigurację" oznacza rzeczywisty odczyt i krótkie potwierdzenie nazwy firmy oraz gotowości, bez technikaliów. Nazwy plików, lokalizacje i rewizje pokazuj tylko po wyraźnej prośbie o diagnostykę. Nie wymagaj nowej rozmowy od klienta jako kroku zakończenia onboardingu. Sprawdzenie dostępu w kolejnej sesji wykonuje asystent przy jej rozpoczęciu; nie twierdź, że już je wykonał, jeśli sprawdził tylko bieżącą sesję.

## Prywatność
Nie zapisuj notatek Fathoma, danych par, ustaleń pojedynczej oferty ani demo do profili. Eksportuj lub zapisuj maile i notatki osobno tylko na polecenie. Nie wysyłaj maili, nie twórz spotkań i nie rezerwuj terminów. Lokalny zapis nie jest obietnicą działania AI offline.
