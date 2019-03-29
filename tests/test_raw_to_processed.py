import pytest

from src.data.cleaner import clean


@pytest.fixture
def clean_data():
    return clean('data/raw/chicago-salaries.csv', 'data/processed/chicago-salaries-processed.csv')


def test_lowercase_column_names(clean_data):
    cols = clean_data.columns

    assert 'full_or_part_time' in cols
    assert 'salary_or_hourly' in cols
    assert 'department' in cols


def test_names(clean_data):
    assert not clean_data.first_name.isna().any()
    assert not clean_data.middle_name.isna().any()
    assert not clean_data.last_name.isna().any()

