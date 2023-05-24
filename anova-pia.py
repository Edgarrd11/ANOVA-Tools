import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import statsmodels.api as sm
import os 


def one_way_anova(df, ind:str, dep:str):
    # Código para ANOVA Unidireccional
    print("Realizando ANOVA Unidireccional...")
    anova = ols(f'{ind} ~ {dep}', data=df).fit()
    an = sm.stats.anova_lm(anova, type=2)
    while True:
        print(an)
        user_input = input("Presiona Enter para volver al menu... ")
        if user_input == "":
            print("Volviendo al menu...")
            break
        else:
            print("Tecla invalida, intenta de nuevo.")
    
    

def two_way_anova(df,ind:str, dep:str, dep2:str):
    # Código para ANOVA Bidireccional
    print("Realizando ANOVA Bidireccional...")
    anova = ols(f'{ind} ~ {dep}+{dep2}', data=df).fit()
    an = sm.stats.anova_lm(anova, type=2)
    while True:
        print(an)
        user_input = input("Presiona Enter para volver al menu... ")
        if user_input == "":
            print("Volviendo al menu...")
            break
        else:
            print("Tecla invalida, intenta de nuevo.")

def two_way_inte_anova(df,ind:str, dep:str,dep2:str):
    # Código para el bidireccional con interaccion
    print("Realizando ANOVA Bidireccional...")
    anova = ols(f'{ind} ~ {dep}+{dep2}+{dep}*{dep2}', data=df).fit()
    an = sm.stats.anova_lm(anova, type=2)
    while True:
        print(an)
        user_input = input("Presiona Enter para volver al menu... ")
        if user_input == "":
            print("Volviendo al menu...")
            break
        else:
            print("Tecla invalida, intenta de nuevo.")

def clear_terminal():
    # Clear the terminal screen
    if os.name == 'posix':  # for UNIX/Linux/Mac OS
        _ = os.system('clear')
    elif os.name == 'nt':  # for Windows
        _ = os.system('cls')
    else:
        # Fallback for other operating systems
        print('\n' * 100)
def main():
    clear_terminal()
    print("\n--- Programa de ANOVA ---")
    file = str(input("Ingrese el nombre de su archivo de Excel: "))
    df = pd.read_excel(f'./tablas/{file}.xlsx')
    while True:
        cols = df.columns.to_list()
        nombres_col = ' - '.join(str(item) for item in cols)
        clear_terminal()
        print("\n--- Menú de ANOVA ---")
        print("1. ANOVA Unidireccional")
        print("2. ANOVA Bidireccional")
        print("3. ANOVA Bidireccional con interaccion")
        print("5. Nueva tabla de Excel")
        print("6. Mostrar tabla")
        print("7. Salir")

        choice = input("Selecciona una opción (1-6): ")

        if choice == '1':
            clear_terminal()
            print(f'Lista de variables:\n {nombres_col}')
            ind = str(input("Ingrese variable independiente: "))
            dep = str(input("Ingrese variable dependiente: "))
            clear_terminal()
            one_way_anova(df,ind,dep)

        elif choice == '2':
            clear_terminal()
            print(f'Lista de variables:\n {nombres_col}')
            ind = str(input("Ingrese variable independiente: "))
            dep = str(input("Ingrese la primera variable dependiente: "))
            dep2 = str(input("Ingrese la segunda variable independiente:"))
            clear_terminal()
            two_way_anova(df,ind,dep,dep2)
        
        elif choice == '3':
            clear_terminal()
            print(f'Lista de variables:\n {nombres_col}')
            ind = str(input("Ingrese variable independiente: "))
            dep = str(input("Ingrese la primera variable dependiente: "))
            dep2 = str(input("Ingrese la segunda variable independiente:"))
            clear_terminal()
            two_way_inte_anova(df,ind,dep,dep2)
       
        elif choice == '5':
            clear_terminal()
            file = str(input("Ingrese el nombre de su archivo de Excel: "))
            df = pd.read_excel(f'./tablas/{file}.xlsx')
       
        elif choice == '6':
            clear_terminal()
            while True:
                print(df)
                user_input = input("Presiona Enter para volver al menu... ")
                if user_input == "":
                    print("Volviendo al menu...")
                    break
                else:
                    print("Tecla invalida, intenta de nuevo.")
            
        elif choice == '7':
            print("\nSaliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == '__main__':
    main()