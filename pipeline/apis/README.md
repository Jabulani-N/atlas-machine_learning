# APIs

* Application Programming Interfaces

SWAPI gives a `response`, and `reponse.json()` gives a usable diciotnary of data. we'll call that data `data`. SWAPI's `data` is in pages ("don't forget the pagination,") so to get the next page, we'll use `data['next']`; if there is no `'next'`, there will be no entry, so it will return `None`, and we'll no longer have any more urls we need to extract from.

