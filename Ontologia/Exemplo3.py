from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, FOAF
import networkx as nx
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import matplotlib.pyplot as plt

# Crie um grafo RDF
g = Graph()

# Crie um namespace para a ontologia
school = Namespace("http://example.org/school/")

def add_person(name, age):
    person_uri = school[name.replace(" ", "_")]
    g.add((person_uri, RDF.type, FOAF.Person))
    g.add((person_uri, FOAF.name, Literal(name)))
    g.add((person_uri, school.hasAge, Literal(age)))
    return person_uri

def add_course(title):
    course_uri = school[title.replace(" ", "_")]
    g.add((course_uri, RDF.type, school.Course))
    g.add((course_uri, school.hasTitle, Literal(title)))
    return course_uri

def enroll_person_in_course(person_uri, course_uri):
    g.add((person_uri, school.takesCourse, course_uri))

def get_people():
    query = """
        SELECT ?person ?name
        WHERE {
            ?person rdf:type foaf:Person .
            ?person foaf:name ?name .
        }
    """
    result = g.query(query, initNs={"rdf": RDF, "foaf": FOAF})
    return result

def get_courses():
    query = """
        SELECT ?course ?title
        WHERE {
            ?course rdf:type school:Course .
            ?course school:hasTitle ?title .
        }
    """
    result = g.query(query, initNs={"rdf": RDF, "school": school})
    return result

def get_courses_for_person(person_uri):
    query = f"""
        SELECT ?course ?title
        WHERE {{
            <{person_uri}> school:takesCourse ?course .
            ?course school:hasTitle ?title .
        }}
    """
    result = g.query(query, initNs={"rdf": RDF, "school": school})
    return result

def visualize_ontology():
    print("\nOntologia:")
    for triple in g:
        print(triple)

def visualize():
    url = 'https://www.w3.org/TeamSubmission/turtle/tests/test-30.ttl'

    result = g.parse(url, format='turtle')

    G = rdflib_to_networkx_multidigraph(result)

    # Plot Networkx instance of RDF Graph
    pos = nx.spring_layout(G, scale=2)
    edge_labels = nx.get_edge_attributes(G, 'r')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, with_labels=True)

    #if not in interactive mode for 
    plt.show()

# Permitir ao usuário adicionar informações, realizar consultas ou visualizar a ontologia
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar pessoa")
    print("2. Adicionar disciplina")
    print("3. Matricular pessoa em disciplina")
    print("4. Consultar pessoas")
    print("5. Consultar disciplinas")
    print("6. Consultar disciplinas de uma pessoa")
    print("7. Visualizar ontologia")
    print("8. Encerrar")

    choice = input("Digite o número da opção desejada: ")

    if choice == "1":
        name = input("Digite o nome da pessoa: ")
        age = input("Digite a idade da pessoa: ")
        person_uri = add_person(name, age)
        print(f"Pessoa '{name}' adicionada com sucesso.")

    elif choice == "2":
        title = input("Digite o título da disciplina: ")
        course_uri = add_course(title)
        print(f"Disciplina '{title}' adicionada com sucesso.")

    elif choice == "3":
        name = input("Digite o nome da pessoa: ")
        title = input("Digite o título da disciplina: ")
        person_uri = school[name.replace(" ", "_")]
        course_uri = school[title.replace(" ", "_")]

        if (person_uri, RDF.type, FOAF.Person) in g and (course_uri, RDF.type, school.Course) in g:
            enroll_person_in_course(person_uri, course_uri)
            print(f"Pessoa '{name}' matriculada na disciplina '{title}' com sucesso.")
        else:
            print("Pessoa ou disciplina não encontrada. Certifique-se de adicionar pessoas e disciplinas antes de matricular.")

    elif choice == "4":
        people_result = get_people()
        print("\nPessoas na ontologia:")
        for row in people_result:
            print(f"{row.name}: {row.person}")

    elif choice == "5":
        courses_result = get_courses()
        print("\nDisciplinas na ontologia:")
        for row in courses_result:
            print(f"{row.title}: {row.course}")

    elif choice == "6":
        name = input("Digite o nome da pessoa: ")
        person_uri = school[name.replace(" ", "_")]

        if (person_uri, RDF.type, FOAF.Person) in g:
            courses_result = get_courses_for_person(person_uri)
            print(f"\nDisciplinas de {name}:")
            for row in courses_result:
                print(f"{row.title}: {row.course}")
        else:
            print("Pessoa não encontrada. Certifique-se de adicionar a pessoa antes de consultar as disciplinas.")

    elif choice == "7":
        visualize_ontology()
        visualize()
        

    elif choice == "8":
        break

    else:
        print("Opção inválida. Tente novamente.")

# Salve a ontologia em um arquivo RDF
g.serialize("school_ontology.rdf", format="xml")

