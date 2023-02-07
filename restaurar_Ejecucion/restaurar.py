import pickle

def save_data(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_data(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# Ejemplo de uso
data = input("Ingrese sus datos: ")
filename = 'data.pkl'
save_data(data, filename)
loaded_data = load_data(filename)
print("Datos restaurados: ", loaded_data)
