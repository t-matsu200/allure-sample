# -*- coding: utf-8 -*-


def test_index(fixture_app_test):
    """Index root"""
    client = fixture_app_test
    response = client.get('/v1')
    assert response.status_code == 200
    assert response.json() == {'state': {
        'client': {'user': {'name': None}},
        'server': {'host': 'testserver', 'port': None}
    }}


def test_404_error(fixture_app_test):
    """Not Found"""
    client = fixture_app_test
    response = client.get('/v1/not-found')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}
