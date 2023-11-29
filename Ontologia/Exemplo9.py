from owlready2 import *

# Criar uma ontologia vazia
onto_covid = get_ontology("http://www.example.org/covid_ontology.owl")

# Definir classes
class Pessoa(Thing):
    namespace = onto_covid

class Paciente(Pessoa):
    namespace = onto_covid

class Sintoma(Thing):
    namespace = onto_covid

class Diagnostico(Thing):
    namespace = onto_covid

class Tratamento(Thing):
    namespace = onto_covid

# Definir propriedades
class temSintoma(ObjectProperty):
    namespace = onto_covid
    domain = [Paciente]
    range = [Sintoma]

# Definir propriedades
class temDiagnostico(ObjectProperty):
    namespace = onto_covid
    domain = [Paciente]
    range = [Diagnostico]

# Definir propriedades
class temTratamento(ObjectProperty):
    namespace = onto_covid
    domain = [Diagnostico]
    range = [Tratamento]
   

# Adicionar instâncias e relações
paciente1 = Paciente("Paciente_Fabio")

# Possiveis sintomas
sintoma1 = Sintoma("Febre")
sintoma2 = Sintoma("Tosse")
sintoma3 = Sintoma("Dificuldade_Respiratória")

# Possiveis diagnosticos
diagnostico1 = Diagnostico("Gripe")
diagnostico2 = Diagnostico("Pneumonia")
diagnostico3 = Diagnostico("COVID-19")
diagnostico4 = Diagnostico("Alergia")

# Possiveis tratamentos
tratamento1 = Tratamento("Vacina")
tratamento2 = Tratamento("Ant-gripal")
tratamento3 = Tratamento("Ant-alergico")
tratamento4 = Tratamento("Antibiotico")


# Associar sintomas ao paciente
paciente1.temSintoma.append(sintoma1)
paciente1.temSintoma.append(sintoma2)
paciente1.temSintoma.append(sintoma3)

# Associar diagnóstico ao tratamento
diagnostico1.temTratamento.append(tratamento2)
diagnostico2.temTratamento.append(tratamento4)
diagnostico3.temTratamento.append(tratamento1)
diagnostico4.temTratamento.append(tratamento3)


# Motor de Inferência para verificar o diagnóstico do paciente
def verificar_diagnostico(paciente):
    sintomas = set(sintoma.name for sintoma in paciente.temSintoma)

    sintomas_covid = {"Febre", "Tosse", "Dificuldade_Respiratória"}
    sintomas_gripe = {"Febre", "Tosse"}
    sintomas_pneumonia = {"Dificuldade_Respiratória", "Tosse"}
    sintomas_alergia = {"Tosse"}

    if sintomas_covid.issubset(sintomas):
        paciente.temDiagnostico.append(diagnostico3)
        return paciente.temDiagnostico[0]
    elif sintomas_gripe.issubset(sintomas):
        paciente.temDiagnostico.append(diagnostico1)
        return paciente.temDiagnostico[0]
    elif sintomas_pneumonia.issubset(sintomas):
        paciente.temDiagnostico.append(diagnostico2)
        return paciente.temDiagnostico[0]
    elif sintomas_alergia.issubset(sintomas):
        paciente.temDiagnostico.append(diagnostico4)
        return paciente.temDiagnostico[0]
    else:
        return "Não foi possível determinar o diagnóstico com base nos sintomas. Consulte um médico para avaliação adequada."

def verificar_tratamento(diagnostico):
    # Consulta para encontrar tratamento para uma doença específica
    result = list(diagnostico.temTratamento)

    for tratamento in result:
        return tratamento

# Exemplo de uso
diagnostico = verificar_diagnostico(paciente1)
tratamento =  verificar_tratamento(diagnostico)

print("Diagnóstico para " + paciente1.name + ":", diagnostico.name)
print("Tratamento: ", tratamento.name)

# Salvar a ontologia em um arquivo RDF
onto_covid.save("covid_ontology.owl", format="rdfxml")







