# Wybór sposobu zapisu
Domyślnie używaj autoryzowanej trwałej przestrzeni i [local-workspace.md](local-workspace.md). Stany wewnętrzne: ROBOCZY -> ZATWIERDZONY -> ZAPISANY -> ODCZYT ZWERYFIKOWANY -> DEMO. Przejścia wynikają z rzeczywistych operacji, nie deklaracji w tekście.

Po pierwszym odczycie zweryfikowanym wykonaj [demo-workflow.md](demo-workflow.md). Nie proś klienta o samodzielne testy, nie pokazuj ścieżek ani rewizji. Nie przechodź do stanu gotowości przy błędzie zapisu.

Tylko na wyraźną prośbę wybierz wariant [project-persistence.md](project-persistence.md). Tam nadal wymagane jest faktyczne utrwalenie źródła, nie samo wygenerowanie pliku. Nie przełączaj trybów po cichu. Dostęp do repozytorium nie daje dostępu do dysku klienta.
