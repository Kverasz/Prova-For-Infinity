salario = float(input("Digite seu salario: "))
dias_atraso = int(input("Digite o numero de dias de atraso: "))

if dias_atraso > 5:
    multa_total = (salario * 2 )/ 100 
    for dia in range(6,dias_atraso):
        multa = (salario * 2 )/ 100 
        multa_total += multa
    print(f"Sua multa foi: R${multa_total:.2f}")
else:
    print("Finalizado")

