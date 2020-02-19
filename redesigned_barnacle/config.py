import os

BOOLEAN_TRUES = [
    'y', 'Y',
    'yes', 'Yes', 'YES',
    'true', 'True', 'TRUE',
    'on', 'On', 'ON'
]

BOOLEAN_FALSES = [
    'n', 'N',
    'no', 'No', 'NO',
    'false', 'False', 'FALSE',
    'off', 'Off', 'OFF'
]


def is_numeric(c):
    return (c >= '0' and c <= '9')


def is_decimal(c):
    return c == '.' or is_numeric(c)


def is_float(s):
    return s.count('.') <= 1 and str_all(s, is_decimal)


def is_integer(s):
    return str_all(s, is_numeric)


def str_all(s, fn):
    return all([fn(c) for c in s])


def convert_value(value):
    if value in BOOLEAN_FALSES:
        return False
    elif value in BOOLEAN_TRUES:
        return True
    elif is_integer(value):
        return int(value)
    elif is_float(value):
        return float(value)
    elif value[0] == '"':
        return value.strip('"')
    else:
        return value


def load_config(path, name):
    files = os.listdir(path)
    if not name in files:
        raise Exception('config file missing')

    config = parse_file('{}/{}'.format(path, name))
    print('Config: {}'.format(config))

    return config


def parse_file(name, open=open):
    with open(name, 'r') as source:
        return parse_str(source.readlines())


def parse_str(lines):
    data = {}
    for rline in lines:
        line = rline.strip()
        if len(line) == 0 or line[0] == '#':
            continue

        parts = line.split(':')
        if len(parts) < 2:
            continue

        key = parts[0].strip()
        value = ''.join(parts[1:]).strip()
        if len(value) == 0:
            continue

        data[key] = convert_value(value)

    return data
