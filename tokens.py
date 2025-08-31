from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Puse todas las variables y las funciones en ingles por que es mas rapido de escribir, lol
# Funcion para obtener el token de inicio de sesion de nexus.
def get_token(user, password):

# Configurar Chrome en modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # headless moderno
    chrome_options.add_argument("--window-size=1920,1080") # Ejecuta Chrome sin interfaz
    chrome_options.add_argument("--disable-gpu")  # Deshabilita GPU (en Linux a veces necesario)
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  


    #Inicializar servicio de de chromedriver para selenium
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,options=chrome_options)
    try:
        driver.get("https://www.uanl.mx/enlinea/")
        
        #Seleccionar los objetos con los campos a llenar
        loginbox = driver.find_element(By.NAME, "loginbox")
        driver.switch_to.frame(loginbox)
        html_user_login = driver.find_element(By.ID, "cuenta")
        html_user_password = driver.find_element(By.ID, "pass")
        button = driver.find_element(By.XPATH, "//button[contains(text(),'Entrar')]")

        # Enviar datos y clickear login
        html_user_login.send_keys(user)
        html_user_password.send_keys(password)  
        button.click()
        time.sleep(2)# Esperar a que Nexus cargue el contenido

        # Bloque que consigue el token de NEXUS
        try:
            driver.switch_to.default_content()

            # Dentro de servicios UANL loggear a Nexus
            nexus = driver.find_element(By.CSS_SELECTOR, "img[src='https://deimos.dgi.uanl.mx/uanlimg/ws/nexus_btn.jpg']")
            nexus.click()
            nexus = driver.find_element(By.NAME, "btnNexus")
            nexus.click()
            time.sleep(14)

            # Recargar Nexus y Obtener Token
            windows = driver.window_handles
            driver.switch_to.window(windows[1])
            driver.refresh()
            time.sleep(6)
            token = driver.wait_for_request("ConsultarModalidades", timeout=10)
            token = token.headers['token']
            success = True
            print("El token fue obtenido con exito.")
            return token
        except:

            #Se ejecuta si al pasar la password a SIASE esta no logra loggear o cualquier otra cosa, posiblemente por credenciales invalidas/incorrectas
            print("Contrasena invalida o error en la ejecucion.")
            return None
    finally:
        driver.quit()
        