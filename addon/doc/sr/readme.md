# Poboljšano čitanje privremene memorije
Ovaj dodatak poboljšava podrazumevanu komandu NVDA+C za čitanje sadržaja privremene memorije.

## Podešavanje ograničenja znakova
Po podrazumevanim podešavanjima, ako privremena memorija sadrži više od 1023 znakova, NVDA+C neće pročitati tekst i umesto toga će vam reći ovo.

Uz ovaj dodatak instaliran i omogućen, možete podesiti prilagođeno ograničenje znakova korišćenjem panela podešavanja "Poboljšano čitanje privremene memorije" u dijalogu sa NVDA podešavanjima. Dokle god ima manje teksta u privremenoj memoriji od podešenog ograničenja, NVDA+C će direktno pročitati tekst, a NVDA+C dva puta će ga sricati. Budite obazrivi: neki sintetizatori će se možda srušiti ako im se pošalje veća količina teksta, eksperimentišite i proverite koje ograničenje je bezbedno za vaš sintetizator.

## Poruke režima pretraživanja
Ako se NVDA+C pritisne tri puta, prikazaće se poruka režima pretraživanja sa sadržajem privremene memorije radi lakšeg pregleda.

Ova poruka će se uvek prikazati nakon jednog pritiskanja ako privremena memorija sadrži više teksta od podešenog ograničenja, umesto da NVDA jednostavno prijavi da privremena memorija sadrži veći deo teksta.

## Zahvalnost
- NV Access i NVDA zajednica: za razvoj NVDA-a, kao i šablona za dodatke.
- Claude Code: za asistenciju u programiranju.
- Prevodioci: za globalizaciju pristupačnosti dodatka svima!