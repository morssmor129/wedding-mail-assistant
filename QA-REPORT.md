# Kontrola wersji 1.3.0
Data przygotowania: 2026-10-22.

## Wykonano
- Potwierdzono zgodność 26 plików wejściowych z blobami commita 8c1fd832a0a62cb8d76a751798f172bc4b8ae122 przed edycją.
- Uruchomiono 25 testów regresji (unittest): struktura, wersja, UTF-8, odnośniki, zamrożony formularz, stałe opcje, wykluczone pola, oddzielenie profili, podpis, reguły migracji i izolacja demo.
- Uruchomiono renderer w osobnym procesie i porównano dokładne pytania z plikiem kanonicznym.
- Sprawdzono rachunek demo: 6500 + 500 + 600 + 300 = 7900; nieznany koszt noclegu nie jest wliczony.
- Zweryfikowano przykładową wiadomość (fikcyjna fixture) oraz przypadki błędnej sumy, CTA, noclegu i niedozwolonego formatowania.
- Zachowano Master Sample v3.0 bajt w bajt. Hash Master Brain zmieniono jawnie po zatwierdzonych poprawkach granic produktu; nie udawano, że Core jest identyczny z 1.2.

## Zakres i ograniczenia
To testy artefaktów, deterministycznych helperów i jednego przykładu, nie pełny test zachowania agenta. Nie wykonano instalacji na komputerze klienta, testu zapisu jego profili ani testu nowej sesji aplikacji desktopowej. Automatyczny pokaz w instrukcjach ma sprawdzać zapis i generację w sesji po konfiguracji, nie udawać testu między sesjami.

Scenariusze integracyjne są w tests/behavior-scenarios.md. Nie przekazuj ich jako zadania klientowi po akceptacji onboardingu. Wydanie nie aktualizuje samoczynnie wcześniej pobranych kopii narzędzia.
