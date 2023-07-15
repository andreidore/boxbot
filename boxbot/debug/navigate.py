import pygame



def main():

    pygame.init()

    display = pygame.display.set_mode((300, 300))

    while True:

        # creating a loop to check events that
        # are occurring
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # checking if keydown event happened or not
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    print("LEFT key pressed")
                elif event.key == pygame.K_RIGHT:
                    print("RIGHT key pressed")
                elif event.key == pygame.K_UP:
                    print("UP key pressed")





if __name__== "__main__":
    main()
