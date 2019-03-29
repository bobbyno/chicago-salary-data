import pandas as pd
import re
from src.data.gender import consolidated_gender


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


# normalization
def hours(row):
    h = row['typical_hours']
    return 40.0 if pd.isna(h) else h


def rate(row):
    r = row['hourly_rate']
    if pd.isna(r):
        return row['annual_salary'] / (52.0 * 40.0)
    return r


def salary(row):
    r = row['annual_salary']
    if pd.isna(r):
        return row['typical_hours'] * row['hourly_rate'] * 52
    return r


def clean(input_filepath):
    data = pd.read_csv(input_filepath)

    # rename columns
    data = data.rename(to_snake, axis='columns')

    # split name
    data = data.assign(last_name=[last_name(n) for n in data.name])
    data = data.assign(first_name=[first_name(n) for n in data.name])
    data = data.assign(middle_name=[middle_name(n) for n in data.name])

    # normalization
    # TODO: introduce new columns for typical hours and hourly rate
    new_hours = pd.DataFrame({'typical_hours': [hours(row) for _, row in data.iterrows()]})
    data.update(new_hours)

    new_rate = pd.DataFrame({'hourly_rate': [rate(row) for _, row in data.iterrows()]})
    data.update(new_rate)

    data = data.assign(annualized_income=[salary(row) for _, row in data.iterrows()])

    # gender
    data = data.assign(gender=[consolidated_gender(n) for n in data.first_name])

    # drop columns with NaN values
    data = data.drop(['annual_salary'], axis=1)

    return data
