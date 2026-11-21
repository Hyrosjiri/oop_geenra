Zadání: Uživatelský systém firmy
Firma potřebuje jednoduchý systém pro správu uživatelských účtů. Všichni uživatelé mají společné vlastnosti, ale jednotlivé role mají také své specifické atributy a oprávnění.
1. Rodičovská třída Uzivatel
Vytvoř třídu, která bude obsahovat:

Atributy konstruktoru:
- jmeno
- email
- heslo
Metody:
- vypis_profil() – vypíše jméno a email uživatele.
- zmen_heslo(nove_heslo) – změní heslo uživatele.
- over_heslo(heslo) – ověří, zda zadané heslo odpovídá uloženému heslu. Vrátí True nebo False.
2. Potomek Administrator
Administrátor dědí z třídy Uzivatel.

Do konstruktoru přidej vlastní atributy:
- uroven_opravneni
- pocet_spravovanych_uzivatelu
Požadavky:
- Pomocí super().__init__() zavolej konstruktor rodiče.
- Vytvoř metodu smaz_uzivatele(), která vypíše informaci o odstranění uživatele.
- Vytvoř metodu vypis_profil(), která nejprve zavolá rodičovskou metodu vypis_profil() a potom vypíše vlastní atributy administrátora.
3. Potomek Zakaznik
Zákazník také dědí z třídy Uzivatel.

Přidej vlastní atributy:
- cislo_uctu
- zustatek
Požadavky:
- Použij super().__init__().
- Vytvoř metodu pridej_peneze(castka), která zvýší zůstatek.
- Vytvoř metodu vypis_profil(), která zavolá rodičovskou metodu a doplní informace o zákaznickém účtu.
- Vytvoř metodu zobraz_zustatek(), která vypíše aktuální zůstatek.
4. Otestuj program
Vytvoř:
- administrátora Jana Nováka s úrovní oprávnění 3, který spravuje 25 uživatelů,
- zákazníka Petra Svobodu s číslem účtu 123456 a počátečním zůstatkem 15 000 Kč.
Proveď následující operace:
1. Vypiš profil obou uživatelů.
2. U zákazníka přidej 2 500 Kč.
3. Zobraz nový zůstatek.
4. Změň zákazníkovi heslo.
5. Ověř správnost nového hesla.
6. Zavolej metodu smaz_uzivatele() u administrátora.
