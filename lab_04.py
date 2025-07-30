
numero_parcelas = 0
valor_total_pago = 0

def calcular_valor_pagamento(valor_prestacao, numero_dias_atraso):
    """Calcula o valor a ser pago com base no valor informado de parcela e dias em atraso"""
    if numero_dias_atraso == 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * 0.001 * numero_dias_atraso
        return valor_prestacao + multa + juros

while True:
    valor_prestacao = float(input("Informe o valor da prestação:"))

    if valor_prestacao == 0:
        break

    
    numero_dias_atraso = int(input("Informe o número de dias em atraso:"))
    valor_a_ser_pago = calcular_valor_pagamento(valor_prestacao, numero_dias_atraso)

    numero_parcelas = numero_parcelas + 1
    valor_total_pago = valor_total_pago + valor_a_ser_pago

    print(f"Valor a ser pago: {valor_a_ser_pago}")

print(f"Foram pagas {numero_parcelas} parcelas no total de {valor_total_pago}")
