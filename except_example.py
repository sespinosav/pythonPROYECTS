def divide():

	try:
		op1 = (float(input("introduce el pirmer numero: ")))

		op2 = (float(input("introduce el segundo numero: ")))

		print("la diviion es: " + str(op1/op2))

	except ValueError:

		print("el valor introducido es erroneo")

	except ZeroDivisionError:

		print("no se puede dividir entre cero")

	print("calculo finalizado")

divide()
