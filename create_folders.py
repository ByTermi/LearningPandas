import os
import json

# Configuración de los temas exactos según tus enlaces
temas = [
    "Adding-and-Dropping-Rows-Columns",       # Parte 6
    "Sorting-Data",                           # Parte 7
    "Updating-Rows-and-Columns",              # Parte 8
    "Handling-Missing-Values",                # Parte 9
    "Data-Cleaning",                          # Parte 10
    "Advanced-Indexing",                      # Parte 11
    "Handling-Outliers"                       # Parte 12
]

start_index = 6

def get_notebook_cells(part_num):
    """
    Devuelve la lista de celdas con contenido educativo específico para cada tema.
    """
    
    # --- CONFIGURACIÓN COMÚN ---
    header_md = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"# Pandas Parte {part_num}\n",
            f"## {temas[part_num-6].replace('-', ' ')}\n",
            "En este notebook exploraremos los conceptos clave de este tema basándonos en las mejores prácticas."
        ]
    }
    
    setup_code = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import pandas as pd\n",
            "import numpy as np"
        ]
    }

    # --- CONTENIDO ESPECÍFICO POR CAPÍTULO ---
    
    # PARTE 6: Adding and Dropping Rows/Columns
    if part_num == 6:
        return [
            header_md, setup_code,
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## 1. Añadir y Eliminar Columnas\n", "Podemos crear nuevas columnas basadas en otras existentes o borrarlas con `drop`."]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "data = {'First': ['Corey', 'Jane', 'John'], 'Last': ['Schafer', 'Doe', 'Doe'], 'Email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com']}\n",
                    "df = pd.DataFrame(data)\n",
                    "\n",
                    "# Combinar columnas\n",
                    "df['Full_Name'] = df['First'] + ' ' + df['Last']\n",
                    "df"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Eliminar columnas (inplace=True para guardar cambios)\n",
                    "df.drop(columns=['First', 'Last'], inplace=True)\n",
                    "df"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## 2. Añadir y Eliminar Filas\n", "Usamos `concat` para añadir y `drop` por índice para borrar."]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Añadir fila\n",
                    "new_row = pd.DataFrame({'Email': ['IronMan@avenge.com'], 'Full_Name': ['Tony Stark']})\n",
                    "df = pd.concat([df, new_row], ignore_index=True)\n",
                    "df"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Eliminar fila por índice\n",
                    "df.drop(index=3, inplace=True)\n",
                    "df"
                ]
            }
        ]

    # PARTE 7: Sorting Data
    elif part_num == 7:
        return [
            header_md, setup_code,
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Ordenando Datos\n", "Uso de `sort_values` para columnas y `sort_index` para índices."]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "df = pd.DataFrame({\n    'Name': ['John', 'Jane', 'Bob', 'Alice'],\n    'Age': [25, 30, 22, 28],\n    'Salary': [50000, 60000, 45000, 55000]\n})\n",
                    "df"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Ordenar por una columna (descendente)\n",
                    "df.sort_values(by='Age', ascending=False)"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Ordenar por múltiples columnas\n",
                    "df.sort_values(by=['Age', 'Salary'], ascending=[True, False])"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Obtener los n valores más grandes\n",
                    "df.nlargest(2, 'Salary')"
                ]
            }
        ]

    # PARTE 8: Updating Rows and Columns
    elif part_num == 8:
        return [
            header_md, setup_code,
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Actualizando Datos\n", "Cómo modificar valores específicos y usar `apply`, `map`, y `replace`."]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "df = pd.DataFrame({'email': ['coreymschafer@gmail.com', 'janedoe@email.com', 'johndoe@email.com'], 'first': ['Corey', 'Jane', 'John'], 'last': ['Schafer', 'Doe', 'Doe']})\n",
                    "df.columns = [x.upper() for x in df.columns] # Renombrar columnas\n",
                    "df"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Modificar una fila completa\n",
                    "df.loc[2] = ['JohnSmith@email.com', 'John', 'Smith']\n",
                    "\n",
                    "# Modificar un valor específico\n",
                    "df.at[2, 'LAST'] = 'Doe'\n",
                    "df"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Usar apply para aplicar funciones a series\n",
                    "df['EMAIL'] = df['EMAIL'].apply(lambda x: x.lower())\n",
                    "df"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Map y Replace para sustituir valores\n",
                    "df['FIRST'].map({'Corey': 'Chris', 'Jane': 'Mary'}) # Map convierte todo lo que no coincide a NaN\n",
                    "df['FIRST'].replace({'Corey': 'Chris', 'Jane': 'Mary'}) # Replace mantiene los valores originales si no hay coincidencia"
                ]
            }
        ]

    # PARTE 9: Handling Missing Values
    elif part_num == 9:
        return [
            header_md, setup_code,
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Manejo de Valores Faltantes (NaN)\n", "Identificar, eliminar o rellenar datos faltantes."]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "people = {\n    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], \n    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], \n    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],\n    'age': ['33', '55', '63', '36', None, None, 'Missing']\n}\n",
                    "df = pd.DataFrame(people)\n",
                    "\n",
                    "# Estandarizar valores nulos personalizados\n",
                    "df.replace(['NA', 'Missing'], np.nan, inplace=True)\n",
                    "df"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Eliminar filas con NaN\n",
                    "df.dropna(axis='index', how='any') # Elimina si hay AL MENOS un NaN"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Rellenar NaN con un valor\n",
                    "df.fillna(0)\n",
                    "# O rellenar columna específica con la media (previa conversion de tipos)\n",
                    "# df['age'] = df['age'].astype(float)\n",
                    "# df['age'].fillna(df['age'].mean())"
                ]
            }
        ]

    # PARTE 10: Data Cleaning
    elif part_num == 10:
        return [
            header_md, setup_code,
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Limpieza de Datos\n", "Eliminar duplicados y limpiar datos de tipo string."]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "data = {'Name': [' John ', 'Jane', 'John ', 'Bob'], 'Age': [25, 30, 25, 22], 'City': ['NY', 'LA', 'NY', 'Chicago']}\n",
                    "df = pd.DataFrame(data)\n",
                    "df"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Limpiar espacios en blanco en strings\n",
                    "df['Name'] = df['Name'].str.strip()\n",
                    "df"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Identificar duplicados\n",
                    "df.duplicated()"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Eliminar duplicados\n",
                    "df.drop_duplicates(keep='first', inplace=True)\n",
                    "df"
                ]
            }
        ]

    # PARTE 11: Advanced Indexing
    elif part_num == 11:
        return [
            header_md, setup_code,
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Indexación Avanzada\n", "Trabajar con MultiIndex y jerarquías."]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Crear datos con jerarquía\n",
                    "arrays = [\n",
                    "    ['Bar', 'Bar', 'Baz', 'Baz', 'Foo', 'Foo', 'Qux', 'Qux'],\n",
                    "    ['One', 'Two', 'One', 'Two', 'One', 'Two', 'One', 'Two']\n",
                    "]\n",
                    "tuples = list(zip(*arrays))\n",
                    "index = pd.MultiIndex.from_tuples(tuples, names=['First', 'Second'])\n",
                    "df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])\n",
                    "df"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Seleccionar datos usando loc en MultiIndex\n",
                    "df.loc['Bar']"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Seleccionar nivel más profundo\n",
                    "df.loc[('Bar', 'Two')]"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Stack y Unstack para pivotar niveles\n",
                    "df.unstack()"
                ]
            }
        ]

    # PARTE 12: Handling Outliers
    elif part_num == 12:
        return [
            header_md, setup_code,
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Manejo de Outliers (Valores Atípicos)\n", "Detección usando métodos estadísticos como IQR o Z-Score."]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "df = pd.DataFrame({'Data': [10, 12, 12, 13, 12, 11, 14, 13, 15, 10, 10, 10, 100, 12, 14, 13, 12, 10, 10, 11]})\n",
                    "df.plot(kind='box') # Visualización rápida"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Método IQR (Rango Intercuartílico)\n",
                    "Q1 = df['Data'].quantile(0.25)\n",
                    "Q3 = df['Data'].quantile(0.75)\n",
                    "IQR = Q3 - Q1\n",
                    "\n",
                    "lower_bound = Q1 - 1.5 * IQR\n",
                    "upper_bound = Q3 + 1.5 * IQR\n",
                    "\n",
                    "print(f\"Rango aceptable: {lower_bound} a {upper_bound}\")"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Filtrar outliers\n",
                    "df_clean = df[(df['Data'] >= lower_bound) & (df['Data'] <= upper_bound)]\n",
                    "df_clean"
                ]
            }
        ]
    
    return [header_md, setup_code]

def create_notebook_file(title, part_num):
    """Estructura JSON completa del notebook"""
    return {
        "cells": get_notebook_cells(part_num),
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.5"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def main():
    base_path = os.getcwd()
    
    print(f"Creando estructura para 7 partes (06-12) en: {base_path}")
    print("-" * 40)

    for i, tema in enumerate(temas):
        num = start_index + i
        
        folder_name = f"{num:02d}-{tema}"
        file_name = f"{tema}.ipynb"
        
        # Crear carpeta
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        # Crear archivo notebook
        file_path = os.path.join(folder_path, file_name)
        content = create_notebook_file(tema, num)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=1)
        
        print(f"✅ Generado: {folder_name}/{file_name} (Con contenido específico)")

    print("-" * 40)
    print("¡Proceso finalizado con éxito!")

if __name__ == "__main__":
    main()