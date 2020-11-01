# Reflexions rename


## CLI


### Renommer une série avec plusieurs saisons

* Commande

En étant dans le répertoire de la série ou en indiquant le repertoire
``` bash
rename.py --serie nom_serie [--rep repertoire]
```

* Fonctionnement

1. Enregistrer les infos passées en argument
2. Se placer dans le repertoire racine de la serie
3. Faire la liste des saisons
   1. Rentrer dans la saison 1
      1. Renommer les épisodes et subs
      2. Renommer le reprtoire de la saison
   2. Ressortir et passer à la saison 2
   3. Traiter toutes les saisons
4. Renommer le repertoire de la serie
5. Fin


### Renommer une saison dans une série

* Commande

En étant dans le répertoire de la saison ou en indiquant le repertoire
``` bash
rename.py --serie nom_serie --saison Numero_saison [--rep repertoire]
```


* Fonctionnement

