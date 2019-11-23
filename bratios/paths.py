"""Path definitions for the project."""

from os.path import join as pjoin

###################################################################################################
###################################################################################################

class BasePaths():

    def __init__(self, location='../', base_name=None):

        self.location = location
        self.base_name = base_name

        self.base = pjoin(location, base_name)

        # Set first level of paths
        self.sims = pjoin(self.base, 'simulations')
        self.eeg = pjoin(self.base, 'eeg')
        self.literature = pjoin(self.base, 'literature')

        # Set second level of paths
        self.sims_single = pjoin(self.sims, 'single_params')
        self.sims_interacting = pjoin(self.sims, 'interacting_params')

    @staticmethod
    def make_file_path(file_path, file_name):
        return pjoin(file_path, file_name)


class DataPaths(BasePaths):

    def __init__(self, location='../', base_name='data'):

        BasePaths.__init__(self, location, base_name)

        # Set custom second level paths
        self.eeg_psds = pjoin(self.eeg, 'psds')
        self.eeg_meta = pjoin(self.eeg, 'metadata')
        self.eeg_outputs = pjoin(self.eeg, 'outputs')


class FigurePaths():

    def __init__(self, location='../', base_name='figures'):

        BasePaths.__init__(self, location, base_name)

        # Set custom first level paths
        self.overview = pjoin(self.base, 'overview')

        # Set custom second level paths
        self.eeg_corrs = pjoin(self.eeg, 'correlations')
        self.eeg_topos = pjoin(self.eeg, 'topographies')


# Create path objects to import
DATA_PATHS = DataPaths()
FIGS_PATHS = FigurePaths()
