import pytest
from main import get_random_cat_image

def test_get_random_cat_image_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"url": "https://cdn2.thecatapi.com/images/abc123.jpg"}]

    result = get_random_cat_image()

    assert result == "https://cdn2.thecatapi.com/images/abc123.jpg"

def test_get_random_cat_image_failure(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    result = get_random_cat_image()

    assert result is None