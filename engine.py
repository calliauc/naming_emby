import os

import rename


class Engine:
    def __init__(self, args, logger):
        self.logger = logger
        self.logger.debug(args)

        if args.simulation == True:
            self.simu = True
            self.logger.warning(f'LE SCRIPT FONCTIONNE EN MODE SIMULATION. AUCUN CHANGEMENT DEFINITIF')
        else:
            self.simu = False
            self.logger.warning(f'Le script fonctionne en mode normal, les changement sont définitifs.')

        self.rename = rename.Rename(args, logger, self.simu)
        self.rep = args.repertoire
        self.season = args.season
        self.name = args.name
        self.exts = ['mkv', 'avi', 'mp4']
        self.ignore = ['OAV', 'oav', 'Bonus', 'bonus', 'Special', 'special', 'Specials', 'specials']

        try:
            os.chdir(self.rep)
            self.logger.debug(f'Dossier changé pour : {self.rep}')
        except:
            self.logger.critical(f'Wesh tufékoi avec \"{self.rep}\" ? C\'est même pas un dossier ')
            self.logger.critical(f'Error 2. \"{self.rep}\" is not a repository or does not exist')
            exit(2)

        self.files = []
        self.seasons = []
        self.episodes = []
        self.subs = []



    def run(self):
        if self.season == False:
            self.generate_list_seasons()
            if  len(self.seasons) >= 1:
                self.logger.info(f'Plusieurs saisons à renommer')
                try:
                    self.seasons.sort()
                    self.logger.info(f'Tri des saisons')
                except:
                    self.logger.error(f'Erreur lors du tri des saisons')
                    exit(4)
                self.logger.info(f'Liste des saisons : {self.seasons}')
                self.walk_in_seasons()
            elif len(self.seasons) == 0:
                self.logger.info(f'Une seule saison à renommer')
                self.generate_lists()
                self.rename.rename_parent_rep(self.name)
        else:
            self.logger.info(f'Renommage de la saison {self.season} de {self.name}')
            self.generate_lists()
            self.rename.generate_season_name(self.season, self.name)



    def generate_list_seasons(self):
        self.seasons = []
        self.files = os.listdir('.')
        self.logger.debug(self.files)
        for file in self.files:
            if os.path.isdir(file):
                if file not in self.ignore:
                    self.logger.debug(f'Trouvé saison : {file}')
                    self.seasons.append(file)
                else:
                    self.logger.info(f'Repertoire {file} ignoré')
            else:
                self.logger.debug(f'{file} n\'est pas un repertoire')



    def walk_in_seasons(self):
        for num, season in enumerate(self.seasons):
            self.logger.debug(f'num : {num+1}, nom : {season}')
            try:
                os.chdir(season)
                self.logger.debug(f'Dossier changé pour : {season}')
            except:
                self.logger.critical(f'Error 2. \"{season}\" is not a repository or does not exist')
                exit(2)
            self.season = (num+1)
            self.generate_lists()
            self.rename.generate_season_name((num+1), self.name)
            try:
                os.chdir('..')
                self.logger.debug(f'Retour au repertoire parent')
            except:
                self.logger.critical(f'Error 3. Echec du retour au repertoire parent')
                exit(3)
        self.rename.rename_parent_rep(self.name)


    def generate_lists(self):
        self.episodes = []
        self.subs = []
        self.files = os.listdir('.')
        self.logger.debug(self.files)
        for file in self.files:
            if os.path.isdir(file):
                self.logger.debug(f'{file} est un repertoire, ignore')
            else:
                pass
            split_name = file.split('.')
            if split_name[-1] in self.exts:
                self.episodes.append(file)
            elif split_name[-1] == 'srt':
                self.subs.append(file)
        if len(self.episodes) > 0:
            self.rename.generate_names_episodes(self.name, self.season, self.episodes)
        if len(self.subs) > 0:
            self.rename.generate_names_subtitles(self.name, self.season, self.subs)


