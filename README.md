# Wedding Mail Assistant by Jester Ads
Wersja 1.2.0. Oferty i follow-upy po polsku dla DJ-ów, fotografów, filmowców i innych usługodawców ślubnych.

## Dla klienta
Główny wariant: ChatGPT Desktop, lokalny Work z dostępem do wydzielonego folderu. Jednorazowo wybierz folder, nadaj odczyt i zapis, przejdź onboarding. Asystent zapisuje firmę i styl, a przy nowych sprawach odczytuje profile z dysku. Nie wymaga pobierania i ponownego przesyłania profili.

Pełna instrukcja: [INSTRUKCJA-KLIENTA.md](INSTRUKCJA-KLIENTA.md).
Instrukcja dla asystenta: [START.md](START.md).

Wklej w lokalnym Work z otwartym swoim folderem:

> Przeczytaj START.md z repozytorium https://github.com/morssmor129/wedding-mail-assistant i uruchom Wedding Mail Assistant w otwartym folderze. Sprawdź dostęp do odczytu i zapisu. Pobierz narzędzie do podfolderu narzedzie, przeprowadź onboarding, a po mojej akceptacji sam zapisz i ponownie odczytaj profile. Nie publikuj moich danych. Nie ogłaszaj instalacji bez sprawdzenia plików.

Repozytorium musi być dostępne dla odbiorcy. Link do prywatnego repozytorium nie nadaje dostępu. Nie proś klientów o przesyłanie haseł lub tokenów w czacie.

## Działanie
- profil/company-profile.md: zatwierdzone dane firmy i oferty.
- profil/user-style.md: indywidualne reguły pisania.
- profil/backups i profile-history.md: kopie oraz historia zmian.

Profile są w folderze klienta, zwykle poza podfolderem narzedzie z kopią repozytorium. Nie ma wspólnej bazy danych u Jester Ads. W nowej rozmowie z tym samym folderem wpisz: "Przeczytaj START.md. Piszemy nowego maila".

Master Brain i Master Sample v3.0 pozostają wzorcem. Styl klienta nie może znosić uczciwości, potwierdzania wyceny, CTA i czystego formatu. Nie jest to jednak kryptograficzna ochrona przed edycją plików.

Cena konkretnego wesela, zakres, dodatki, dojazd i załączniki są potwierdzane osobno. PDF i projekt umowy są tylko wzmianką w mailu. Narzędzie nie wysyła wiadomości, nie rezerwuje terminów i nie analizuje umów. Finalny mail jest bez Markdowna i długich myślników.

## Wymagania i ograniczenia
Dostęp do lokalnego Work zależy od konta, aplikacji i uprawnień. Sam płatny abonament nie zastępuje dostępu do plików. Zwykły czat oraz pliki w sandboxie nie są trwałym folderem klienta. Nowa sesja musi mieć dostęp do tej samej przestrzeni i odczytać instrukcje. AGENTS.md jest pomocą, nie gwarancją automatycznego wczytania we wszystkich aplikacjach.

Nie obiecujemy instalacji bez zgód, działania offline ani nieograniczonego użycia. Lokalny zapis nie wyklucza przetwarzania kontekstu w chmurze dostawcy. Brak testu na konkretnym desktopie klienta; wykonaj test z instrukcji.

## Dla autora
Zachowano metodologię i sample. Aktualizacja dotyczy sposobu zapisu oraz uruchamiania. Wersja Projects pozostaje alternatywą w pakiecie, nie główną ścieżką klienta desktopowego.

Pochodzenie: [references/sources.md](references/sources.md). marketingskills to inspiracja, nie zainstalowana zależność. Nie dołączono wypełnionych profili, transkrypcji ani kluczy API. Nie wprowadzono dodatkowej licencji dystrybucyjnej bez decyzji autora.
