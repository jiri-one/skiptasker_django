Základní dokumentace:

Vzhledem k tomu, že tento repozitář je pouze základní ukázkou práce s Pythonem, Djangem a Dockerem, tak i tato dokumentace bude jednoduchá a bude spíše obsahovat některé poznámky.

Popis aplikace:
Aplikace je vyloženě jednoduchý úkolníček, který umožňuje vytvářet, modifikovat a mazat jednotlivé úkoly. Každý úkol má dva povinné parametry: jméno a popis. Dále je možné při vytvoření úkolu zadat také jeho status - pokud status zadán nebude, tak se doplní výchozí status CREATED. Všechny tyto tři atributy, tedy jméno, popis a status jsou editovatelné parametry. K jednotlivým parametrům náleží ještě needitovatelné parametry, konkrétně čas vytvoření a čas dokončení. Needitovatelné parametry se doplňují a mění automaticky a uživatel je může pouze vidět a ovládat jejich hodnotu pouze nepřímo (čas dokončení se totiž odvíjí od hodnoty, která je nastavená ve statusu).

Popis jednotlivých parametrů jednoho tasku REST API:
name - libovolné jméno úkolu (musí být unikátní v rámci celé databáze)
description - libovolný popis úkolu
status - může nabývat pouze tří parametrů, CREATED, INPROGRESS a COMPLETED
creation_time - needitovatelný datetime, automaticky nastavená hodnota při vytvoření tasku
completion_time - needitovatelný datetime, automaticky nastavovaná hodnota odvíjející se od hodnoty parametru status

Jak s aplikací pracovat:
Aplikace je připravená pouze jako REST API server, tedy aby bylo možné úkoly vytvářet, číst a měnit, tak je nutné použít nějaký HTTP klient - prohlížeč, curl, ... 
Všechny endpointy komunikují za pomocí JSON formátu.

Nicméně je také možné využít Django administraci, přes kterou je také možné aplikaci ovládat přímo přes webové rozhraní. Pro tyto účely byl vytvořen administrátorský účet skip_pay s heslem skip .
