# Kontrakt danych firmy i stylu

## Dwa osobne pliki wynikowe
W desktopie zapisuj `profil/company-profile.md` i `profil/user-style.md`. W wariancie Projects eksportuj `company-profile.txt` i `user-style.txt`. Schemat jest wspólny; nie utrzymuj dwóch aktywnych formatów. Schemat i pola znajdziesz w dołączonych wzorach `assets/company-profile.template.txt` oraz `assets/user-style.template.txt` (w wariancie Projects wzory są częścią bazy).

Nagłówek każdego profilu ma zawierać:
- `profile_type`: company lub style;
- `schema_version`: 1;
- `tool_version`: 1.2.0;
- `company_key`: wspólny identyfikator firmy, np. slug nazwy, zatwierdzony przez użytkownika;
- `revision`: dodatni numer całkowity, początkowo 1;
- `approval`: approved tylko po zatwierdzeniu, wcześniej draft;
- `updated_at`: rzeczywista znana data YYYY-MM-DD albo nieustalona;
- `change_note`: krótki opis ostatniej zmiany.

Nie dodawaj pola twierdzącego, że plik jest zapisany w projekcie. Zapis weryfikuj przez odczyt z autoryzowanego folderu albo źródła projektu zgodnie z persistence-workflow.

## COMPANY: trwałe fakty o usługodawcy
Zapisz nazwę marki, branżę, nadawcę, linki podane przez użytkownika, zakres i pakiety, typowy skład, dodatki, zasady dojazdu/noclegu, orientacyjny cennik, sposób prezentacji kwot, proces rezerwacji, potwierdzone wyróżniki, podpis/stopkę i zwyczaj dołączania dokumentów.

Gdy pole nie ma zastosowania, wpisz "nie dotyczy"; gdy użytkownik go nie podał, wpisz "nieustalone". Brak linku lub cennika orientacyjnego nie blokuje onboardingu. Nie zakładaj duetu, kraju działania ani marki Jester Events u nowego użytkownika.

Cena konkretnego wydarzenia, wybór pakietu, aktualna dostępność, rabaty i daty kontaktu nie należą do stałego profilu. Wycena orientacyjna nie zastępuje potwierdzenia ceny końcowej.

## STYLE: zatwierdzone preferencje językowe
Zapisz formalność, energię, powitanie, formę "ja/my", zwroty do pary, rytm zdań, słownictwo preferowane i unikane, humor, zgodę na emoji, preferowane zakończenie, cel długości w ustalonym standardzie i abstrakcyjne obserwacje ze wzorców.

Nie kopiuj całych maili ani danych par. Nie traktuj pochwały "super" jako polecenia trwałej zmiany stylu. Nie zapisuj preferencji sprzecznych z prawdziwością, potwierdzaniem ceny, CTA i czystym formatem.

## Komendy
- "Pokaż mój profil": przedstaw aktualnie odczytane dane i luki.
- "Zmień konfigurację": odczytaj profil, ustal tylko zmieniane pola, zatwierdź i zapisz nową rewizję według persistence-workflow.
- "Przygotuj profil do eksportu": eksportuj oba kompletne zatwierdzone profile, bez pytań o znane dane.
- "Sprawdź konfigurację": zweryfikuj odczyt z dysku albo źródła projektu, nie z samej historii.
