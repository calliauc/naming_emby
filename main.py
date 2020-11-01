import os
import argparse

import engine
import log


parser = argparse.ArgumentParser()
# verbose_group = parser.add_mutually_exclusive_group()
# verbose_group.add_argument(
#     "-m", "--mute", help="Mode silencieux, affiche uniquement les erreurs", action="store_true")
# parser.add_argument(
#     "-s", "--season", help="Numero de la saison a renommer", type=str, default='0')
parser.add_argument(
    "-n", "--name", help="Nom de la série", type=str, default='Name')
parser.add_argument(
    "-r", "--rep", help="Repertoire de la serie", type=str, default='.')

logger = log.generate_logger()

def main():
    args = parser.parse_args()
    process = engine.Engine(args, logger)
    process.run()

main()



# Création d'une liste de video et d'une liste de sous-titres


