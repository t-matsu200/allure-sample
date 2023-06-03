# -*- coding: utf-8 -*-
from unittest.mock import MagicMock, patch


def test_get_user_normal(fixture_app_test):
    """Get user list"""
    client = fixture_app_test
    response = client.get('/v1/users')
    result = response.json()

    assert response.status_code == 200
    assert type(result) == dict
    assert len(result) == 1
    assert type(result.get('user')) == list
    assert result.get('user') == [{'id': 0, 'name': 'test-user'}]


def test_get_user_500_error(fixture_app_test):
    """Server Error"""
    with patch('routers.users.Users') as mock:
        mock.find_all.side_effect = Exception('ユーザー一覧の取得エラー')
        client = fixture_app_test
        response = client.get('/v1/users')

        assert response.status_code == 500
        assert response.json() == {'Error': {
            'code': 500, 'derail': 'Occurred server error in /v1/users.', 'message': 'Internal Server Error'}
        }
