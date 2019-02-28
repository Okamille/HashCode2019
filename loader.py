from image import Image
from slide import Slide

def load_file(path):
    with open(path) as file:
        N = int(file.readline())
        images = [processLine(file.readline(), i) for i in range(N)]
    return images

def processLine(line, index):
    line = line.split(' ')
    type = line[0]
    n_tags = int(line[1])
    tags = [line[2 + i].rstrip('\n') for i in range(n_tags)]
    return Image(tags=tags, type=type, index=index)

def findTag(tag, image_list):
    return [containsTag(image, tag) for image in image_list]

def containsTag(image, tag):
    return tag in image.tags

def load_file_dict(image_list):
    hashtag = dict()
    for image in image_list:
        for tag in image.tags:
            if tag not in hashtag.keys():
                hashtag[tag] = [image]
            else:
                hashtag[tag].append(image)
    return hashtag