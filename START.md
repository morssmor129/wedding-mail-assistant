# Wedding Mail Assistant by Jester Ads - START
Wersja: 1.5.0. Instrukcja dla asystenta.
Repozytorium: https://github.com/morssmor129/wedding-mail-assistant

## Przygotowanie przestrzeni
Użyj folderu wskazanego przez klienta w agencie z rzeczywistym odczytem i zapisem. Nie zastępuj go sandboxem. Respektuj wymagane zgody. Sprawdź odczyt i zapis własnym plikiem testowym, a potem usuń tylko ten plik.

## Instalacja
Umieść narzędzie w ROOT/narzedzie, chyba że istnieje kompletna kopia. Przeczytaj SKILL.md, Master Brain, Master Sample, onboarding, moduły usług, analizę materiałów, profile, zapis, ofertę, styl, podpis, demo i kontrolę jakości. Nie wykonuj push ani nie zmieniaj widoczności repozytorium.

## Konfiguracja
Najpierw odczytaj istniejące profile.

Nowy użytkownik:
1. zadaj Q01;
2. zinterpretuj wszystkie usługi i sposób ich realizacji;
3. pokaż krótką mapę usług i poproś o potwierdzenie, dopytując tylko o realne niejasności;
4. zaproponuj opcjonalny import PDF/DOCX/wklejonego maila/WWW;
5. wybierz właściwe moduły i zadaj tylko brakujące, istotne pytania;
6. zadaj pozostałe wspólne pytania Q02, Q03, Q09-Q16, o ile odpowiedzi nie są już znane.

Firma może mieć wiele aktywnych modułów. Partner tylko polecany nie wymaga pełnego modułu. Nie oznaczaj pominiętego pola jako "brak".

Istniejący użytkownik: zachowaj profile i styl. Zaproponuj mapę usług z dotychczasowych danych, potwierdź ją i dopytaj tylko o braki potrzebne do schematu 3. Nie uruchamiaj całego onboardingu ponownie.

Pokaż podsumowanie firmy, usług, języka i podpisu. Po akceptacji zapisz i odczytaj profile. Następnie automatycznie wykonaj demo-workflow z właściwym scenariuszem branżowym.

## Dalsza praca
"Piszemy nowego maila" uruchamia offer-workflow po odczycie profili. Najpierw ustal aktywną usługę lub pakiet z Fathoma/notatek. Dla firmy kompleksowej nie wrzucaj wszystkich usług do każdej wiadomości.

"Piszemy follow-up" uruchamia followup-workflow.

## Aktualizacje
Wczytaj references/updates.md oraz assets/update-task.json. Poranny harmonogram tylko sprawdza stabilne wydanie i pyta o aktualizację. Instalacja wymaga osobnej zgody. Nigdy nie modyfikuj profili firmy ani stylu podczas aktualizacji narzędzia.
