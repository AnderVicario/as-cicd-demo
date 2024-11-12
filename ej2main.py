def suma(a, b):
    """Función que devuelve la suma de dos números."""
    return a + b

# Variables de ejemplo
num1 = 5
num2 = 10

# Mostrar el resultado de la suma
print(f"La suma de {num1} y {num2} es: {suma(num1, num2)}")

def incrementar_saldo(saldo):
    """Función que incrementa el saldo en 1000."""
    return saldo + 1000

# Test para incrementar_saldo
def test_incrementar_saldo():
    assert incrementar_saldo(500) == 1500