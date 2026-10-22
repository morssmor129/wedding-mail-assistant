# Wedding Mail Assistant by Jester Ads
Wersja 1.3.0. Oferty i follow-upy po polsku dla usługodawców ślubnych.

## Dla klienta
Raz konfigurujesz firmę, odpowiadając na uporządkowane pytania. Po zatwierdzeniu asystent zapisuje ustawienia, sprawdza je i od razu pokazuje fikcyjny przykładowy mail. Przy kolejnych ofertach korzysta z profilu, a Ty podajesz notatki i warunki konkretnego zlecenia. Nie zarządzasz ręcznie plikami.

[Instrukcja klienta](INSTRUKCJA-KLIENTA.md). [Uruchomienie dla asystenta](START.md).

Wymagana jest aplikacja-agenta z dostępem do odczytu i zapisu w wydzielonej przestrzeni użytkownika, np. odpowiednio skonfigurowany lokalny Work. Sam płatny plan lub zwykły czat nie daje takich uprawnień. Zachowaj wymagane zgody. Nie obiecujemy działania offline ani bez limitów.

## Zmiany 1.3
- Jeden formularz: 16 pytań, cztery stałe sekcje i niezmienne opcje. Bez pytania o cenę podstawową, VAT, kilometrówkę lub koszty noclegu.
- Osobne katalogi atrakcji, dodatkowych występów i partnerów. Tylko tam zapisujemy ceny standardowe. Realna wycena jest potwierdzana przed mailem.
- Stały podpis: zwrot, imię i nazwisko, firma, wskazany link.
- Master Brain nie jest menu ustawień klienta. Podsumowanie nie pokazuje limitów długości ani parametrów metodologii.
- Zapis i odczyt sprawdzane wewnętrznie, a zamiast komunikatów technicznych automatyczny przykład. Scenariusz demo: 6500 + 500 + 600 + 300 = 7900 zł oraz nocleg na dwie doby po stronie klienta. Dane demo nie trafiają do profili.

## Dla autora
Pytania: [assets/onboarding-questions.json](assets/onboarding-questions.json). Scenariusz: [assets/demo-offer.json](assets/demo-offer.json). Zapis: [references/local-workspace.md](references/local-workspace.md). Testy: [tests/validate_package.py](tests/validate_package.py). Historia: [CHANGELOG.md](CHANGELOG.md).

Nie zmieniono Master Sample v3.0. Zmiany Core dotyczą wyłącznie zatwierdzonych granic konfiguracji i stałego podpisu. Pliki są otwarte, a instrukcje nie stanowią ochrony kryptograficznej. Zmiana repozytorium nie aktualizuje automatycznie już pobranej kopii klienta.

GitHub jest źródłem narzędzia, nie bazą danych klientów. Nie publikuj wypełnionych profili i Fathoma. Aktualizacja ma zachować prywatne ustawienia i kopie. Repozytorium prywatne wymaga dostępu odbiorcy; sam link nie nadaje uprawnień.

Narzędzie przygotowuje tekst. Nie wysyła maili, nie rezerwuje terminów, nie tworzy spotkań i nie analizuje załączników. [Pochodzenie metodologii](references/sources.md). [Zakres weryfikacji](QA-REPORT.md).
