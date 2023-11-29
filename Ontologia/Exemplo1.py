from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, FOAF

# Crie um grafo RDF
g = Graph()

# Crie um namespace para a ontologia
school = Namespace("http://example.org/school/")

# Adicione algumas informações à ontologia
g.add((school.John, RDF.type, FOAF.Person))
g.add((school.John, FOAF.name, Literal("John Doe")))
g.add((school.John, school.hasAge, Literal(25)))

g.add((school.Mary, RDF.type, FOAF.Person))
g.add((school.Mary, FOAF.name, Literal("Mary Johnson")))
g.add((school.Mary, school.hasAge, Literal(30)))

g.add((school.Maths, RDF.type, school.Course))
g.add((school.Maths, school.hasTitle, Literal("Mathematics")))

# Salve a ontologia em um arquivo RDF
g.serialize("school_ontology.rdf", format="xml")

# Consulta: Obtenha todas as pessoas na ontologia
query = """
    SELECT ?person ?name
    WHERE {
        ?person rdf:type foaf:Person .
        ?person foaf:name ?name .
    }
"""

result = g.query(query, initNs={"rdf": RDF, "foaf": FOAF})

print("\nPessoas na ontologia:")
for row in result:
    print(f"{row.name}: {row.person}")

# Consulta: Obtenha todos os cursos na ontologia
query_courses = """
    SELECT ?course ?title
    WHERE {
        ?course rdf:type school:Course .
        ?course school:hasTitle ?title .
    }
"""

result_courses = g.query(query_courses, initNs={"rdf": RDF, "school": school})

print("\nCursos na ontologia:")
for row in result_courses:
    print(f"{row.title}: {row.course}")






