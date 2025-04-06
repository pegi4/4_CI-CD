import unittest
from client import app
import os

class TestClient(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        
    def test_index_server_down(self):
        """Test index route when server is not accessible"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 503)
        self.assertIn(b"Server not accessible", response.data)
        
    def test_static_directory_exists(self):
        """Test if static directory exists for storing images"""
        static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
        self.assertTrue(os.path.exists(static_dir), "Static directory should exist")

if __name__ == '__main__':
    unittest.main() 