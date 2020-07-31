def get_levels(sc, ec, jump):
    jump += 1
    start = min(sc, ec)
    end = max(sc, ec)
    inc = round((end - start) / jump)
    levels = [start]
    for _ in range(jump):
        levels.append(levels[-1]+inc)
    if levels[-1] >= end:
        del levels[-1]
        levels.append(end)
    else:
        levels.append(end)
    if sc > ec:
        levels.reverse()
    hexes = []
    for n in levels:
        if n == 0:
            hexes.append('00')
            continue
        hexn = hex(n).lstrip('0x')
        if len(hexn) == 1:
            hexn = '0' + hexn
        hexes.append(hexn)
    return levels, hexes


if __name__ == "__main__":
    from display_tk import display
    import display_html

    starting_color = input('enter starting color in hex\n')
    starting_color = starting_color.lstrip('#')
    ending_color = input('enter ending color in hex\n')
    ending_color = ending_color.lstrip('#')
    levels = int(input('how many levels to go through?\n'))
    choice = input('Display in 1.GUI or 2.HTML? ')
    sr, sg, sb = int(starting_color[:2], base=16), int(
        starting_color[2:4], base=16), int(starting_color[4:6], base=16)
    er, eg, eb = int(ending_color[:2], base=16), int(
        ending_color[2:4], base=16), int(ending_color[4:6], base=16)

    r_range = get_levels(sr, er, levels)
    g_range = get_levels(sg, eg, levels)
    b_range = get_levels(sb, eb, levels)
    complete = list(zip(r_range[0], g_range[0], b_range[0]))
    complete_hex = [''.join(t)
                    for t in list(zip(r_range[1], g_range[1], b_range[1]))]
    print(complete)
    print(complete_hex)

    if choice == '1':
        display(complete_hex)
    elif choice == '2':
        display_html.make_html(complete_hex)
    else:
        print(complete)
        print(complete_hex)
