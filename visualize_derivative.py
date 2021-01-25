import matplotlib.pyplot as plt, os

k_values = [2**k for k in [1,2,3,4,5]]

frames = [0,112,108,111,111,114,110]
emotions = ['Anger', 'Disgust', 'Happiness', 'Fear', 'Sadness', 'Surprise']

subject = ['F001','M001']
metrics = ['bottleneck', 'wasserstein']

subsections = [
    ('leftEye', 'rightEye', 'leftEyebrow', 'rightEyebrow', 'nose', 'mouth', 'jawline'),
    ('leftEye', 'rightEye', 'leftEyebrow', 'rightEyebrow', 'nose', 'mouth'),
    ('leftEyebrow', 'rightEyebrow', 'nose'),
    ('leftEye', 'rightEye', 'nose'),
    ('nose', 'mouth')
]

j = 0

for i in range(5):
    source_file = f'../Output/{subject[j]}/metric/signal/{metrics[j]}_{"_".join(subsections[j])}_{k_values[i]}.txt'

    with open(source_file, 'r') as file:
        y_vals = [float(d) for d in file.read().splitlines()]

    x_vals = [i for i in range(len(y_vals))]

    for f in range(len(frames)-1):
        plt.clf()
        DOMAIN = range(k_values[i],frames[f+1])
        RANGE = y_vals[frames[f]+k_values[i]:frames[f]+frames[f+1]]
        plt.plot(DOMAIN,RANGE)

        plt.text(0, max(RANGE)+0.05, f'k: {k_values[i]}, emotion: {emotions[f]}', horizontalalignment='left', verticalalignment='top')

        plt.savefig(f'../Images/k{k_values[i]}_{emotions[f]}.png')