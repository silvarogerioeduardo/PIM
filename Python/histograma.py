import numpy as np
import scipy.misc
import matplotlib.pyplot as plt

path = "imagens/"
imagem = scipy.misc.imread(path+"lena.jpg")

# gera o histograma e seus intervalos
histograma, intervalos = np.histogram(imagem,bins=np.arange(0,256))

# determina o valor do centro dos intervalos
center = (intervalos[:-1] + intervalos[1:])/2

# exibe o histograma
plt.bar(center, histograma, align='center')
plt.show()
