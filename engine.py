import os

import rename


class Engine:
    def __init__(self, args, logger):
        self.rename = rename.Rename(args, logger)
        self.logger = logger
        self.rep = args.rep
        self.logger.debug(args)
        self.season = args.season
        self.name = args.name
        self.exts = ['mkv', 'avi', 'mp4']

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
        if self.season == '0':
            self.generate_list_seasons()
            self.walk_in_seasons()
                

    def generate_list_seasons(self):
        self.files = os.listdir('.')
        self.logger.debug(self.files)
        for file in self.files:
            if os.path.isdir(file):
                self.logger.debug(f'Trouvé saison : {file}')
                self.seasons.append(file)
            else:
                self.logger.debug(f'{file} n\'est pas un repertoire')
        self.logger.info(f'Liste des saisons : {self.seasons}')


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


