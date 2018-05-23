def html_color_notation_to_tuple(color):
    r = int(color[1:3], base=16)
    g = int(color[3:5], base=16)
    b = int(color[5:7], base=16)
    return r, g, b


def parse_tuple_color_notation(color):
    rgb_list = []
    for i in color.replace('(', '').replace(')', '').split(','):
        rgb_list.append(int(i))
    return tuple(rgb_list)


def format_color(color, color_palette):
    if color in color_palette.keys():
        return color_palette[color]
    elif color[0] == '#':
        return html_color_notation_to_tuple(color)
    else:
        return parse_tuple_color_notation(color)


def parse_color_palette(file_content):
    color_palette = file_content['Palette']
    for key, value in color_palette.items():
        if isinstance(value, str):
            color_palette[key] = html_color_notation_to_tuple(value)

    return color_palette
