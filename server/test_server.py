import unittest
from server import app
import cv2 as cv
import numpy as np

class TestServer(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_image_endpoint(self):
        """Test if /image endpoint returns an image"""
        response = self.client.get('/image')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'image/jpeg')
        
    def test_image_content(self):
        """Test if the image contains timestamp"""
        response = self.client.get('/image')
        # Convert response data to image
        nparr = np.frombuffer(response.data, np.uint8)
        img = cv.imdecode(nparr, cv.IMREAD_COLOR)
        # Check if image is not empty
        self.assertIsNotNone(img)
        self.assertTrue(img.size > 0)

if __name__ == '__main__':
    unittest.main() 