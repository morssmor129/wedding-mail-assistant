# Automatyczny pokaz po konfiguracji

## Warunek
Uruchom po pierwszym zatwierdzeniu, skutecznym zapisie i ponownym odczycie obu profili, a po migracji tylko jeżeli pokaz nie odbył się w tej konfiguracji. Nie uruchamiaj go przy każdym prawdziwym mailu ani przy zwykłej zmianie stylu. Na prośbę "Pokaż przykładowy mail" możesz go powtórzyć.

## Stały scenariusz
Odczytaj [demo-offer.json](../assets/demo-offer.json). To fikcyjne notatki Fathom i zatwierdzona przez autora narzędzia wycena WYŁĄCZNIE DLA DEMO. Nie otwieraj nagrania, nie pytaj klienta o ceny i nie wymagaj dodatkowej akceptacji. Nigdy nie uznawaj tego mechanizmu za zgodę na pomijanie potwierdzeń w prawdziwej ofercie.

Przejdź rzeczywisty workflow oferty: odczytaj profile, wyodrębnij potrzeby, sprawdź zakres, oblicz sumę, napisz nowy mail w zatwierdzonym stylu, dodaj podpis i wykonaj quality-check. Nie oddawaj niezmiennego tekstu z fixture jako rzekomo spersonalizowanego wyniku.

Zachowaj kwoty: pakiet DJ i konferansjer 6500 zł, dojazd 500 zł, wybrane dodatki ciężki dym 600 zł i fontanny iskier 300 zł. Razem 7900 zł. Nocleg na dwie doby zapewnia klient; jego nieznanego kosztu nie wyceniaj, nie dodawaj do sumy i nie przedstawiaj jako wliczonego. Dodatki są wybrane, a nie opcjonalne. Brak planowanych załączników w scenariuszu: nie dopisuj PDF-u ani umowy. CTA: rozmowa jutro o 18:00 w celu potwierdzenia decyzji, plus zaproszenie do pytań. To fikcyjne ustalenie w treści, nie zadanie w kalendarzu.

Wybrany pakiet "DJ i konferansjer" nie potwierdza sam w sobie duetu. Jeżeli aktualny profil DJ-a potwierdza duet, możesz wykorzystać jego korzyść. Nie obiecuj dwóch osób tylko na podstawie nazwy pakietu. Nie deklaruj zablokowania terminu, skoro data wesela nie jest ustalona.

## Inne branże
Scenariusz DJ jest stały. Nie dopisuj go do oferty fotografa, muzyka ani innej firmy. Dla profilu niezwiązanego z DJ użyj fikcyjnego nadawcy "Marek Nowak", marki "Przykładowa firma DJ" i pomiń nieistniejący link; zachowaj wybrany ton, powitanie i zakończenie. Przed mailem dopisz: "Przykład dotyczy fikcyjnej usługi DJ i konferansjera, nie oferty Twojej firmy". W prawdziwych mailach korzystaj wyłącznie z rzeczywistej branży i oferty.

## Wynik widoczny dla użytkownika
Powiedz: "Konfiguracja gotowa. Tak będzie wyglądał przykładowy mail. To fikcyjna oferta pokazująca sposób działania narzędzia".
Następnie pokaż sam temat i treść maila w osobnym bloku do kopiowania. Nie pokazuj surowych notatek testowych, ścieżek, rewizji, liczników słów ani raportu kontroli. Po mailu możesz dodać jedno zdanie: "Teraz wpisz: Piszemy nowego maila, i wklej notatki ze swojej rozmowy". Nie nazywaj tego obowiązkiem wykonania testu.

## Izolacja i rzetelność
Przechowuj demo wyłącznie jako sprawę tymczasową z is_demo=true. Nigdy nie zapisuj jego pary, cen, noclegu, CTA, składu ani dodatków do company-profile lub user-style. Nie aktualizuj katalogu klienta cenami demo nawet przy konflikcie (np. fontanny 250 zł w katalogu). Zatwierdzenie przykładu nie zmienia profilu. Przed kolejną prawdziwą sprawą usuń demonstrację z aktywnych ustaleń i odczytaj realny profil.

Sprawdzenie zapisu i generacji wykonujesz w bieżącej sesji. Nie twierdź, że przetestowano nową sesję lub komputer klienta. Nie wysyłaj maila, nie zapisuj spotkania i nie blokuj terminu. Pomocniczy scripts/check_demo.py sprawdza rachunek i format; nie zastępuje oceny sensu tekstu.
