from pygame import draw
from pygame import gfxdraw
from abc import ABC, abstractmethod
from json_parser.colors_data_parser import format_color


class FiguresData:
    def __init__(self, file_content, color_palette, default_color):
        self.list_of_figures = []
        self._parse_figures_data(file_content, color_palette, default_color)

    def display(self, screen):
        for figure in self.list_of_figures:
            figure.display(screen)

    def _parse_figures_data(self, file_content, color_palette, default_color):
        figures_parameters = file_content['Figures']
        figure_types = [['point', Point],
                        ['polygon', Polygon],
                        ['rectangle', Rectangle],
                        ['square', Square],
                        ['circle', Circle]]
        for figure_type in figure_types:
            for figure in figures_parameters:
                if figure_type[0] == figure['type']:
                    self.list_of_figures.append(figure_type[1](figure, color_palette, default_color))


class Figure(ABC):
    def __init__(self, figure, color_palette, default_color):
        if 'color' in figure.keys():
            self._color = format_color(figure['color'], color_palette)
        else:
            self._color = default_color

    @abstractmethod
    def display(self, screen):
        pass


class Point(Figure):
    def __init__(self, figure, color_palette, default_color):
        super().__init__(figure, color_palette, default_color)
        self._x = figure['x']
        self._y = figure['y']

    def display(self, screen):
        gfxdraw.pixel(screen, self._x, self._y, self._color)


class Polygon(Figure):
    def __init__(self, figure, color_palette, default_color):
        super().__init__(figure, color_palette, default_color)
        self._points = figure['points']

    def display(self, screen):
        draw.polygon(screen, self._color, self._points, 1)


class Rectangle(Figure):
    def __init__(self, figure, color_palette, default_color):
        super().__init__(figure, color_palette, default_color)
        self._dimensions = [figure['x'] - figure['width'] // 2,
                            figure['y'] - figure['height'] // 2,
                            figure['width'],
                            figure['height']]

    def display(self, screen):
        draw.rect(screen, self._color, self._dimensions, 1)


class Square(Figure):
    def __init__(self, figure, color_palette, default_color):
        super().__init__(figure, color_palette, default_color)
        self._dimensions = [figure['x'] - figure['size'] // 2,
                            figure['y'] - figure['size'] // 2,
                            figure['size'],
                            figure['size']]

    def display(self, screen):
        draw.rect(screen, self._color, self._dimensions, 1)


class Circle(Figure):
    def __init__(self, figure, color_palette, default_color):
        super().__init__(figure, color_palette, default_color)
        self._center = [figure['x'], figure['y']]
        self._radius = figure['radius']

    def display(self, screen):
        draw.circle(screen, self._color, self._center, self._radius, 0)
