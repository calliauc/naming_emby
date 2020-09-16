import os

import logging
logger = logging.getLogger('Journal_exemple')
logger.setLevel(logging.DEBUG)

fl = logging.FileHandler('debug.log')
fl.setLevel(logging.WARNING)
logger.addHandler(fl)

cl = logging.StreamHandler()
cl.setLevel(logging.DEBUG)
logger.addHandler(cl)

# logger.debug('Information-Debug')
# logger.info('Message info')
# logger.warning('avertissement')
# logger.error('message-erreur')
# logger.critical('erreur grave')

# Arguments :
#   rep : répertoire de travail. Defaut : .
#   season : N° de saison. Defaut : null
#   name : nom de la série. Defaut : null
#

rep = '.'
season = 1
name = 'truc'
exts = ['mkv', 'avi', 'mp4']

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

files = os.listdir(rep)
episodes = []
sub = []

# Création d'une liste de video et d'une liste de sous-titres

logger.debug(files)
for file in files:
    # pass
    split_name = file.split('.')
    if split_name[-1] in exts:
        episodes.append(file)
    elif split_name[-1] == 'srt':
        sub.append(file)

logger.debug(episodes)
logger.debug(sub)

new_name = ''

# Renommage des episodes
nEp = 0
for file in episodes:
    nEp += 1
    ext = file.split('.')[-1]
    os.rename(file, new_name+'_s'+str(season)+'e'+str(nEp)+'.'+ext)