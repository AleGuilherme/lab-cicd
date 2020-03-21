#!/usr/bin/env python
import unittest
import app

class TestB3Z(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_inicio(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Rota Inicio!\n')

    def test_startup_name(self):
        rv = self.app.get('/startup')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'B3Z - COMBATE A DENGUE!\n')

    def test_startup_equipe(self):
        rv = self.app.get('/startup/equipe')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'ALEXANDRE GUILHERME\nADRIANO CESAR MARTINS\nVITOR CHALUPPE RADI\n')

    def test_startup_din(self):
        name = '<rota_dinamica>'
        rv = self.app.get(f'/startup/{name}')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray(f"{name}", 'utf-8'), rv.data)

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
