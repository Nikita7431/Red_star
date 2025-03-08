def red_flag_end(nuber, index):
    x1 = x
    y1 = y - cell_height
    x2 = x + (cell_width - 2 * SPACING)
    y2 = y - SPACING

    pdf.line(x1, y1, x2, y2)
    pdf.line(x2, y1, x1, y2)

