def crearFacebook():
    print("Creemos una cuenta de Facebook ")
    usuario = input("Nombre de usuario\n> ")
    edad = float (input("Edad\n> "))
    ciudad = input("Ciudad en la que resides\n> ")
    pais = input("País\n> ")
    correo = input("Correo electrónico\n> ")
    cadena = (f"Tus datos son:\n"
              f"Usuario: {usuario}\nEdad: {edad}\nCiudad: {ciudad}\n"
              f"País: {pais}\nCorreo Electrónico: {correo}\n")
    return cadena

def crearTwitter():
    print("Creemos una cuenta de Twitter")
    usuario = input("Nombre de usuario\n> ")
    apellidos = input("Apellidos\n> ")
    edad = int(input("Escribe tu Edad\n> "))
    ciudad = input("Ciudad en la que vives\n> ")
    pais = input("País\n> ")
    idioma = input("ingresa tu idioma\n> ")
    correo = input("Correo electrónico\n> ")
    print(f"Tus datos personales son: \n"
          f"Usuario: {usuario}\nApellidos: {apellidos}\nEdad: {edad}\n"
          f"Ciudad: {ciudad}\nPaís: {pais}\nIdioma: {idioma}\n"
          f"Correo Electrónico: {correo}\n")


def crearWhatsapp():
    print("Creemos una cuenta de Whatsapp ")
    usuario = input("Nombre de usuario\n> ")
    numero = int(input("Número de teléfono\n> "))
    edad = int(input("Edad\n> "))
    ciudad = input("Ciudad en la que vives\n> ")
    pais = input("País\n> ")
    cadena = (f"Tus Datos son:\n"
              f"Usuario: {usuario}\nNúmero de teléfono: {numero}\n"
              f"Edad: {edad}\nCiudad: {ciudad}\nPaís: {pais}\n"
              f"-----------")
    return cadena


def crearTelegram():
    print("Creemos una cuenta de Telegram --*")
    usuario = input("Nombre de usuario\n> ")
    numero = int(input("Número de teléfono\n> "))
    ciudad = input("Ciudad en la que vives\n> ")
    pais = input("País\n> ")
    area_interes = input("Escrube un Area de tu interés\n> ")
    print(f"Tus datos personales son:\n"
          f"Usuario: {usuario}\nNúmero de teléfono: {numero}\n"
          f"Ciudad: {ciudad}\nPaís: {pais}\nÁrea de Interés: {area_interes}\n")


def crearSignal():
    print("Creemos una cuenta de Signal --*")
    usuario = input("Nombre de Usuario\n> ")
    numero = int(input("Número de teléfono\n> "))
    ciudad = input("Ciudad\n> ")
    pais = input("País\n> ")
    hobby = input("Hobby principal\n> ")
    cadena = (f"Tus datos personales son: \n"
              f"Usuario: {usuario}\nNúmero de teléfono: {numero}\n"
              f"Ciudad: {ciudad}\nPaís: {pais}\nHobby principla: {hobby}\n")
    return cadena


def crearInstagram():
    print("*-- Usted eligió la opción para crear una cuenta de Instagram --*")
    usuario = input("Ingrese su nombre de usuario\n> ")
    ciudad = input("Ingrese su ciudad\n> ")
    edad = int(input("Ingrese su edad\n> "))
    correo = input("Ingrese su correo electrónico\n> ")
    print(f"Tus datos personales son: \n"
          f"Usuario: {usuario}\nCiudad: {ciudad}\ndad: {edad}\n"
          f"Correo Electrónico: {correo}\n")


def crearFlickr():
    print("Creemos una cuenta de Flickr *")
    usuario = input("Nombre de usuario\n> ")
    correo = input("Correo electrónico\n> ")
    cadena = (f" Datos Ingresados\n"
              f"Usuario: {usuario}\nCorreo Electrónico: {correo}\n")
    return cadena


def obtenerMensaje(a):
    mensaje_final = ["Campaña con poca afluencia",
                     "Campaña moderada siga adelante", "Excelente campaña"]

    if ((a >= 1) and (a <= 5)):
        cadena = mensaje_final[0]
    else:
        if ((a >= 6) and (a <= 15)):
            cadena = mensaje_final[1]
        else:
            if (a >= 16):
                cadena = mensaje_final[2]
    return cadena


if __name__ == "__main__":
    bandera = True
    contador = 0
    while bandera:
        print("Opciones")
        opcion = int(input("> Inserte 1 para creara una cuenta de Facebook.\n"
                           + "> Ingrese 2 para creara una cuenta de Twitter.\n"
                           + "> Ingrese 3 para creara una cuenta de Whatsapp.\n"
                           + "> Ingrese 4 para creara una cuenta de Telegram.\n"
                           + "> Ingrese 5 para creara una cuenta de Signal.\n"
                           + "> Ingrese 6 para creara una cuenta de Instagram.\n"
                           + "> Ingrese 7 para creara una cuenta de Flickr.\n"))
        if (opcion == 1):
            contador += 1
            cuenta_facebook = crearFacebook()
            print(cuenta_facebook)
        else:
            if (opcion == 2):
                contador += 1
                crearTwitter()
            else:
                if (opcion == 3):
                    contador += 1
                    cuenta_whatsapp = crearWhatsapp()
                    print(cuenta_whatsapp)
                else:
                    if (opcion == 4):
                        contador += 1
                        crearTelegram()
                    else:
                        if (opcion == 5):
                            contador += 1
                            cuenta_signal = crearSignal()
                            print(cuenta_signal)
                        else:
                            if (opcion == 6):
                                contador += 1
                                crearInstagram()
                            else:
                                if (opcion == 7):
                                    cuenta_flickr = crearFlickr()
                                    print(cuenta_flickr)
                                else:
                                    print("Opción incorrecta")
        salida = input("Ingrese 'salir' si desea salir del ciclo o diguite"
                       " 1 para crear otra cuenta\n> ")
        if (salida == "salir"):
            bandera = False
    print(obtenerMensaje(contador))