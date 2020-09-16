import os

import argparse
import logging

logger = logging.getLogger('Journal_exemple')
logger.setLevel(logging.DEBUG)

fl = logging.FileHandler('debug.log')
fl.setLevel(logging.WARNING)
logger.addHandler(fl)

cl = logging.StreamHandler()
cl.setLevel(logging.DEBUG)
logger.addHandler(cl)


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

class Rename:
    def __init__(self, args):
        self.rep = args.rep
        self.season = args.season
        self.name = args.name
        self.exts = ['mkv', 'avi', 'mp4']

        # os.chdir(self.rep)

        self.files = os.listdir(self.rep)
        self.episodes = []
        self.sub = []

    def scan_rep(self):
        logger.debug(self.files)


        for file in self.files:
            # if os.path.isdir(file):
            #     logger.debug(file + ' est un repertoire')
            # else:
            #     logger.debug(file + ' n\'est pas un repertoire')
            split_name = file.split('.')
            if split_name[-1] in self.exts:
                self.episodes.append(file)
            elif split_name[-1] == 'srt':
                self.sub.append(file)

        logger.debug(self.episodes)
        logger.debug(self.sub)


    def rename_episodes(self):
        nEp = 0
        for file in self.episodes:
            self.name
            nEp += 1
            ext = file.split('.')[-1]
            os.rename(file, self.name+'_s'+str(self.season)+'e'+str(nEp)+'.'+ext)


    def rename_subtitle(self):
        nSb = 0
        for file in self.sub:
            new_name = self.name
            nSb += 1
            ext = file.split('.')[-1]
            os.rename(file, new_name+'_s'+str(self.season)+'e'+str(nSb)+'.'+ext)


args = parser.parse_args()

r = Rename(args)

r.scan_rep()

r.rename_episodes()
r.rename_subtitle()

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


