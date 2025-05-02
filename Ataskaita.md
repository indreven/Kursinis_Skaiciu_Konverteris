# MARKDOWN

# 1. Įžanga
 
### Mano sukūrta programa  - **tai skaičių konverteris**, kuris konvertuoja skaičius tarp ***romėniškų*** ir ***dešimtainių*** skaičiavimo sistemų.

### Norint paleisti programą:
i. Pirmiausia reikia atsidaryti tekstinį failą *"input.txt"*

ii. Jame įrašyti, kurį konverterį *('RomanToDecimal' ar 'DecimalToRoman')* norite naudoti

iii. Naujoje eilutėje įrašyti skaičių, kurį norite konvertuoti. 

iv. Paleisti programą

v. Konvertuotas skaičius bus rodomas konsolėje ir išsaugotas naujame faile *"output.txt"*.

### Norint naudotis programa, pirmiausia reikia nurodyti, kokį konvertavimo tipą naudoti (**RomanToDecimal** arba **DecimalToRoman**) ir įrašyti skaičių. Programa šią informaciją panaudos konvertavimui ir pateiks rezultatą.

## 2. Dėstymas

+ Abstrakcija
+ Paveldėjimas
+ Polymorfizmas
+ Inkapsuliacija

###  Abstrakcija

Abstrakcija – tai pagrindinė programavimo sąvoka, leidžianti supaprastinti sudėtingus procesus ir sutelkti dėmesį į esmines detales.

Abstrakcija taikoma tam, kad vieną kartą apibrėžus metodą kaip *tuščią* (naudojant pass), jį būtų galima vėliau iškviesti ir įgyvendinti konkrečiose klasėse, **neperrašinėjant** bendros struktūros.

#### Štai ***abstrakcijos*** pavyzdys mano kode:

Sukūriau abstraktų metodą ***convert_to***, tam, kad skirtingos klasės jį įgyvendintų savaip, išlaikydamos bendrą struktūrą.

![image](https://github.com/user-attachments/assets/34d408c8-d4e3-4d5d-8014-ac16f903d829)

###  Paveldėjimas

**Paveldėjimas** - tai objektinio programavimo principas, leidžiantis apibrėžti klasę, kuri paveldi visus metodus ir savybes iš kitos klasės.

+ Pirminė klasė yra klasė, iš kurios paveldima, dar vadinama bazine klase.
+ Vaikų klasė yra klasė, kuri paveldima iš kitos klasės, dar vadinama išvestine klase.

***Paveldėjimas*** taikomas tam, kad *vaikinė* klasė galėtų greitai perimti anksčiau apibrėžtus metodus ir savybes iš *pirminės* klasės.

#### Štai ***paveldėjimo*** pavyzdys mano kode:

Naujoji klasė pavadinimuu **"DecimalToRoman"** paveldi bazinę klasę **"Converter"** ir jos metodą *convert_to*.

![image](https://github.com/user-attachments/assets/daf2df6c-50ec-43b9-bf49-632eab86482b)

### Polimorfizmas

**Polimorfizmas** - objektinio programavimo principas, leidžiantis skirtingoms klasėms turėti tą patį metodo pavadinimą, bet skirtingą įgyvendinimą (elgseną).

***Polimorfzimas*** taikomas tam, kad tas pats metodo pavadinimas galėtų būti naudojamas skirtingose klasėse, tačiau kiekvienoje klasėje jis veiktų pagal individualų poreikį – nereikia kurti atskirų metodų su skirtingais pavadinimais.

#### Štai ***polimorfizmo*** pavyzdys mano kode:

Klasėje **DecimalToRoman** metodą *convert_to* pakeičiame pagal poreikius.

![image](https://github.com/user-attachments/assets/c72cd172-c3fa-40bf-a27b-3f04d4b350c9)

Dar vienas pavyzdys kaip naudojame polimorfizmą klasėje **RomanToDecimal**.

![image](https://github.com/user-attachments/assets/40b67d48-d5de-4826-b76a-9eac7565f9af)

### Inkapsuliacija 

**Inkapsuliacija** – užtikrina, kad objekto naudotojas negali pakeisti objekto būsenos nenumatytu būdu. Tik objekto vidiniai metodai turi galimybę keisti objekto būseną.

Yra keli prieigos matomumai:
+ Public
+ Protected 
+ Private

***Inkapsuliacija taikoma tam, kad:***

> Atributai ir metodai būtų tvarkingai paslėpti.
>
> Jų negalima būtų keisti tiesiogiai iš išorės, jei to nereikia.
>
> Užtikrinti duomenų vientisuma.

#### *Inkapsuliacijos* pavyzdys mano kode:

Kodo eilutė 'self._converter' yra "protected" tipo atributas, tam, kad apsaugotų nuo nenumatytų klaidų, jei kažkas kitas bandytų pakeisti konverterį „rankiniu būdu“ iš kitos vietos.

![image](https://github.com/user-attachments/assets/fc371645-fca6-432e-981a-40e396658618)

## Design pattern

Savo kode naudoju design pattern **Factory Method**.

**Factory metodas** – tai kūrybinis dizaino šablonas, kuris išsprendžia objektų kūrimo problemą nenurodant konkrečių jų klasių, leidžiant sprendimą dėl to, kokį objektą sukurti, priimti vykdymo metu.

***Factory design pattern*** pavaizdavimas mano kode:

*if* teiginys remdamasis *converter_type* reikšme nusprendžia kokį objektą sukurt vykdymo metu.

![image](https://github.com/user-attachments/assets/f0b2a6f5-daba-4cc2-aaba-3ef304a4c074)

### Kodėl pasirinkau 'Factory Method'?

Pasirinkau Factory Method, todėl, nes man reikėjo lankstaus būdo sukurti vieną iš kelių galimų objektų priklausomai nuo naudotojo pasirinkimo. Šis šablonas leidžia tai padaryti nesusiejant kodo su konkrečiomis klasėmis ir leidžia lengvai išplėsti sistemą ateityje.

## Kompozicija

Savo kode, naudojau kompoziją.

**Kompozicija** - tai objektinio programavimo principas, kai viena klasė savo viduje turi kitos klasės objektą ir naudoja jį savo veikimui. Toks ryšys vadinamas „yra sudaryta iš“ (angl. has-a) tipo ryšiu.

Štai pavyzdys mano kode:

Klasėje 'ConverterApp' sukuriamas kitos klasės objektas, kuris atlieka skaičiavimus ir yra **būtinas** programos veikimui.

![image](https://github.com/user-attachments/assets/244eb01c-6604-45aa-b6d2-5c1b8f29eb26)

## 3. Results and Summary

a. See “Results” functional requirement

b. See “Conclusions” functional
requirement

##### Štai ***abstrakcijos*** pavyzdys mano kode:

Sukūriau abstraktų metodą ***convert_to***, tam, kad skirtingos klasės jį įgyvendintų savaip, išlaikydamos bendrą struktūrą.

![image](https://github.com/user-attachments/assets/982e8df5-af3d-4a75-8c05-89bd9751ebe0)


## 4. Optional: Resources, references list.
