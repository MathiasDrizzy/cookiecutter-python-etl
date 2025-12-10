import pytest

from extract import extract_data
from transform import transform_data
from load import load_data


def test_etl_pipeline_runs():
    raw = extract_data()
    transformed = transform_data(raw)
    result = load_data(transformed)
    assert result is True
