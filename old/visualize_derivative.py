import matplotlib.pyplot as plt, os, pandas as pd

k_values = [2**k for k in [1,2,3,4,5]]
color = [
    '#a6cee3',
    '#1f78b4',
    '#b2df8a',
    '#33a02c',
    '#fb9a99',
    '#e31a1c'
    ]

frames = [0,112,108,111,111,114,110]
emotions = ['Anger', 'Disgust', 'Happiness', 'Fear', 'Sadness', 'Surprise']
e = ['angry', 'disgust', 'happy', 'fear', 'sad', 'surprise']

cols = [
    [7,10,11,16,21],
    [7,10,19,21],
    [5,6,10,14,19,21],
    [9,10,13,17,19,21],
    [10,14,16,21],
    [5,6,10,14,19,21],
]

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

for f in range(len(frames)-1):
    plt.clf()
    fig, (ax1,ax2) = plt.subplots(2)
    for i in range(5):
        source_file = f'../Output/{subject[j]}/metric/signal/{metrics[j]}_{"_".join(subsections[j])}_{k_values[i]}.txt'

        
        plt.subplots_adjust(wspace=0.4, hspace=0.4)

        with open(source_file, 'r') as file:
            y_vals = [float(d) for d in file.read().splitlines()]

        x_vals = [i for i in range(len(y_vals))]

        DOMAIN = range(k_values[i],frames[f+1])
        RANGE = y_vals[sum(frames[:f+1])+k_values[i]:sum(frames[:f+2])]
        ax1.plot(DOMAIN,RANGE,color=color[i],label=f'k: {k_values[i]}')
    
        ax1.set_title('Topology')
        lgd = ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        #ax1.text(0, max(RANGE)+0.05, f'Emotion: {emotions[f]}', horizontalalignment='left', verticalalignment='top')

    df = pd.read_csv(f'../AUData/{subject[j]}_{e[f]}_tex.csv', usecols=cols[f])

    ax2.set_title('Action Units')

    df.plot(ax=ax2)
    lgd2 = ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.savefig(f'../Images/{emotions[f]}_{"_".join(subsections[j])}.png', bbox_extra_artists=(lgd,lgd2), bbox_inches='tight')
