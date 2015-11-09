from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()

    def test_realizar_registro(self):
#Misael ha escuchado sobre una nueva aplicación cool!! online, "airplane".
#Él va a revisar la página de inicio.
       self.browser.get('http://localhost:8000')
#Él se da cuenta de que el titulo y encabezado de la págona mencionan "airplane"
       self.assertIn ('Airplane', self.browser.title)
       header_text = self.browser.find_element_by_tag_name('h1').text
       self.assertIn('Aereopuerto', header_text)
#Él es invitado a realizar su registro.
       button = self.browser.find_element_by_id('id_nuevo_registro')
       self.assertEqual(button.get_attribute('placeholder'), 'Comenzar registro')
       self.fail('Finish the test!')

#Él llena el formulario con sus datos y da clic en registrar
       inputbox = self.browser.find_element_by_id('id_name')
       inputbox.send_keys('Misael')
       inputbox.send_keys(Keys.ENTER)
if __name__ == '__main__':
    unittest.main(warnings='ignore')




#Él llena el formulario con sus datos y da clic en registrar

#Él es invitado a ver las líneas de aviones disponibles

#Él selecciona una línea y se da cuenta de que en el título
#menciona "Aereolinea"

#Después de visualizar los datos de la línea, él se va a dormir.
