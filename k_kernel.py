import os

k_values = [2**k for k in [1,2,3,4,5]]

subjects = ['F001','M001']

subsections = [
    ('leftEye', 'rightEye', 'leftEyebrow', 'rightEyebrow', 'nose', 'mouth', 'jawline'),
    ('leftEye', 'rightEye', 'leftEyebrow', 'rightEyebrow', 'nose', 'mouth'),
    ('leftEyebrow', 'rightEyebrow', 'nose'),
    ('leftEye', 'rightEye', 'nose'),
    ('nose', 'mouth')
]

bottleneck_path = '../hera/bottleneck/bottleneck_dist'
wasserstein_path = '../hera/wasserstein/wasserstein_dist'

for subject in subjects:
    for subsection in subsections:
        for k in k_values:
            h0_filepath = f'../Output/{subject}/metric/persistence/h0/{"_".join(subsection)}/'
            h1_filepath = f'../Output/{subject}/metric/persistence/h1/{"_".join(subsection)}/'

            bottleneck_output_filepath = f'../Output/{subject}/metric/signal/bottleneck_{"_".join(subsection)}_{k}.txt'
            wasserstein_output_filepath = f'../Output/{subject}/metric/signal/wasserstein_{"_".join(subsection)}_{k}.txt'

            h0_bottleneck_frames = os.popen(f'{bottleneck_path} {h0_filepath} {k}').read().split(' ')[:-1]
            h1_bottleneck_frames = os.popen(f'{bottleneck_path} {h1_filepath} {k}').read().split(' ')[:-1]
            h0_wasserstein_frames = os.popen(f'{wasserstein_path} {h0_filepath} {k}').read().split(' ')[:-1]
            h1_wasserstein_frames = os.popen(f'{wasserstein_path} {h1_filepath} {k}').read().split(' ')[:-1]
            
            number_of_frames = len(h0_bottleneck_frames)

            bottleneck_frames = []
            wasserstein_frames = []

            for i in range(number_of_frames):
                bottleneck_frames.append(str(max([float(h0_bottleneck_frames[i]),float(h1_bottleneck_frames[i])])))
                wasserstein_frames.append(str(sum([float(h0_wasserstein_frames[i]),float(h1_wasserstein_frames[i])])))

            with open(bottleneck_output_filepath, 'w') as file:
                file.write('\n'.join(bottleneck_frames))
            with open(wasserstein_output_filepath, 'w') as file:
                file.write('\n'.join(wasserstein_frames))