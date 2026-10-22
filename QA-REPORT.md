# QA wersji 1.2.0
Walidacja techniczna: struktura skilla, odniesienia, UTF-8, zachowanie Master Sample i Master Brain, brak wypełnionych profili oraz integralność archiwum. Uruchom tests/validate_package.py i standardowy walidator skilla.

Nie wykonano instalacji w rzeczywistym ChatGPT Desktop klienta. Nie potwierdzono działania interfejsu, lokalnych uprawnień, automatycznego odczytu AGENTS.md ani zachowania pomiędzy osobnymi sesjami.

Warunek odbioru: onboarding, zapis dwóch profili, poprawny odczyt w nowej rozmowie, stała zmiana stylu z kopią oraz odczyt wyższej rewizji w kolejnej rozmowie. Błąd zapisu musi dać komunikat o niepowodzeniu, nie "zapamiętałem". Nie zaliczaj scenariuszy opisanych w plikach jako wykonanych testów.

Wykonano 11 kontroli technicznych w tests/validate_package.py oraz walidację struktury skilla. Master Sample i Master Brain zachowują identyczne skróty SHA-256 jak w pakiecie 1.1. Nie jest to test jakości maili ani ciągłości profilu w aplikacji.
