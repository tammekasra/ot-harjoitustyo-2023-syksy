# Sudoku Game

## Purpose
The Sudoku game is a game where there are m x m rows and columns such that each row and column can have numbers from 1 to 9. The main idea of the game is at the beginning the 9x9 grid has random numbers generated to it.
The user then has to figure out whhich numbers to put where until the full grid is completed!

For full details you should check [Vaatimusmaarittely](https://github.com/tammekasra/ot-harjoitustyo-2023-syksy/blob/main/Dokumentaatio/vaatimusmaarittely.md)


The links below are for week1 and week2 -kattavusraporrti (Couldn't figure out how to get 100%...)



[Changelog](https://github.com/tammekasra/ot-harjoitustyo-2023-syksy/blob/main/Dokumentaatio/changelog.md)

[Tyoaikakirjanpito](https://github.com/tammekasra/ot-harjoitustyo-2023-syksy/blob/main/Dokumentaatio/tyoaikakirjanpito.md)

[arkkitehtuuri](https://github.com/tammekasra/ot-harjoitustyo-2023-syksy/blob/main/Dokumentaatio/arhitekktuuri.md)


## I have no idea why "poetry run pytest" doesn't work at all 

I get the following error despite that all the tests and modules are in the correct directory src/ ?!?!?!?!?!?

(poetry-py3.10) raql@5500-DOWU0011A:~/ot-harjoitustyo-2023-syksy/src/tests$ poetry run pytest
=============================================================== test session starts ================================================================platform linux -- Python 3.10.12, pytest-7.4.3, pluggy-1.3.0
rootdir: /home/raql/ot-harjoitustyo-2023-syksy/src/tests
collected 0 items / 1 error

====================================================================== ERRORS ======================================================================__________________________________________________________ ERROR collecting test_game.py ___________________________________________________________ImportError while importing test module '/home/raql/ot-harjoitustyo-2023-syksy/src/tests/test_game.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
test_game.py:5: in <module>
    from Sudoku.game import SudokuGame  # Adjust the import based on your actual module structure
E   ModuleNotFoundError: No module named 'Sudoku'




