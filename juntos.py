from colorama import Back, init
import os, time, pyfiglet, stdiomask, progressbar, math
from colorama import *
import os , colorama
from art import * 
import math
import os , msvcrt , progressbar ,time ,stdiomask ,getpass , pyfiglet
import progressbar , time



# VARIABLES
nombre= ""
passw= ""
num= 0

#PROCESOS
texto2=  pyfiglet.figlet_format(text="JOTA", justify= "center", width=70,  font="slant")
print(Fore.CYAN)

# TIME.SLEEP(5)
time.sleep(2)
print(texto2)
from ascii_magic import AsciiArt
print(Fore.YELLOW)
print("╔═══════════════════════════════════════════════════════════════════════════╗")
print("║                                                                           ║")
print("║                                                                           ║")
print("║               ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓                ║")
print("║               ▓                                          ▓                ║")
print("║               ▓           ╔═══════════════════╗          ▓                ║")
print("║               ▓           ║                   ║          ▓                ║")
print("║               ▓           ║                   ║          ▓                ║")
print("║               ▓           ╚═══════╗   ╔═══════╝          ▓                ║")
print("║               ▓                   ║   ║                  ▓                ║")
print("║               ▓                   ║   ║                  ▓                ║")
print(Fore.BLUE)        
print("║               ▓                   ║   ║                  ▓                ║")
print("║               ▓          ╔════════╝   ║                  ▓                ║")
print("║               ▓          ║            ║                  ▓                ║")
print("║               ▓          ╚════════════╝                  ▓                ║")
print("║               ▓                                          ▓                ║")
print("║               ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                ║")
print("║              ▒___│___│___│___│___│___│___│___│___│___│___│▒               ║")
print("║             ▒___│___│___│___│___│___│___│___│___│___│___│__▒              ║")
print(Fore.RED)
print("║            ▒___│___│___│___│___│___│___│___│___│___│___│___│▒             ║")
print("║           ▒   │   │   │   │   │           │   │   │   │   │  ▒            ║")
print("║          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒           ║")
print("║                                                                           ║")
print("║                                                                           ║")
print("╚═══════════════════════════════════════════════════════════════════════════╝")
print(Fore.RESET)
print ("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║           USUARIO:__________________                                      ║
║                                                                           ║
║                                                                           ║
║           CONTRASEÑA:__________________                                   ║
║                                                                           ║
║                                                                           ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
""")
nombre= input("ingrese el nombre de usuario: ")
passw= input("ingrese el nombre de contraseña: ")
init()

print("INICIANDO EL SISTEMA...")
def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = (Back.LIGHTBLUE_EX+' '+Back.RESET) * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")


numbers = [x * 5 for x in range(1000,2000)]


results = []


for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))
os.system("cls")
# TIME.SLEEP(5)
print(texto2)
print (f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║           USUARIO:  {nombre}                                              ║
║                                                                           ║
║                                                                           ║
║           CONTRASEÑA:{passw}                                              ║
║                                                                           ║
║                                                                           ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
""")
if (nombre== "joshue" and passw== "123" ):
    print(f"Bienvenido al sistema... {nombre}")
    print("")
    while True:
        os.system("cls")
        print(Fore.RED)
        print ("""
           ╔════════════════════════════════════════════════════════╗
           ║            ♣♣♣ MENU PRINCIPAL ♣♣♣                      ║
           ║      1. EMAIL                                          ║
           ║      2. NUMEROS USUARIO                                ║
           ║      3. NUMEROS POSITIVOS                              ║
           ║      4. TITULO                                         ║
           ║      5. GRAFICO                                        ║
           ║      6. SALIRR                                         ║
           ╚════════════════════════════════════════════════════════╝
           """)
        print(Fore.RESET)
        op= input("Ingrese una opcio [1-6]: ")
        match op:
            case '1':
                def validar(email):
                    caracterBuscado="@"
                    emailValido=False
                    for c in email:
                        if c==caracterBuscado:
                            return True
                    return False

 
                direccion=input("Tu email: ")
                if validar(direccion):
                    print("Dirección válida")
                else:
                    print("Dirección inválida")
                input("Presione una tecla para regresar del sistema..")
            case '2':
                def sumaDigitos(numero):
                    suma=0
                    while numero!=0:
                        digito=numero%10
                        suma=suma+digito
                        numero=numero//10
                    return suma

 
                num=int(input("Número a procesar: "))
                while num!=0:
                    print("Suma:",sumaDigitos(num))
                    num=int(input("Número a procesar: "))
                input("Presione una tecla para regresar del sistema..")
            case '3':
                def sumaDigitos(numero):
                    suma=0
                    while numero!=0:
                        digito=numero%10
                        suma=suma+digito
                        numero=numero//10
                    return suma
                cantidad=0
                mayor=-1
                numero=int(input("Número positivo: "))
                while numero>=0:
                    suma=sumaDigitos(numero)
                    if suma > mayor:
                        mayor=suma
                        n_mayorsuma=numero
                    if suma < 10:
                        cantidad+=1
                    numero=int(input("Número positivo: "))
                print("Sumatoria de dígitos de",n_mayorsuma,":",mayor)
                print("Cantidad con sumatoria menor a 10:",cantidad)
                
                input("Presione una tecla para regresar del sistema..")
            case '4':
                def letra_mayuscula():
                    global repite1 
                    repite1 = True
                    while repite1:
                        os.system("cls")
                        try:
                            frase = str(input(f"{Fore.YELLOW}Ingrese la frase: "))
                            while (frase ==""):
                                frase = str(input(f"{Fore.YELLOW}Ingrese la frase: "))
                            fr = frase.title()
                            repite1 = False
                        except:
                            print(f"{Fore.RED} ..Error debe ingresar solo numeros enteros y sin espacios.. {Fore.RESET}")
                            msvcrt.getch()
                    print(f"{Fore.RED}La frase convertida es:  {fr} {Fore.RESET}")
                letra_mayuscula()
                input("Presione una tecla para regresar del sistema..")
            case '5':
                
                    
                    print(Fore.BLUE+"""Ingrese el  rango de números de 20 a 40 solo números pares:
                    """+Fore.RESET)
                    num=int(input(Fore.GREEN + "Ingrese un numero: " + Fore.RESET))
                    print(Fore.RED + "  "+"*"*(num-4) + Fore.RESET)
            
                    print(Fore.CYAN + "/"+"↓"*(num-2)+"\\" + Fore.RESET)
            
                    print(Fore.CYAN + "→  "+"+"+"-"*(num-8)+"+"+"  ←" + Fore.RESET)
            
                    print(Fore.CYAN + "→  "+"|"+"▒"*((num//2)-5)+f"{num}"+"▒"*((num//2)-5)+"|"+"  ←")
            
                    numf=(num//4)
                    i = ((num//2)-6)
                    k = (num//4)-1
                    j = 4
                    l = 0
                    for f in range(1, numf):
                        print( "→  "+"|"+"▒"*i+" "*j+"▒"*i+"|"+"  ←")
                        i-=1
                        j+=2
                    i+=1
                    j-=2  
                    # Completa la parte inferior de la figura
                    for f in range(numf-1, 0, -1):
                        print( "→  "+"|"+"▒"*i+" "*j+"▒"*i+"|"+"  ←")
                        i+=1
                        j-=2
        
                    print(Fore.CYAN + "→  "+"|"+"▒"*((num//2)-5)+f"{num//2}"+"▒"*((num//2)-5)+"|"+"  ←" + Fore.RESET)
        
                    print(Fore.CYAN + "→  "+"+"+"-"*(num-8)+"+"+"  ←" + Fore.RESET)
        
        
                    print(Fore.CYAN + "\\"+"↑"*(num-2)+"/" + Fore.RESET)
        
                    print(Fore.RED + "  "+"*"*(num-4) + Fore.RESET)
                    
                
                
                    input("Presione una tecla para regresar del sistema..")
            case '6':
                print("SALIENDO DEL SISTEMA")
                break
            case _:
                print("Opcion incorrceta")
                input("Presione una tecla para regresar del sistema..")
        

  
    
    
        
else:
    print("Credenciales incorrectas...ADIOS")