import pygame 
def main():
    class Button:
        def __init__(self, x, y, x1, y1, x2, y2 , pl , st , nt  ,ls):
            self.imgDefault = pause_img
            self.imgPause = play_img
            self.img = self.imgDefault
            self.rect = self.img.get_rect()
            self.rect1 = next_img.get_rect()
            self.rect2 = previous_img.get_rect()
            self.rect.topleft = (x, y)
            self.rect1.topleft = (x1, y1)
            self.rect2.topleft = (x2, y2)
            self.clicked = False
            self.paused = True
            self.next_bool = False
            self.prev_bool = False
            self.play = pl
            self.stop = st
            self.next = nt
            self.last = ls
            self.paused_time = 0

        def draw(self):
            pos = pygame.mouse.get_pos()
            pressed = pygame.key.get_pressed()
            right = pressed[pygame.K_RIGHT]
            left = pressed[pygame.K_LEFT]
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] and not self.clicked:
                    self.clicked = True
                    self.paused = not self.paused
                    self.play()
                    if self.paused:
                        if pygame.mixer.music.get_busy():
                            self.stop()
                            self.img = self.imgPause
                        # self.paused.time = pygame.mixer.get_pose()
                        
                    else:
                        pygame.mixer.music.unpause()
                        self.img = self.imgDefault

                    
            elif not pygame.mouse.get_pressed()[0]:
                self.clicked = False
            
            if right and not self.next_bool:
                
                self.next_bool = True
                self.next()
            if not right:
                self.next_bool = False
                
            if left and not self.prev_bool:
                self.prev_bool = True
                self.last()
            if not left:
                self.prev_bool = False


            

            screen.blit(self.img, (self.rect.x, self.rect.y))
            screen.blit(next_img, (self.rect1.x, self.rect1.y))
            screen.blit(previous_img, (self.rect2.x, self.rect2.y))

    def music_play():
        global _currently_playing_song
        _currently_playing_song = _songs[0]
        pygame.mixer.music.load(_currently_playing_song)
        pygame.mixer.music.play()
    
    def stop_play():
        pygame.mixer.music.pause()
    
    def next_track():
        global _currently_playing_song, _songs
        current_index = _songs.index(_currently_playing_song)
        next_index = (current_index + 1) % len(_songs) # wrap around to start if at end
        _currently_playing_song = _songs[next_index]
        pygame.mixer.music.load(_currently_playing_song)
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.set_pos(pygame.mixer.music.get_pos())
        pygame.mixer.music.play()

    def previous_track():
        global _currently_playing_song, _songs
        current_index = _songs.index(_currently_playing_song)
        last_index = (current_index - 1) % len(_songs)
        _currently_playing_song = _songs[last_index]
        pygame.mixer.music.load(_currently_playing_song)
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.set_pos(pygame.mixer.music.get_pos())
        pygame.mixer.music.play()

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((400 , 700))
    done = False
    clock = pygame.time.Clock()
    FPS = 30
    colour_red = (255 , 0 , 0) 
    screen.fill((32 , 178 , 170))
    
    play_img = pygame.image.load("play.png")
    next_img = pygame.image.load("next-track.png")
    previous_img = pygame.image.load("previous-track.png")
    pause_img = pygame.image.load('pause-button.png')
    play_img = pygame.transform.scale(play_img , (100 ,100)) # size
    next_img = pygame.transform.scale(next_img , (170 ,170))
    previous_img = pygame.transform.scale(previous_img , (170 ,170))
    pause_img = pygame.transform.scale(pause_img , (100 ,100))
    B = Button(150 ,500 , 240,460 , 0,460 , music_play , stop_play , next_track ,previous_track )
    global _songs
    _songs = ['seya.mp3' , 'ria.mp3' , 'chan.mp3']
    while not done :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        right = pressed[pygame.K_RIGHT]
        left = pressed[pygame.K_LEFT]    
        B.draw()
        
        pygame.display.flip()
        clock.tick(FPS)
    pygame.mixer.music.stop()
    pygame.quit()


if __name__ == '__main__': 
    main()


 