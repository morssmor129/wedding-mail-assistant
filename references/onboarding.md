# Stały onboarding 1.3

## Jedno źródło pytań
Odczytaj [onboarding-questions.json](../assets/onboarding-questions.json). Zadaj dokładnie pytania Q01-Q16 w zapisanej kolejności i brzmieniu. Nie parafrazuj, nie łącz, nie zastępuj improwizowanym wywiadem. Formularz jest taki sam dla każdej branży. Odpowiedzi "brak", "nie dotyczy" i "indywidualnie" są dopuszczalne.

Wyświetlaj po jednej sekcji A, B, C, D. Zachowaj numery 1-16. Dla wyboru jednej odpowiedzi zachowaj opcje A-E z pliku. Używaj prawdziwych kontrolek tylko gdy narzędzie je udostępnia; w przeciwnym razie pokaż opcje tekstowe i przyjmij literę lub nazwę. Nie udawaj przycisków. Możesz uruchomić scripts/onboarding_form.py, aby otrzymać dokładną treść.

Przed konfiguracją odczytaj istniejące profile. Przy kontynuacji wypełnij pola odpowiedziami już udzielonymi, bez ponownego pytania. Nie importuj niezatwierdzonych danych z innych firm i rozmów. W ramach bieżącego formularza możesz pokazać znane odpowiedzi jako uzupełnione. Nie żądaj ponownego zatwierdzania pojedynczych odpowiedzi przed podsumowaniem.

## Granice i dopytania
Dopytuj wyłącznie o brak istotny dla zadanego pola, np. nazwisko nadawcy, wybrany link lub to, czy cena dodatku jest stała. Nie twórz nowych bloków pytań. Przy niejednoznacznym wyborze poproś o wskazanie istniejącej opcji; przy Q16 E ustal sam zwrot. Nie wymagaj linku, gdy użytkownik go nie ma.

Nie pytaj ani nie zapisuj w konfiguracji ceny podstawowej, orientacyjnego cennika pakietów, statusu VAT, brutto/netto, kilometrówki, progów dojazdu, kosztów noclegu, nadgodzin, kwoty zadatku ani domyślnych załączników. Cena konkretnej oferty i logistyka należą do offer-workflow. Wyjątek: katalog cen dodatków, muzyków i partnerów z Q06-Q08. Katalog nie jest potwierdzeniem zamówienia ani dostępności partnera.

Nie pytaj o długość maili, formatowanie, CTA, konstrukcję sprzedażową ani inne reguły Master Brain. Nie proponuj ich zmiany i nie umieszczaj ich w profilu stylu ani w podsumowaniu. Preferencje języka nie zastępują metodologii.

## Podsumowanie i akceptacja
Pokaż tylko trzy sekcje: "Firma i oferta", "Twój sposób komunikacji", "Gotowy podpis". Podsumuj wyłącznie dane użytkownika. Podpis złóż według references/signature.md. Nie pytaj, czy w ogóle go dodać, ani co ma zawierać stopka.

Poproś o akceptację danych. Po akceptacji zapisz oba profile zgodnie z persistence-workflow i sprawdź rzeczywisty odczyt. Wyraźne zatwierdzenie jest zgodą na zapis, nie pytaj o to ponownie.

## Zakończenie
Po udanym zapisie i odczycie AUTOMATYCZNIE wykonaj [demo-workflow.md](demo-workflow.md). Nie proś o nowy czat, test użytkownika, wklejenie Fathoma ani o potwierdzenie cen przykładu. Nie pokazuj ścieżek, rewizji, nazw plików lub kart plików. Szczegóły techniczne podawaj tylko na wyraźne pytanie diagnostyczne.

Jeżeli zapis się nie udał, powiedz o tym prostym językiem. Nie komunikuj zakończenia konfiguracji i nie udawaj pomyślnego testu. Wariant Projects nadal wymaga rzeczywistego utrwalenia źródła, nie fikcyjnego autozapisu.
