while True:
    print('    ')
    print('Calculadora: ')
    print('Escribe 1 si quieres sumar.')
    print('Escribe 2 si quieres restar.')
    print('Escribe 3 si quieres multiplicar.')
    print('Escribe 4 si quieres dividir.')
    print('Escribe 5 si quieres salir.')
    print('    ')

    user_in = int(input('Elige una opción: '))

    
    if user_in == 1:
        num1 = float(input('Introduce el primer número: '))
        num2 = float(input('Introduce el segundo número: '))
        print('La suma es: ', num1 + num2)
    elif user_in == 2:
        num1 = float(input('Introduce el primer número: '))
        num2 = float(input('Introduce el segundo número: '))
        print('La  resta es: ', num1 - num2)
    elif user_in == 3:
        num1 = float(input('Introduce el primer número: '))
        num2 = float(input('Introduce el segundo número: '))
        print('La multiplicación es: ', num1 * num2)
    elif user_in == 4:
        num1 = float(input('Introduce el primer número: '))
        num2 = float(input('Introduce el segundo número: '))
        if num2 != 0:
            print('La división es: ', num1 / num2)
        else:
            print('No se puede dividir entre cero')
    elif user_in == 5:
        print('Hasta luego')
    else:
        print('Opción no válida')
    break