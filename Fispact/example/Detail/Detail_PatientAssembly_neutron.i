<< -----set initial switches and get nuclear data----- >>
CLOBBER
MONITOR 1
JSON
GETXS 1 709
GETDECAY 1
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
<< -----irradiation phase----- >>
PULSE 50
PULSE 10
FLUX 3.3392E+03
ATOMS
TIME 1 MINS
ATOMS
<< -----cooling phase----- >>
FLUX 0.
TIME 30 MINS ATOMS
ENDPULSE
FLUX 0.
TIME 1130 MINS ATOMS
ENDPULSE
END
* END
/*
/*