# Automatyczny pokaz po konfiguracji

## Warunek
Uruchom po pierwszym zatwierdzeniu, skutecznym zapisie i ponownym odczycie profili. Nie uruchamiaj przy każdym prawdziwym mailu ani przy zwykłej zmianie stylu. Na prośbę "Pokaż przykładowy mail" możesz go powtórzyć.

## Wybór scenariusza
Odczytaj [demo-scenarios.json](../assets/demo-scenarios.json). Wybierz demo według zatwierdzonej mapy usług:
- wyłącznie lub głównie DJ / prowadzenie -> dj;
- fotografia -> photography;
- film / video -> video;
- muzyk / zespół -> music;
- firma sprzedaje co najmniej dwie wyraźnie różne główne usługi, np. DJ + foto/video -> combined;
- inna usługa -> universal.

Jeżeli firma ma wiele usług, ale użytkownik wskazał jedną główną specjalizację, możesz użyć jej scenariusza zamiast combined. Nie używaj DJ demo u fotografa ani fotograficznego u muzyka.

Scenariusze są fikcyjne i zatwierdzone wyłącznie do demonstracji. Nie pytaj klienta o ich ceny i nie zapisuj ich do profilu.

## Generacja
Przejdź przez rzeczywisty workflow oferty w trybie is_demo=true: odczytaj styl, wyodrębnij potrzeby, sprawdź zakres, policz sumę, napisz nowy mail, dodaj podpis i wykonaj quality-check. Nie kopiuj gotowego tekstu; demo ma pokazać styl konkretnego użytkownika.

Każdy scenariusz zawiera service_lines, travel, lodging, attachments, total_payable i CTA. Dodaj tylko pozycje wpisane w scenariuszu. Nocleg z ceną null nie wchodzi do sumy. Nie wymyślaj liczby osób w zespole, jeżeli scenariusz ani profil jej nie potwierdzają.

## Wynik
Powiedz: "Konfiguracja gotowa. Tak będzie wyglądał przykładowy mail. To fikcyjna oferta pokazująca sposób działania narzędzia."
Następnie pokaż temat i treść maila. Nie pokazuj surowych danych scenariusza, ścieżek, rewizji, liczników słów ani raportu kontroli.

Po mailu możesz dodać jedno zdanie: "Teraz wpisz: Piszemy nowego maila, i wklej notatki ze swojej rozmowy".

## Izolacja
Nigdy nie zapisuj danych demo, cen, CTA, noclegu, dodatków ani fikcyjnej pary do profili. Zatwierdzenie przykładu nie zmienia profilu. Przed prawdziwą sprawą odczytaj realny profil i usuń demonstrację z aktywnych ustaleń.

Sprawdzenie w bieżącej sesji nie jest testem nowego komputera ani nowej sesji. Nie wysyłaj maila, nie twórz spotkania i nie blokuj terminu.
