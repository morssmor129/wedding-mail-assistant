# Profile firmy i języka, schemat 2

W desktopie utrzymuj dwa prywatne pliki: profil/company-profile.md i profil/user-style.md. W wyraźnie wybranym trybie Projects analogiczne źródła TXT. Nie umieszczaj w nich instrukcji Master Brain. Szablony: [firma](../assets/company-profile.template.txt), [styl](../assets/user-style.template.txt).

Nagłówek techniczny: profile_type, schema_version: 2, tool_version: 1.4.0, wspólny company_key, revision (od 1), approval: approved dopiero po zgodzie, rzeczywista znana data updated_at oraz change_note. Wyznacz company_key z nazwy, bez osobnego pytania do klienta. Nazwy plików, wersje i pola nagłówka nie należą do zwykłego podsumowania.

## Firma
Zapisuj wyłącznie fakty z Q01-Q10 i imię oraz nazwisko z Q15. Ceny wolno utrwalać tylko w katalogach atrakcji, muzyków i partnerów (Q06-Q08), jako stałe lub ustalane indywidualnie. Katalog nie zastępuje potwierdzenia kwot dla konkretnej pary ani nie potwierdza dostępności współpracownika. Oferta podstawowa opisuje zakres, nie cennik.

Nie zapisuj ceny podstawowej, statusu podatkowego, brutto/netto, kilometrówki, progów logistycznych, kosztów noclegu, nadgodzin, kwoty zadatku ani załączników do konkretnego maila. Lokalizacja bazy i obszar pracy są danymi firmy, koszty dojazdu są danymi konkretnej oferty.

## Styl
Zapisuj Q11-Q14 i zwrot kończący Q16. Dopuszczaj zatwierdzone później preferencje języka, ale nie reguły długości, CTA, formatowania lub metodologii. Nie przenoś całych przykładowych maili ani danych par. Podpis składaj z profili według [signature.md](signature.md).

## Podsumowanie
Pokazuj trzy sekcje: "Firma i oferta", "Twój sposób komunikacji", "Gotowy podpis". Bez VAT, cen pakietów, parametrów Master Brain, ścieżek, rewizji i statusów technicznych. "Pokaż mój profil" ma taki sam format. Szczegóły techniczne udostępnij tylko na wyraźną prośbę.

## Migracja istniejącego profilu
Nie uruchamiaj automatycznie wszystkich 16 pytań ponownie. Odczytaj pełne stare profile, zachowaj ich kopie i wykorzystaj zatwierdzone odpowiedzi. W nowym aktywnym schemacie pomiń niedozwolone pola z dawnego onboardingu; nie kasuj kopii historycznych. Nie przenoś ceny podstawowej do katalogu dodatków. Podziel dawne "dodatki i współpracownicy" na Q06-Q08 tylko gdy fakty są jednoznaczne. Uzupełnij wyłącznie istotne braki, np. nazwisko lub link do podpisu, zgodnie z pytaniem kanonicznym. Pokaż klientowi oczyszczone podsumowanie do zatwierdzenia, bez wyliczania usuwanych reguł technicznych. Zachowaj company_key, zwiększ revision i po zgodzie zapisz z odczytem kontrolnym. Aktualizacja narzędzia nie może po cichu wyzerować ani nadpisać profili.
