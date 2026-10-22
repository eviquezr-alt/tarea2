# Nombre del estudiante: Esteban Víquez
# Problema seleccionado: Cajero automático
# Descripción: permite varios retiros sobre un saldo inicial,
# valida el mínimo, el máximo y el saldo disponible,
# y al final muestra el saldo restante y los retiros exitosos.

# --- Constantes ---
SALDO_INICIAL = 250000
RETIRO_MINIMO = 5000
RETIRO_MAXIMO = 100000

# --- Inicialización ---
saldo_actual = SALDO_INICIAL
retiros_exitosos = 0
continuar_retirando = "s"

print("===== CAJERO AUTOMÁTICO =====")

# --- Ciclo principal ---
while continuar_retirando == "s" and saldo_actual > 0:
    monto_retirar = int(input("Monto a retirar: "))

    if monto_retirar < RETIRO_MINIMO:
        print("El retiro mínimo es ₡5000")
    elif monto_retirar > RETIRO_MAXIMO:
        print("El retiro maximo es de ₡100000")
    elif saldo_actual < monto_retirar:
        print("Saldo insuficiente")
    else:
        print("Retiro autorizado")
        saldo_actual = saldo_actual - monto_retirar
        retiros_exitosos = retiros_exitosos + 1

    print("Saldo actual", saldo_actual)

    continuar_retirando = input("¿Desea seguir retirando? (s/n): ")

# --- Salida final ---
print()
print("Gracias por usar el cajero.")
print("Le quedan", saldo_actual, "colones en su cuenta.")
print("Realizó", retiros_exitosos, "retiros exitosos.")