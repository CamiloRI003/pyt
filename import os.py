import os


vehiculos = []

def funcion(vehiculos):
    vehiculos

while True:
    print("\nMenú:")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir certificado")
    print("4. Salir")
    
    opcion = input("Seleccione una opcion ")
    
    if opcion == '1':
        tipo = input("Ingrese tipo de vehículo (automovil, camion, camioneta, moto): ")
        while tipo not in ['automovil', 'camion', 'camioneta', 'moto']:
            print("Tipo de vehículo inválido.")
            tipo = input("Ingrese tipo de vehículo (automovil, camion, camioneta, moto ): ")
        
        
        while True:
            patente = input("Ingrese la patente del vehículo (4 letras consonantes seguidas de 2 números exepto m,n,ñ): ")
            patente=patente.replace("","ñ")
            patente=patente.replace("n","ñ")
            patente=patente.replace("m","ñ")           
            if patente =="ñ":
                
                print("Patente inválida no debe contener n m o ñ")
            else:
                break





        marca = input("Ingrese la marca del vehículo (2 a 15 caracteres): ")
        while not (2 <= len(marca) <= 15):
            print("Marca inválida.")
            marca = input("Ingrese la marca del vehículo (2 a 15 caracteres): ")

        precio = int(input("Ingrese el precio del vehículo (mayor a 5000000): "))
        while precio <= 5000000:
            print("Precio inválido.")
            precio = int(input("Ingrese el precio del vehículo (mayor a 5000000): "))
        
        multa = int(input("Ingrese el multas (0 o más): "))
        fecha_registro = input("Ingrese la fecha de registro del vehículo (YYYY-MM-DD): ")
        try:
            fecha_registro = (fecha_registro, )
        except: 
            999
            print("Fecha inválida. Usando fecha actual.")
            fecha_registro = int(input("fecha"))
        
        run = input("Ingrese el run o rut del dueño: ")
        nombre_duenio = input("Ingrese el nombre del dueño: ")
        
        vehiculo = {
            'tipo': tipo,
            'patente': patente,
            'marca': marca,
            'precio': precio,
            'multa': multa,
            'fecha_registro': fecha_registro,
            'run': run,
            'nombre_duenio': nombre_duenio,
            'certificados': {}
        }

        funcion (vehiculos)
        print(f"Vehículo con patente {patente} grabado correctamente.")
        
    
    elif opcion == '2':
        patente_buscar = input("Ingrese la patente del vehículo a buscar: ")
        
        for vehiculo in vehiculos:
            if vehiculo['patente'] == patente_buscar:
                print(f"Información del vehículo con patente {patente_buscar}:")
                for elemento, l in vehiculo:
                    if elemento != 'certificados':
                        print(f"{elemento}: {l}")
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró ningún vehículo con patente {patente_buscar};v.")
    
    elif opcion == '3':
        certificados = {
            1: "Emisión de Contaminantes",
            2: "Anotaciones Vigentes",
            3: "Multas"
        }
        patente_buscar = input("Ingrese la patente del vehículo para imprimir certificado: ")
        encontrado = False
        for vehiculo in vehiculos:
            if vehiculo['patente'] == patente_buscar:
                print("Tipos de certificados disponibles:")
                for elemento, value in certificados:
                    print(f"{elemento}. {l}")
                tipo_certificado = int(input("Seleccione el tipo de certificado (1-3): "))
                if tipo_certificado in certificados:
                    nombre_certificado = certificados[tipo_certificado]
                    costo = int(input(f"Ingrese el costo del certificado {nombre_certificado} (entre 1500 y 3500): "))
                    while not (1500 <= costo <= 3500):
                        print("Costo inválido.")
                        costo = int(input(f"Ingrese el costo del certificado {nombre_certificado} (entre 1500 y 3500): "))
                    
                    vehiculo['certificados'][nombre_certificado] = costo
                    
                    print("Certificado:")
                    print(f"Nombre del certificado: {nombre_certificado}")
                    print(f"Patente del auto: {patente_buscar}")
                    print(f"Nombre del dueño: {vehiculo['nombre_duenio']}")
                    print(f"RUN del dueño: {vehiculo['run']}")
                    encontrado = True
                else:
                    print("Opción de certificado inválida.")
                break
        if not encontrado:
            print(f"No se encontró ningún vehículo con patente {patente_buscar}.")
    
    elif opcion == '4':
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        print(f"Gracias {nombre} {apellido}, hasta luego.")
        break
    
    else:
        print("Opción inválida. Intente nuevamente.")