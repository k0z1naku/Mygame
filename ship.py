class Ship:
    def __init__(self, coords, paths, steering):
        self.__paths = paths
        self.__coords = np.array(coords, dtype=float)
        self.__angle = -90
        self.__steer = Steering(steering)
        self.__spd = np.array([0, 0], dtype=float)
        self.__image = Image(self.__paths[0])
        self.__heatrad = 0
        self.__lastrocket = pygame.time.get_ticks()
        self.__lastbullet = pygame.time.get_ticks()

    '''
    def __normSpd(self):
        if (vec_len(self.__spd) >=  MAX_SPD):
            self.__spd = self.__spd / vec_len(self.__spd) * MAX_SPD
'''
    def changespd(self):
        '''this function is for changing ship's velocity according to player's actions'''
        keystatus = pygame.key.get_pressed()
        if keystatus[self.__steer.left]:
            #decrease coord if player spinning conterclockwise
            self.__spd = ed_vec(180) * MAX_SPD
        if keystatus[self.__steer.right]:
            #increase coord if player spinning clockwise
            self.__spd = MAX_SPD * ed_vec(0)
        if not keystatus[self.__steer.left] and not keystatus[self.__steer.right]:
            self.__spd = ed_vec(999) * 0
        '''self.__force = ed_vec(self.__angle) * FORCE
        self.__spd += self.__force / self.__MASS * TIME_PERIOD'''
        '''self.__normSpd()'''

    def move(self, scale):
        self.__coords += self.__spd * TIME_PERIOD
        self.__image.draw(-self.__angle - 90, self.__coords, scale)

    def shoot(self, bullets):
        now = pygame.time.get_ticks()
        if now - self.__lastbullet >= BULLETCD:
            self.__lastbullet = now
            if pygame.key.get_pressed()[self.__steer.shoot]:
                bulCoords = self.get_coord() * 1
                bullets.append(Bullet(bulCoords, self.__angle, BULLETIMG[1]))



    def rocket(self, rockets):
        now = pygame.time.get_ticks()
        if now - self.__lastrocket >= ROCKETCD:
            self.__lastrocket = now
            bulCoords1 = self.get_coord() - np.array([28, -17])
            bulCoords2 = self.get_coord() + np.array([28, 17])
            rockets.append(Bullet(bulCoords1, self.__angle, BULLETIMG[0]))
            rockets.append(Bullet(bulCoords2, self.__angle, BULLETIMG[0]))


    def get_spd(self):
        return self.__spd

    def get_coord(self):
        return self.__coords

    def get_rad(self):
        return self.__heatrad

    def set_spd(self, spd):
        self.__spd = spd

    def get_steer(self):
        return self.__steer
