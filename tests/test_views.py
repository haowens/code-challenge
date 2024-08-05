import pytest
from rest_framework.test import APIClient
from rest_framework import status

def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    client = APIClient()
    response = client.get('/api/parse/?address='+ address_string)
    assert response.status_code == status.HTTP_200_OK
    assert 'input_string' in response.data
    assert 'address_components' in response.data
    assert 'address_type' in response.data


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    client = APIClient()
    response = client.get('/api/parse/?address='+ address_string)
    assert response.status_code == status.HTTP_200_OK
    assert 'error' in response.data
