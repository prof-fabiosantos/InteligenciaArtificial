from owlready2 import *

# Criar uma ontologia
onto = get_ontology("http://www.example.org/universidade.owl")

# Definir classes
class Curso(Thing):
    namespace = onto

class Professor(Thing):
    namespace = onto

class Aluno(Thing):
    namespace = onto

class Departamento(Thing):
    namespace = onto

class Prédio(Thing):
    namespace = onto

# Definir propriedades
class ministraCurso(ObjectProperty):
    namespace = onto
    domain = [Professor]
    range = [Curso]

class pertenceCurso(ObjectProperty):
    namespace = onto
    domain = [Aluno]
    range = [Curso]

class pertenceDepartamento(ObjectProperty):
    namespace = onto
    domain = [Professor, Aluno]
    range = [Departamento]


class estaLocalizadoEm(ObjectProperty):
    namespace = onto
    domain = [Departamento, Curso]
    range = [Prédio]

# Adicionar instâncias
professor1 = Professor("Prof_Fabio_Santos")
curso1 = Curso("Sistemas_de_Informação")
departamento1 = Departamento("Departamento_de_Computação")
prédio1 = Prédio("EST")
aluno1 = Aluno("Mario_Silva")

# Atribuir propriedades
professor1.ministraCurso.append(curso1)
professor1.pertenceDepartamento.append(departamento1)
curso1.pertenceDepartamento.append(departamento1)
departamento1.estaLocalizadoEm.append(prédio1)
aluno1.pertenceCurso.append(curso1)

def verificar_curso_aluno(aluno):
    # Consulta para encontrar tratamento para uma doença específica
    result = list(aluno.pertenceCurso)

    for curso in result:
        return curso.name


print("Curso do aluno "+aluno1.name+":", verificar_curso_aluno(aluno1))

# Salvar a ontologia
onto.save("universidade.owl", format="rdfxml")

