import pandas as pd 
# Crear datos (simulación estudiantes)
datos={"nombre":["Ana","Luis","Carlos","Sofia","Pedro"],
"edad":[30,70,18,21,22],
"nota":[3.5,4.2,2.8,4.8,3.0]

}
df =pd.DataFrame(datos)
print(df)
print("promedio de notas:",df["nota"].mean())
print("promedio de edad:",df["edad"].mean())


