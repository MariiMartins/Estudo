import pandas as pd

def compare_excel_structure(model_file, new_file):
    def_model = pd.read_excel(model_file)
    def_new = pd.read_excel(new_file)

    if set(def_model.columns) == set(def_new.columns):
        print("A estrutura dos arquivos é a mesma!")
    
    else:
        missing_columns = set(def_model.columns) - set(def_new.columns)
        additional_columns = set(def_new.columns) - set(def_model.columns)

        if missing_columns:
            print(f"As colunas {missing_columns} estão faltando no novo arquivo.")
        if additional_columns:
            print(f"As colunas {additional_columns} foram adicionadas no novo arquivo.")

compare_excel_structure('model.xlsx', 'new_data.xlsx')