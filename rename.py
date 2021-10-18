import os

import log


class Rename:
    def __init__(self, args, logger, simu):
        self.logger = logger
        self.simu = simu


    def rename_parent_rep(self, name):
        try:
            old_name = os.path.abspath('.')
            new_name = f"{os.path.dirname(os.path.abspath('.'))}/{name}"

            if self.simu:
                os.rename(old_name, new_name)
            self.logger.info(f'Renaming rep \"{new_name}\" from \"{old_name}\"')
        except:
            self.logger.warning(f'Failed to rename rep : \"{new_name}\" from \"{old_name}\"')

    def rename_file(self, name, new_name):
        try:
            if self.simu:
                os.rename(name, new_name)
            self.logger.info(f'Renaming file \"{new_name}\" from \"{name}\"')
        except:
            self.logger.warning(f'Failed to rename file : \"{new_name}\" from \"{name}\"')


    def generate_season_name(self, num, name):
        new_name = f'{name}_saison_{num :0>2}'
        self.logger.debug(new_name)
        self.rename_parent_rep(new_name)

    def generate_names_episodes(self, name, season, episodes):
        try:
            episodes.sort()
            self.logger.info(f'Tri des episodes')
        except:
            self.logger.error(f'Erreur lors du tri des episodes')
            exit(5)
        self.logger.info(f'Liste des episodes : {episodes}')
        nEp = 0
        for file in episodes:
            nEp += 1
            ext = file.split('.')[-1]
            if int(season) == 0: 
                newName = f'{name}_e{str(nEp) :0>2}.{ext}'
            else:
                newName = f'{name}_s{str(season) :0>2}e{str(nEp) :0>2}.{ext}'
            self.rename_file(file, newName)

    def generate_names_subtitles(self, name, season, subs):
        try:
            subs.sort()
            self.logger.info(f'Tri des subs')
        except:
            self.logger.error(f'Erreur lors du tri des subs')
            exit(6)
        self.logger.info(subs)
        nSb = 0
        for file in subs:
            nSb += 1
            ext = file.split('.')[-1]
            newSub = f'{name}_s{str(season) :0>2}e{str(nSb) :0>2}.{ext}'
            self.rename_file(file, newSub)
