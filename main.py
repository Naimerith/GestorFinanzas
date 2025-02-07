# main.py

print("¡Bienvenido a tu Gestor de Finanzas Personales! 💰")

# Variables para almacenar ingresos y gastos
ingresos = 0
gastos = 0

# Menú de opciones
while True:
    print("\nMenú:")
    print("1. Agregar Ingreso")
    print("2. Agregar Gasto")
    print("3. Mostrar Balance")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        monto = float(input("Ingrese el monto del ingreso: "))
        ingresos += monto
        print(f"✅ Ingreso de ${monto} registrado.")
    
    elif opcion == "2":
        monto = float(input("Ingrese el monto del gasto: "))
        gastos += monto
        print(f"❌ Gasto de ${monto} registrado.")
    
    elif opcion == "3":
        balance = ingresos - gastos
        print("\n📊 Resumen Financiero")
        print(f"💰 Ingresos: ${ingresos}")
        print(f"💸 Gastos: ${gastos}")
        print(f"📌 Balance Total: ${balance}")
    
    elif opcion == "4":
        print("¡Gracias por usar el Gestor de Finanzas! 👋")
        break
    
    else:
        print("❌ Opción inválida. Intenta de nuevo.")
