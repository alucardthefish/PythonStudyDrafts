import pandas as pd
import numpy as np

excel_file = "ExtractoConsolidadoBancolombia2023.xlsx"

df_first_shift = pd.read_excel(excel_file, sheet_name="Movimiento2023")

# print(df_first_shift)
# print(df_first_shift["DESCRIPCIÓN"])

# print(df_first_shift.columns)

df_first_shift["DESCRIPCIÓN"] = df_first_shift["DESCRIPCIÓN"].str.strip()
df_first_shift["VALOR"] = df_first_shift["VALOR"].str.replace(',', '').astype(float)

total_values = df_first_shift.groupby("DESCRIPCIÓN", as_index=False)["VALOR"].sum()

# Filter negative and positive values
expenses = total_values[total_values["VALOR"] < 0].copy()
income = total_values[total_values["VALOR"] > 0].copy()

# Calculate total amount for each
expenses_total = expenses["VALOR"].sum()
income_total = income["VALOR"].sum()

# Add a row with the total amount to each DataFrame
expenses_index = len(expenses) + 2
print(f"{expenses_index = }")
income_index = len(income) + 2
print(f"{income_index = }")
expenses.loc[expenses_index] = ["Total", expenses_total]
income.loc[income_index] = ["Total", income_total]

# Write the results to different sheets in the same Excel file
with pd.ExcelWriter("ExtractoTotalesReporte.xlsx") as writer:
    total_values.to_excel(writer, sheet_name="General", index=False)
    expenses.to_excel(writer, sheet_name="Egresos o gastos", index=False)
    income.to_excel(writer, sheet_name="Ingresos o pagos", index=False)

# total_value.to_excel("ExtractoTotales.xlsx", index=False)

print("Reporte generado exitosamente en archivo 'ExtractoTotalesReporte.xlsx'")
