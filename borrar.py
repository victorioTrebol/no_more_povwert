import numpy as np
from scipy.interpolate import interp1d
from scipy.signal import resample
import matplotlib.pyplot as plt

# Supongamos que los vectores están definidos aquí
vector_corto = np.array([1., 0.86666667, 0.73333333, 0.6, 0.6, 0.68, 0.76, 0.84, 0.92, 1.])
vector_largo = np.array([1., 0.98, 0.96, 0.94, 0.92, 0.9, 0.88, 0.86, 0.84, 0.82, 0.8, 0.78, 0.76, 0.74, 0.72,
                         0.7, 0.68, 0.66, 0.64, 0.62, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6,
                         0.6, 0.62105263, 0.64210526, 0.66315789, 0.68421053, 0.70526316, 0.72631579, 0.74736842, 0.76842105, 0.78947368,
                         0.81052632, 0.83157895, 0.85263158, 0.87368421, 0.89473684, 0.91578947, 0.93684211, 0.95789474, 0.97894737, 1.])

# Interpolación del vector corto para igualar la longitud del vector largo
x_corto = np.linspace(0, 1, len(vector_corto))
x_para_interpolado = np.linspace(0, 1, len(vector_largo))
interpolador = interp1d(x_corto, vector_corto, kind='cubic')
vector_corto_interpolado = interpolador(x_para_interpolado)

# Remuestreo del vector largo para igualar la longitud del vector corto original
vector_largo_remuestreado = resample(vector_largo, len(vector_corto))

# Generación de gráficas
plt.figure(figsize=(14, 6))

# Vector largo: Original vs. Remuestreado
plt.subplot(1, 2, 1)
plt.plot(np.linspace(0, 1, len(vector_largo)), vector_largo, label='Original Largo', marker='o')
plt.plot(np.linspace(0, 1, len(vector_corto)), vector_largo_remuestreado, label='Remuestreado', marker='x')
plt.title('Vector Largo: Original vs. Remuestreado')
plt.legend()

# Vector corto: Original vs. Interpolado
plt.subplot(1, 2, 2)
plt.plot(np.linspace(0, 1, len(vector_corto)), vector_corto, label='Original Corto', marker='o')
plt.plot(np.linspace(0, 1, len(vector_largo)), vector_corto_interpolado, label='Interpolado', marker='x')
plt.title('Vector Corto: Original vs. Interpolado')
plt.legend()



print(f"Longitud del vector corto original: {len(vector_corto)}")
print(f"Longitud del vector corto interpolado (igual al vector largo original): {len(vector_corto_interpolado)}")
print(f"Longitud del vector largo original: {len(vector_largo)}")
print(f"Longitud del vector largo remuestreado (igual al vector corto original): {len(vector_largo_remuestreado)}")



print("#### ANALISIS 50 PARAMETROS ####")
diferencias_interpolado = []
diferencias_largo = []
for index,value in enumerate(zip(vector_corto_interpolado,vector_largo)):
    if index > 0 :
        diferencia_interpolado = value[0]/ vector_corto_interpolado[index-1]
        diferencia_largo = value[1]/ vector_largo[index-1]
        diferencias_interpolado.append(diferencia_interpolado)
        diferencias_largo.append(diferencia_largo)
        print("valor "+index.__str__()+ " diferencia_interpolado: "+str(diferencia_interpolado))
        print("valor "+index.__str__() + " diferencia_largo:       "+str(diferencia_largo))
        porcentaje_diff = abs(diferencia_interpolado - diferencia_largo) / diferencia_largo
        print("porcentaje_diff: "+str(porcentaje_diff*100))
        print("---------------------")

plt.subplot(2, 2, 1)
plt.plot(np.linspace(0, 1, len(diferencias_largo)), diferencias_largo, label='diferencias vector largo original', marker='o')
plt.plot(np.linspace(0, 1, len(diferencias_interpolado)), diferencias_interpolado, label='diferencias inerpolado', marker='x')
plt.title('Vector Largo: Original vs. Remuestreado')
plt.legend()

plt.show()
