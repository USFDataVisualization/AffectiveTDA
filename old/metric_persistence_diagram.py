from ripser import ripser
from scipy.spatial import distance
import math, numpy as np, os, pandas as pd

subject = 'M001'

subsections = [
    ('leftEye', 'rightEye', 'leftEyebrow', 'rightEyebrow', 'nose', 'mouth', 'jawline'),
    ('leftEye', 'rightEye', 'leftEyebrow', 'rightEyebrow', 'nose', 'mouth'),
    ('leftEyebrow', 'rightEyebrow', 'nose'),
    ('leftEye', 'rightEye', 'nose'),
    ('nose', 'mouth')
]

def min_max(subsection):
    return {
        "leftEye": (0,8),
        "rightEye": (8,16),                                                                                 
        "leftEyebrow": (16,26),
        "rightEyebrow": (26,36),
        "nose": (36,48),
        "mouth": (48,68),
        "jawline": (68,83)
    }.get(subsection)

def getFileNames(d, extension):
    filesindir = []
    for elem in os.listdir(d):
        if os.path.isdir(d + '/' + elem):
            filesindir += getFileNames(d + '/' + elem, extension)
        else:
            if elem[elem.find('.'):] == extension:
                filesindir.append(d + '/' + elem)
    return filesindir

def generate_dissimilarity_matrix(filename, section_list):
    df = pd.read_csv(filename, sep=' ', header=None, usecols=[1,2,3])
    df = list([tuple(l) for l in df.to_records(index=False)])

    indices = [min_max(subsection) for subsection in section_list]
    data = [t for e in indices for t in df[e[0]:e[1]]]

    mat = [[distance.euclidean(d,e)/distance.euclidean(df[36],df[47]) for d in data] for e in data]

    return np.asarray(mat)

if __name__ == '__main__':
    data_source = '../Data/' + subject
    data_destination = '../Output/' + subject + '/metric/persistence'
    files = getFileNames(data_source, '.bnd')

    for filename in files:
        for section_list in subsections:
            diagrams = ripser(generate_dissimilarity_matrix(filename, section_list), distance_matrix=True)['dgms']

            h0 = '{}/h0/{}/pd_{}_{}.txt'.format(
                data_destination,
                '_'.join(section_list),
                filename.split('/')[-2],
                filename.split('/')[-1].split('.')[0]
            )

            h1 = '{}/h1/{}/pd_{}_{}.txt'.format(
                data_destination,
                '_'.join(section_list),
                filename.split('/')[-2],
                filename.split('/')[-1].split('.')[0]
            )

            print(h0)
            print(h1)

            with open(h0, 'w') as file:
                for feature in diagrams[0]:
                    file.write(' '.join([str(f) for f in feature]))
                    file.write('\n')
            
            with open(h1, 'w') as file:
                for feature in diagrams[1]:
                    file.write(' '.join([str(f) for f in feature]))
                    file.write('\n')
            


    