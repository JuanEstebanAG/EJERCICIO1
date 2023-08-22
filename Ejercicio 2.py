#Clase para almacenar
class Sistema:
    #Database donde voy a almacenar los datos
    def __init__(self):
        self.database = []
        #Para que no se modifique y dependa solo del tamaño de la lista
        self.numberPatient = len(self.database)
    
    def insertPatient(self):
        name = input('Ingrese el nombre: ')   
        cc = int(input('Digite la cédula: '))
        gender = input('Ingrese el género: ')
        service = input('Ingrese el servicio: ')
        p = Paciente()
        p.assignName(name)
        p.assignCc(cc)
        p.assignGender(gender)
        p.assignService(service)
        
        self.database.append(p)
        self.numberPatient = len(self.database)
    
    def showNumberPatient(self):
        return self.numberPatient
    
    def showDataPatient(self):
        cc = int(input('Digite la cédula que está buscando: '))
        for patient in self.database:
            if cc == Paciente.showCc(self):
                print(f'''
                    Nombre:  {patient.showName()}
                    Cédula: {str(patient.showCc())}
                    Género: {patient.showGender()}
                    Servicio: {patient.showService()}''')

#Clase que almacenaré
class Paciente:
    def __init__(self):
        self.name = ""
        self.cc = 0
        self.gender = ""
        self.service = ""
    
    
    #MÉTODO VER
    def showName(self):
        return self.name
    def showService(self):
        return self.service
    def showGender(self):
        return self.gender
    def showCc(self):
        return self.cc
    
    #MÉTODO ASIGNAR
    def assignName(self, n):
        self.name = n
    def assignService(self, s):
        self.name = s
    def assignGender(self, g):
        self.name = g
    def assignCc(self, c):
        self.name = c
            
    

system = Sistema()

while True:
    menu =  input('''\nSeleccione la opción que desea realizar:
                1. Ingresar nuevo paciente.
                2. Ver número de pacientes.
                3. Ver datos del paciente.
                4. Salir.
                -> ''')
    if menu == '1':
        system.insertPatient()
    elif menu == '2':
        print(f'\nActualmente existen: {system.showNumberPatient()} pacientes.')
    elif menu == '3':
        system.showDataPatient()
    elif menu == '4':
        break
    else:
        print('\nSeleccione una opción válida.')