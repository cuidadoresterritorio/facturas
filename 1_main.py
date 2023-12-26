# Genera la lista completa de todas las facturas por cada miembro del equipo

import pandas as pd
import os, pdfkit

def show_menu():
    print("---- Menú ----")
    print("1. Clemencia")
    print("2. Andres")
    print("3. Sergio")
    print("4. Julian")
    print("5. Erika")
    print("0. Salir")


def create_directory(directory_name):
    new_directory = directory_name
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)


def generate_invoices(df, directory):
    print(df.shape)
    with open('./1_template/index.html', 'r') as file:
        template_html = file.read()

    # Iterar sobre cada fila y generar la carta en HTML
    for index, fila in df.iterrows():
        nombre_archivo = f"{fila['# factura']}_factura.pdf"
        ruta_archivo = os.path.join(f'./{directory}', nombre_archivo)
        
        factura_equivalente = template_html.format(Nombre=fila['Nombre del beneficiario'], 
                                                   Valor=(lambda x: "{:,.0f}".format(x))(fila['Valor en COP$']*1000),
                                                   Telefono=fila['Telefono'],
                                                   Concepto=fila['Descripción del gasto/Evidencia'],
                                                   Fecha=fila['Fecha Efectiva de Pago\n(DD/MM/AA)'],
                                                   NIT=fila['NIT'],
                                                   Direccion=fila['Ciudad y direccion del Beneficiario'])
        pdfkit.from_string(factura_equivalente, ruta_archivo)



if __name__ == "__main__":
    show_menu()
    member = input("Escribe el nombre: ")

    create_directory(member)
    df = pd.read_csv('./facturacion.csv')

    filter= df[df['ejecutor del gasto'] == member]
    print(filter.shape)
        
    generate_invoices(df=filter, directory=member)


    
