class Modulo7Functions:
    def __init__(self, lista):
        self.lista = lista

    def es_primo(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def valor_modal(self):
        frecuencias = {}
        for num in self.lista:
            if num in frecuencias:
                frecuencias[num] += 1
            else:
                frecuencias[num] = 1
        moda = max(frecuencias, key=frecuencias.get)
        return moda

    def convertir_grados_celsius_a_fahrenheit(self, grados_celsius):
        return (grados_celsius * 9/5) + 32

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)