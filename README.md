# To run the test in BDD
```
behave
```
Cum vedem toate packet-ele? 
```commandline
pip freeze > requirements.txt
behave --tags=smoke -f html -o raport.html 
brehave => ruleaza toate testele
--tags=smoke => alege sa ruleze testele cu tegul 'smoke'
-f => vine de la formatul de output si setam html
-o => vine de la output raport cum sa se numeasca

behave .\features\checboxes.feature (pentru a rula un anumit feature)
```
Ce este HOOK - carlig?
```commandline
Carlig - este o functie, prin care poti sa ageti de toate testele tale, in special pe partea de initializarea
driver-ului. Pe langa hook, e si feature - ii o functie care ne ajuta sa initializazi o alta functie.
Adica, partea de webdriver -  poti sa setezi in functie ce browser vrei sa folosesti, dintr-un singur loc, 
si sa mearga in tot proiect tau
```