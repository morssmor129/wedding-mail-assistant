# Modułowy onboarding 1.5

## Cel
Zachowaj stały szkielet danych, ale nie zadawaj pytań, które nie dotyczą usług konkretnej firmy. Źródła pytań to [onboarding-questions.json](../assets/onboarding-questions.json) oraz [service-modules.json](../assets/service-modules.json). Nie wymyślaj własnych wariantów pytań branżowych.

## 1. Najpierw Q01 i mapa usług
Zacznij od Q01. Z odpowiedzi wyodrębnij:
- nazwę firmy;
- wszystkie usługi sprzedawane klientom;
- czy usługa jest realizowana przez właściciela, zespół, podwykonawcę lub tylko polecanego partnera;
- strukturę firmy, jeśli użytkownik ją opisał.

Nie traktuj synonimów jako automatycznie osobnych usług. Przykład: "filmowiec" i "kamerzysta" mogą oznaczać jeden zakres. Z drugiej strony "fotografia i film" zwykle oznaczają dwa zakresy. Jeżeli znaczenie jest niejasne, dopytaj tylko o tę różnicę.

Przed pytaniami modułowymi pokaż krótką interpretację i poproś o potwierdzenie, np. "Rozumiem, że oferujecie fotografię i film, a oba zakresy realizuje Wasz zespół. Czy dobrze rozumiem?". Dla firmy kompleksowej wypisz wszystkie rozpoznane usługi. Nie zapisuj mapy jako zatwierdzonego faktu przed potwierdzeniem.

Po potwierdzeniu przypisz każdej rzeczywiście sprzedawanej usłudze moduł: dj, photography, video, music albo universal. Jedna firma może mieć kilka aktywnych modułów. Partner polecany, którego firma nie sprzedaje, nie uruchamia osobnego pełnego modułu.

## 2. Opcjonalne materiały przed dalszym wywiadem
Po potwierdzeniu mapy usług zaproponuj jedną opcjonalną możliwość:
"Masz już opis swojej oferty? Możesz przesłać PDF, dokument Word, wkleić wcześniejszy mail ofertowy albo podać adres strony WWW. Odczytam dostępne informacje i zapytam tylko o brakujące lub niejasne rzeczy. Możesz też kontynuować bez materiałów."

Jeżeli użytkownik dostarcza materiał, zastosuj [source-analysis.md](source-analysis.md) przed pytaniami modułowymi. Nie wymagaj materiałów. Nie ponawiaj pytań, na które wiarygodna odpowiedź została już znaleziona i potem potwierdzona.

## 3. Pytania wspólne i modułowe
Zadaj Q02, Q03, Q09-Q16 z rdzenia, o ile odpowiedzi nie są już znane i potwierdzone. Q11-Q16 pozostają wspólną konfiguracją języka i podpisu.

Dla każdej potwierdzonej usługi przejdź przez logiczne pola modułu: scope, delivery_team, extras, related_services. Pytanie modułowe zadaj tylko wtedy, gdy pole jest istotne i nadal nieustalone. Jeżeli wcześniejsza odpowiedź lub materiał jednoznacznie pokrywa pole, nie pytaj ponownie. Jeżeli pole rzeczywiście nie ma zastosowania, pomiń je zamiast zmuszać użytkownika do wpisywania "nie dotyczy".

Nie interpretuj pominiętego pytania jako "brak". Brak danych pozostaje "nieustalone", dopóki nie wynika inaczej z potwierdzonego kontekstu.

W firmie wielousługowej nie pytaj osobno o te same informacje firmowe dla każdego modułu. Możesz grupować pytania modułowe w jednej wiadomości, ale zachowaj ich dokładne brzmienie i identyfikatory. Jeżeli firma ma wiele usług, uporządkuj pytania nazwami usług, żeby użytkownik wiedział, czego dotyczy odpowiedź.

## 4. Granice
Nie pytaj ani nie zapisuj w konfiguracji ceny podstawowej, orientacyjnego cennika pakietów, statusu VAT, brutto/netto, kilometrówki, progów dojazdu, kosztów noclegu, nadgodzin, kwoty zadatku ani domyślnych załączników. Cena konkretnej oferty i logistyka należą do offer-workflow. Ceny dodatków lub rozszerzeń mogą trafić do katalogu po potwierdzeniu.

Nie pytaj o długość maili, formatowanie, CTA, konstrukcję sprzedażową ani inne reguły Master Brain. Preferencje języka nie zastępują metodologii.

## 5. Podsumowanie i akceptacja
Pokaż trzy sekcje: "Firma i oferta", "Twój sposób komunikacji", "Gotowy podpis". W "Firma i oferta" pokaż mapę usług firmy, sposób ich realizacji, zakresy i potwierdzone katalogi dodatków/partnerów. Nie pokazuj pól technicznych ani informacji, których użytkownik nie zatwierdził.

Poproś o akceptację. Po akceptacji zapisz profile zgodnie z persistence-workflow i sprawdź rzeczywisty odczyt. Wyraźna akceptacja jest zgodą na zapis.

## 6. Istniejący użytkownicy
Przy aktualizacji starego profilu nie uruchamiaj całego onboardingu od początku. Odczytaj dotychczasowe dane i styl, zaproponuj mapę usług na podstawie posiadanych informacji, poproś o jej potwierdzenie i dopytaj tylko o istotne braki potrzebne do nowej struktury. Nigdy nie zeruj user-style.

## 7. Zakończenie
Po udanym zapisie i odczycie automatycznie uruchom [demo-workflow.md](demo-workflow.md) z demo odpowiadającym głównej usłudze lub potwierdzonej ofercie łączonej. Nie każ użytkownikowi samodzielnie testować narzędzia i nie pokazuj ścieżek ani rewizji.
