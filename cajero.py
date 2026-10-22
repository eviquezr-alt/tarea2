


SALDO_INICIAL = 250000
RETIRO_MINIMO = 5000
RETIRO_MAXIMO = 100000

saldo_actual = SALDO_INICIAL
retiros_exitosos = 0
continuar_retirando = "s"

while continuar_retirando == "s" and saldo_actual > 0:
    monto_retirar = int(input("Monto a retirar: "))

    if  monto_retirar < RETIRO_MINIMO:
        print("El retiro mínimo es ₡5000")
    elif monto_retirar > RETIRO_MAXIMO:
        print("El retiro maximo es de ₡100000")
