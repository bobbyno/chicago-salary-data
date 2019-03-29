import pandas as pd
import re


# columns
def to_snake(s):
    return re.sub(r'([\s]+|[-]+)', '_', s).lower().lstrip('_')


# names
def last_name(s):
    return s.split(',')[0]


def first_name(s):
    first_names = s.split(',')[1].strip()
    return first_names.split(' ')[0]


def middle_name(s):
    first_names = s.split(',')[1].strip()
    maybe_first_names = first_names.split(' ')
    if len(maybe_first_names) > 1:
        return maybe_first_names[1]
    return ' '


def clean(input_filepath, output_filepath):
    data = pd.read_csv(input_filepath)

    # rename columns
    data = data.rename(to_snake, axis='columns')

    # split name
    data = data.assign(last_name=[last_name(n) for n in data.name])
    data = data.assign(first_name=[first_name(n) for n in data.name])
    data = data.assign(middle_name=[middle_name(n) for n in data.name])

    return data
