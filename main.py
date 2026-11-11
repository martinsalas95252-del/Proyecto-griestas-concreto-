import os

print("="*50)
print("CONTEO DE IMÁGENES - PROYECTO GRIETAS")
print("="*50)

ruta_negative = "database/Negative"
ruta_positive = "database/Positive"


try:
    total_negative = len(os.listdir(ruta_negative))
    total_positive = len(os.listdir(ruta_positive))
    
    print(f"Imágenes de concreto sano (Negative): {total_negative}")
    print(f"Imágenes con grietas (Positive): {total_positive}")
    print(f"Total de imágenes en el dataset: {total_negative + total_positive}")

except FileNotFoundError:
    print("\n[Aviso]: Asegúrate de que las carpetas 'Negative' y 'Positive' estén dentro de la carpeta 'database'.")

print("="*50)