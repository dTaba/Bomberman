import pygame
import game
import background

CONTROLES = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}


class GameEngine():
    def __init__(self):
        self.dimensions = [925, 555]
        self.game = game.Game()

        self.background = background.Background(self.dimensions, self.game)
        self.loadImages()

        # Creo obstaculos para despues en reload background dibujarlos y alli setear el rect de cada uno
        self.game.createObstacles(self.dimensions)
        self.game.placeEnemies()
        self.background.reloadEnemyRect()
        self.background.reloadBackground(self.dimensions)
        self.game.createRects()

        self.mainLoop()

    def esc():
        pass

    def goMenu():
        pass

    def goOption():
        pass

    def exit():
        pass

    def loadImages(self):
        self.background.loadBombermanImage('sprites/Bomberman.png', (37, 37))  # Lo pone al principio del mapa
        self.background.loadObstacle("sprites/pilar.png")
        self.background.loadImagenMenu("sprites/fondoBombmanMenu.jpeg")
        self.background.loadStartMenu("sprites/pressStart.png")
        self.background.loadEnemigoBomberman("sprites/enemigoBomberman.png")

    def mainLoop(self):
        menu = True
        clock = pygame.time.Clock()
        while True:
            while menu:
                print("Entro al loopeano")
                self.background.reloadMenu()
                clock.tick(30)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                    if event.type == pygame.KEYDOWN:
                        print("SAlgo del loopeano")
                        menu = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.background.fillBlack()

                    self.game.givePosition((CONTROLES[str(event.key)]), self.background.screen)
                    self.background.reloadBombermanRect()
                    
                    self.background.reloadBackground(self.dimensions)

                    playerrect = self.game.getPlayerRect()

                    #print(len(self.game.lalistaderects))

                    #print(playerrect.collidelistall(self.game.getListaDeRects()))

                    if len(playerrect.collidelistall(self.game.getListaDeRects())) > 0:
                        self.game.setBombermanPosition()

                    self.background.reloadBomberman()
                    enemyrect = self.game.getEnemyRect()

                    self.game.moverEnemigo(self.game.getdireccionenemigo())
                    print(enemyrect)
                    for i in range(0, len(enemyrect)):
                        if len(enemyrect[i].collidelistall(self.game.getListaDeRects())) > 0:
                            self.game.setdireccionenemigo(self.game.getdireccionenemigo()*-1)
                            self.game.moverEnemigo(self.game.getdireccionenemigo()) 
                            print("ENTRO AL LOOP EPICO")
                    print(len(enemyrect[i].collidelistall(self.game.getListaDeRects())))
                    self.background.reloadEnemy()
                    self.background.reloadEnemyRect()
                pygame.display.flip()
                clock.tick(30)

if __name__ == "__main__":
    controlador = GameEngine()
