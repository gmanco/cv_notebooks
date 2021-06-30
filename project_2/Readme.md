# Progetto 2021 - Appello 2



Data Rilascio 30/06/2021

Data Consegna 26/07/2021 ore 20.00

Data Appello 29/07/2021 ore 9.00



Specifiche presenti nel file PDF allegato nella folder del primo appello **project_1**.

### Nuove baseline

Per il secondo appello saranno utilizzate queste baseline 

- Baseline 1 - 8 pt: Micro-avg F1 0.26 con almeno **15** classi con **f1-score** > 0
- Baseline 2 - 7 pt + bonus: Micro-avg F1 0.30 con almeno **35** classi con **f1-score** > 0

Il vincolo sul numero di classi si calcola a partire dall'output del classification report del test set. Qualora non venga soddisfatto, la baseline non può considerarsi superata.

Nel seguente esempio solo 3 classi delle 5 visualizzate superano il criterio.

```
                        precision    recall  f1-score   support

                LGBT       0.09      0.67      0.16        61
              action       0.21      0.97      0.34       191
     action_comedies       0.00      0.00      0.00         6
          ....
             western       0.00      0.00      0.00        33
             zombies       0.29      0.13      0.18        15

             micro	avg	   0.16	     0.55	     0.25	     3167
             macro	avg	   0.02	     0.12	     0.03	     3167
             weighted	avg	 0.13	     0.55	     0.20	     3167
             samples avg	 0.16	     0.60	     0.24	     3167
```

Ad esempio, si consideri un modello che raggiunga un valore di micro-avg F1 di 0.32 ma con sole 21 classi che hanno un f1-score >0. In questo caso la seconda baseline non può considerarsi superata, quindi il punteggio assegnato sarà **8+7 pt**, cioè il punteggio della baseline 1 più il massimo punteggio pre-baseline 2.



### Modalità di consegna

Una mail con il link (drive, onedrive, ecc.) ad un archivio zip/rar/tgz/... con nome **appello2_cognome_matricola_cognome_matricola.ext** contenente:

- la presentazione del progetto che sarà mostrata durante l'esame
- il dump del modello
- un notebook con il quale caricare il modello e etichettare il test set, vedi esempio in **project_1**
- il codice/notebook utilizzato per il training

## Progetti primo appello

Nella folder *previous_models* sono riportati alcuni progetti presentati al primo appello e che possono  fornire qualche suggerimento su come costruire un modello efficace. Non saranno accettati progetti che riprendono in gran parte quanto già presentato.

## Dataset

- progetto_2021_dataset_labeled.tgz MD5: a4389434280d273d8ed81e720cae2c89

  https://owncloud.cs.icar.cnr.it/owncloud/index.php/s/gEC5TS5FeGtrt8x 

- progetto_2021_dataset_UNlabeled1.tgz MD5: b0dfb49a4030f3e79682cfb0df0c8b50

  https://owncloud.cs.icar.cnr.it/owncloud/index.php/s/nb9AUqMDxV17RxX  

- progetto_2021_dataset_UNlabeled2.tgz MD5: 070c7916081f0e19eb5f7bdc94102d0e

  https://owncloud.cs.icar.cnr.it/owncloud/index.php/s/2T8J8DHDL9ZmhtU  

- progetto_2021_dataset_UNlabeled3.tgz MD5: 0251edf0cbb544752accb57271748f04

  https://owncloud.cs.icar.cnr.it/owncloud/index.php/s/RMaNWGly2Cgb7Nb

