from image import Image

def load_file(path):
    with open(path) as file:
        N = int(file.readline())
        images = [processLine(file.readline()) for i in range(N)]
    return images

def processLine(line):
    line = line.split(' ')
    orientation = line[0]
    n_tags = int(line[1])
    tags = [line[2 + i] for i in range(n_tags)]
    return Image(tags=tags, orientation=orientation)
