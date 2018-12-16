import unittest
import flask_testing
from temp_conv import temp_conv


class TempConvTestCase(flask_testing.TestCase):
    def create_app(self):
        temp_conv.config['WTF_CSRF_ENABLED'] = False
        return temp_conv

    def test_canOpen(self):
        response = self.client.get('/')
        text = response.get_data(as_text=True)

        self.assertIn('<html>', text)

        for expected_tag in ['<html>', '<head>', '<body>']:
            self.assertTrue(expected_tag in text, expected_tag)

        # self.assertNotEqual(text, None)


    def test_canConvert_CToF(self):
        response = self.client.post('/', data={'celsius': '0', 'convert_to_f': '', 'fahrenheit': ''})
        text = response.get_data(as_text=True)

        self.assert200(response)
        self.assertIn('value="32.0"', text)


    def test_canConvert_FToC(self):
        response = self.client.post('/', data = {'celsius':'', 'convert_to_c':'', 'fahrenheit':'212.0'})
        text = response.get_data(as_text=True)

        self.assert200(response)
        self.assertIn('value="100.0"', text)

    def test_canConvert_DifferentValues(self):
        response = self.client.post('/', data = {'celsius':'', 'convert_to_c':'', 'fahrenheit':'32.0'})
        text = response.get_data(as_text=True)

        self.assert200(response)
        self.assertIn('value="0.0"', text)



if __name__ == '__main__':
    unittest.main()