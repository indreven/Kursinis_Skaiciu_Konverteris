## MARKDOWN

## 1. Įžanga
 
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

####  Abstrakcija

Abstrakcija – tai pagrindinė programavimo sąvoka, leidžianti supaprastinti sudėtingus procesus ir sutelkti dėmesį į esmines detales.

Abstrakcija taikoma tam, kad vieną kartą apibrėžus metodą kaip *tuščią* (naudojant pass), jį būtų galima vėliau iškviesti ir įgyvendinti konkrečiose klasėse, **neperrašinėjant** bendros struktūros.

##### Štai ***abstrakcijos*** pavyzdys mano kode:

Sukūriau abstraktų metodą ***convert_to***, tam, kad skirtingos klasės jį įgyvendintų savaip, išlaikydamos bendrą struktūrą.

![image](https://github.com/user-attachments/assets/34d408c8-d4e3-4d5d-8014-ac16f903d829)

####  Paveldėjimas

**Paveldėjimas** - tai objektinio programavimo principas, leidžiantis apibrėžti klasę, kuri paveldi visus metodus ir savybes iš kitos klasės.

+ Pirminė klasė yra klasė, iš kurios paveldima, dar vadinama bazine klase.
+ Vaikų klasė yra klasė, kuri paveldima iš kitos klasės, dar vadinama išvestine klase.

***Paveldėjimas*** taikomas tam, kad *vaikinė* klasė galėtų greitai perimti anksčiau apibrėžtus metodus ir savybes iš *pirminės* klasės.

##### Štai ***paveldėjimo*** pavyzdys mano kode:

Naujoji klasė pavadinimuu **"DecimalToRoman"** paveldi bazinę klasę **"Converter"** ir jos metodą *convert_to*.

![image](https://github.com/user-attachments/assets/daf2df6c-50ec-43b9-bf49-632eab86482b)

#### Polimorfizmas

**Polimorfizmas** - objektinio programavimo principas, leidžiantis skirtingoms klasėms turėti tą patį metodo pavadinimą, bet skirtingą įgyvendinimą (elgseną).

***Polimorfzimas*** taikomas tam, kad tas pats metodo pavadinimas galėtų būti naudojamas skirtingose klasėse, tačiau kiekvienoje klasėje jis veiktų pagal individualų poreikį – nereikia kurti atskirų metodų su skirtingais pavadinimais.

#### Štai ***polimorfizmo*** pavyzdys mano kode:

Klasėje **DecimalToRoman** metodą *convert_to* pakeičiame pagal poreikius.

![image](https://github.com/user-attachments/assets/c72cd172-c3fa-40bf-a27b-3f04d4b350c9)

Dar vienas pavyzdys kaip naudojame polimorfizmą klasėje **RomanToDecimal**.

![image](https://github.com/user-attachments/assets/40b67d48-d5de-4826-b76a-9eac7565f9af)

#### Inkapsuliacija 

**Inkapsuliacija** 

● Inheritance
● Encapsulation
Each of them should be described in the report,
explaining what it is, how it works, and how it was
used in code (tip: use code snippets/screenshots of
your program).

b. Used pattern should fit the program and be explained
how it works and why it is most suitable compared to
others

c. Your code should demonstrate the use of composition
and/or aggregation, and this should be explained in
your report.

## 3. Results and Summary

a. See “Results” functional requirement

b. See “Conclusions” functional
requirement

##### Štai ***abstrakcijos*** pavyzdys mano kode:

Sukūriau abstraktų metodą ***convert_to***, tam, kad skirtingos klasės jį įgyvendintų savaip, išlaikydamos bendrą struktūrą.

![image](https://github.com/user-attachments/assets/982e8df5-af3d-4a75-8c05-89bd9751ebe0)

####  Paveldėjimas

**Paveldėjimas** leidžia mums apibrėžti klasę, kuri paveldi visus metodus ir savybes iš kitos klasės.

+ Pirminė klasė yra klasė, iš kurios paveldima, dar vadinama bazine klase.
+ Vaikų klasė yra klasė, kuri paveldima iš kitos klasės, dar vadinama išvestine klase.

***Paveldėjimas*** taikomas tam, kad *vaikinė* klasė galėtų greitai perimti anksčiau apibrėžtus metodus ir savybes iš *pirminės* klasės.

##### Štai ***paveldėjimo*** pavyzdys mano kode:

Naujoji klasė pavadinimuu **"DecimalToRoman"** paveldi bazinę klasę **"Converter"** ir jos metodą *convert_to*.

![image](https://github.com/user-attachments/assets/b853d361-e2ea-4515-8a88-b58f9951e28b)



● Inheritance
● Encapsulation
Each of them should be described in the report,
explaining what it is, how it works, and how it was
used in code (tip: use code snippets/screenshots of
your program).

b. Used pattern should fit the program and be explained
how it works and why it is most suitable compared to
others

c. Your code should demonstrate the use of composition
and/or aggregation, and this should be explained in
your report.

## 3. Results and Summary

a. See “Results” functional requirement

b. See “Conclusions” functional
requirement

c. How it would be possible to extend
your application?

## 4. Optional: Resources, references list.
