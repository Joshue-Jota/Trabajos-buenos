from colorama import Back, init
import os, time, pyfiglet, stdiomask, progressbar, math, statistics, random
from tabulate import tabulate
from colorama import *
from prettytable import PrettyTable
import math, random, os, getpass, colorama, pyfiglet, colorama
import time, pyfiglet, stdiomask
from colorama import Fore, Style
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
print(Fore.LIGHTYELLOW_EX)
print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⡤⣴⠞⠛⢒⡷⠾⣽⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡠⠊⠁⡴⠁⠀⢠⠎⠀⠀⠈⠙⢦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡞⠀⠀⠈⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⡀⠀⠀⠲⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🔥 🔥⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠈⠋⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠑⠦⠤⠤⠤⠔⣺⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣹⠳⠤⣀⣀⣀⣀⣀⣠⠴⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⠷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⠎⣸⠀⠘⣦⠀⠀⠀⠀⠀⢐⠒⠀⠀⠀⠀⠀⠀⢸⡦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀
⠀⢀⠜⠁⠀⡇⠀⠀⠈⢳⡀⠀⠀⠀⣘⡉⠃⠀⠀⠀⠀⣠⣾⢳⠀⠀⠀⠀⢀⣀⣀⡤⣤⣤⣤⣶⠶⠾⠿⠟⢹⡟
⣠⠏⠀⠀⣸⣀⣀⣀⠤⠤⠿⣖⠚⠉⢹⢻⠀⠀⠀⣠⠞⠁⣿⣼⠀⠀⣸⣿⣽⣿⠶⠟⠛⣭⡶⠆⠀⠀⠀⠀⡿⠀
⠛⠚⠉⠉⢹⠉⠀⠀⠀⠀⠀⠈⠳⣄⢸⣼⢀⡤⠚⠁⠀⠀⣿⣧⠀⢠⢧⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀
⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⠵⠏⠀⠀⠀⠀⠀⠉⠉⢀⢟⣾⠏⠀⠀💢💢💢⠀⠀⠀⢠⠃⠀⠀
⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⠤⠴⠒⡟⡟⡜⠀⠀⠀⠀⠀💢⠀⠀⠀⠀⠀⠏⠀⠀⠀
⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⣀⣀⡤⠤⠖⠒⢉⣉⣥⠤⠒⣻⣿⣾⡽⠀⠀💢⠀💢⠀⠀⠀⠀⢠⡞⠀⠀⠀⠀
⠀⠀⣀⣀⠧⠤⠔⠒⠒⠉⠉⢡⣤⠖⠒⠊⠉⢁⣀⠭⣿⣿⣿⢳⠿⠁⠀⠀⠀⠀⠀⠀⣀⣠⣤⣴⠟⠁⠀⠀⠀⠀
⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢿⣶⣤⣛⡿⣟⣛⣿⢶⠇⠎⠀⠀⠀⣀⣤⣴⣶⠯⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⣿⣿⣯⣦⣤⣶⠾⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      """)
print(Fore.RESET)
print(Fore.LIGHTCYAN_EX)
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
print(Fore.RESET)
nombre= input(Fore.RED+"ingrese el nombre de usuario: "+Fore.RESET)
passw= input(Fore.RED+"ingrese el nombre de contraseña: "+Fore.RESET)
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
        print("""
              ⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠""")
        print(Fore.LIGHTBLACK_EX)
        print(f"""
                        █▄██▄█                                                    █▄██▄█
                        ▐█┼██▌█▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▄██▄█▄█▄█▐█┼██▌
                        ▐████▌║               {Fore.RED}  Menú de usuario {Fore.RESET}                 ║▐████▌
                        ▐████▌║──────────────────────────────────────────────────║▐████▌ 
                        ▐████▌║        {Fore.CYAN}        1. ASIGNATURAS DEL CURSO  {Fore.RESET}        ║▐████▌
                        ▐████▌║        {Fore.CYAN}        2. POLINDROMO             {Fore.RESET}        ║▐████▌
                        ▐████▌║        {Fore.CYAN}        3. NUMERO DE VECES DE VOCALES  {Fore.RESET}   ║▐████▌
                        ▐████▌║        {Fore.CYAN}        4. MUESTRA DE NUEMEROS         {Fore.RESET}   ║▐████▌
                        ▐████▌║        {Fore.CYAN}        5. SUMA ACUMULADA              {Fore.RESET}   ║▐████▌                              
                        ▐████▌║        {Fore.CYAN}        6. 20 NUMEROS ALEATORIOS       {Fore.RESET}   ║▐████▌
                        ▐████▌║        {Fore.CYAN}        7. 10 VALORES ALEATORIOS       {Fore.RESET}   ║▐████▌
                        ▐████▌║        {Fore.CYAN}        8. DATOS DE UNA PERSONA        {Fore.RESET}   ║▐████▌
                        ▐████▌║──────────────────────────────────────────────────║▐████▌
                        ▐████▌║        {Fore.CYAN}        9. SALIR                       {Fore.RESET}   ║▐████▌
                              ╙──────────────────────────────────────────────────╜ """)

    
        print(Fore.RESET)
        print(Fore.LIGHTYELLOW_EX)
        op= input("Ingrese una opcio [1-9]: "+Fore.LIGHTCYAN_EX)
        print(Fore.RESET)
        match op:
            case '1':
                asignaturas = ['Mateáticas','Física','Química','Historia','Lenguaje']
                matriz_aprobadas = []
                notas = []
                aprobado = []
                i=0
                prom=0
                def promedio(notas):
                    prom = sum(notas)/len(notas)
                    return prom
                
                while i<len(asignaturas):
                    try:
                        print(Fore.LIGHTCYAN_EX)
                        n = float(input(f"Ingrese la calificación que obtuvo en {asignaturas[i]}: "))
                        print(Fore.RESET)
                        if n>=0 and n<=10:
                            notas.append(n)
                            if n<8:
                                aprobado = [asignaturas[i],notas[i],"Reprobado"]
                                matriz_aprobadas.append(aprobado)
                            i+=1
                        else:
                            print("La calificación es de 0 a 10")
                    except:
                        
                        print("Ingrese números, utilice el punto para decimales")
                print(Fore.YELLOW)
                print(tabulate(matriz_aprobadas,headers=['Asignatura','Calificación','Estado']))
                print("El promedio total es: ",promedio(notas))
                print(Fore.CYAN)
                print("""
                        ⠀⠀⠀⠀⠀⠀⠐⢶⣒⠢⠤⣀⡀⠀⠀⠀⠠⣄⠀⠀⠀⠀⠀⢹⢻⡌⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣄⠑⢮⣕⣢⣄⡀⢹⣿⠢⡀⠀⠀⢸⠈⣿⣆⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣷⣄⠙⠻⣿⣯⣷⣯⢧⠈⠲⣄⢸⠀⣿⣿⡄⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣧⡀⠙⢿⣿⣿⡎⣇⣧⡈⢺⡀⣿⣿⣷⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣄⠀⠙⢿⣧⠸⣿⣷⡀⢱⣿⣿⣿⡆⢹⠀⣆⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⢀⣀⠤⠔⠒⠒⠛⠻⢿⣿⣧⠀⠈⢻⠀⢿⣿⣷⡀⢿⣿⣿⡇⠸⣷⣿⡀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⣀⡤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⣠⠬⣙⡣⠄⢸⠀⠸⣿⣿⣷⠘⣿⣿⡇⠀⠿⢹⡷⠀⠀⠀⠀⠀⠀
                        ⠀⠚⠛⠶⠶⣶⣶⣤⣤⣀⡐⠲⢤⣄⣀⠙⠺⢿⣶⣾⠀⠀⢻⣿⣿⡇⢻⣿⡇⠀⢀⣿⣧⣤⣤⣀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠈⢙⣿⣿⣿⣿⣶⣬⣙⣿⠦⠤⠽⠟⣀⠴⠚⠉⢻⣧⠈⢿⣇⣀⠀⠀⣉⣉⡒⠤⣀⠀⠀
                        ⠀⠀⠀⠀⢀⣴⡾⠟⣋⡽⠿⢿⣿⡿⠉⠀⠀⣀⡴⠊⠁⠀⠀⠐⣺⣿⠦⠚⠛⢬⡹⣿⣿⣿⣿⣿⣾⣷⣄
                        ⠀⠀⢀⣴⠗⠁⠀⢈⣠⣤⣴⣶⡟⢠⠄⡴⣫⠞⠁⡀⢀⣤⣒⣭⣿⡿⠔⢦⠀⢸⣷⡘⢿⣿⣟⠋⠉⠉⠙
                        ⠀⢠⣾⠏⣠⣴⣾⣿⣿⣿⣿⡿⢀⡞⢀⣼⡟⠀⡴⠁⣾⡾⠿⠿⢿⣤⣦⢸⠄⣾⣿⣷⡘⣿⡙⢧⡀⠀⠀
                        ⠀⣾⠷⠚⠉⠁⢾⡟⣡⠈⢻⡇⣼⢠⣿⢿⠀⡼⣥⡾⠋⠀⠀⠀⠀⠀⢸⢸⢰⣿⣿⣿⣷⣿⡿⠀⠀⠀⠀
                        ⠈⠁⠀⠀⠀⠀⠀⠉⠣⢄⣀⣷⣿⢸⠇⢸⢸⣱⣟⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡿⣿⣾⡶⣾⣾⡟⠀⠑⠤⠀⣀⠔⠊⠀⣿⣿⣿⣿⣿⣾⡏⠛⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⢹⣿⣇⠹⣿⣿⣗⣄⢀⡀⠀⣠⣴⠮⣿⠟⢱⣿⠃⡾⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢎⢿⣧⠀⠹⠭⠷⠾⠉⢓⠋⠭⠥⠜⠃⠀⣿⢋⠜⠁⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢆⠀⠀⠀⠀⠀⠼⠇⠀⠀⠀⢀⡜⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣱⢤⡀⠀⠉⠟⠃⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⠴⠇⠀⢉⠒⢤⣀⣠⣴⡿⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣴⣾⡟⠁⠀⠀⠀⠈⢣⡀⠉⢉⡅⠀⠿⠻⣷⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣆⠀⠀⢀⣈⣦⣙⣄⠀⠀⠀⣤⢀⡨⠝⢿⣿⣿⣷⡆⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠈⣿⠟⠉⠛⢿⣿⣿⣿⣿⣿⣿⣉⠁⠀⠀⠀⠈⠉⠒⠦⠛⠁⠀⠀⠈⣿⣿⣿⣿⠳⡀⠀⠀⠀
                        ⠀⠀⠀⠀⢰⠃⡤⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⣿⣿⣿⣿⠀⢹⡄⠀⠀
                        ⠀⠀⠀⠀⢻⠈⠁⠀⠀⢀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⢻⠀⠀⠀⣿⣿⣿⣿⣆⢸⠃⠀⠀
                        ⠀⠀⠀⢀⡜⢿⣆⡴⠋⠀⠉⠢⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠘⠂⠀⢠⣿⣿⣿⣿⣿⣾⡆⠀⠀
                        ⠀⠀⠀⢸⠀⢀⡏⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣤⣤⣠⣾⣿⣿⣿⣿⣿⡟⣷⠀⠀
                        ⠀⠀⠀⢸⠃⢸⠁⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢷⢸⠀⠀
                        ⠀⠀⢠⡏⠀⢸⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣼⠀⠀
                        ⠀⠀⣼⠀⠀⢻⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣾⡇⠀⠀
                        ⠀⠀⣿⠀⠀⢘⠆⠀⠀⠀⠀⠠⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢵⠖⠁⠣⠀⠀
                      """)
                print(Fore.RESET)     
                print(Fore.LIGHTRED_EX)   
                input("Presione una tecla para regresar del sistema..")
                print(Fore.RESET)
                
            case '2':
                def es_palindromo(texto):
                    texto = texto.replace(" ", "").lower()
                    longitud = len(texto)
                    for i in range(longitud // 2):
                        if texto[i] != texto[longitud - i - 1]:
                            return False
                    return True

                def contar_letras(texto):
                    texto = texto.replace(" ", "").lower()
                    vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
                    consonantes = {}
                    for letra in texto:
                        if letra in vocales:
                            vocales[letra] += 1
                        elif letra.isalpha() and letra not in consonantes:
                            consonantes[letra] = 1
                        elif letra.isalpha():
                            consonantes[letra] += 1
                    print(Fore.RED)
                    print("Vocales:")
                    print(Fore.RESET)
                    for vocal, cantidad in vocales.items():
                        print(f"{vocal}: {cantidad}")
                    
                    print(Fore.RED)
                    print("Consonantes:")
                    print(Fore.RESET)
                    for consonante, cantidad in consonantes.items():
                        print(f"{consonante}: {cantidad}")

                def contar_palabras(texto):

                    palabras = texto.split()
                    cantidad_palabras = len(palabras)
                    print(f"El texto tiene {cantidad_palabras} palabras.")

                entrada = input(Fore.LIGHTYELLOW_EX+"Ingrese una palabra, frase o párrafo: "+Fore.RESET)
                print(Fore.CYAN)
                if es_palindromo(entrada):
                    print("El texto ingresado es un palíndromo.")
                else:
                    print("El texto ingresado no es un palíndromo.")
                if len(entrada.split()) == 1:
                    print("Conteo de letras:")
                    contar_letras(entrada)
                if len(entrada.split()) > 1:
                    contar_palabras(entrada)
                print(Fore.RESET)
                print(Fore.RED)
                print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀                            ⣀⣤⣶⠶⠟⠛⠛⠛⠛⠛⠻⠶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⢀⣤⣶⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⣠⣾⡿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⣴⡿⠋⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⣼⣿⠅⢀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⢰⣿⠁⠄⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⣼⡏⠀⠀⢿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⣿⡇⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⢹⡇⠀⠀⣀⣿⣦⠴⠶⠛⠛⠛⠛⠛⢻⠶⠶⠶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⢸⣿⣠⡿⠋⠁⠀⠀⠀⠀⠀⢀⡤⠊⠁⠀⣠⠔⠉⠈⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠈⣿⣿⠁⠀⠀⠀⠀⠀⣠⠔⠁⠀⢀⡠⠚⠁⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⠿⠶⠶⠶⠶⢶⣤⣤⣀⠀⠀⠀⠀⠀
                            ⠀⢹⣯⠀⠐⠀⢀⡠⠊⠁⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⣰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣄⡀⠀
                            ⠀⣾⡿⣇⣀⠔⣉⣤⡴⠖⠛⠛⠉⠉⠙⠛⠳⢦⣤⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣆
                            ⣸⣿⠀⣻⣷⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻
                            ⣿⠿⣶⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾
                            ⣿⡀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣦⣤⣴⣶⡶⠶⠤⠤⣄⠀⢀⣠⣾⡟
                            ⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡿⢿⣿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠿⠛⠁⠀
                            ⠀⠻⢷⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣤⣤⣶⢶⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠈⣿⠛⢛⣫⣯⣭⣭⣭⡽⠿⠿⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⣿⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⢠⣿⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⣼⡇⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⢠⣿⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⠉⢹⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⣾⠇⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⣸⡟⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⠀⠀⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⣿⡇⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⣾⡟⠀⠀⢰⣿⠿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠛⠿⣷⣄⣹⣆⠀⠀⣀⣀⣀⣼⠟⠁⠀⠀⢸⣿⣄⡙⢷⣄⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠙⠻⠿⠿⢿⣷⣶⣶⣶⣶⣾⠿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                      """)
                print(Fore.LIGHTRED_EX) 
                input("Presione una tecla para regresar del sistema..")
                print(Fore.RESET)
            case '3':
                frase = str(input("Ingrese una palabra o frase: ")).lower()
                palabras = frase.split()

                for palabra in palabras:
                    letraa=0
                    letrae=0
                    letrai=0
                    letrao=0
                    letrau=0


                    for letra in palabra:
                        if letra=='a':
                            letraa+=1
                        elif letra=='e':
                            letrae+=1
                        elif letra=='i':
                            letrai+=1
                        elif letra=='o':
                            letrao+=1
                        elif letra=='u':
                            letrau+=1
                    print(f"""Palabra: {palabra}   
                          A = {letraa}     E = {letrae}     I = {letrai}     O = {letrao}     U = {letrau} \n""")

                print(Fore.YELLOW)
                print("""  
                            █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█
                            █                            █
                            █    ORDENAR PALABRA/FRASE   █
                            █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█
                            █           1.- A - Z        █
                            █           2.- Z - A        █
                            █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█
                """)
                print(Fore.RESET)
                op = input("Ingrese una opcion [1-2]: ")
                match op:
                    case '1':
                        for palabra in palabras:
                            palabra_az = ''.join(sorted(palabra))
                            print(F"La palabra {palabra} ordenada de la A-Z: {palabra_az}")
                    case '2':
                        for palabra in palabras:
                            palabra_za = ''.join(sorted(palabra,reverse=True))
                            print(F"La palabra {palabra} ordenada de la A-Z: {palabra_za}")
                    case _:
                        print("Opción incorrecta")
                print(Fore.GREEN)
                print(""" 
                      ⠀⠀⠀⠀⠀⢀⣤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⢀⡼⠋⠀⣀⠄⡂⠍⣀⣒⣒⠂⠀⠬⠤⠤⠬⠍⠉⠝⠲⣄⡀⠀⠀
                    ⠀⠀⠀⢀⡾⠁⠀⠊⢔⠕⠈⣀⣀⡀⠈⠆⠀⠀⠀⡍⠁⠀⠁⢂⠀⠈⣷⠀⠀
                    ⠀⠀⣠⣾⠥⠀⠀⣠⢠⣞⣿⣿⣿⣉⠳⣄⠀⠀⣀⣤⣶⣶⣶⡄⠀⠀⣘⢦⡀
                    ⢀⡞⡍⣠⠞⢋⡛⠶⠤⣤⠴⠚⠀⠈⠙⠁⠀⠀⢹⡏⠁⠀⣀⣠⠤⢤⡕⠱⣷
                    ⠘⡇⠇⣯⠤⢾⡙⠲⢤⣀⡀⠤⠀⢲⡖⣂⣀⠀⠀⢙⣶⣄⠈⠉⣸⡄⠠⣠⡿
                    ⠀⠹⣜⡪⠀⠈⢷⣦⣬⣏⠉⠛⠲⣮⣧⣁⣀⣀⠶⠞⢁⣀⣨⢶⢿⣧⠉⡼⠁
                    ⠀⠀⠈⢷⡀⠀⠀⠳⣌⡟⠻⠷⣶⣧⣀⣀⣹⣉⣉⣿⣉⣉⣇⣼⣾⣿⠀⡇⠀
                    ⠀⠀⠀⠈⢳⡄⠀⠀⠘⠳⣄⡀⡼⠈⠉⠛⡿⠿⠿⡿⠿⣿⢿⣿⣿⡇⠀⡇⠀
                    ⠀⠀⠀⠀⠀⠙⢦⣕⠠⣒⠌⡙⠓⠶⠤⣤⣧⣀⣸⣇⣴⣧⠾⠾⠋⠀⠀⡇⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⣭⣒⠩⠖⢠⣤⠄⠀⠀⠀⠀⠀⠠⠔⠁⡰⠀⣧⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⢤⣀⣀⠉⠉⠀⠀⠀⠀⠀⠁⠀⣠⠏⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠒⠲⠶⠤⠴⠒⠚⠁⠀⠀
                      """)
                print(Fore.RESET)
                print(Fore.LIGHTRED_EX) 
                input("Presione una tecla para regresar del sistema..")
                print(Fore.RESET)
            case '4':
                def obtener_numeros():
                    while True:
                        print(Fore.RED)
                        numeros_str = input("Ingrese una muestra de números separados por comas: "+Fore.LIGHTBLUE_EX)
                        print(Fore.RESET)
                        numeros = numeros_str.split(",")
                        try:
                            numeros_float = [float(num) for num in numeros]
                            return numeros_float
                        except ValueError:
                            print("Error: Ingrese solo números separados por comas.")

                numeros = obtener_numeros()

                media = statistics.mean(numeros)
                desviacion_tipica = statistics.stdev(numeros)
                print(Fore.LIGHTYELLOW_EX)
                print("Media:", media)
                print("Desviación típica:", desviacion_tipica)
                print("""
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣶⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡟⠀⠀⠀⠀⣀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠟⠛⠿⣿⣷⡄⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⢠⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠘⣿⣷⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⢸⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⣀⣤⣤⣿⡿⠷⠶⣶⣶⠆⠀
                        ⠀⢠⣤⣤⣶⣶⣾⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⡟⠛⠋⢀⣠⣤⣶⠿⠛⠀⠀⠀
                        ⠀⠘⠿⣦⣄⡀⠀⠸⣿⣿⣦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⢶⣿⣿⣿⣿⠿⣿⣿⣛⣿⣿⡇⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠈⠙⠻⠷⣦⣌⣻⣿⡿⠿⢿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⡿⠿⠋⠀⠀⠀⠀⠀⣀⣀⣤⣴⡶⠾⠛⠋⣉⣴⠾⠋⠁⣿⣿⠀⠀⠉⠛⢿⣿⡇⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⢀⣴⡶⠟⠛⣿⣿⣿⣶⣶⣦⣤⣤⣭⣍⣉⣉⠉⠉⠉⠉⠉⠉⠀⠀⠀⣀⣀⣤⣤⣴⡶⠶⠛⠛⠋⠉⠁⢀⣠⣴⠟⠋⠁⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀
                        ⠀⠀⣠⣾⠟⠋⠀⠀⠀⣿⣿⡇⠈⠻⣧⣄⠀⠉⠉⠛⠛⠛⠛⠛⠿⣿⣿⡿⠿⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⢀⣤⣶⠟⠋⠀⠀⠀⠀⠀⠀⠀⣿⣿⣦⣀⠀⠀⠀⠀⠈⠻⣧⡀⠀⠀
                        ⠀⣰⡿⠁⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠈⠛⠿⣦⣄⡀⠀⠀⠀⣠⣾⠟⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤⣤⣤⣤⣽⣿⠆⠀
                        ⢸⡟⠀⠀⠀⢀⣀⣠⣴⣿⣿⠇⠀⠀⠀⠀⠀⠈⠙⠻⠷⣶⣾⣿⣁⣀⠀⠀⠙⢿⣶⣄⣀⣠⣶⠿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠈⣿⣿⠉⠀⠀⠀⠀⠀
                        ⣿⢁⣤⣶⠾⠛⠋⠉⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠋⠉⠉⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀
                        ⣿⣿⠋⠀⠀⠀⠀⠀⢰⣿⣿⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀
                        ⠉⠁⠀⠀⠀⠀⠀⢠⡿⣿⣿⠋⠉⠉⠛⠛⠛⠻⣷⠶⣶⡶⠶⠶⢶⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣿⣿⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⣰⡿⠃⣿⣿⡷⠶⢦⣤⣤⣤⣤⣿⣠⣾⣇⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠛⠙⣿⣿⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⣼⡟⠡⠀⣿⣿⡀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠙⠛⠛⠛⠛⠛⠛⠓⠒⠒⠒⠒⠒⠶⠶⠶⠶⠶⠶⢶⣶⣤⣤⣤⣤⣼⣿⡿⠀⠀⠀⠀⣿⣿⡄⠀⠀⠀⠀⠀
                        ⠀⠀⠀⢀⣾⠏⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡀⠀⠀⣰⣿⡟⢿⣄⠀⠀⠀⠀
                        ⠀⠀⠀⣾⠏⠀⠀⠀⠀⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠿⠟⠁⠈⣿⡀⠀⠀⠀
                        ⠀⠀⣼⡟⠀⠀⠀⠀⠀⠸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠋⠁⠀⠉⠉⠙⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡏⢻⣆⠀⠀⠀⠀⠀⢸⣷⠀⠀⠀
                        ⠀⠀⣿⠁⣰⡄⠀⠀⠀⣠⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡏⠀⠀⠀⠀⠀⠀⢹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠈⣿⡄⠀⠀⠀⠀⠈⣿⣆⠀⠀
                        ⠀⠀⣿⣴⠟⣷⡀⢠⣾⠟⠁⢻⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⠀⠀⠀⠙⣷⡀⠀⢠⣦⣤⣀⠛⣷⣤
                        ⠀⠀⣿⡏⠀⢹⣷⡿⠁⠀⠀⠀⠙⠿⣿⣷⣶⣶⣤⣴⣶⣶⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣶⣤⣀⣠⣤⣶⣿⣿⠟⠁⠀⠀⠀⠀⠀⠙⠿⣶⣼⣿⠉⠉⠉⠉⠉
                        ⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                      """)
                print(Fore.RESET)
                print(Fore.LIGHTRED_EX) 
                input("Presione una tecla para regresar del sistema..")
                print(Fore.RESET)
            case '5':
                lista_numeros = []
                print(Fore.LIGHTBLUE_EX)
                numeros=int(input("Ingrese un numero: "))
                print(Fore.RESET)
                lista_numeros.append(numeros)
                print(Fore.LIGHTRED_EX)
                decicion=input("¿desea añadir mas numeros? s/n: ")
                print(Fore.RESET)
                while decicion =='s':
                    print(Fore.LIGHTBLUE_EX)
                    numeros=int(input("Ingrese un numero: "))
                    print(Fore.RESET)
                    lista_numeros.append(numeros)
                    print(Fore.LIGHTRED_EX)
                    decicion=input("¿desea añadir mas numeros? s/n: ")
                    print(Fore.RESET)
                def suma_acumulada(numeros):
                    suma_acum = []
                    suma = 0
                    for num in numeros:
                        suma += num
                        suma_acum.append(suma)
                
                    pares = 0
                    impares = 0
                    primos = 0
                    for num in numeros:
                        if num % 2 == 0:
                            pares += 1
                        else:
                            impares += 1
                        if es_primo(num):
                            primos += 1
                    print(Fore.CYAN)
                    print("Suma acumulada:", suma_acum)
                    print("Números pares:", pares)
                    print("Números impares:", impares)
                    print("Números primos:", primos)
                
                def es_primo(num):
                    if num < 2:
                        return False
                    for i in range(2, int(num**0.5) + 1):
                        if num % i == 0:
                            return False
                    return True
                suma_acumulada(lista_numeros)
                print(Fore.RESET)
                print(Fore.LIGHTCYAN_EX)
                print("""
                    ⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⡴⠋⠀⣀⣤⣾⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⣴⣡⣴⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢀⣀⣤⣴⣶⠛
                    ⠐⠂⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⡟⢁⣀⣤⣶⣿⣿⣿⡿⠋⠁⠀
                    ⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀
                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠈⠫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀
                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣴⡶⣦⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⡀
                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⡏⠀⠈⠙⢿⣿⣿⣿⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⣀⣠⣤⣴⣶⡶⠟⠋⠀
                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⡿⠁⢸⡁⠀⠀⠀⠀⣿⣿⠃⠀⢹⣿⣿⡿⠉⠪⡙⢿⣿⣯⣴⣾⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀
                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠙⣿⣿⣿⣿⣿⠇⠀⠸⡁⠀⢠⠚⠉⣿⢯⠀⠀⠈⣿⣿⣷⠃⠀⠘⡄⢿⣿⣿⣿⣿⢟⣋⣀⠀⠀⠀⠀⠀⠀
                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⡿⠀⠀⠀⠀⠠⠇⠀⢸⠋⠀⠳⡀⠀⣿⡏⢸⠤⢤⡀⢸⣸⡿⠿⠿⠶⡶⠶⠶⣾⣏⣉⣛⡛⠃
                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⢄⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠹⡴⠏⢳⡎⠀⢠⠃⢰⡽⠀⠀⠀⠀⢱⠀⢆⠀⠀⠀⠀⠱⣤
                    ⣿⣿⣿⣿⣿⣿⣿⣿⠇⢸⠀⠙⢿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⢸⡇⠖⠁⢠⢾⢣⠀⠀⠀⠀⠸⡀⢸⠀⠀⠀⠀⠀⣿
                    ⣿⣿⣿⣿⣿⣿⣿⣿⣤⠚⠗⠂⠀⢻⣿⠀⠀⠀⠀⠀⠀⢼⣦⠀⠀⠀⢀⣠⡼⠎⠘⣷⠀⣴⠟⣏⢾⡀⠀⠀⠀⠀⡇⠈⡄⠀⠀⠀⠀⢨
                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠘⠀⠀⠀⠻⠄⢀⡀⠀⠀⠀⠈⠉⠀⢠⠴⠞⠋⢀⠀⠀⢿⡛⠉⠀⠘⢎⢧⠀⠀⠀⠀⢿⠀⠇⠀⠀⠀⠀⢸
                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠘⠿⠆⠀⣀⠀⠀⠀⠀⠀⠀⠀⠈⣞⣆⠀⣧⠀⠀⠀⠀⠈⢆⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠈
                    ⣿⣿⣿⣿⣿⣿⣿⣿⣭⡻⠿⣷⣀⠀⠀⠀⠀⢀⡀⠠⢾⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠆⠀⢀⡀⠀⠸⣆⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀
                    ⢉⣿⣿⣿⡿⠛⠿⢿⣿⠚⠓⠀⠙⢦⣀⠤⢖⠍⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⢠⠎⠀⠀⠀⢹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⣾⣿⣿⣿⣇⠀⠋⠀⢨⡛⠷⣄⠀⠊⠵⠊⠁⠀⠀⠀⠀⠀⠀⠰⣤⡀⠀⠀⠀⠀⢠⠃⠀⣰⠁⠀⠀⠀⠀⣾⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
                    ⣿⣿⣿⡿⠿⢷⣖⣀⠀⠙⠒⠚⠓⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣽⠄⠀⠀⢰⠏⠀⣠⠃⠀⠀⠀⠀⣼⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀
                    ⠉⠉⠁⠀⡴⢹⠋⠙⠢⡤⠤⢤⡔⢖⠛⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⢠⠃⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀
                    ⠀⠀⢀⢾⣡⡇⠀⠀⠸⡈⢢⣀⠙⢮⢆⠀⠈⠙⠒⠶⠶⠶⠶⠖⠖⠶⠖⠚⠃⠀⠀⡏⠀⠀⢀⣰⣾⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
                    ⠀⢠⣫⢷⡿⠁⠀⠀⠀⢱⡄⠳⡱⣄⠻⣧⡀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠘⠁⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
                    ⣰⢳⡿⠉⠀⠀⠀⠀⠀⠀⠹⡄⠙⠈⠳⣌⠻⣔⡲⠤⣀⡀⠀⠀⠀⠀⠀⠀⣀⣠⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⡀⠀⠀⠀
                    ⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⠈⠳⣜⢿⣿⣿⣿⣿⣷⣶⣮⣭⣽⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢠⠃⠀⠀⠀
                    ⠲⣿⣿⣦⢄⡀⠀⠀⠀⠀⠀⠀⠀⠱⠀⠀⠀⠈⠢⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⠃⠀⢀⠎⠀⠀⠀⠀
                    ⠘⣿⣿⣿⣷⣯⡲⢤⡀⠀⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣻⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢀⠎⠀⠀⠀⠀⠀
                    ⠀⢹⣿⣿⣿⣿⣿⣦⣌⠀⠀⠱⣄⢀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠯⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣠⠋⠀⠀⠀⠀⠀⠀
                    ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠈⢮⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣵⡝⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⠿⢿⣿⣿⣿⣿⣗⠀⠀⠀⠀⡠⠀⠀⠀⠀
                    ⠀⠸⣟⡛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣹⣦⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠢⡄⠀⢠⠞⠃⢀⠄⠤⠀
                    ⠀⠀⠹⡇⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠈⣷⣄⠓⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⡏⢢⡈⠻⣅⠢⢴⡁⠀⠀⠀
                    ⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⡿⠈⢦⡈⠳⢤⡀⠀⠀⠀⠀⠤⠤⠤⠤⠤⠤⠔⠒⡞⠋⢱⠙⡄⠳⡀⠈⠢⣄⠉⠓⠤⡀
                    ⠀⠀⠀⠈⡇⠀⠀⠀⠀⢠⠞⠀⠀⢀⡠⠤⢴⠧⣄⣀⠙⠤⢠⣑⡤⡤⠤⠤⠤⠬⠉⣩⢥⡁⠒⣺⠓⠒⣿⠃⢣⠀⠙⢄⠀⠈⠢⡀⠀⠈
                    ⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⢀⡤⠚⠁⠀⠀⠈⠀⠀⠀⠙⠻⢽⡛⣿⣿⣷⣤⡄⢀⠜⠁⠀⠈⣳⡅⠀⣰⠹⡀⠸⡀⠀⠈⢦⠀⠀⠈⢦⡀
                    ⠀⠀⠀⠀⣿⡄⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡏⠉⠀⠀⠀⡰⠁⠉⢱⡏⠀⡇⠀⢇⠀⠀⠈⠣⡀⠀⠀⠙
                    ⠀⠀⠀⠀⠸⢵⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠖⠒⠉⠉⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⣰⠁⠀⠀⡼⣇⠀⢱⡀⠸⡀⠀⠀⠀⠑⣄⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠣⡀⠀⠀⠀⠀⠀⠔⠊⠁⠀⠀⠀⠀⠀⠀⢸⢸⣿⣿⣿⣿⣇⠀⠀⠀⠣⣄⢀⡴⠁⠙⡄⠈⡇⠀⣷⠀⠀⠀⠀⠈⢆⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠈⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢼⣿⣿⣿⣿⣟⣄⠀⠀⠀⢀⠉⠀⠀⠀⣸⠀⢸⡀⢸⡀⠀⠀⠀⠀⠀⠃
                      """)
                print(Fore.RESET)
                print(Fore.LIGHTRED_EX) 
                input("Presione una tecla para regresar del sistema..")
                print(Fore.RESET)
            case '6':
                numeros = [random.randint(1, 100) for _ in range(20)]
                frecuencias = {}
                for num in numeros:
                    if num in frecuencias:
                        frecuencias[num] += 1
                    else:
                        frecuencias[num] = 1
                print(Fore.LIGHTYELLOW_EX)
                print("Números generados:"+Fore.CYAN, numeros)
                print(Fore.LIGHTYELLOW_EX)
                print("Frecuencias de cada número:")
                print(Fore.RESET)
                print(Fore.LIGHTCYAN_EX)
                for num, frecuencia in frecuencias.items():
                    print(f"{num}: {frecuencia} veces")
                print(Fore.RESET)
                print(Fore.LIGHTYELLOW_EX)
                print("""
                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⠛⠛⠛⠲⠦⣤⣤⣴⠶⠛⣋⣉⠉⠉⠛⠶⠶⢤⡤⠶⠚⠛⠉⠉⣁⣍⡙⠓⠶⣤⣤⣤⣤⣵⠶⠶⠶⢶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⢀⣴⣶⡄⠀⠀⠀⠈⣉⣹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠋⡍⠙⠇⠀⠀⠀⠀⠀⠀⣤⣄⠀⠀⠈⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⣠⡄⠘⠛⠋⠀⠀⠀⣀⣼⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠀⠀⠀⠻⢿⠃⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⠋⠀⠀⠀⠀⣀⣤⣾⣟⣉⠉⠙⠓⢦⣀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠟⠛⢷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⡶⠶⣶⣶⣿⣿⣿⢿⣿⣿⣿⣶⣄⠀⠙⢶⡀⠀⠀⠀⢠⡴⠋⢁⣤⣶⣶⣿⣿⣿⣿⣷⣶⡶⢶⣶⡶⠞⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⢀⣾⣿⣿⣹⣷⣾⣿⣷⣿⣏⢹⣿⣷⡄⠀⢻⡄⠀⣴⠋⢀⣴⣿⡿⢋⣽⣷⣿⣯⣭⡿⢻⣿⣦⠀⠙⢦⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡇⢀⣿⡿⣠⣾⣿⣿⣿⣿⠃⠀⠀⢹⣯⣻⣿⡄⠀⣿⣰⠃⢰⣿⡏⣻⣾⣿⣿⣿⣿⠋⠉⠙⣿⡙⣿⣷⡀⠈⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣾⣿⠁⣿⣿⣿⣿⣿⣿⣷⣤⣴⣿⣿⡿⢿⣿⠀⢸⡏⠀⣿⣿⢀⣿⣿⣿⣿⣿⣿⣄⣀⣠⣿⣿⠛⣿⡇⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣿⡟⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣿⣿⠀⢸⡇⠀⣿⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⡇⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠹⣿⣟⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣸⣿⠃⢀⣿⡇⠀⢻⣿⡄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣾⣿⠃⠀⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣇⠀⡽⣿⣷⡏⢻⣿⣿⣿⣿⡿⠟⢷⣌⣿⠏⢀⣼⠟⢿⡄⠈⢿⣷⣤⡿⢿⣿⣿⣿⣿⣿⣿⠋⣠⣿⠏⠀⣰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⡀⠈⠻⠿⣦⣾⣅⣀⣩⣤⣶⡿⠟⢁⣰⡟⣻⠀⢸⠻⣄⠀⠙⢿⣶⣄⣹⣟⣋⣉⣿⣬⣷⠿⠃⢀⣼⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠳⣤⣀⡀⠈⠉⠉⠉⠉⢁⣠⡴⠟⠋⠀⣿⠀⢸⠀⠘⠷⣤⣀⡈⠉⠛⠛⠛⠛⠛⠋⣀⣠⡴⠟⢡⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠉⠉⠛⠛⠛⠛⠋⡍⠉⠀⠀⠀⠀⣿⠀⢸⠀⠀⠀⠀⠉⠛⠓⠲⠶⠶⠶⠶⠞⠛⠉⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡖⠀⠀⠀⠀⠀⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⢸⣦⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⣿⣿⠀⢸⠿⣄⡀⠀⠀⠀⠀⢀⡞⠉⢻⣆⠀⠀⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⠋⣿⠀⢸⠀⠈⢷⡀⠀⠀⢀⡾⠀⠀⠀⢻⡀⢸⡇⢀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣧⠀⠀⣴⣶⣤⡄⠀⠀⢀⣼⠃⠀⠀⠀⡟⠀⢸⡇⠀⠈⡇⢠⠀⢸⠁⢀⣠⣄⣸⡇⠈⢀⡾⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⣿⠀⠀⠙⠻⠟⠃⠀⠀⢿⣍⡴⠀⠀⢀⡇⠀⢸⡇⠈⢷⣴⠟⠀⠘⢦⣌⠛⠿⠛⠀⠀⢀⡇⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⡷⠶⠚⠓⠲⠶⠶⢶⣶⠛⠓⠲⢶⣾⡇⠀⢸⣿⡦⢤⡤⠶⣾⡶⠶⣤⣤⣤⠶⣤⣀⣼⠃⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢻⡿⢿⣀⣀⣀⠀⠀⠀⠀⠀⠉⠳⠤⠜⣹⡇⠀⢸⡇⠱⣦⡤⠚⠉⠀⠀⠀⠀⠀⠀⠀⢹⢿⡶⠶⠋⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⡿⣯⣿⣿⣿⣿⠛⣿⣿⣿⣷⣾⣿⠃⠀⠈⣿⣶⣿⣾⡿⠶⣾⣷⣶⣶⣶⣶⢶⣾⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠤⠤⠾⣧⢸⡀⠈⠉⠉⠉⠁⠀⠈⠙⠉⠙⠛⣿⣄⠀⣰⡿⠛⠛⠛⠃⠀⠙⠛⠛⠛⠛⠋⠀⡏⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠸⣷⡤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣬⣭⣿⣯⣀⣀⣀⣀⣀⣤⣠⣤⣄⣤⣤⣄⣰⣧⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢇⠀⣿⠀⢰⣿⣤⣀⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⣽⣟⣛⡛⠛⣿⣿⠉⠉⣽⠇⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡌⣇⣿⠀⠀⠈⠉⢹⠛⢻⡋⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⣿⠛⣟⠛⠋⠀⠀⣿⣰⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⣹⡟⠀⠀⠀⠀⢸⡇⢾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢶⡏⠀⠀⠀⠀⢻⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠟⠃⠀⠀⠀⠀⢸⣏⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣽⡃⠀⠀⠀⠀⠸⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡅⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢸⡄⠀⠀⠀⠀⠀⠀⣤⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⣧⡀⣠⣾⠁⣸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡏⢸⣷⡄⠀⣀⣀⡀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⡀⢀⣀⣀⣀⣸⣿⣿⣿⣿⣷⣾⣿⣙⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣈⣛⣿⣛⣛⣛⣙⣛⣛⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣈⣻⣿⣿⣛⣻⣿⣿⣿⣛⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀
                      """)
                print(Fore.RESET)
                print(Fore.LIGHTRED_EX) 
                input("Presione una tecla para regresar del sistema..")
                print(Fore.RESET)
            case '7':
                lista_sim = ['¼', '*', '-', '+', '\\', '~', '@', '“', '‘', '╬']
                lista_num_alea = []

                def numeros_aleat():
                    while len(lista_num_alea) < 10:
                        numero = random.randint(0, 9)
                        if lista_num_alea.count(numero) < 2 and (not lista_num_alea or lista_num_alea[-1] != numero):
                            lista_num_alea.append(numero)
                    if 5 in lista_num_alea:
                        lista_num_alea.remove(5)
                        lista_num_alea.insert(len(lista_num_alea) // 2, 5)
                numeros_aleat()
                print(Fore.CYAN)
                print("Lista de números aleatorios:", lista_num_alea)
                print("Lista reemplazada:", end=" ")
                for num in lista_num_alea:
                    print(lista_sim[num], end=" ")
                print(Fore.RESET)
                print(Fore.YELLOW)
                print("""
                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠒⠒⠶⣤⣾⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣴⣿⣿⠃⢀⡤⠾⢶⣌⠙⠻⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⢫⣷⠉⢿⣿⣿⠀⣾⢧⣄⡀⠈⠓⣦⠀⠉⣙⢛⣛⣿⣷⢶⡀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢰⠿⡄⣸⣿⠏⠠⠿⠦⢤⣉⣛⣶⠏⠀⣰⣯⠉⠁⠀⠹⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀
                    ⡟⠁⠀⠈⠙⠲⠦⣄⣀⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⣠⠖⠋⠁⠀⣀⣀⣀⣀⣀⠀⠉⠏⢽⡛⢙⣮⣉⡓⠲⣴⠟⠲⣄⠀⠀⠀⠀⠀⠀⠀
                    ⠳⣄⠀⠀⠀⠀⠀⠀⠉⠉⠻⠿⣷⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣯⠆⣠⠖⠋⠉⡿⡄⠈⠉⠙⢦⡀⠀⢹⡏⠙⠻⠉⠛⠷⣟⠃⢸⡆⠀⠀⠀⠀⠀⠀
                    ⠀⠈⠓⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⢡⢾⢹⡀⠀⢠⠇⢹⡄⠀⠀⣼⣿⠓⠒⣿⠉⠙⢳⣦⠀⠈⣧⡼⠁⠀⢀⣤⣤⣄⡀
                    ⠀⠀⢀⡏⠀⡏⠙⠒⠲⠤⢤⡀⠀⠘⠉⠙⠛⢿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⡀⠀⠀⠀⢸⡃⣏⡼⠀⢧⠀⡞⠀⠀⢧⢀⡴⠁⢸⠀⣼⠋⡇⢀⡞⡏⢳⡀⡿⠀⣠⣾⣿⣿⣿⣿⣿
                    ⠀⠀⠀⣧⠀⢷⠀⠀⠀⠰⣄⢁⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⢧⡈⠻⠦⠼⣿⠥⠤⠤⠼⠿⠤⢤⣸⣟⡁⠀⣇⠞⠀⣇⢈⡇⢧⣸⣿⣿⡿⠛⠛⠛⠿
                    ⠀⠀⠀⠘⢦⣈⣳⣄⡤⠞⠋⠉⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣶⡓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢤⣄⣿⢟⡇⣸⣿⣿⣿⠁⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠈⠉⣽⠁⠀⠀⠀⢀⣀⠀⠀⠀⢰⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣮⣝⣻⡵⠋⣿⣿⣿⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠹⣤⣠⠔⠋⠉⠉⠉⠉⠉⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠉⠉⠀⠀⠀⠰⣤⣤⣤⣤⣶⠋⠁⠀⠀⠀⠀⠹⣿⣿⣇⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣦⠀⠀⠀⠀⠀⠀⢻⣿⣿⣧⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡆⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢻⣿⣿⡇⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⣼⣿⣿⡃⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⣿⣿⣷⣶⣤⣀⠀⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣧⠀⠀⣠⣾⣿⣿⡿⠃⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡻⠿⠟⢿⣿⣿⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠴⠒⠋⠉⠉⠿⠛⣿⠿⣿⠛⠿⠟⠁⢹⡄⠀⠀⠀⠈⠉⢸⠟⠙⡿⠛⠛⠛⠛⠛⠉⠁⠈⠙⢓⡦⣤⣏⠁⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏⣡⠶⠚⣀⣤⠀⠀⠀⠀⢀⣀⣁⡤⠤⠴⠚⠋⠀⠀⠀⠀⠀⠀⠈⠓⠶⠤⠤⣄⣀⠀⠀⠀⠐⠦⢤⣈⠙⢳⣈⣿⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠤⣏⣁⣠⠤⠴⠒⠋⠉⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠦⣤⣀⣀⣹⠦⠴⠏⠁⠀⠀⠀⠀⠀⠀
                      """)
                print(Fore.RESET)
                print(Fore.LIGHTRED_EX) 
                input("Presione una tecla para regresar del sistema..")
                print(Fore.RESET)
            case '8':
                personas = []


                def generar_correo(apellido, codigo,cedula):
                    letras = apellido.lower()
                    cedula1= random.sample(cedula,3)
                    cedula2= "".join(cedula1)
                    correo = f"{letras[0]}{letras[len(letras)//2]}{letras[-2:].upper()}->{codigo}{cedula2}@gmail.com"
                    return correo
                
                def registrar_persona(codigo, cedula, apellido, edad, estado):
                    correo = generar_correo(apellido, codigo,cedula)
                    persona = {'codigo': codigo, 'cedula': cedula, 'apellido': apellido, 'correo': correo, 'edad': edad, 'estado': estado}
                    personas.append(persona)
                    print("Persona registrada exitosamente.")
                
                def mostrar_personas_activas():
                    print(Fore.BLUE)
                    print("Personas Activas:")
                    personas_activas = [persona for persona in personas if persona['estado'] == 'Activo']
                    print(tabulate(personas_activas, headers='keys'))
                    print(Fore.RESET)
                
                def mostrar_personas_ordenadas_apellido():
                    print(Fore.GREEN)
                    print("Personas ordenadas por apellido:")
                    personas_ordenadas = sorted(personas, key=lambda x: x['apellido'])
                    print_table(personas_ordenadas)
                    print(Fore.RESET)
                
                def buscar_persona(cedula):
                    for persona in personas:
                        if persona['cedula'] == cedula:
                            print("Persona encontrada:")
                            print_table([persona])
                            return
                    print("Persona no encontrada.")
                
                def editar_persona(codigo):
                    for persona in personas:
                        if persona['codigo'] == codigo:
                            print("Editar persona:")
                            print_table([persona])
                            print("""
                                  Opcion 1: Cambiar cedula 
                                  Opcion 2: Cambiar apellido 
                                  Opcion 3: Cambiar edad 
                                  Opcion 4: Cambiar estado 
                                  """)
                            opcion8=input("Ingrese la opcion [1-4]: ")
                            match opcion8:
                                case '1':
                                    persona['cedula'] = input("Ingrese el nuevo cedula: ")
                                case '2': 
                                    persona['apellido'] = input("Ingrese el nuevo apellido: ")
                                case '3':
                                    
                                    persona['edad'] = int(input("Ingrese la nueva edad: "))
                                case '4':
                                    
                                    persona['estado'] = input("Ingrese el nuevo estado (Activo/Inactivo): ").capitalize()
                                case _:
                                    print("Opcion incorrrecta")
                            persona['correo'] = generar_correo(persona['apellido'], persona['codigo'],persona['cedula'])  # Actualizar correo
                            print("Persona editada exitosamente.")
                            return
                    print("Persona no encontrada.")
                
                def eliminar_persona(cedula):
                    global personas
                    personas = [persona for persona in personas if persona['cedula'] != cedula]
                    print("Persona eliminada exitosamente.")
                
                def print_table(personas):
                    if not personas:
                        print("No hay personas para mostrar.")
                        return
                    print("Código\tCédula\tApellido\tCorreo\t\t\t\tEdad\tEstado")
                    for persona in personas:
                        print(f"{persona['codigo']}\t{persona['cedula']}\t{persona['apellido']}\t{persona['correo']}\t{persona['edad']}\t{persona['estado']}")
                
                # Proceso
                
                while True:
                    print(Fore.CYAN)
                    print("""
                        --- Menú ---
                        1. Registrar persona
                        2. Mostrar personas activas
                        3. Mostrar personas en orden alfabético por apellido
                        4. Buscar persona por cédula
                        5. Editar persona
                        6. Eliminar persona
                        7. Salir""")
                    print(Fore.RESET)
                    print(Fore.RED)
                    opcion = input("Seleccione una opción: ")
                    print(Fore.RESET)
                    match opcion:
                        case '1':
                            os.system("cls")
                            codigo = len(personas) + 1
                            cedula = input("Ingrese la cédula de la persona: ")
                            apellido = input("Ingrese el apellido de la persona: ")
                            edad = int(input("Ingrese la edad de la persona: "))
                            estado = input("Ingrese el estado de la persona (Activo/Inactivo): ").capitalize()
                            registrar_persona(codigo, cedula, apellido, edad, estado)
                
                        case '2':
                            os.system("cls")
                            mostrar_personas_activas()
                            input()
                
                        case '3':
                            os.system("cls")
                            mostrar_personas_ordenadas_apellido()
                            input()
                
                        case '4':
                            os.system("cls")
                            cedula = input("Ingrese la cédula de la persona que desea buscar: ")
                            buscar_persona(cedula)
                            input()
                
                        case '5':
                            os.system("cls")
                            codigo = int(input("Ingrese la cédula de la persona que desea editar: "))
                            editar_persona(codigo)
                            input()
                
                        case '6':
                            os.system("cls")
                            cedula = input("Ingrese la cédula de la persona que desea eliminar: ")
                            eliminar_persona(cedula)
                            input()
                        
            case "_":
                input("Opción no válida presione enter para intentarlo de nuevo")
            case '9':
                print("SALIENDO DEL SISTEMA")
                break
            case _:
                print("Opcion incorrceta")
                input("Presione una tecla para regresar del sistema..")
    else:
        print("mal..")