def center_box(rect, factor=0.75):
    x1, y1, x2, y2 = rect

    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2

    width = (x2 - x1) * factor
    height = (y2 - y1) * factor

    x1 = center_x - width / 2
    y1 = center_y - height / 2
    x2 = center_x + width / 2
    y2 = center_y + height / 2

    return x1, y1, x2, y2
