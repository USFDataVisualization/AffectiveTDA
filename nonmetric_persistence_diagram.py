from ripser import ripser
from scipy.spatial import distance
from misc import subsections, min_max, getFileNames
import math, numpy as np, pandas as pd, geom

subjects = ['']#['F001', 'M001']
nose_bridge_1 = 36
nose_bridge_2 = 47

def generate_dissimilarity_matrix(filename, section_list):
    data = pd.read_csv(filename, sep=' ', header=None, usecols=[1,2,3]).values.tolist()

    norm = distance.euclidean(list(data[nose_bridge_1]), list(data[nose_bridge_2]))
    data = [np.asarray([data[x] for x in e]) for s in section_list for e in min_max(s, 'nonmetric')]

    return np.asarray([[geom.seg_seg_distance(a[0],a[1],b[0],b[1])/norm for b in data] for a in data])

if __name__ == '__main__':
    for i in range(1,44):
        subject = "M{0:0=3d}".format(i)
        data_source = '../Data/' + subject 
        data_destination = f'../Output/{subject}/nonmetric/persistence'

        files = getFileNames(data_source, '.bnd')

        for filename in files:
            for section_list in subsections:
                diagrams = ripser(generate_dissimilarity_matrix(filename, section_list),distance_matrix=True)['dgms']

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

                print(f'pd_{filename.split("/")[-2]}_{filename.split("/")[-1].split(".")[0]}.txt')

                with open(h0, 'w') as file:
                    for feature in diagrams[0]:
                        file.write(' '.join([str(f) for f in feature]))
                        file.write('\n')
                
                with open(h1, 'w') as file:
                    for feature in diagrams[1]:
                        file.write(' '.join([str(f) for f in feature]))
                        file.write('\n')