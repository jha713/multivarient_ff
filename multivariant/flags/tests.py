# flags/tests/test_views.py

from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock
from rest_framework import status

class FeatureFlagViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_email = 'user1@trinet.com'
        self.url = reverse('feature-flag', args=[self.user_email])

    @patch('flags.views.CfClient')
    def test_get_feature_flag_success(self, MockCfClient):
        # Mock the CfClient and its method
        mock_client = MockCfClient.return_value
        mock_client.string_variation.return_value = 'c'

        # Make the GET request
        response = self.client.get(self.url)

        # Assert the response status code and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"variation": 'c'})

        # Ensure the mock was called correctly
        mock_client.string_variation.assert_called_once_with(
            'multivariant',
            MagicMock(identifier=self.user_email, name='group'),
            'default'
        )

    @patch('flags.views.CfClient')
    def test_get_feature_flag_default(self, MockCfClient):
        # Mock the CfClient and its method to return default
        mock_client = MockCfClient.return_value
        mock_client.string_variation.return_value = 'default'

        # Make the GET request
        response = self.client.get(self.url)

        # Assert the response status code and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"variation": 'default'})

        # Ensure the mock was called correctly
        mock_client.string_variation.assert_called_once_with(
            'multivariant',
            MagicMock(identifier=self.user_email, name='group'),
            'default'
        )

    @patch('flags.views.CfClient')
    def test_get_feature_flag_error(self, MockCfClient):
        # Mock the CfClient and its method to raise an exception
        mock_client = MockCfClient.return_value
        mock_client.string_variation.side_effect = Exception('Error fetching variation')

        # Make the GET request
        response = self.client.get(self.url)

        # Assert the response status code and data
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.json(), {"detail": "Error fetching variation"})

if __name__ == '__main__':
    TestCase.main()
