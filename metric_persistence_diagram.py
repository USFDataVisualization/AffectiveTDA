from ripser import ripser
from scipy.spatial import distance
from misc import subsections, min_max, getFileNames
import math, numpy as np, pandas as pd, syss

# This function generates the standard Euclidean dissimilarity matrix for a set of 83 landmark points 
# (this has only been tested on BU4DFE dataset)
# Parameters: filename (location of file containing the 83 landmark points [3D points, each dimension separated by ' '])
#             section_list (list of subsections of the face [e.g. leftEye, rightEye, leftEyebrow, rightEyebrow, nose, mouth, jawline])
def generate_dissimilarity_matrix(filename, section_list):
    # read in the data with pandas and ignore the first column (the BU4DFE dataset has four comma-separated values (index, x, y, z))
    df = pd.read_csv(filename, sep=' ', header=None, usecols=[1,2,3])
    # convert dataframe into a list of tuples
    df = list([tuple(l) for l in df.to_records(index=False)])

    # get the indices of the subsections we are interested in (for example, the indices for leftEye are 0 through 7)
    indices = [min_max(subsection, 'metric') for subsection in section_list]
    # get the corresponding values from the data frame for these indices
    data = [t for e in indices for t in df[e[0]:e[1]]]

    # build the dissimilarity matrix by calculating pairwise Euclidean distance for the values in the data array
    mat = [[distance.euclidean(d,e)/distance.euclidean(df[36],df[47]) for d in data] for e in data]

    # return the matrix as a numpy array
    return np.asarray(mat)

# Usage: python metric_persistence_diagram.py <subject-id>
if __name__ == '__main__':
    # if no command-line arguments are passed, end the program
    if len(sys.argv) < 2:
        sys.exit()
    subject = sys.argv[1]
    # Data folder in previous directory should contain the dataset
    data_source = '../Data/' + subject
    data_destination = '../Output/' + subject + '/metric/persistence'
    # all files in the data directory ending with .bnd
    files = getFileNames(data_source, '.bnd')

    # for each file
    for filename in files:
        # and each possible list of subsections
        for section_list in subsections:
            # generate the metric persistence diagram and run the output through ripser (ripser returns the persistent homology)
            diagrams = ripser(generate_dissimilarity_matrix(filename, section_list), distance_matrix=True)['dgms']

            # output file location for the h0 features
            h0 = '{}/h0/{}/pd_{}_{}.txt'.format(
                data_destination,
                '_'.join(section_list),
                filename.split('/')[-2],
                filename.split('/')[-1].split('.')[0]
            )

            # output file location for the h1 features
            h1 = '{}/h1/{}/pd_{}_{}.txt'.format(
                data_destination,
                '_'.join(section_list),
                filename.split('/')[-2],
                filename.split('/')[-1].split('.')[0]
            )

            print(h0)
            print(h1)

            # save the h0 features
            with open(h0, 'w') as file:
                for feature in diagrams[0]:
                    file.write(' '.join([str(f) for f in feature]))
                    file.write('\n')
            
            # save the h1 features
            with open(h1, 'w') as file:
                for feature in diagrams[1]:
                    file.write(' '.join([str(f) for f in feature]))
                    file.write('\n')
            


    