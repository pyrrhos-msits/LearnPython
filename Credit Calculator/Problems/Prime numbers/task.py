prime_numbers = [n for n in range(2, 1001) if all(n % i != 0 for i in range(2, n - 1))]






# natürliche Zahl teilbar durch 1 oder durch sich selbst
# 1 ist keine Primzahl, da nur durch 1 teilbar