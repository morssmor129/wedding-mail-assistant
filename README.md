# Wedding Mail Assistant by Jester Ads
Wersja 1.2.0. Narzędzie do przygotowywania po polsku ofert i follow-upów dla usługodawców ślubnych. To instrukcje i wzorce wykonywane przez agenta AI, nie samodzielna aplikacja.

## Uruchomienie
Główny wariant: ChatGPT Desktop, lokalny Work z dostępem do prywatnego folderu. Jednorazowo wybierz folder, przyznaj odczyt i zapis, a następnie uruchom konfigurację. Asystent sam obsługuje profile, bez pobierania i ponownego wgrywania ich przez klienta.

- Instrukcja dla klienta: [INSTRUKCJA-KLIENTA.md](INSTRUKCJA-KLIENTA.md).
- Punkt startowy dla asystenta: [START.md](START.md).
- Zasady: [SKILL.md](SKILL.md).

Polecenie do wklejenia w lokalnym Work z otwartym folderem:

> Przeczytaj START.md z repozytorium https://github.com/morssmor129/wedding-mail-assistant i uruchom Wedding Mail Assistant w otwartym folderze. Sprawdź odczyt i zapis. Pobierz komplet narzędzia do podfolderu narzedzie. Przeprowadź onboarding, a po mojej akceptacji sam zapisz profile i sprawdź je przez odczyt. Nie nadpisuj moich danych i nie publikuj ich. Przy braku dostępu nie ogłaszaj instalacji.

Repozytorium musi być dostępne dla odbiorcy. Sam link do repozytorium prywatnego nie nadaje uprawnień. Nie proś o hasła ani tokeny w czacie.

## Działanie
Publiczna lub udostępniona kopia narzędzia trafia do podfolderu narzedzie. Prywatne dane pozostają obok, w profil/company-profile.md i profil/user-style.md. Zatwierdzone stałe zmiany mają aktualizować pliki z zachowaniem kopii poprzedniej rewizji oraz odczytem kontrolnym. Nowa rozmowa musi mieć dostęp do tego samego folderu.

W nowej rozmowie wpisz: "Przeczytaj START.md z tego folderu. Piszemy nowego maila". Po pierwszej konfiguracji nie powtarzaj wywiadu; potwierdzaj wycenę i zakres konkretnej oferty.

Master Brain i zatwierdzony Master Sample v3.0 pozostają bez zmian. Styl użytkownika jest od nich oddzielony. Maile są bez Markdowna i długich myślników. PDF i projekt umowy to tylko planowane załączniki do wzmianki; narzędzie ich nie czyta ani nie tworzy. Nie wysyła maili i nie rezerwuje terminów.

## Granice
Dostęp do lokalnego Work zależy od aplikacji, planu i uprawnień. Sandbox i zwykły czat nie są trwałym folderem klienta. Nie obiecujemy instalacji bez zgód, nieograniczonego użycia ani działania offline. AGENTS.md nie jest gwarancją automatycznego wczytania we wszystkich aplikacjach.

Sprawdź [QA-REPORT.md](QA-REPORT.md). Walidacja plików nie zastępuje testu na komputerze klienta. Nie publikuj profili, Fathoma ani maili. .gitignore ogranicza przypadkowe dodanie danych, nie zastępuje kontroli przed publikacją.

Wariant Projects 1.1 jest zachowany w archiwum ZIP jako alternatywa wymagająca ręcznego zapisu źródeł. Nie jest główną ścieżką instalacji desktopowej. Pochodzenie: [references/sources.md](references/sources.md). marketingskills jest inspiracją, nie dołączoną zależnością. Nie dodano telemetrii, serwera profili ani nowej licencji bez decyzji autora.
