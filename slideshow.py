class Slideshow:
    def __init__(self, slides):
        self.slides = slides
    
    def exportToFile(self, filename):
        with open(filename, 'w+') as file:
            file.write(str(len(self.slides)) + '\n')
            for slide in self.slides:
                if(slide.type == 'H'):
                    file.write(str(slide.images.index) + '\n')
                else:
                    file.write(str(slide.images[0].index) + ' ' + str(slide.images[1].index) + '\n')
        print('Export completed')