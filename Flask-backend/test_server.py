from unittest import main, TestCase
from server import app


class FlaskTestServer(TestCase):
    # Ensure that flask was set up properly
    def setUp(self):
        self.app = app.test_client()

    # Testing gene route with valid input ENG
    def test_genes(self):
        tester = app.test_client(self)
        response = tester.get('/genes/ENG', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # Testing variants route with valid input ENG
    def test_variants(self):
        tester = app.test_client(self)
        response = tester.get('/variants/ENG', content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    main()
