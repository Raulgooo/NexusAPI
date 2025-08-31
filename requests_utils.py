import requests
import json
from tokens import get_token


def get_cursos(token):

  url = "https://api.nexus.uanl.mx/WebApi/Curso/ConsultarCarpetaCursos"

  payload = json.dumps({
    "CarpetaId": 0,
    "Pagina": 1,
    "Paginacion": 10
  })
  headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'es-MX,es-419;q=0.9,es;q=0.8,en;q=0.7',
    'areaacademicaid': '44',
    'content-type': 'application/json',
    'origin': 'https://plataformanexus.uanl.mx',
    'priority': 'u=1, i',
    'referer': 'https://plataformanexus.uanl.mx/',
    'rolid': '5',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sistemaid': '1',
    'token': 'none',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
  }
  headers['token'] = token

  response = requests.request("POST", url, headers=headers, data=payload)

  # Convertimos la respuesta a JSON
  data_json = response.json()
  # Carpeta → Cursos → Nombre y Profesores
  cursos_json = []

  for carpeta in data_json.get("Carpetas", []):
      for curso in carpeta.get("Cursos", []):
          # Extraer información del curso
          nombre_curso = curso.get("Nombre")
          fecha_inicio = curso.get("FechaInicio")
          fecha_fin = curso.get("FechaFin")
          
          # Extraer profesores
          profesores = []
          for prof in curso.get("Profesores", []):
              nombre_profesor = f"{prof.get('Nombre')} {prof.get('ApellidoPaterno')} {prof.get('ApellidoMaterno')}"
              correo = prof.get("CorreoUniversitario")
              profesores.append(f"{nombre_profesor} ({correo})")
          
          # Extraer grupos
          grupos = [grupo.get("Nombre") for grupo in curso.get("Grupos", [])]

          # Construir diccionario del curso
          curso_info = {
              "Nombre": nombre_curso,
              "FechaInicio": fecha_inicio,
              "FechaFin": fecha_fin,
              "Profesores": profesores,
              "Grupos": grupos
          }

          cursos_json.append(curso_info)

  return cursos_json


def get_tareas(token):
    url = "https://api.nexus.uanl.mx/WebApi/Tarea/ConsultarTareas"

    payload = json.dumps({
        "CursoId": curso_id
    })

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'es-MX,es-419;q=0.9,es;q=0.8,en;q=0.7',
        'areaacademicaid': '44',
        'content-type': 'application/json',
        'origin': 'https://plataformanexus.uanl.mx',
        'priority': 'u=1, i',
        'referer': 'https://plataformanexus.uanl.mx/',
        'rolid': '5',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sistemaid': '1',
        'token': token,
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
    }

    response = requests.post(url, headers=headers, data=payload)
    data_json = response.json()

    tareas_json = []

    for tarea in data_json.get("Tareas", []):
        tarea_info = {
            "Descripcion": tarea.get("Descripcion"),
            "FechaEntrega": tarea.get("FechaFin"),
            "Curso": tarea.get("Curso", {}).get("Nombre")

        }

        tareas_json.append(tarea_info)

    return tareas_json

# Ejemplo de uso:
# token = "TU_TOKEN_AQUI"
# tareas = get_tareas(token)
# print(json.dumps(tareas, indent=4, ensure_ascii=False))
def get_user(token):
  url = "https://api.nexus.uanl.mx/WebApi/Seguridad/ConsultarPerfil"

  payload = json.dumps({})
  headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'es-MX,es-419;q=0.9,es;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://plataformanexus.uanl.mx',
    'priority': 'u=1, i',
    'referer': 'https://plataformanexus.uanl.mx/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sistemaid': '1',
    'token': 'U2VaHYytJVOTMmlUpFaN/WpkJGpgG/JXX/EsxHcPk2U3V1xAghJikjNBVPyp7SB/GfkobhF3ZuXW+ohS42G66OJKHk4+kYWbHn9z46fknH1kDjm6IhRsPBYDXvXGZsjzdtlg6bhUxQ1ZAF9v2EZHsA5X+FdJM7hUd6UMkYRpZi5HRWM6n5gjLNJG+dU+PVS15ZxDAkLflQBjqYemAQDOpKfp97cWRp/fIrFctLziM2AWya+Gp+tBSagGX+hrBdhiZEdGJVO1aJ0v6g5w6Wpr1HCr6m5UENz1Eyw2sZ5WzFgyYx20FD0OmIQfktraZK/XeFtwqcQ/1b1uL/IPOU04mDsUUy+UABiiP9J1cXZtT5m/oXNl+r7OHnHRjraztYrYZlZ3vWRU0y9513NkDSaLuF1h1wWbWSp1ASQsQwXYgiYzYT1xrSTTL0ovstDVM/8bHUbt9uSEfYA54hOKJ2AeAbIviuJ3v0y42jOK8jyWKEIMtxxryEhGbfhCH5qYqjFS',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  data_json = response.json()

  userdata = []

  persona = data_json.get("Persona", {})
  nombre_completo = f"{persona.get('Nombre', '')} {persona.get('ApellidoPaterno', '')} {persona.get('ApellidoMaterno', '')}".strip()
  
  for cuenta in persona.get("Cuentas", []):
      # Obtener dependencias de esta cuenta
      dependencias = []
      for area in cuenta.get("AreasAcademicas", []):
          dep = area.get("AreaAcademica", {}).get("Dependencia", {}).get("NombreCorto")
          if dep and dep not in dependencias:
              dependencias.append(dep)

      user_info = {
          "NombreAlumno": nombre_completo,
          "NombreUsuario": cuenta.get("NombreUsuario"),
          "CorreoUniversitario": cuenta.get("CorreoUniversitario"),
          "Dependencias": dependencias
      }
      userdata.append(user_info)

  return userdata
token2 = get_token("XXX", "XXXX")
print(get_cursos(token2)) #19200 segundos segundos