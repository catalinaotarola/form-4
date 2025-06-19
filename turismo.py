turistas = {
    "001": ["John Doe", "Estados Unidos","12-01-2024"],
    "002": ["Emily Smith","Estdos Unidos","23-03-2024"],
    "012": ["Julian Martinez","Argentina","19-09-2023"],
    "014": ["Agustin Morales","Argentina","28-03-2024"],
    "005": ["Carlos Garcia","Mexico", "10-05-2024"],
    "006": ["Maria Lopez","Mexico", "08-12-2023"],
    "007": ["Joao Silva","Brasil", "20-06-2024"],
    "003": ["Michael Brown","Estados Unidos","05-07-2023"],
    "004": ["Jessica Davis","Estados Unidos","15-11-2024"],
    "008": ["Ana Santos","Brasil","03-10-2023"],
    "010": ["Martin Fernandez","Argentina","13-02-2023"],
    "011": ["Sofia Gomez","Argentina","07-04-2024"]
}

def turistas_por_pais(pais):
    encontrados = []
    for clave, datos in turistas.items():
        pais_turista = datos[1]
        if pais_turista.lower() == pais.lower():
            nombre_turista = datos[0]
            encontrados.append(nombre_turista)
    if len(encontrados) > 0:
        print(encontrados)
    else:
        print("No hay turistas de ese pais.")

def turistas_por_mes(mes):
    total = len(turistas)
    cuenta = 0
    for datos in turistas.values():
        fecha = datos[2]
        partes_fecha = fecha.split("-")
        mes_ingreso = int(partes_fecha[1])
        if mes_ingreso == mes:
            cuenta += 1
    porcentaje = (cuenta / total * 100)
    if total > 0
    else:
        0
    return round(porcentaje, 1)

def eliminar_turista():
    nombre_i = input("Ingrese nombre de turista a eliminar: ").lower()
    clave_a_eliminar = None
    for clave, datos in turistas.items():
        nombre_turista = datos[0]
        if nombre_turista.lower() == nombre_i:
            clave_a_eliminar = clave
            break
    if clave_a_eliminar is not None:
        del turistas[clave_a_eliminar]
        print("Turista eliminado con exito.")
    else:
        print("El Turista no se ah encontrado, No se pudo eliminar.")
