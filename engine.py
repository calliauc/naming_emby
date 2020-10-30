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
            self.logger.info(f'Dossier changé pour : {self.rep}')
        except:
            self.logger.critical(f'Wesh tufékoi avec {self.rep}?')

        self.files = []
        self.episodes = []
        self.subs = []



    def run(self):
        self.find_files()



    def find_files(self):
        self.files = os.listdir('.')
        self.logger.info(self.files)
        for file in self.files:
            if os.path.isdir(file):
                self.logger.debug(f'{file} est un repertoire')
            else:
                self.logger.debug(f'{file} n\'est pas un repertoire')
            split_name = file.split('.')
            if split_name[-1] in self.exts:
                self.episodes.append(file)
            elif split_name[-1] == 'srt':
                self.subs.append(file)
        if len(self.episodes) > 0:
            self.rename.rename_episodes(self.name, self.season, self.episodes)
        if len(self.subs) > 0:
            self.rename.rename_subtitle(self.name, self.season, self.subs)


