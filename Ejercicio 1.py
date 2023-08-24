# Clase que almacenaré
class Paciente:
    def __init__(self):
        self.name = ""
        self.cc = 0
        self.gender = ""
        self.service = ""
    
    # MÉTODO VER
    def showName(self):
        return self.name
    def showService(self):
        return self.service
    def showGender(self):
        return self.gender
    def showCc(self):
        return self.cc
    
    # MÉTODO ASIGNAR
    def assignName(self, n):
        self.name = n
    def assignService(self, s):
        self.service = s
    def assignGender(self, g):
        self.gender = g
    def assignCc(self, c):
        self.cc = c

# Clase para almacenar
class Sistema:
    # Database donde voy a almacenar los datos
    def __init__(self):
        self.database = []
    
    def insertPatient(self, pat):
        self.database.append(pat)
        return True  #Retorna True si el paciente se insertó correctamente
        
    def showNumberPatient(self):
        print(f'En la base de datos hay: {str(len(self.database))} pacientes.')
    
    def showDataPatient(self, c):
        for p in self.database:
            if c == p.showCc():
                return p

def main():
    sis = Sistema()
    while True:
        menu = input('''Elija la opción que desea realizar:
                     1. Ingresar nuevo paciente.
                     2. Ver datos del paciente. 
                     3. Ver número de pacientes.
                     4. Salir.
                     -> ''')
        if menu == '1':
            name = input('Nombre: ')
            cc = int(input('Cédula: '))
            gender = input('Género: ')
            service = input('Servicio: ')
            pat = Paciente()
            pat.assignCc(cc)
            pat.assignGender(gender)
            pat.assignName(name)
            pat.assignService(service)
            success = sis.insertPatient(pat)
            if success:
                print('\nPaciente insertado correctamente.')
            else:
                print('\nError al insertar el paciente.')

        elif menu == '2':
            c = int(input('\nDigite la cédula que está buscando: '))
            p = sis.showDataPatient(c)
            print(f'''
                Datos del paciente:
                Nombre: {p.showName()}
                Cédula: {str(p.showCc())}
                Género: {p.showGender()}
                Servicio: {p.showService()}''')
        
        elif menu == '3':
            sis.showNumberPatient()
        
        elif menu == '4':
            print('Hasta la próxima.') #Decoración jajaja
            break
        
        else:
            print('S\neleccione una opción válida.')

if __name__ == "__main__":
    main() #RECONOCE EL PROPIO MÓDULO
