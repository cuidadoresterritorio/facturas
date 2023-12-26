import pandas as pd
import os, pdfkit

def create_directory(directory_name):
    new_directory = directory_name
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)


def generate_invoices(df):
    with open('./template.html', 'r') as file:
        template_html = file.read()

    # Iterar sobre cada fila y generar la carta en HTML
    for index, fila in df.iterrows():
        nombre_archivo = f"{fila['id']}_factura.pdf"
        ruta_archivo = os.path.join('./facturas', nombre_archivo)
        
        factura_equivalente = template_html.format(Nombre=fila['name'], Apellido=fila['lastname'])
#        pdfkit.from_string(factura_equivalente, ruta_archivo,
#                            configuration=pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf'))
        pdfkit.from_string(factura_equivalente, ruta_archivo)
        print(index)


if __name__ == "__main__":
    create_directory('facturas')
    df = pd.read_csv('clientes1.csv')
    generate_invoices(df)

    
