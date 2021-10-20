from firefly import tess
from multiprocessing import Pool
from subprocess import run
import numpy as np
from pandas import read_csv
import signal


class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)
        
        
def main(exoplanet):
    # Kill process in 5 days
    max_runtime = 60 * 60 * 24 * 6
    with timeout(seconds=max_runtime):
        print(f'Executing firefly on {exoplanet}')
        run(['python', 'main.py', f'{exoplanet}'])
        print(f'Finished {exoplanet}')

# Set how many targets to run in parallel
processes = 10
# Define various lists to pass
# targets, all_targets, ttv_targets = tess(archive='nasa', survey=None)
all_targets = \
    read_csv('nasa_tess_viable.csv') \
             .sort_values('Epochs', ascending=False)['Exoplanet'].tolist()
# all_targets = [
#     'wasp100b', 'wasp126b', 'lhs1815b', 'kepler42c', 'wasp119b',
#     'wasp18b', 'hip65ab', 'l9859b', 'gj1252b', 'wasp62b',
#     'toi157b',
# ]
#spear = read_csv('firefly/data/spear.csv')['pl_name'] .values
#nasa = read_csv('nasa_tess_viable.csv')['Exoplanet'] .values
#diff = np.setdiff1d(nasa, spear)
#print(len(diff))
# Redefine list to use here
exoplanet = all_targets
if __name__ == '__main__':
    with Pool(processes=processes) as pool:
        pool.map(main, exoplanet, chunksize=1)
