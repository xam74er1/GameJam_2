import pygame


def main():
    screen = pygame.display.set_mode((640, 480))


    font = pygame.font.Font("Font/JELLYBELLY.TTF", 40)
    input_box = pygame.Rect(100, 100, 140, 32)
    color = pygame.Color('white')
    text = ''
    done = False
    score = 25

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # ecrire dans un fichier
                    fichier = open("Score.txt", "a")
                    fichier.write(str(score)+"|"+str(text)+"|"+"\n")
                    fichier.close()
                    done = True

                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        screen.fill((30, 30, 30))

        # Render the current text.
        txt_surface = font.render(text, True, color)

        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width

        # ecrie le nom que l'on tape
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()