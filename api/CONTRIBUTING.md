# Package `repository`

Les modules de ce package contiennent des fonctions qui implémentent des _queries_ SQL Alchemy basées sur les _Models_ SQL Alchemy définis dans le package `models` ou de la lecture de variables d'environnement (l'environnement étant une
dépendance externe au système).

The modules in this package contain functions that implement SQL Alchemy queries based on SQL Alchemy Models defined in the models package or reading environment variables (the environment being an external dependency on the system).

## Do

Ces fonctions doivent contenir uniquement des requêtes vers la base de données qui retournent soit des tuples de données "primitives" (e.g. une liste d'adresses e-mail), soit des instances de modèles SQL Alchemy. On pourra aussi avoir des fonctions qui retournent des "morceaux" de queries, c'est-à-dire des fonctions (privées) qui construisent des queries
qui ne sont pas déclenchées (i.e. qui n'ont pas de `.all()` ou `.first()`). On utilisera des indications de type dans les signatures des fonctions pour indiquer quelles sont les données attendues en entrée et en sortie.

These functions should only contain queries to the database that return either "primitive" data tuples (e.g. a list of e-mail addresses) or instances of SQL Alchemy models. We can also have functions which return a "subset" of queries, that is to say (private) functions that build queries which are not triggered (ie which do not have an .all () or. first ()). Type indications will be used in the function signatures to indicate what data is expected at input and output.


## Don't

Ces fonctions ne doivent pas contenir :

- Des notions relatives au `routing` (e.g. _status codes_ HTTP, verbes HTTP) ;
- Des règles de gestion ;
- Des appels à des web services.

These functions must not contain:

- Notions relating to routing (e.g. HTTP status codes, HTTP verbs);
- Management rules;
- Calls to web services.

## Testing

Ces fonctions sont testées dans un contexte Flask, donc avec une connexion à la base de données. On considère que ce sont des tests d'intégration. Ces tests déclenchent donc de vraies requêtes SQL et nécessitent que des données soient présentes en base. Ces tests utilisent le décorateur `@clean_database` qui s'occupe de vider chaque table avant l'exécution d'un test et insèrent les données nécessaires dans leur partie `# given`.

Ils ont pour objectif de :

- Vérifier qu'une requête fait bien ce qu'elle dit et retourne des données censées ;
- Vérifier que les requêtes gèrent bien les cas aux limites via des exceptions attendues.


These functions are tested in a Flask context, therefore with a connection to the database. We consider these integration tests. These tests trigger real SQL queries and require data to be present in the database. These tests use the `@ clean_database` decorator which takes care of emptying each table before executing a test and insert the necessary data in their `# given` part.


They aim to:

- Verify that a request does what it says and returns the correct data;
- Verify that the queries handle the boundary cases well via expected exceptions.

## Pour en savoir plus // For more information

- http://flask-sqlalchemy.pocoo.org/2.3/queries/

## Notes on tsvector functions within keywords.py file

tsvector (text search vector) is a data type which consists of the following characteristics:

- a sorted list (alphabetically)
- normalized words to merge different variants of the same word
- duplicates of same words are removed

Reference: https://stackoverflow.com/questions/42388956/create-a-full-text-search-index-with-sqlalchemy-on-postgresql