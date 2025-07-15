def print_banner(message, pad=2, border_char='*'):
    lines = message.split('\n')
    max_length = max(len(line) for line in lines)
    width = max_length + pad * 2

    border = border_char * (width + 2)
    print(border)
    for line in lines:
        print(f"{border_char}{' ' * pad}{line.ljust(max_length)}{' ' * pad}{border_char}")
    print(border)
