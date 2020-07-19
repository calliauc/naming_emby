import logging
logger = logging.getLogger('Journal_exemple')
logger.setLevel(logging.DEBUG)

fl = logging.FileHandler('debug.log')
fl.setLevel(logging.warning)
logger.addHandler(fl)

cl = logging.StreamHandler()
cl.setLevel(logging.DEBUG)
logger.addHandler(cl)

logger.debug('Information-Debug')
logger.info('Message info')
logger.warning('avertissement')
logger.error('message-erreur')
logger.critical('erreur grave')

# Arguments :
#   rep : répertoire de travail. Defaut : .
#   season : N° de saison. Defaut : null
#   name : nom de la série. Defaut : null
#

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
