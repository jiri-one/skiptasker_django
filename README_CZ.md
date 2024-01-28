# Základní dokumentace:

Vzhledem k tomu, že tento repozitář je pouze základní ukázkou práce s Pythonem, Djangem a Dockerem, tak i tato dokumentace bude jednoduchá a bude spíše obsahovat některé poznámky.

**Popis aplikace:**

Aplikace je vyloženě jednoduchý úkolníček, který umožňuje vytvářet, modifikovat a mazat jednotlivé úkoly. Každý úkol má dva povinné parametry: jméno a popis. Dále je možné při vytvoření úkolu zadat také jeho status - pokud status zadán nebude, tak se doplní výchozí status CREATED. Všechny tyto tři atributy, tedy jméno, popis a status jsou editovatelné parametry. K těmto parametrům náleží ještě needitovatelné parametry, konkrétně čas vytvoření a čas dokončení. Needitovatelné parametry se doplňují a mění automaticky a uživatel je může pouze vidět a ovládat jejich hodnotu pouze nepřímo (čas dokončení se totiž odvíjí od hodnoty, která je nastavená ve statusu).

**Popis jednotlivých parametrů jednoho tasku REST API:**

`name` - libovolné jméno úkolu (musí být unikátní v rámci celé databáze)

`description` - libovolný popis úkolu

`status` - může nabývat pouze tří parametrů, CREATED, INPROGRESS a COMPLETED

`creation_time` - needitovatelný datetime, automaticky nastavená hodnota při vytvoření tasku

`completion_time` - needitovatelný datetime, automaticky nastavovaná hodnota odvíjející se od hodnoty parametru status

**Popis metod, které se pro REST API používají:**

`GET` - používá pro získání všech tasků nebo pro získání jednoho tasku (dle endpointu - kořenový endpoint pro všechny tasky a /task_id pro jeden task [task_id musí být celé číslo a musí existovat])

`POST` - používá se pouze pro vytvoření jednoho tasku

`PUT` - používá se pouze pro změnu/aktualizaci jednoho tasku

`DELETE` - používá se pouze pro smazání jedhoho tasku

**Jak s aplikací pracovat:**

Aplikace je připravená pouze jako REST API server, tedy aby bylo možné úkoly vytvářet, číst a měnit, tak je nutné použít nějaký HTTP klient - prohlížeč, curl, Python requests lib, ... 
Všechny endpointy komunikují za pomocí JSON formátu.

Nicméně je také možné využít Django administraci, přes kterou je také možné aplikaci ovládat přímo přes webové rozhraní. Pro tyto účely byl vytvořen administrátorský účet **skip_pay** s heslem **skip**.

**Testy:**

Pro aplikaci jsou vytvořeny základní testy, které testují funkčnost aplikace.
Pokud chcete testy spustit, tak v adresáři se souborem manage.py spusťte následující příkaz:

`python manage.py test`

**Jak pracovat s aplikací pomocí programu curl:**
```
curl -X POST -H "Content-Type: application/json" \
    -d '{"name": "new name, "description": "some desc"}' \
    127.0.0.1:8000
```

Tento příkaz vytvoří nový úkol a uloží ho do databáze. Jak postupovat pro další http metody se nejlépe dozvíte v testech (api/tests.py), kde jsou otestovány všechny možnosti samotného API.

**Jak spustit aplikační server s REST API:**

Aplikaci je možné spustit mnoha způsoby. Doporučeným způsobem je pomocí containerové technolgie Docker a za pomocí nástroje docker-compose pomocí příkazu (příkaz předpokládá, že jste v kořenovém adresáři, respektive tam, kde je soubor docker-compose.yml):

`docker-compose up -d`

V dnešní době je moderní pouštět containery spíše za pomocí nástroje podman a k němu také náleží ekvivalentní nástroj podman-compose se stejnými parametry jako u Docker verze:

`podman-compose up -d`

Další možností jak server spustit je přímo z Pythonu a ideálně za použití virtuálního prostředí (následující příkazy předpokládají operační systém Linux, u jiných systémů se příkazy drobně liší):
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

**POZNÁMKA:**
Tato dokumentace je opravdu pouze ukázková a tedy není vyčerpávající (vlastně je psaná v rychlosti na "první dobrou" ;-) ).
