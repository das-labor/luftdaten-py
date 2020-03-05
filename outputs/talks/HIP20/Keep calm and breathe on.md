---
title: Keep calm and breathe on
description: Wir stellen Bestrebungen buergerbasierter Feinstaubmessung vor
tags: Open Science, Citizen Science, Open Data, Feinstaub, Particulate Matter
robots: noindex, nofollows
lang: de
breaks: false
slideOptions:
  transition: fade
  
---

## keep calm and breathe on
#### Die atemberaubende Welt der Feinstaubdaten

<br> 
<small> ilaqa, d2ns, depate </small> <br>

<small> [das labor](https://das-labor.org) </small>

Note:
ilaqa
* Vorstellung der Vortragenden
* OpenScience Gruppe
    * OpenSource Software
    * OpenData veröffentlichen und nutzen
    * OpenAccess
    * Ziel: Reproduzierbare Ergebnisse

---

### Inhalt

* Feinstaub: Was ist das?
* luftdaten.info
* Unser Ziel: Daten verwerten 
* Vorbereitende Analysen
* Diskussion 

Note:
ilaqa

---

### Feinstaub: Was ist das?

* Partikel mit Durchmesser < 10 Mikrometer 
* Je kleiner, desto lungengaengiger
* Produkt aus:
    * Verbrennungsprozessen
    * Abrieb


Note: 
Patrik
* Aerodynamischer Durchmesser
    * besonders relevanten Kategorien sind:
        * <=2.5 &mu;m
        * <=10 &mu;m
* Durchschnitt Haardicke: 50 Mikrometer
* Pollen: 10-100 Mikrometer
* Milbe: 100 Mikrometer

---

### Feinstaubmessung

<!-- .slide: data-background="https://www.waz-online.de/var/storage/images/rnd/nachrichten/politik/inland/feinstaub-internationale-forscher-widersprechen-deutschen-grenzwert-skeptikern/712632677-4-ger-DE/Internationale-Forscher-widersprechen-deutschen-Lungenaerzten_big_teaser_article.jpg" data-background-position="right" data-background-size="50%" data-background-opacity="0.2"-->


- offizielle Messstationen
    ![](https://www.lanuv.nrw.de/fileadmin/lanuv/gifs/style/LANUV-Absenderkennung3_web.png) 
    - Fokus auf PM10 
    - Tagesmittelwerte
    - wenige Messstationen pro Stadt 
    - kaum Vergleichbarkeit zwischen Städten
    - keine Normierung des Aufstellungsortes
   
Note:
Patrik
- LANUV: Landesamt fuer Natur-, Umwelt- und Verbraucherschutz
- Sensoren in Essen: 
    - Gladbecker Straße, Steeler Straße, Vogelheim
- Aufstellstandort entscheidend
    - Aussenbezirk vs. Hauptverkehrsachse
    - Feinstaubalarme nur in D.?


---

<!-- .slide: data-background="#666"-->

> Alles muss man selber machen!

*Unbekannt*

Note:
d2ns

---

<!-- .slide: data-background="#4ecac2" -->
## luftdaten . info
#### Ein Citizen Science Projekt

- Seit 2015
- **OK Lab Stuttgart**
    - Sensorentwicklung
    - Datenspeicherung
    - Kartendarstellung

Note:
d2ns

---


### Verwendung der Daten: Heute

<iframe width="100%" height="500px" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://deutschland.maps.sensor.community/#13/51.4461/7.0150" style="border: 1px solid black"></iframe>
<br>

<small> Quelle: [deutschland.maps.sensor.community](https://deutschland.maps.sensor.community) </small>

Note:
d2ns

---

### Messprinzip
<!-- .slide: data-background="https://luftdaten.info/wp-content/uploads/2017/03/feinstaub-sensor.jpg" data-background-repeat="repeat" data-background-size="100%" data-background-opacity="0.2"-->

- Ansaugung der Umgebungsluft
- Lichtdetektion nach Streuung
    - LED 
    - Photodetektor
- Rueckrechnung auf Partikelgroesse
    - Blackbox-Algorithmus

Note: 
Patrik

Offizielle Messwerte:
   * getrocknet, gravimetrisch
   * Laserstreuung, optisch
luftdaten.info:
    * Lichtstreuung
        * Dioden, statt Laser

---

## Störungen 
* Wind :wind_chime:
* Luftfeuchtigkeit :sweat_drops: 
* Temperatur :fire: vs. :snowflake: 
* Kalibrierungs- und Chargeneffekte :wrench:
* Alter :older_woman: :older_man:
* Anbringungshöhe :tokyo_tower: 
* Hausseite :house_with_garden:

Note:
Patrik
- Aerodynamischer Durchmesser (Luftfeuchte)
- Temperaturabhängigkeit der Luftfeuchte
- low-budget Ausführung:
    - Diode vs. Laser
    - Staubansammlung
- Blackbox-Algorithmus
    - Lichtdetektion d. Streuung
    - Rueckrechnung auf Partikelgroesse
    - Physikalischer Prozess komplex:
        - Rayleigh
        - Stokes
        - Raman
        - Mie
- Kalibrierung
    - Teilweise starke Abweichungen

---

## Unser Ziel: 
### Daten nutzbar machen

* Datenqualität erhöhen
* Daten analysieren
* Sensorabdeckung erhöhen
* Erkenntnisse kommunizieren

Note: 
ilaqa

* Unterrepräsentierte Stadtteile abdecken
* Tagesmittelwerte pro Quartier

---

## Umsetzung
* Referenzmessungen
* Statistisches Modell
* Workshops
    * (abhg. v. Sensorenverteilung)
* Wissenskommunikation

Note:
ilaqa

---

### Referenzmessungen
* Viele Feinstaubsensoren gleichzeitig messen lassen
    \+ Referenzmessgerät
    \+ Temperatursensor
    \+ Luftfeuchtigkeitssensor
    \+ Variation der Anbringung 

Note:
ilaqa
* Mit der hohen Anzahl an Feinstaubsensoren können Chargeneffekte erkannt werden.
* Hof- oder Straßenseite, Höhe, Entfernung 

---

### Statistisches Modell
* Regression (linear/nicht-linear)?
* Maschinelles Lernen
* Zusätzliche Einflussgrößen ins Modell aufnehmen

Note:
ilaqa
* zusätzliche Einflussgrößen: 
    * DWD-Daten
    * Tageszeit
    * WE vs. Werktag
    * Jahreszeit
    * Entfernung zu:
        * A40/ größere Straßen
        * Industriegebiete
        * Wälder, Grünflächen, Gewässer
        * etc

---

### Workshops
* Auswahl von Stadtteilen
* Orte:
    * Vereine
    * Schulen
    * Volkshochschulen

Note:
d2ns

---

#### Orientierung für Auswahl der Stadtteile
* Vermutung hoher Feinstaubbelastung
* Soziale Merkmale berücksichtigen
* Geringe Sensorabdeckungen

Note:
d2ns

---

### Wissenskommunikation
* Lesbares und erreichbares wissenschaftliches Paper (Open Access)
* Datenvisualisierungen
* Wissensvermittlung während Workshops
* Vorträge

Note:
d2ns

---

### Vergleich zwischen Städten (Verteilung)

#### Dortmund und Essen

Note:
d2ns

---

### Juni 2017

![Juni 2017](https://wiki.das-labor.org/images/thumb/4/40/Feinstaubsensorstandorte_SDS011_Dortmund_Juni_2017.png/800px-Feinstaubsensorstandorte_SDS011_Dortmund_Juni_2017.png)

---

### Januar 2018
![Januar 2018](https://wiki.das-labor.org/images/thumb/4/4a/Feinstaubsensorstandorte_SDS011_Dortmund_Jan_2018.png/800px-Feinstaubsensorstandorte_SDS011_Dortmund_Jan_2018.png)

---

### Oktober 2018

![Oktober 2018](https://wiki.das-labor.org/images/thumb/6/67/Feinstaubsensorstandorte_SDS011_Dortmund_Okt_2018.png/800px-Feinstaubsensorstandorte_SDS011_Dortmund_Okt_2018.png)

---

### Oktober 2019

![Oktober 2019](https://wiki.das-labor.org/images/thumb/6/67/Feinstaubsensorstandorte_SDS011_Dortmund_Okt_2019.png/800px-Feinstaubsensorstandorte_SDS011_Dortmund_Okt_20189.png)

---

### Februar 2020

![Februar 2020](https://wiki.das-labor.org/images/thumb/7/7b/Feinstaubsensorstandorte_SDS011_Dortmund_Feb_2020.png/800px-Feinstaubsensorstandorte_SDS011_Dortmund_Feb_2020.png)

---

### Juni 2017

![Juni 2017](https://wiki.das-labor.org/images/thumb/9/93/Feinstaubsensorstandorte_SDS011_Essen_Okt_2018.png/800px-Feinstaubsensorstandorte_SDS011_Essen_Okt_2018.png)

---

### Januar 2018

![Januar 2018](https://wiki.das-labor.org/images/thumb/2/22/Feinstaubsensorstandorte_SDS011_Essen_Jan_2018.png/800px-Feinstaubsensorstandorte_SDS011_Essen_Jan_2018.png)

---

### Oktober 2018

![Oktober 2018](https://wiki.das-labor.org/images/thumb/9/93/Feinstaubsensorstandorte_SDS011_Essen_Okt_2018.png/800px-Feinstaubsensorstandorte_SDS011_Essen_Okt_2018.png)

---

### Oktober 2019

![Oktober 2019](https://wiki.das-labor.org/images/thumb/d/dc/Feinstaubsensorstandorte_SDS011_Essen_Okt_2019.png/800px-Feinstaubsensorstandorte_SDS011_Essen_Okt_2019.png)

---

### Februar 2020

![Februar 2020](https://wiki.das-labor.org/images/thumb/2/2d/Feinstaubsensorstandorte_SDS011_Essen_Feb_2020.png/800px-Feinstaubsensorstandorte_SDS011_Essen_Feb_2020.png)


---

### Danke! Eure Fragen!

---

## Aufforderung zur Kooperation


Note:
* Wie mit großen Datenmengen umgehen?
* Python oder R?
* Wie Code organisieren?


--- 

<!-- ## Vorbereitende Analysen
* Vergleich zwischen Städten (Verteilung)
* Vergleich von Zeiten ("Wann sind Sensoren dazu gekommen?")
### Vergleich von Zeiten (Verlaufsdigramm für's Ruhrgebiet)
-->

