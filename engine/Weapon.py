# Ryan Schumacher
# Weapon.py
#
# Class for a weapon object. All weapons belong to units

class Weapon:
    ''' An item that a unit (either the player or an AI unit) uses in combat '''
    def __init__(self, damage, stamUsage, projImage, projOnCollide, projDX, projDY, canvas):
        self.damageScore  = damage
        self.staminaUsage = stamUsage

        self.projectileImage = projImage         # Image of the projectile made
        self.projectileOnCollide = projOnCollide # Projectile collision image

        self.firedList = pygame.sprite.Group()
        self.projDX = projDX
        self.projDY = projDY

        self.screen = canvas

    def fire(x, y, dx, dy):
        self.firedList.add (Projectile (self.projectileImage, 
                                        self.projectileOnCollide, 
                                        self.damageScore, self.projDX, 
                                        self.projDY, self.screen))
                                        
        
