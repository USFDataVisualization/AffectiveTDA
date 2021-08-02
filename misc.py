import os

subsections = [
    ('leftEye', 'rightEye', 'leftEyebrow', 'rightEyebrow', 'nose', 'mouth', 'jawline'),
    ('leftEye', 'rightEye', 'leftEyebrow', 'rightEyebrow', 'nose', 'mouth'),
    ('leftEyebrow', 'rightEyebrow', 'nose'),
    ('leftEye', 'rightEye', 'nose'),
    ('nose', 'mouth')
]

def min_max(subsection, metric_or_nonmetric):
    if metric_or_nonmetric == 'metric':
        ret = {
            "leftEye": (0,8),
            "rightEye": (8,16),                                                                                 
            "leftEyebrow": (16,26),
            "rightEyebrow": (26,36),
            "nose": (36,48),
            "mouth": (48,68),
            "jawline": (68,83)
        }
    else:
        ret = {
            "leftEye": [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,0)],
            "rightEye": [(8,9),(9,10),(10,11),(11,12),(12,13),(13,14),(14,15),(15,0)],                                                                                 
            "leftEyebrow": [(16,17),(17,18),(18,19),(19,20),(20,21),(21,22),(22,23),(23,24),(24,25),(25,0)],
            "rightEyebrow": [(26,27),(27,28),(28,29),(29,30),(30,31),(31,32),(32,33),(33,34),(34,35),(35,0)],
            "nose": [(36,37),(37,38),(38,39),(39,40),(40,41),(41,42),(42,43),(43,44),(44,45),(45,46),(46,47)],
            "mouth": [(48,49),(49,50),(50,51),(51,52),(52,53),(53,54),(54,55),(55,56),(56,57),(57,58),(58,59),(59,0),(60,61),(61,62),(62,63),(63,64),(64,65),(65,66),(66,67),(67,0)],
            "jawline": [(67,68),(69,70),(70,71),(71,72),(72,73),(73,74),(74,75),(75,76),(76,77),(77,78),(78,79),(79,80),(80,81),(81,82)]
        }

    return ret.get(subsection)

def getFileNames(d, extension):
    filesindir = []
    for elem in os.listdir(d):
        if os.path.isdir(d + '/' + elem):
            filesindir += getFileNames(d + '/' + elem, extension)
        else:
            if elem[elem.find('.'):] == extension:
                filesindir.append(d + '/' + elem)
    return filesindir