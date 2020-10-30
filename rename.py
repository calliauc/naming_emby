import os

import log

class Rename:
    def __init__(self, args, logger):
        self.logger = logger


    def rename_parent_rep(self, name):
        try:
            old_name = os.path.abspath(self.rep)
            new_name = f"{os.path.dirname(os.path.abspath(self.rep))}/{name}"

            self.logger.info(f'Renaming : {name}')
            os.rename(old_name, new_name)
            self.logger.info(f'Succes -> {name}')
        except:
            self.logger.warning(f'Failed to rename {name}')


    def rename_file(self, Name, newName):
        try:
            self.logger.info(f'Renaming : {Name}')
            os.rename(Name, newName)
            self.logger.info(f'Succes -> {newName}')
        except:
            self.logger.warning(f'Failed to rename {Name}')

    def rename_episodes(self, name, season, episodes):
        self.logger.info(episodes)
        nEp = 0
        for file in episodes:
            nEp += 1
            ext = file.split('.')[-1]
            newName = f'{name}_s{str(season)}e{str(nEp)}.{ext}'
            self.rename_file(file, newName)

    def rename_subtitle(self, name, season, subs):
        self.logger.info(subs)
        nSb = 0
        for file in subs:
            nSb += 1
            ext = file.split('.')[-1]
            newSub = f'{name}_s{str(season)}e{str(nSb)}.{ext}'
            self.rename_file(file, newSub)
