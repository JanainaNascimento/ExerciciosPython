''' abrir e reproduzir um audio de arquivo mp3 '''

from pygame import mixer
mixer.init() #inicia o pygame
mixer.music.load('ex 019.mp3')
mixer.music.play() #toca a musica
x = input('Digite algo para parar a música...')



