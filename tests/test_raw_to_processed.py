import pytest
import pandas as pd


@pytest.fixture
def clean_data():
    return pd.read_csv('data/processed/chicago-salaries-processed.csv')


def test_lowercase_column_names(clean_data):
    cols = clean_data.columns
    assert 'full_or_part_time' in cols
    assert 'salary_or_hourly' in cols
    assert 'department' in cols


def test_no_salary_column(clean_data):
    print(clean_data.columns)
    assert 'annual_salary' not in clean_data.columns


def test_names(clean_data):
    assert not clean_data.first_name.isna().any()
    assert not clean_data.middle_name.isna().any()
    assert not clean_data.last_name.isna().any()


def test_typical_hours_normalization(clean_data):
    assert not clean_data.typical_hours.isna().any()
    assert clean_data.typical_hours.min() > 0.0
    assert clean_data.typical_hours.max() <= 40.0


def test_hourly_rate(clean_data):
    assert not clean_data.hourly_rate.isna().any()
    assert clean_data.hourly_rate.min() > 0.0
    assert clean_data.hourly_rate.max() < 1000.0


def test_salary(clean_data):
    assert not clean_data.annualized_income.isna().any()
    assert clean_data.annualized_income.min() > 0.0
    assert clean_data.annualized_income.max() < 500000.0


def test_gender(clean_data):
    assert not clean_data.gender.isna().any()
