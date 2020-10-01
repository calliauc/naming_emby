import os

class Rename:
    def __init__(self, args, logger):
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

        self.files = os.listdir('.')
        self.episodes = []
        self.sub = []

    def run(self):
        self.scan_rep()

    def scan_rep(self):
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
                self.sub.append(file)
        if len(self.episodes) > 0:
            self.rename_episodes()
        if len(self.sub) > 0:
            self.rename_subtitle()



    def rename_file(self, Name, newName):
        try:
            self.logger.info(f'Renaming : {Name}')
            os.rename(Name, newName)
            self.logger.info(f'Succes -> {newName}')
        except:
            self.logger.warning(f'Failed to rename {Name}')

    def rename_episodes(self):
        self.logger.info(self.episodes)
        nEp = 0
        for file in self.episodes:
            nEp += 1
            ext = file.split('.')[-1]
            newName = f'{self.name}_s{str(self.season)}e{str(nEp)}.{ext}'
            self.rename_file(file, newName)

    def rename_subtitle(self):
        self.logger.info(self.sub)
        nSb = 0
        for file in self.sub:
            nSb += 1
            ext = file.split('.')[-1]
            newSub = f'{self.name}_s{str(self.season)}e{str(nSb)}.{ext}'
            self.rename_file(file, newSub)
