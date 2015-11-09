from selenium import webdriver
import unnitest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()

    def test_realizar_registro(self):
#Misael ha escuchado sobre una nueva aplicación cool!! online, "airplane".
#Él va a revisar la página de inicio.
       browser.get('http://localhost:8000')
#Él se da cuenta de que el titulo y encabezado de la págona mencionan "airplane"
       self.assertIn ('Airplane', browser.title)
       self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
#Él es invitado a realizar su registro.

#Él selecciona la opción de registro

#Él llena el formulario con sus datos y da clic en registrar

#Él es invitado a ver las líneas de aviones disponibles

#Él selecciona una línea y se da cuenta de que en el título
#menciona "Aereolinea"

#Después de visualizar los datos de la línea, él se va a dormir.
