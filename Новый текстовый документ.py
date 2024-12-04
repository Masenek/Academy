from PTL import ImageGrab , ImageOps 
import payutogi
from numy import*

class DinoBot:
    def_init_(self, replaybtn):
        self.replaybtn = replaybtn
    
    def restartgame(self):
        pyautogi.click(self.repalybtn)
        
    def jump(self):
        payutogi.keyDown('space')
        time.sleep(0.05)
        payutogi.keyUp('space')
    def grabimage(self):
        box = (self.dino[0] + 35, self.dino[1], self.dino[0] + 75, self.dino[1] + 30)
        image = ImageGrab.grab(box)
        greyImage = ImageOps.grayscale(image)
        a = array(greyImage.getcolors())
        return a.sum()
        
    def start(self):
        self.restartgame()
        while True:
            if self.grabimage() ! = 1447:
                self.jump()
        
def main():
    bot = DinoBot((270,405),(139,410))
    bot.start()
