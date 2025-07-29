
import random

# soma = lambda x, y : x + y
# resultado = soma(10, 5)

# print(resultado)

cor = lambda: """rgb({}, {}, {})""".format(random.randint(0, 255),
                                       random.randint(0, 255),
                                       random.randint(0, 255))

resultado = cor()
print(resultado)



