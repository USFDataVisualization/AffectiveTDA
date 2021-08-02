import matplotlib.pyplot as plt, os
from sklearn.manifold import TSNE, MDS

metrics = ['bottleneck', 'wasserstein']

emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise']

subsections = [
    ('leftEye', 'rightEye', 'leftEyebrow', 'rightEyebrow', 'nose', 'mouth', 'jawline'),
    ('leftEye', 'rightEye', 'leftEyebrow', 'rightEyebrow', 'nose', 'mouth'),
    ('leftEyebrow', 'rightEyebrow', 'nose'),
    ('leftEye', 'rightEye', 'nose'),
    ('nose', 'mouth')
]

for metric in metrics:
    for subset in subsections:
        fig = plt.figure()
        axis = fig.add_subplot(111)
        for i in range(1,11):
            subject = "F{0:0=3d}".format(i)
            filepath = f'../Output/{subject}/nonmetric/signal/{metric}_{"_".join(subset)}.txt'

            emotion_indices = [0] + [max(map(lambda l: int(l[:-4]), os.listdir(f'../Data/{subject}/{emotion}')))+1 for emotion in emotions]

            emotion_indices = [sum(emotion_indices[:i]) for i in range(1,len(emotion_indices)+1)]

            with open(filepath, 'r') as file:
                lines = [[float(l) for l in line.split(' ')] for line in file.readlines()]

            reduced_data = MDS(dissimilarity='precomputed', random_state=0).fit_transform(lines)[:emotion_indices[1]] #TSNE(metric='precomputed').fit_transform(lines)[:emotion_indices[1]]
            reduced_data = list(map(tuple, reduced_data))

            data1, data2 = zip(*reduced_data)



            axis.scatter(data1, data2)
        plt.savefig('png.png')
            
            #print(emotion_indices)
        break
    break