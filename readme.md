# Renommage serie TV

## Principe

Renomme intégralement une serie TV
* Repertoire racine
* Repertoire de chaque saison
* Chaque episode et fichier sous-titre

##  Renommer une série avec plusieurs saisons

Par défaut, le programme se lance dans le repertoire courant

``` bash
rename.py --serie nom_serie [--repertoire repertoire_racine_serie] [--verbose] [--very-verbose]
```
``` bash
rename.py -s nom_serie [--r repertoire_racine_serie] [-v] [-vv]
```


## AVERTISSEMENT

<b><u>Travail en progression</u></b>

* Le code ne prend en charge que les formats video `.mkv`, `.avi` et `.mp4`.
* Le code ne prend en charge que le format de sous-titre `.srt`
* Code instable, aucune vérification des fichiers avant renommage
* A ne pas utilier sans protection/sauvegarde !