def rgb_html(r=0, g=0, b=0, *, alpha=255):
    """Converte R, G, B em #RRGGBB"""
    return '#%02x%02x%02x' % (r, g, b)

def html_rgb(color='#000000'):
    """Converte #RRGGBB em R, G, B"""
    if color.startswith('#'): color = color[1:]
    r = int(color[:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:], 16)
    return r, g, b # Uma tupla
