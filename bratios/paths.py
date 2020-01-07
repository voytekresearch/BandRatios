"""Path definitions for the project."""

import os
from os.path import join as pjoin

###################################################################################################
###################################################################################################

class BasePaths():

    def __init__(self, location='../', base_name=None):

        self.location = location
        self.base_name = base_name

        self.base = pjoin(location, base_name)

        # Set first level of paths
        self.demo = pjoin(self.base, 'demo')
        self.literature = pjoin(self.base, 'literature')
        self.sims = pjoin(self.base, 'simulations')
        self.eeg = pjoin(self.base, 'eeg')

        # Set second level of paths
        self.sims_single = pjoin(self.sims, 'single_params')
        self.sims_interacting = pjoin(self.sims, 'interacting_params')

    def get_files(self, directory):

        files = os.listdir(getattr(self, directory))

        # Drop hidden files and sort results
        files = [file for file in files if file[0] != '.']
        files.sort()

        return files

    def list_files(self, directory):

        print('Files in the {} directory:'.format(directory))
        [print('    ', file) for file in self.get_files(directory)];

    @staticmethod
    def make_file_path(file_path, file_name, file_ext=''):

        file_name = file_name + '.' + file_ext if file_ext else file_name
        return pjoin(file_path, file_name)


class DataPaths(BasePaths):

    def __init__(self, location='../', base_name='data'):

        BasePaths.__init__(self, location, base_name)

        # Set custom second level paths
        self.eeg_psds = pjoin(self.eeg, 'psds')
        self.eeg_meta = pjoin(self.eeg, 'metadata')
        self.eeg_outputs = pjoin(self.eeg, 'outputs')


class FigurePaths(BasePaths):

    def __init__(self, location='../', base_name='figures'):

        BasePaths.__init__(self, location, base_name)

        # Set custom second level paths
        self.eeg_corrs = pjoin(self.eeg, 'correlations')
        self.eeg_topos = pjoin(self.eeg, 'topographies')


# Create path objects to import
DATA_PATHS = DataPaths()
FIGS_PATHS = FigurePaths()
