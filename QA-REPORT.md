# QA Report - Wedding Mail Assistant 1.5.0

Zakres testów statycznych i skryptowych:
- Master Sample v3.0 i Master Brain zachowane bez zmiany;
- rdzeń onboardingu oddzielony od modułów branżowych;
- moduły DJ, fotografia, video, muzyk/zespół i universal mają te same logiczne pola;
- fotografia nie zawiera pytań o dodatkowych muzyków, a moduł muzyczny nie zawiera pytań o albumy fotograficzne;
- firma może mieć kilka modułów jednocześnie;
- PDF/DOCX/mail/WWW mają osobną procedurę analizy, z zakazem automatycznej analizy Instagrama/Facebooka;
- konflikty źródeł wymagają potwierdzenia użytkownika;
- cena podstawowa i logistyka konkretnej Pary pozostają poza onboardingiem;
- demo ma osobne scenariusze DJ, foto, video, music, combined i universal;
- updater nadal nie modyfikuje profili klienta.

Testy nie są testem integracyjnym konkretnej wersji ChatGPT Desktop ani Claude Desktop i nie dowodzą dostępu aplikacji do lokalnego folderu lub strony WWW.
