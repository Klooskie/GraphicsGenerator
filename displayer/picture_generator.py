import pygame


def generate_picture(screen_data, figures_data, output_file):
    pygame.init()
    pygame.display.set_caption("Generated picture")
    screen = screen_data.generate_screen()
    figures_data.display(screen)
    pygame.display.flip()

    if output_file:
        if output_file[-4:] != '.png':
            output_file += '.png'
        pygame.image.save(screen, output_file)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    pygame.quit()
