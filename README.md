# poc-emmental

Why emmental ? Take a quick look in the code, there are some `*TBW*` holes in the scripts... This is where critical code needs `To Be Written` to make the application working.


## Task 3 : poc-react

Time has come to show data for users. Essential of the task would be to setup a full react redux webapp boilerplate in order to display a one single non interactive fetching reviews page like this:

<p align="center">
  <img
    alt="Demo of what to expect with poc-react"
    src="https://github.com/feedback-news/poc-emmental/blob/poc-react/images/poc-react.gif"
  />
</p>


### Notes on tsvector functions within keywords.py file

tsvector (text search vector) is a data type which consists of the following characteristics:

- a sorted list (alphabetically)
- normalized words to merge different variants of the same word 
- duplicates of same words are removed


```python
def import_keywords():
            Claim.__ts_vector__ = create_tsvector(
        
        # coalesce returns the first non-null value in text column

        # cast entire text column into a string

        # pass string into create_tsvector function

        # empty string at the end to be returned as is if current row in Claim.text column is Null
        cast(coalesce(Claim.text, ''), TEXT),
    )
    Claim.__table_args__ = (
    # create a PostgreSQL Full Text Search index for the claim table using the created tsvector as a GIN (Generalized Inverted Index) index which handle cases where the items to be indexed are composite values
        Index(
            'idx_claim_fts',
            Claim.__ts_vector__,
            postgresql_using='gin'
        ),
    )

def create_tsvector(*targets):
    exp = targets[0]
    # combine all words in the array passed in into a single text string separated by a space character (format needed to create a tsvector) between each word
    for target in targets[1:]:
        exp += ' ' + target
    
    # create tsvector using english as the configured language
    return func.to_tsvector('english', exp)

```

#### Reference
1. https://www.postgresql.org/docs/10/datatype-textsearch.html
2. https://www.postgresql.org/docs/9.1/textsearch-controls.html
3. https://stackoverflow.com/questions/42388956/create-a-full-text-search-index-with-sqlalchemy-on-postgresql
4. https://www.postgresql.org/docs/9.5/gin-intro.html#:~:text=61.1.,appear%20within%20the%20composite%20items.