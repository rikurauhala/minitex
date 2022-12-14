# Raportti

Minitex-projektin parissa työskentelivät:
- Riku Rauhala
- Henri Remonen
- Isak Pulkki
- Samppa Salo
- Ilari Haho

## Sprinttien ongelmat

### Sprintti 0

Ensimmäisen eli 0-sprintin suunnittelun jälkeen istuimme heti alas ja organisoiduimme, jaoimme taskeja ja aloimme kommunikoimaan Telegramissa. Tämän avulla luultavasti vältyimme suuremmilta ongelmilta. Sprintin aikana haasteellista oli saada Robot Framework toimivaksi, emmekä saaneetkaan sitä vielä tässä sprintissä toimimaan. Tämä tapahtui osittain siksi koska ensimmäiset testattavat toiminnallisuudet luonnollisesti valmistuivat vasta sprintin loppupuolella joten aikaa testien kirjoittamisella ja ongelmien ratkaisemiselle jäi vähemmän. Ongelma olisi mahdollisesti ollut selätettävissä jos Robot Frameworkin olisi hallinnut paremmin toimiin ryhtyessä. Erityisesti Stub- ja AppLibrary-luokan tekeminen ja niiden toiminnallisuuden hahmottaminen suhteessa toisiinsa vei aikaa, mutta epäonnistumisen jälkeen sen hahmotti jo huomattavasti paremmin.

### Sprintti 1

Tässä Sprintissä Robot Framework saatiin jo implementoitua mallikkaasti. Loppuvaiheessa Robot-testit menivät rikki, mm. pääohjelman tulostuksia muuttaessa, mutta testit saatiin korjattua.

### Sprintti 2

Robot Frameworkin kanssa oli haasteita uusia testejä luotaessa. Ongelman korjaamisessa meni kohtuuttoman kauan sen luonteen vuoksi (jokaisella epäonnistuneella testikerralla Robot-testi korruptoi koko kansion, jolloin suuri osa ajasta kului kansioiden palauttamiseksi, koska pullaaminenkaan ei korjannut tilannetta). Lopulta vaikeasti löytyvä ongelma ratkesi pienellä korjauksella ja kaikki testit toimivat heti kerralla.

Aivan sprintin loppupuolella, demotilaisuuden jälkeen ilmeni ongelmia DOI-toiminnallisuudessa käytetyn *crossref-commons*-moduulin kanssa. API ei vastannut pyyntöihin ja johti aina ConnectionError-virheeseen. Tämä luonnollisesti johti kyseistä moduulia hyödyntävän toiminnallisuuden ja testien rikkoutumiseen. Tästä voidaan oppia, että ulkopuolisiin, etenkin verkkoyhteyttä hyödyntäviin komponentteihin nojaaminen saattaa aiheuttaa yllättäviä ongelmia.

## Projektin sujuvuus

### Hyvää

Mietimme ja kysyimme heti alussa, mitkä ovat virhealttiita tilanteita, joten onnistuimme luomaan aika hyvän toimintatavan heti alusta lähtien. Taskien jako ja yhdessä toteutustavoista kommunikointi suojasivat katastrofaalisilta tilanteilta. Ryhmänkeskeinen kommunikaatio myös auttoi esimerkiksi koodista johtuvien epäselvyyksien selventämisessä, ja bugien löytämisessä ja korjaamisessa.

### Huonoa

Aikatauluja oli vaikea arvioida ja aluksi sovimme ryhmän sisäisen deadlinen liian lähelle sprint reviewiä, jolloin emme ehtineet ja osanneet mm. 0-sprintissä kommunikoimaan Robot Framework -ongelmasta ajoissa.

## Mitä opimme

Vahvistimme käsityksen yhdessä suunnittelun ja kommunikoinnin tärkeydestä. Luultavasti osaamme tulevaisuudessakin alussa saada ryhmän ajatukset projektista synkronisoitua, jotta voimme alkaa viemään projektia samaan suuntaan. Opimme kukin aika kokonaisvaltaisesti projektin rakentamisesta, oppiminen painottuen hieman siihen, mitä kukin yleensä sai ratkaistavakseen. Testien kirjoittaminen ei sinänsä ollut uutta, mutta niiden ja koodin laadun jatkuva ylläpitäminen tulivat tutuksi projektin aikana.

## Mitä olisimme halunneet oppia

Demossa nähty terminaalin näppäinvalintatoiminnallisuus olisi ollut mielenkiintoista oppia. Emme vain tienneet tällaisen olevan edes mahdollista toteuttaa. Muutenkin olisi ollut kiinnostavaa tehdä hieman edistyneempi käyttöliittymä, mutta tähän tuskin aika olisi riittänyt ilman ominaisuuksien karsimista. Toisaalta käyttöliittymän pitäminen yksinkertaisena mahdollisti paremmin keskittymisen kurssin kannalta oleellisiin asioihin.

## Mikä oli turhaa

Turhalta tuntui muiden ryhmäläisten tekemään koodiin tutustumiseen käytetty aika. Tätä ongelmaa olisi voinut tietenkin välttää esimerkiksi pariohjelmoimalla enemmän.
