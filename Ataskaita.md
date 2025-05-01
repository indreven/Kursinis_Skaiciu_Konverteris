## MARKDOWN

### 1. Įžanga
 
a. Mano sukūrta programa  - **tai skaičių konverteris**, kuris konvertuoja skaičius tarp ***romėniškų*** ir ***dešimtainių*** skaičiavimo sistemų.

b. Norint paleisti programą, pirmiausia reikia į tekstinį failą *"input.txt"* įrašyti, kurį konverterį norite naudoti, o kitoje eilutėje – skaičių, kurį norite konvertuoti. Paleidus programą, konvertuotas skaičius bus rodomas konsolėje ir išsaugotas naujame faile *"output.txt"*.

c. Norint naudotis programa, pirmiausia reikia nurodyti, kokį konvertavimo tipą naudoti (**RomanToDecimal** arba **DecimalToRoman**) ir įrašyti skaičių. Programa šią informaciją panaudos konvertavimui ir pateiks rezultatą.

### 2. Dėstymas

+ Abstrakcija
+ Paveldėjimas
+ Polymorfizmas
+ Enkapsuliacija

####  Abstrakcija

##### Abstrakcija – tai pagrindinė programavimo sąvoka, leidžianti supaprastinti sudėtingus procesus ir sutelkti dėmesį į esmines detales.

Abstrakcija taikoma tam, kad vieną kartą apibrėžus metodą kaip *tuščią* (naudojant pass), jį būtų galima vėliau iškviesti ir įgyvendinti konkrečiose klasėse, **neperrašinėjant** bendros struktūros.

##### Štai ***abstrakcijos*** pavyzdys mano kode:

![image](https://github.com/user-attachments/assets/982e8df5-af3d-4a75-8c05-89bd9751ebe0)

Sukūriau abstraktų metodą ***convert_to***, tam, kad skirtingos klasės jį įgyvendintų savaip, išlaikydamos bendrą struktūrą.

####  Paveldėjimas

##### **Paveldėjimas** leidžia mums apibrėžti klasę, kuri paveldi visus metodus ir savybes iš kitos klasės.

+ Pirminė klasė yra klasė, iš kurios paveldima, dar vadinama bazine klase.
+ Vaikų klasė yra klasė, kuri paveldima iš kitos klasės, dar vadinama išvestine klase.

***Paveldėjimas*** taikomas tam, kad *vaikinė* klasė galėtų greitai perimti anksčiau apibrėžtus metodus ir savybes iš *pirminės* klasės.

##### Štai ***paveldėjimo*** pavyzdys mano kode:

![image](https://github.com/user-attachments/assets/b853d361-e2ea-4515-8a88-b58f9951e28b)

Naujoji klasė pavadinimuu **"DecimalToRoman"** paveldi bazinę klasę **"Converter"** ir jos metodą *convert_to*.

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

### 3. Results and Summary

a. See “Results” functional requirement

b. See “Conclusions” functional
requirement

c. How it would be possible to extend
your application?

### 4. Optional: Resources, references list.
