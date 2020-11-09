# Renommage serie TV


##  Renommer une série complète

<b>Renomme intégralement une serie TV</b>

* Repertoire racine
* Repertoire de chaque saison
* Chaque episode et fichier sous-titre
* Ignore une liste définie de dossiers nommés : `'OAV'`, `'Bonus'` et `'Special'`.

``` bash
rename.py --repertoire repertoire_racine_serie --serie nom_serie [--verbose] [--very-verbose]
```

``` bash
rename.py -r repertoire_racine_serie <-s nom_serie [-v] [-vv]
```

##  Renommer uniquement une saison

<b>Renomme intégralement une saison dans un repertoire de série</b>

* Le repertoire de la saison
* Chaque episode et fichier sous-titre

``` bash
rename.py --repertoire repertoire_saison --serie nom_serie --season num_saison [--verbose] [--very-verbose]
```

``` bash
rename.py -r repertoire_saison -s nom_serie -s num_saison [-v] [-vv]
```


## AVERTISSEMENT

<b><u>Travail en progression</u></b>

* Le code ne prend en charge que les formats video `.mkv`, `.avi` et `.mp4`.
* Le code ne prend en charge que le format de sous-titre `.srt`
* Fonctionnement brut, aucune vérification des fichiers avant renommage
* -> A ne pas utilier sans protection/sauvegarde !

* Features a venir
    * Empaquetage du code pour une utilisation simplifiée
    * Mode interractif pour éviter un renommage involontaire
    * Plus de formats pris en charge
    * Externalisation des paramètres (extentions, exceptions)
