# Trwały profil w lokalnym folderze

## Zakres
ROOT to folder wskazany przez klienta. Nie zgaduj ścieżki Windows/macOS ani nie używaj zamiast niej folderu serwera. Kopię narzędzia trzymaj zwykle w ROOT/narzedzie, a prywatne dane obok:
- ROOT/profil/company-profile.md
- ROOT/profil/user-style.md
- ROOT/profil/profile-history.md
- ROOT/profil/backups/

Jedna przestrzeń to jedna firma. Nie przeszukuj innych folderów, nie wysyłaj profili na GitHub. Jeżeli ROOT jest katalogiem repozytorium, .gitignore ma wykluczać katalog profil. Samo .gitignore nie jest szyfrowaniem ani gwarancją prywatności.

## Odczyt przed nową sprawą
1. Odczytaj pełną zawartość obu aktywnych profili z ROOT/profil.
2. Sprawdź profile_type, schema_version, wspólny company_key, revision > 0 i approval: approved. TEMPLATE nie jest konfiguracją.
3. Nie wybieraj automatycznie kopii z backups jako aktywnej wersji. Konflikt dwóch aktywnych wersji lub firm wyjaśnij, nie łącz ich.
4. Istniejący profil oznacza brak powtórzenia onboardingu. Przy braku dostępu sprawdź folder i uprawnienia. Brak jednej części nie uzasadnia kasowania drugiej.
5. Dane już zatwierdzone w bieżącej rozmowie możesz zapisać bez ponownego wywiadu. Przy migracji .txt zachowaj treść i kopie; po zatwierdzeniu pozostaw jeden aktywny format.

## Pierwszy zapis
1. Uzyskaj zatwierdzenie podsumowania. Wyraźne polecenie zapisania konkretnych danych jest zgodą, nie pytaj ponownie.
2. Przygotuj oba kompletne profile według company-profile.md: revision: 1, approval: approved, ten sam company_key, tool_version: 1.2.0 i rzeczywista znana data.
3. Sprawdź, czy pliki nie istnieją. Jeżeli istnieją, przejdź do aktualizacji, nie nadpisuj ich pustym wzorem.
4. Zapisz UTF-8 w ROOT/profil. Gdy narzędzie pozwala, najpierw utwórz pliki tymczasowe o unikalnych nazwach, sprawdź ich treść i dopiero wtedy zastąp pliki docelowe.
5. Odczytaj zapisane pliki i porównaj je z zatwierdzoną treścią, typem, company_key i revision. Jeżeli jeden zapis się nie udał, zgłoś częściowy wynik.
6. Dopisz do profile-history.md datę, nazwy profili i rewizje. Nie dodawaj danych par ani całych rozmów.
7. Po zweryfikowanym odczycie potwierdź rzeczywiste ścieżki i rewizje. Nie każ klientowi pobierać i ponownie wgrywać profili.

## Aktualizacja stałej preferencji
1. "Od teraz zawsze" oznacza stałą zmianę, "w tym mailu" tylko lokalną. Pochwała maila nie zmienia profilu.
2. Odczytaj cały aktywny profil. Zmień tylko zatwierdzone pola; zachowaj resztę, company_key i Master Brain.
3. Przed zapisem sprawdź ponownie rewizję lub skrót aktywnego pliku. Gdy inna sesja go zmieniła, odczytaj zmiany i uzgodnij konflikt, nie nadpisuj w ciemno.
4. Zachowaj poprzednie bajty w nowej, unikalnie nazwanej kopii w backups. Nie nadpisuj starszych kopii.
5. Zwiększ revision o 1, uaktualnij change_note i datę. Zapisz cały profil, nie pojedyncze zdanie. Preferuj bezpieczne zastąpienie pliku po sprawdzeniu pliku tymczasowego.
6. Odczytaj wynik, sprawdź zgodność i dopisz historię. Nie deklaruj powodzenia przy błędzie. Niezapisana poprawka działa tylko w bieżącej rozmowie.
7. Nie zmieniaj przy tym narzędzia ani profili innych firm. Kopie przywracaj tylko na polecenie.

## Sprawdź konfigurację
Wykonaj odczyt z dysku i podaj ROOT, nazwy aktywnych plików, rewizje, nazwę firmy, branżę, skład i 2-3 reguły stylu. Nie odtwarzaj wyniku z samej pamięci rozmowy. Przy błędzie zgłoś brak weryfikacji.

## Granice
Nie zapisuj do profili danych par, Fathoma, wyceny konkretnego wydarzenia ani deklaracji jego dostępności. Maile i notatki zapisuj osobno tylko na żądanie klienta, poza katalogiem dystrybucji. Nie publikuj danych i nie wysyłaj wiadomości. Lokalny folder nie oznacza offline ani braku przetwarzania kontekstu w chmurze dostawcy.
