# Package `models`

Les modules de ce package contiennent principalement des classes qui implémentent le modèle de données relationnel du backend. Ces classes peuvent représenter :

- des tables SQL (héritage depuis `ApiHandler` et `Model`) ;
- des colonnes de tables SQL (on parle alors de classe `*Mixin`).

Ce système repose entièrement sur l'ORM SQL `Alchemy`.

The modules in this package mainly contain classes that implement the relational data model for the backend. These classes are represented as follows:

- SQL tables (inheritance from `ApiHandler` and` Model`);
- columns of SQL tables (we call class `* Mixin`).

This system is entirely based on the ORM SQL `Alchemy`.

## Do

Les modifications apportées au modèle de données doivent impérativement et systématiquement être scriptées dans une migration de schéma relationnel avec `Alembic`. Les deux modifications (classes d'ORM et migration `Alembic`) doivent être mergée simultanément dans la branche master. Il est impératif d'être ISO entre une classe ORM et la révision `Alembic` car la production ne joue que les révisions `Alembic` et ne s'occupe pas des `Model`. Il est important de savoir qu'une clé étrangère n'est pas un index par défaut en `Postgres`, il faut donc le rajouter en fonction de votre contexte.

The modifications made to the data model must be imperatively and systematically scripted in a relational schema migration with `Alembic`. Both modifications (ORM classes and `Alembic` migration) must be merged simultaneously in the master branch. It is imperative to be ISO between an ORM class and the `Alembic` revision because the production only plays the` Alembic` revisions and does not take care about the `Model`. It is important to know that a foreign key is not a default index in `Postgres`, so you have to add it according to your context.

Donc quand on a :

So when we have:

```python
fooId = Column(BigInteger,
    ForeignKey('foo.id'),
    index=True)
```

Il faut dans la révision `Alembic` :

In the `Alembic` revision, you need:

```python
ALTER TABLE ONLY bar_foo ADD CONSTRAINT "bar_foo_fooId_fkey" FOREIGN KEY ("fooId") REFERENCES foo(id);
CREATE INDEX "idx_bar_foo_fooId" ON offer_foo ("fooId");
```

## Testing

Les classes présentes dans ce package ne sont pas testables puisque composées, dans leur forme la plus simple, uniquement de déclaration de champs. Toutefois, si on souhaite leur donner des comportements ou de la logique (e.g. via des méthodes d'instance ou des _properties_) il est possible de les tester unitairement.

The classes present in this package are not testable since they are designed, in their simplest form, to comprised only of declaration of fields. However, if we want to give them behaviors or logic (e.g. via instance methods or _properties_) it is possible to test them individually.


## Pour en savoir plus // For more information

- https://fr.wikipedia.org/wiki/Mapping_objet-relationnel
- https://www.sqlalchemy.org/features.html
- https://alembic.sqlalchemy.org/en/latest/index.html