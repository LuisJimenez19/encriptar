 # Encriptacion super wow
 


BARRA_INCLINADA = "\\"
TAM_MAX_CLAVE = 26

def obtenerModo(): # pide al usuario que desea hacer
    while True:
        print('¿Deseas encriptar o desencriptar un mensaje?')
        modo = input().lower()
        if modo in 'encriptar e desencriptar d'.split():
            return modo
        else:
            print('Ingresa "encriptar" o "e" o "desencriptar" o "d"')
 
def obtenerMensaje(): #funcion que pide mensaje al usuario
    
    print("Desea cargar un mensaje: (si o no)")
    carga_mensaje = input("").lower().startswith("s")
    
    while carga_mensaje:   # si hay un archivo de texto con el cual desea trabajar
        
        nombre_archivo = input("ingrese el nombre del archivo de texto: ").lower()
        
        ruta = input("Escribe la ruta de acceso a la carpeta donde quieres guardar o cargar los mensajes. ")
        
        
        try:
            archivo = open(ruta + BARRA_INCLINADA + nombre_archivo + ".txt", "r")
            mensaje = archivo.read()
            archivo.close()
            print("-"* len(mensaje))
            print(f"este es el mensaje: {mensaje}")
            print("-"* len(mensaje))
            return mensaje
        except FileNotFoundError:
            print("No hay archivos con ese nombre, verifique que esta ingresando bien el nombre \n")
            intentar_de_nuevo = input("desea crear un archivo nuevo?: (si o no) \n").lower().startswith("s")
            
            if intentar_de_nuevo:
                break
            
            
        
    print('Ingresa tu mensaje:')
    return input()
 
def obtenerClave(): #Funcion que le pide al usuario la clave para encriptar el mensaje
    clave = 0
    while True:
        print(f'Ingresa el número de clave (1-{TAM_MAX_CLAVE})')
        try:
            clave = int(input())
        except ValueError:
            print("ingresa un número.")
            
        if (clave >= 1 and clave <= TAM_MAX_CLAVE):
            return clave
        elif clave == 27:
            return clave
 
def obtenerMensajeTraducido(modo, mensaje, clave):  #funcion que desencripta o encripta el mensaje
    if modo[0] == 'd':
        clave= -clave
    traduccion = ''
    

 
    for simbolo in mensaje:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += clave
 
            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
 
            traduccion += chr(num)
        else:
            traduccion += simbolo
    return traduccion 
 
 
def guardar_mensaje_encriptado(): #funcion que crea el archivo tecto y lo guarda
    
    guardar = input("desea guardar el mensaje en un archivo de texto: ").lower().startswith("s")
    
    if guardar:
        nombre_archivo = input("ingrese el nombre del archivo: ").lower()
        ruta = input("Escribe la ruta de acceso a la carpeta donde quieres guardar o cargar los mensajes. ")
        archivo = open( ruta + BARRA_INCLINADA + nombre_archivo+".txt", "w")
        archivo.write(mensaje_encriptado)
        archivo.close()
        print("Mensaje guardado exitosamente. ")
        
    else:
        print("Dirigiendose al menú principal.. ")
    
    
def realizar_de_nuevo(): #funcion que le pregunta al usuario si desea haer algo mas
    
    de_nuevo = input("Desea hacer algo mas: ").lower().startswith("s")
    
    return de_nuevo
    

    
    
#inicio del programa
centinela = True
descripcion = "Programa para encriptar un mensaje."
print(descripcion)
print("-" * len(descripcion))
while centinela:
   
    
    modo = obtenerModo() #Almacena lo que el usuario desea hacer

    mensaje = obtenerMensaje() # Almacena el mensaje 
    clave = obtenerClave() # Almacena la clave para decifrar el mensaje
    
    print('Tu texto traducido es:')
    mensaje_encriptado = obtenerMensajeTraducido(modo, mensaje, clave)
    print(mensaje_encriptado)
    
    if clave == 27:
        for i in range(1,TAM_MAX_CLAVE+1):
            print("clave"+str(i)+": "+obtenerMensajeTraducido(modo,mensaje, i))
        continue

    guardar_mensaje_encriptado()

    if realizar_de_nuevo():
        centinela = True
    else:
        dudas = input("si funciono como esperaba: (si o no): ").lower().startswith("s")
        
        if dudas:
            valoracion = input("cuentenos su experiencia: ")
            print("muchas gracias valorenos en la Play Store o App store")
            print("saliendo del programa.♥")
            centinela = False
        else:
            print("Si el mensaje no se descifro bien asegurese de que la clave sea igual que al momento de encriptarlo  ")
            intentar = input("desea intentar de nuevo (si o no): ").lower().startswith("s")
            
            if intentar:
                centinela = True
            else:
                print("saliendo del programa.")
                centinela = False
        
        
        