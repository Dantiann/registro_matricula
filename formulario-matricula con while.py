## PRESENTACIÓN FORMULARIO
print('''
''')
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print(' FORMULARIO DE DESCUENTO DE MATRICULAS\n\t UNIVERSIDAD DE LA VIDA')
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print('''
''')
print('''Antes de diligenciar el formulario, tenga en cuenta la siguiente informacion :
- Ingrese los datos correctamente de la persona que solicita el descuento
- Sí considera que ingresó un dato erradamente diligencie nuevamente el formulario
- En los campos que se soliciten números "NO" ingresar puntos ni comas ''')
print()
print('Por favor, ingrese los siguientes datos:')
print()

## SOLICITUD DE DOCUMENTOS
print('SOLICITUD DE DOCUMENTOS')
apellido1=input('A. Primer apellido: \t\t').upper()
while apellido1.isalpha() != True:
    print('\t\t\t¡Dato no valido!')
    apellido1=input('   Primer apellido: \t\t').upper()

apellido2=input('A. Segundo apellido: \t\t').upper()
while apellido2.isalpha() != True:
    print('\t\t\t¡Dato no valido!')
    apellido2=input('   Segundo apellido: \t\t').upper()    

nombre1=input('A. Primer nombre:          \t').upper()
while nombre1.isalpha() != True:
    print('\t\t\t¡Dato no valido!')
    nombre1=input('   Primer nombre:        \t').upper()

nombre2=input('A. segundo nombre:          \t').upper()
while nombre2.isalpha() != True:
    print('\t\t\t¡Dato no valido!')
    nombre2=input('   Segundo nombre:       \t').upper()
    
documento=input('B. Documento de identidad:   \t')
while documento.isdigit() != True:
    print('\t\t\t¡Valor no valido!')
    documento=input('   Documento de identidad:\t')

estado_civil=input('C. Estado civil: soltero, viudo,\n   casado, o unión libre:\t').upper()
estado_civiless=estado_civil.lower()
while estado_civil !='CASADO' and estado_civil !='SOLTERO' and estado_civil !='VIUDO' and estado_civil !='UNIÓN LIBRE':
    print('\t\t\t ¡Estado civil no existente! ')
    estado_civil=input('   Estado civil: soltero, viudo,\n   casado, o unión libre:\t').upper()
    estado_civiless=estado_civil.lower()

educacion=input('D. Nivel educativo: profesional,\n   bachiller, o sena:\t\t' ).upper()
educacioness=educacion.lower()
while educacion !='PROFESIONAL' and educacion != 'BACHILLER' and educacion !='SENA':
    print('\t\t\t!Nivel educativo no existente!')
    educacion=input('   Nivel educativo: profesional,\n   bachiller, o sena:\t\t').upper()
    educacioness=educacion.lower()

edad=input('E. Edad:\t\t\t')
while edad.isdigit() != True:
    print('\t\t\t¡No es un valor valido!')
    edad=input('   Edad:\t\t\t')
edades=int(edad)

hijos=input('G. Número de hijos:\t\t')
while hijos.isdigit() != True:
    print('\t\t\t¡No es un valor valido!')
    hijos=input('   Número de hijos:\t\t')
hijoso=int(hijos)   

salario=input('F. Ingrese su salario $:\t')
while salario.isdigit() != True:
    print('\t\t\t¡No es un valor valido!')
    salario=input('   Ingrese su salario $:\t')
salarios=int(salario)

## CONDICIONAL DESCUENTOS
if 18<=edades<=25: descu1=10
elif 26<=edades<=35: descu1=5
else: descu1=0

if estado_civil=='CASADO':descu2=25
elif estado_civil=='SOLTERO':descu2=15
elif estado_civil=='VIUDO':descu2=20
elif estado_civil=='UNIÓN LIBRE':descu2=0
else: print('Los datos ingresados son incorrectos. Volver a diligenciar el formulario'); descu2=0

if hijoso==3:descu3=10
elif hijoso==2:descu3=7
elif hijoso==1:descu3=5
else: hijoso>3 or hijoso <1; descu3=0

if educacion=='SENA': descu4=10
elif educacion=='BACHILLER': descu4=15
elif educacion=='PROFESIONAL': descu4=0
else:print('Los datos ingresados son incorrectos. Volver a diligenciar el formulario'); descu4=0
print()

### IMPRIMIR RESULTADO    
print('-------------------------------------------------------------------')
print('DATOS DEL INTERESADO:')
print(f'NOMBRE:\t\t{nombre1} {nombre2} {apellido1} {apellido2}\nEDAD:\t\t{edades} AÑOS')
print(f'ESTADO CIVIL:\t{estado_civil}\nEDUCACIÓN:\t{educacion}')
print(f'N° DE HIJOS:\t{hijos} HIJO(S)\nSALARIO:\t${salario} COP')
print()
print()
print('DESCUENTOS POR EDAD:')
print(f'Sr(a). {nombre1} {apellido1}, tiene derecho al {descu1}% de descuento en la matricula por tener {edades} años de edad.')
print(descu1,'%')
print()
print('DESCUENTOS POR ESTADO CIVIL:')
print(f'Sr(a). {nombre1} {apellido1}, tiene derecho al {descu2}% de descuento en la matricula por su estado civil de {estado_civiless}.' )
print(descu2,'%')
print()
print('DESCUENTOS POR NÚMERO DE HIJOS:')
print(f'Sr(a). {nombre1} {apellido1}, tiene derecho al {descu3}% de descuento en la matricula por tener {hijoso} hijos.' )
print(descu3,'%')
print()
print('DESCUENTOS POR NIVEL DE EDUCACIÓN:')
print(f'Sr(a). {nombre1} {apellido1}, tiene derecho al {descu4}% de descuento en la matricula por pertenecer a nivel {educacioness}.' )
print(descu4,'%')
print('-------------------------------------------------------------------')
print()
print('TOTAL DESCUENTO:')
descuento=descu4+descu3+descu2+descu1
print(f'Sr(a). {nombre1} {apellido1}, el total de descuento al que tiene derecho en la matricula corresponde al:\n{descuento}%')
