from json_parser.colors_data_parser import format_color
from pygame import display


class ScreenData:
    def __init__(self, file_content, color_palette):
        self._parse_screen_data(file_content, color_palette)

    def generate_screen(self):
        screen = display.set_mode(self._size)
        screen.fill(self._bg_color)
        return screen

    def _parse_screen_data(self, file_content, color_palette):
        screen_parameters = file_content['Screen']
        if 'width' in screen_parameters.keys():
            width = screen_parameters['width']
        else:
            print('Using default screen width of 500 pixels')
            width = 500

        if 'height' in screen_parameters.keys():
            height = screen_parameters['height']
        else:
            print('Using default screen height of 500 pixels')
            height = 500

        self._size = (width, height)

        if 'bg_color' in screen_parameters.keys():
            self._bg_color = format_color(screen_parameters['bg_color'], color_palette)
        else:
            print('Using default background color - white')
            self._bg_color = (255, 255, 255)

        if 'fg_color' in screen_parameters.keys():
            self.fg_color = format_color(screen_parameters['fg_color'], color_palette)
        else:
            print('Using default foreground color - black')
            self.fg_color = (0, 0, 0)
