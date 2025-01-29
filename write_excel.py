import openpyxl
import pandas as pd

def write_df(sheet, df, start_row, start_col):
    for y in range(len(df)):
        for x in range(len(df.columns)):
            sheet.cell(row=start_row + y,
                       column=start_col + x,
                       value=df.iloc[y, x])
            
def write_excel(data, j):
    df5 = pd.DataFrame(data)
    wb = openpyxl.load_workbook("spectrum.xlsx")
    sheet = wb["Sheet1"]
    write_df(sheet, df5, (j-1)*4+2, 2)
    wb.save("spectrum.xlsx")