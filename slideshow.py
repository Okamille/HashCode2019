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
    
    
    def scoring(self, S1, S2):
	    return np.min([len(set(S1.tags) & set(S2.tags)), len(set(S1.tags) - set(S2.tags)), len(set(S2.tags) - set(S1.tags))])

    def score_matrix(self):
        n = len(self.slides)
        matrix = np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                matrix[i,j] = self.scoring(self.slides[i], self.slides[j])
        return matrix