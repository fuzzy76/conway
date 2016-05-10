Conway's Game of Life LAB!
==========================

Teorien:
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

Prøv selv:
http://pmav.eu/stuff/javascript-game-of-life-v3.1.1/

Steg for å sette opp miljøet.
====================

1) Installer pyenv og pyenv-virtualenv.

   https://github.com/yyuu/pyenv
   https://github.com/yyuu/pyenv-virtualenv

2) Opprett en arbeidsmappe og aktiver virtualenv med Python 3.5.1.

   $ mkdir PythonGameOfLife
   $ cd PythonGameOfLife
   $ echo -e "PythonGameOfLife\n3.5.1" > .python-version
   $ pyenv virtualenv 3.5.1 PythonGameOfLife

Regler.
===================

(Fra Wikipedia)

```
Any live cell with fewer than two live neighbours dies, as if caused by under-population.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by over-population.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
```

Hva behøver vi (eksempel)?
==========================

World objekt:
 * En to-dimensjonal verden, oppgitt i x og y koordinat.
 * Holder levende Cell'er og deres koordinater.
   Tips: Lagre individuelt koordinat (x,y) i tuplet, bruk så ett "set" objekt til listen.
 * Manuelt oppsett av celler i verden.
 * Mulighet for å sjekke om koordinat for celle er lovlig.
 * Forsøk på å lagre celle utenfor kartet kaster unntaksfeil.
 * Mulighet for å autopopulere verden med tilfeldige sett av levende celler.
 * Celle ytterst til venstre er nabo med celle ytterst til høyre på samme rad.
 * Celle øverst er nabo med celle nederst på samme kollonne.
 * Beregne hvilke celler som overlever og hvem som dør i ny generasjon,
   i henhold til reglene i Conway's Game Of Life.
 * Noe mer?

Game python fil:
 * Starte spillet via kommandolinjen (bonus oppgave).

Filstruktur
===============

$ mkdir -p lib tests/lib
$ touch game.py lib/__init__.py lib/world.py
$ touch tests/__init__.py tests/lib/__init__.py tests/lib/test_world.py

Følgende filstruktur:

$ tree
.
├── game.py
├── lab-notes.txt
├── lib
│   ├── __init__.py
│   └── world.py
└── tests
    ├── __init__.py
    └── lib
        ├── __init__.py
        └── test_world.py

3 directories, 7 files

Kopier initielle klasser.
===========================

Kopier innholdet i lab_world.py til world.py, se plassering i filstruktur i forrige avsnitt.

Kopier innholdet i lab_test_world.py til test_world.py, se plassering i filstruktur i forrige avsnitt.

Åpne ./tests/lib/test_world.py i tekst-editor, videre veiledning står der.

Bonusoppgave
============

Fullfør implementasjon av test_world.py og world.py, DERETTER implementer game.py.

Lag visuell demo som viser fungerende Conway's Game Of Life implementasjon.
