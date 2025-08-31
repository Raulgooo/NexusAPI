import requests
import json

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
token1 = input("inserte token: ")
headers['token'] = token1
response = requests.request("POST", url, headers=headers, data=payload)

# Convertimos la respuesta a JSON
data_json = response.json()

# Carpeta → Cursos → Nombre y Profesores
for carpeta in data_json.get("Carpetas", []):
    for curso in carpeta.get("Cursos", []):
        nombre_curso = curso.get("Nombre")
        fecha_inicio = curso.get("FechaInicio")
        fecha_fin = curso.get("FechaFin")
        
        # Profesores
        profesores = []
        for prof in curso.get("Profesores", []):
            nombre_profesor = f"{prof.get('Nombre')} {prof.get('ApellidoPaterno')} {prof.get('ApellidoMaterno')}"
            correo = prof.get("CorreoUniversitario")
            profesores.append(f"{nombre_profesor} ({correo})")
        
        print(f"Curso: {nombre_curso}")
        print(f"Fechas: {fecha_inicio} → {fecha_fin}")
        print("Profesores:", ", ".join(profesores))
        print("-" * 40)


