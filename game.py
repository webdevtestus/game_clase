"""
game.py 
"""
import sys
import pygame

# generamos la Clase principal; Game
class Game:
    # defino el metodo init que pintara nuestra ventana principal
    def __init__(self):
        pygame.init()
        
        # almacenamos la superficie en un ATRIBUTO surface
        self.surface = pygame.display.set_mode = ( (1400, 600) )
        
        # le ponemos titulo a la ventana
        pygame.display.set_caption('Alien warfare')
        
        print ("anda?")
        
        # creo el ATRIBUTO running=True para saber si el programa esta corriendo
        self.running = True
        
               
    
    # defino los metodos que voy a necesitar
    def start(self):
        # ejecutamos el metodo new
        self.new()
    
    def new(self):
        # ejecutara el metodo run
        self.run()
    
    def run(self):
        # evaluamos el metodo running y ejecutamos metodos necesarios
        while self.running:
            self.events()
            self.draw()
            self.update()
            
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
                
    
    def draw(self):
        pass
    
    def update(self):
        # usaremos el metodo FLIP en vez de UPDATE
        pygame.display.flip() # refresca TODA la superficie
    
    def stop(self):
        pass
    
    
        