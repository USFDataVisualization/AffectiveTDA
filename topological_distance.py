import subprocess

emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise']
distances = ['/home/hamza/AffectiveTDA2/hera/bottleneck/bottleneck_dist', '/home/hamza/AffectiveTDA2/hera/wasserstein/wasserstein_dist']

subsections = [
    ('leftEye', 'rightEye', 'leftEyebrow', 'rightEyebrow', 'nose', 'mouth', 'jawline'),
    ('leftEye', 'rightEye', 'leftEyebrow', 'rightEyebrow', 'nose', 'mouth'),
    ('leftEyebrow', 'rightEyebrow', 'nose'),
    ('leftEye', 'rightEye', 'nose'),
    ('nose', 'mouth')
]

if __name__ == '__main__':
    for distance in distances[1:]:
        for emotion in emotions:
            for i in range(len(subsections)):
                print('{} ../Output/ {} {}'.format(distance,emotion,i))
                p = subprocess.Popen(
                    '{} ../Output/ {} {}'.format(distance,emotion,i), 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE, 
                    shell=True)

                std_out, std_err = p.communicate()
                std_out = std_out.decode('ascii')
                std_out = std_out.split('\n')[:-1]

                outfile = '../Output/F002/nonmetric/signal/{}_{}_{}.txt'.format(
                    distance.split('/')[-2], 
                    '_'.join(subsections[i]), emotion)

                print(outfile)

                with open(outfile, 'w') as file:
                    for line in std_out:
                        file.write(line + '\n')
