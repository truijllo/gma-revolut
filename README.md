# Giacenza Media – Calcolo della giacenza media da file CSV estrapolato da revolut

Il calcolo della giacenza media è un'operazione tediosa, ma necessaria per richiedere il rilascio di documenti relativi alla propria situazione economica, come l'Indicatore della **Situazione Economica Equivalente (ISEE)**, attualmente Revolut non mette a disposizione nessun tool che lo calcoli.

Questo script e' specifico per l'Italia, in caso il CSV non fosse compatibile modificare la localizzazione dello script tramite l'apposita variabile o modificare il CSV stesso.

esempio di utilizzo:

```
python gma-revolut.py ../../Revolut-EUR-Statement-gen\ –\ dic\ 2019.csv  
```

oppure, qualora ci fosse un saldo pregresso si puo' indicare la cifra di partenza
```
python gma-revolut.py ../../Revolut-EUR-Statement-gen\ –\ dic\ 2019.csv  10
```

