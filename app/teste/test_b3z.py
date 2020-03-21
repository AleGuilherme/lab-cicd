#!/usr/bin/env python
import unittest
import app_b3z

class TestB3Z(unittest.TestCase):

    def setUp(self):
        app_b3z.app.testing = True
        self.app_b3z = app_b3z.app.test_client()

    def test_inicio(self):
        rv = self.app_b3z.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Pagina Inicial - B3Z!\n')

    def test_startup_name(self):
        rv = self.app_b3z.get('/startup')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'B3Z - COMBATE A DENGUE!\n')

    def test_startup_equipe(self):
        rv = self.app_b3z.get('/startup/equipe')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'ALEXANDRE GUILHERME<br>ADRIANO CESAR MARTINS<br>VITOR CHALUPPE RADI<br>')

    def test_startup_apptype(self):
        rv = self.app_b3z.get('/startup/app_type')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(rv.data, b'BZ3 BLUE GREEN')

    def test_startup_din(self):
        name = '<rota_dinamica>'
        rv = self.app_b3z.get(f'/startup/{name}')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray(f"{name}", 'utf-8'), rv.data)

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
