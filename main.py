import argparse
import json

from displayer import generate_picture
from json_parser import FiguresData
from json_parser import ScreenData
from json_parser import parse_color_palette


def parse_file(input_file):
    with open(input_file) as json_file:
        file_content = json.load(json_file)

    color_palette = parse_color_palette(file_content)
    screen_data = ScreenData(file_content, color_palette)
    figures_data = FiguresData(file_content, color_palette, screen_data.fg_color)
    return screen_data, figures_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='name of the JSON input file', type=str)
    parser.add_argument('-o', '--output', help='name of the file to save png picture', type=str)
    args = parser.parse_args()

    screen_data, figures_data = parse_file(args.input_file)

    generate_picture(screen_data, figures_data, args.output)


if __name__ == '__main__':
    main()
