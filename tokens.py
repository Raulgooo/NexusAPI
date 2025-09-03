import httpx
import re
from urllib.parse import urlparse, parse_qs
def get_token(user, password):

    url = "https://deimos.dgi.uanl.mx/cgi-bin/wspd_cgi.sh/eselcarrera.htm"
    url_nexus = "https://api.nexus.uanl.mx/WebApi/Seguridad/CrearSesionSIASE"
    data = {
        "HTMLTipCve": "01",
        "HTMLUsuCve": user,
        "HTMLPassword": password,
        "HTMLPrograma": ""
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://deimos.dgi.uanl.mx",
        "Referer": "https://deimos.dgi.uanl.mx/cgi-bin/wspd_cgi.sh/login.htm",
        "User-Agent": "Mozilla/5.0"
    }

    headers_nexus = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.5",
        "accept-encoding": "gzip, deflate, br, zstd",
        "control":  None,
        "clienteip": "0.0.0.0",
        "usuario": None,
        "usuarioclave": None,
        "tipoclave": "01",
        "sistemaid": "1",
        "content-type": "application/json",
        "content-length": "2",
        "origin": "https://plataformanexus.uanl.mx",
        "referer": "https://plataformanexus.uanl.mx/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "te": "trailers"
    }

    res = httpx.post(url, data=data, headers=headers)

    # Aquí sí usamos el contenido de la respuesta
    html_content = res.text

    # Regex para extraer el contenido de attr("action", "...") dentro de #idfrNexus
    pattern = r'\$\(\s*"#idfrNexus"\s*\)\.attr\(\s*"action"\s*,\s*"([^"]+)"\s*\)'

    match = re.search(pattern, html_content, re.DOTALL)
    if match:
        url_login = match.group(1)
    else:
        print("No se encontró la URL")
    url_login = url_login.split('=')
    control = url_login[2] + "="
    usu = url_login[1].split("&Ctrl")[0]
    headers_nexus["control"] = control
    headers_nexus["usuario"] = usu


    asknexus = httpx.post(url_nexus,  headers=headers_nexus, json={})
    token = asknexus.json()['Sesion']['Token']
    return token

