import numpy as np
import pandas as pd
import os

def list_available_csv_files():
    csv_files = [f for f in os.listdir() if f.endswith('.csv')]
    return csv_files

class HopfieldNetwork:
    def __init__(self, num_neurons):
        """Inicializa una instancia de la red de Hopfield con el numero de neuronas y crea una matriz de pesos inicializada con ceros."""
        self.num_neurons = num_neurons
        self.weights = np.zeros((num_neurons, num_neurons))

    def train(self, patterns):
        """Entrena la red de Hopfield con patrones dados.
        
        Args:
            patterns: Un arreglo de patrones de entrada.
        """
        for pattern in patterns:
            """Itera sobre los patrones de entrada y actualiza los pesos de la red en función de estos patrones."""
            pattern = pattern.reshape(-1, 1)
            self.weights += np.dot(pattern, pattern.T)
            np.fill_diagonal(self.weights, 0)

    def update(self, pattern):
        """Aplica un patrón de entrada a la red y recupera un patrón de salida.
        
        Args:
            pattern: El patrón de entrada a aplicar a la red.
        
        Returns:
            El patrón de salida recuperado de la red.
        """
        pattern = pattern.reshape(-1, 1)
        for _ in range(self.num_neurons):
            """Itera sobre la red para actualizar el patron de entrada."""
            activation = np.dot(self.weights, pattern)
            pattern = np.sign(activation)
        return pattern

if __name__ == "__main__":
    print("Bienvenido al programa de la red de Hopfield")

    results_folder = 'results'
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    while True:
        choice = input("¿Desea ejecutar el programa con la red de Hopfield? (si/no): ").strip().lower()
        if choice == "si":
            # Listar archivos CSV disponibles en el directorio
            csv_files = list_available_csv_files()
            if not csv_files:
                print("No se encontraron archivos CSV en el directorio actual.")
                continue

            # Mostrar la lista de archivos CSV disponibles
            print("Archivos CSV disponibles:")
            for i, filename in enumerate(csv_files):
                print(f"{i + 1}. {filename}")

            # Solicitar al usuario que elija un archivo CSV
            try:
                selected_index = int(input("Seleccione el número del archivo CSV que desea analizar: ")) - 1
                if 0 <= selected_index < len(csv_files):
                    selected_csv = csv_files[selected_index]
                else:
                    print("Número fuera de rango. Por favor, seleccione un número válido.")
                    continue
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número válido.")
                continue

            try:
                # Cargar datos de entrada desde el archivo CSV seleccionado
                data = pd.read_csv(selected_csv)

                # Crear una instancia de la red de Hopfield
                num_neurons = len(data.columns)
                hopfield_net = HopfieldNetwork(num_neurons)

                # Entrenar la red con los patrones del archivo CSV
                patterns = data.values
                hopfield_net.train(patterns)

                # Probar la red con un patrón de entrada
                input_pattern = np.array([1, -1, 1, -1, 1])
                # Reemplaza esto con tu patrón de entrada
                output_pattern = hopfield_net.update(input_pattern)

                # Generar un nombre único para el archivo de salida dentro de la carpeta 'results'
                output_filename = os.path.join(results_folder, 'salida.csv')
                count = 1
                while os.path.exists(output_filename):
                    output_filename = os.path.join(results_folder, f'salida{count}.csv')
                    count += 1

                # Guardar el patrón de salida en un archivo CSV dentro de la carpeta 'results'
                output_data = pd.DataFrame(output_pattern.reshape(1, -1).astype(int), columns=data.columns)
                output_data.to_csv(output_filename, index=False)

                print(f"Resultado guardado en '{output_filename}'")
            except Exception as e:
                print("Error: Se produjo un error durante la corrida. Detalles del error:")
                print(e)
        elif choice == "no":
            print("Muchas Gracias")
            break
        else:
            print("Opción no válida. Por favor, elija 'si' o 'no'.")