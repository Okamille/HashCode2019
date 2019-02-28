class Slide:
    def __init__(self, images):
        if(type(images) == list):
            if(images[0].type == 'H' or images[1].type == 'H'):
                raise ValueError
            self.type = 'V'
        else:
            if(images.type == 'V'):
                raise ValueError
            self.type = 'H'
        self.images = images
        self.tags = self.getTags()
    
    def getTags(self):
        if(self.type == 'H'):
            return self.images.tags
        else:
            tag1 = self.images[0].tags
            tag2 = self.images[1].tags
            return list(set(tag1 + tag2))

            