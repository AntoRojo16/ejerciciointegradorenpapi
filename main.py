from ClaseMAnejadorAlumnos import ManejadorAlumno
from claseManejadorMateria import MateriasAprobadas

if __name__=="__main__":
    print('Inicia el programa')
    alumnos=ManejadorAlumno()
    alumnos.inicalizar()
    print("alumnos sin ordenar")
    alumnos.mostrar()
    alumnos.ordenarAlumnos()
    print("ordenar alumnos")
    alumnos.mostrar()
    materia=MateriasAprobadas()
    materia.inicializar()
    print("materias")
    #print(materia)
    print('Termina el programa')
    materia.calcularMaterias()
    
