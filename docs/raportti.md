# Raportti

Minitex -projektin parissa työskentelivät:
- Riku Rauhala
- Henri Remonen
- Isak Pulkki
- Samppa Salo
- Ilari Haho

## Sprinttien ongelmat

### Sprintti 0

Ensimmäisen eli 0-sprintin suunnittelun jälkeen istuimme heti alas ja organisoiduimme, jaoimme taskeja ja aloimme kommunikoimaan Telegramissa. Tämän avulla luultavasti vältyimme suuremmilta ongelmilta. Sprintin aikana haasteellista oli saada Robot Framework toimivaksi, emmekä saaneetkaan sitä vielä tässä sprintissä toimimaan. Tämä tapahtui osittain siksi koska ensimmäiset testattavat toiminnallisuudet luonnollisesti valmistuivat vasta sprintin loppupuolella joten aikaa testien kirjoittamisella ja ongelmien ratkaisemiselle jäi vähemmän. Ongelma olisi mahdollisesti ollut selätettävissä jos Robot Frameworkin olisi hallinnut paremmin toimiin ryhtyessä. Erityisesti Stub- ja Library-luokan tekeminen ja niiden toiminnallisuuden hahmottaminen suhteessa toisiinsa vei aikaa, mutta epäonnistumisen jälkeen sen hahmotti jo huomattavasti paremmin.

### Sprintti 1

Tässä Sprintissä Robot Framework saatiin jo implementoitua mallikkaasti. Lopuvaiheessa Robot -testit menivät rikki, mm. pääohjelman tulostuksia muuttaessa, mutta testit saatiin korjattua.

### Sprintti 2

Robot Frameworkin kanssa oli haasteita uusia testejä luotaessa. Ongelman korjaamisessa meni kohtuuttoman kauan sen luonteen vuoksi (jokaisella epäonnistuneella testikerralla robot testi korruptoi koko kansion, jolloin suuri osa ajasta kului kansioiden palauttamiseksi, koska pullaaminenkaan ei korjannut tilannetta). Lopulta vaikeasti löytyvä ongelma ratkesi pienellä korjauksella ja kaikki testit toimivat heti kerralla.

## Projektin sujuvuus

### Hyvää

Mietimme ja kysyimme heti alussa, mitkä ovat virhealttiita tilanteita, joten onnistuimme luomaan aika hyvän toimintatavan heti alusta lähtien. Taskien jako ja yhdessä toteutustavoista kommunikointi suojasivat katastrofaalisilta tilanteilta.

### Huonoa

Aikatauluja oli vaikea arvioida ja aluksi sovimme ryhmän sisäisen deadlinen liian lähelle sprint reviewiä, jolloin emme ehtineet ja osanneet mm. 0-sprintissä kommunikoimaan Robot Framework -ongelmasta ajoissa.

## Mitä opimme

Vahvistimme käsityksen yhdessä sunnittelun ja kommunikoinnin tärkeydestä. Luultavasti osaamme tulevaisuudessakin alussa saada ryhmän ajatukset projektista synkronisoitua, jotta voimme alkaa viemään projektia samaan suuntaan. Opimme kukin aika kokonaisvaltaisesti projektin rakentamisesta, oppiminen painottuen hieman siihen, mitä kukin yleensä sai ratkaistavakseen.

## Mitä olisimme halunneet oppia

Demossa nähty terminaalin näppäinvalintatoiminnallisuus olisi ollut mielenkiintoista oppia. Emme vain tienneet tällaisen olevan edes mahdollista toteuttaa.

## Mikä oli turhaa

