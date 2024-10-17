if splat == False:
            key = pygame.key.get_pressed()             
            if key[K_UP] and self.rect.top >= 0:
                self.rect.move_ip(0,-12)
            if key[K_LEFT] and self.rect.left>=LEFT_B:
                self.rect.move_ip(-7,0)
            if key[K_RIGHT] and self.rect.right<=RIGHT_B:
                self.rect.move_ip(7,0) 