import os
import argparse

import rename
import log

parser = argparse.ArgumentParser()
# verbose_group = parser.add_mutually_exclusive_group()
# verbose_group.add_argument(
#     "-m", "--mute", help="Mode silencieux, affiche uniquement les erreurs", action="store_true")
parser.add_argument(
    "-s", "--season", help="Numero de la saison des fichiers à renommer", type=str, default='')
parser.add_argument(
    "-n", "--name", help="Nom de la série des fichiers à renommer", type=str, default='')
parser.add_argument(
    "-r", "--rep", help="Repertoire de travail", type=str, default='.')

logger = log.generate_logger()

def main():
    args = parser.parse_args()
    r = rename.Rename(args, logger)
    r.run()

main()

# Scanner le répertoire parent +1
# Si "saison XX" garder XX en mémoire sous season
#   Scanner le réportoire parent +2 et garder le nom complet en mémoire sous name
# Sinon, garder le nom complet en mémoire sous name
# (ajouter les tests de season & name non null)

# Scanner le répertoire rep
# Exclure les fichiers non multimedia de la liste
# (mp4, mkv, avi, ..., srt)
# Boucler sur les fichiers avec incrément YY en gardant l'extension en mémoire sous ext
# Renommer les fichiers multimedia sous la forme :
# "name_sXXeYY.ext"
# Quitter à la fin de la boucle

## TODO : interactif

# Création d'une liste de video et d'une liste de sous-titres


