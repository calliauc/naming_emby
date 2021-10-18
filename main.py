#!/usr/bin/env python3

import os
import argparse

import engine
import log


parser = argparse.ArgumentParser()
# verbose_group = parser.add_mutually_exclusive_group()
# verbose_group.add_argument(
#     "-m", "--mute", help="Mode silencieux, affiche uniquement les erreurs", action="store_true")
parser.add_argument(
     "-s", "--season", help="Numero de la saison a renommer", type=str, default=False)
parser.add_argument(
    "-n", "--name", help="Nom de la série", type=str, default='Name')
parser.add_argument(
    "-r", "--repertoire", help="Repertoire de la serie", type=str, default='.')
parser.add_argument(
    "-S", "--simulation", help="Simule sans agir", default="store_true")
parser.add_argument(
    "-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument(
    "-vv", "--very-verbose", help="increase a lot output verbosity", action="store_true")

def main():
    args = parser.parse_args()
    logger = log.generate_logger(args)
    process = engine.Engine(args, logger)
    process.run()

main()

