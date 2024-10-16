# APIs

* Application Programming Interfaces

SWAPI gives a `response`, and `reponse.json()` gives a usable diciotnary of data. we'll call that data `data`. SWAPI's `data` is in pages ("don't forget the pagination,") so to get the next page, we'll use `data['next']`; if there is no `'next'`, there will be no entry, so it will return `None`, and we'll no longer have any more urls we need to extract from.

* due to this, it may be most efficient to create a helper function to just make the list in its entirity.
  * on second thought, that will not work if the results are like 100 pages of data I'd be attempting to temporarily store. It is paginated for a reason, after all.
    * likely, it's more efficient to simply scroll through the pages and extract the useful data as I go, so I never spend more than one page's worth of memory.

## Task 1 - Where am I?

Planets don't get a species list. instead, create a list of homeworlds for each entry in sentient species.
* remove dupes from the list