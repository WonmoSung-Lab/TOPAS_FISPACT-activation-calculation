<< -----set initial switches and get nuclear data----- >>
CLOBBER
MONITOR 1
JSON
PROJ 3
GETDECAY 1
GETXS 1 162
FISPACT
* brass
DENSITY 8.55
MASS 9.31 2
Cu 70
Zn 30
UNCERTAINTY 2
DOSE 2 0.3
HALF
HAZARDS
FLUX 1.2180E+04
ATOMS
TIME 15 YEARS
ATOMS
<< -----cooling phase----- >>
FLUX 0.
TIME 1 DAYS ATOMS
TIME 2 DAYS ATOMS
TIME 2 DAYS ATOMS
TIME 2 DAYS ATOMS
TIME 7 DAYS ATOMS
TIME 16 DAYS ATOMS
TIME 30 DAYS ATOMS
TIME 30 DAYS ATOMS
TIME 90 DAYS ATOMS
TIME 185 DAYS ATOMS
TIME 365 DAYS ATOMS
END
* END
/*