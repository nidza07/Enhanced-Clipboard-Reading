# Poboljšano čitanje privremene memorije
Ovaj dodatak poboljšava podrazumevanu komandu NVDA+C za čitanje sadržaja privremene memorije, i dodaje posebnu komandu NVDA+Y za izgovor broja znakova u privremenoj memoriji.

Sve prečice se mogu promeniti u dijalogu ulaznih komandi, u kategoriji "razno".

## Preuzimanje
Možete preuzeti [najnoviju verziju dodatka ovde](https://github.com/nidza07/Enhanced-Clipboard-Reading/releases/download/3.0/EnhancedClipboardReading-3.0.nvda-addon).

Dodatak je takođe dostupan iz NVDA prodavnice dodataka.

## Podešavanje ograničenja znakova
Po podrazumevanim podešavanjima, ako privremena memorija sadrži više od 1023 znakova, NVDA+C neće pročitati tekst i umesto toga će vam reći ovo.

Uz ovaj dodatak instaliran i omogućen, možete podesiti prilagođeno ograničenje znakova korišćenjem panela podešavanja "Poboljšano čitanje privremene memorije" u dijalogu sa NVDA podešavanjima. Dokle god ima manje teksta u privremenoj memoriji od podešenog ograničenja, NVDA+C će direktno pročitati tekst, a NVDA+C dva puta će ga sricati. Budite obazrivi: neki sintetizatori će se možda srušiti ako im se pošalje veća količina teksta, eksperimentišite i proverite koje ograničenje je bezbedno za vaš sintetizator.

## Poruke režima pretraživanja
Ako se NVDA+C pritisne tri puta, prikazaće se poruka režima pretraživanja sa sadržajem privremene memorije radi lakšeg pregleda.

Ova poruka će se uvek prikazati nakon jednog pritiskanja ako privremena memorija sadrži više teksta od podešenog ograničenja, umesto da NVDA jednostavno prijavi da privremena memorija sadrži veći deo teksta.

## Prijavljivanje broja znakova
U nekim slučajevima, možda ćete želeti da znate koliko znakova je u privremenoj memoriji. Možete koristiti komandu NVDA+Y, i broj znakova će biti izgovoren.

Broj znakova će takođe biti prikazan u naslovima poruka režima pretraživanja.

## Zahvalnost
- NV Access i NVDA zajednica: za razvoj NVDA-a, kao i šablona za dodatke.
- Claude Code: za asistenciju u programiranju.
- Prevodioci: za globalizaciju pristupačnosti dodatka svima!