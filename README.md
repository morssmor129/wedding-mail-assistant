# Wedding Mail Assistant by Jester Ads
Wersja 1.5.0. Oferty i follow-upy po polsku dla usługodawców ślubnych.

## Co robi
Jednorazowo poznaje firmę i zapisuje jej profil oraz styl. Obsługuje DJ-ów, fotografów, filmowców, muzyków, zespoły i firmy wielousługowe. Po odpowiedzi na pierwsze pytanie rozpoznaje zakres działalności, prosi o potwierdzenie i uruchamia wyłącznie właściwe moduły pytań.

Firma może mieć kilka usług jednocześnie. Narzędzie nie sprowadza pakietu foto-video albo firmy DJ + foto + video do jednej błędnej kategorii.

## Materiały firmy
Podczas konfiguracji użytkownik może opcjonalnie przesłać PDF, DOCX, wkleić wcześniejszy mail albo podać publiczną stronę WWW. Narzędzie wykorzystuje tylko potwierdzalne informacje, pokazuje konflikty i pyta o braki. Nie analizuje automatycznie Instagrama/Facebooka jako źródła oferty.

PDF planowany jako załącznik do konkretnego maila to inny przypadek: samo jego dołączenie nie uruchamia analizy.

## Codzienna praca
Przed prawdziwą ofertą użytkownik potwierdza cenę, aktywny zakres usług, dodatki, dojazd/nocleg i załączniki. W firmie wielousługowej mail dotyczy tylko usług wybranych przez konkretną Parę, chyba że użytkownik potwierdzi pakiet łączony.

Master Brain, długość maila, język korzyści, CTA i formatowanie są zasadami produktu, nie ustawieniami do negocjowania w onboardingu.

## Dla autora
- rdzeń pytań: [assets/onboarding-questions.json](assets/onboarding-questions.json)
- moduły branżowe: [assets/service-modules.json](assets/service-modules.json)
- analiza materiałów: [references/source-analysis.md](references/source-analysis.md)
- scenariusze demo: [assets/demo-scenarios.json](assets/demo-scenarios.json)
- testy: [tests/validate_package.py](tests/validate_package.py)

GitHub jest źródłem narzędzia, nie bazą danych klientów. Nie publikuj profili, Fathoma ani prywatnych materiałów użytkowników.
