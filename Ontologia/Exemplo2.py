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
g.add((school.John, school.takesCourse, school.Maths))

g.add((school.Mary, RDF.type, FOAF.Person))
g.add((school.Mary, FOAF.name, Literal("Mary Johnson")))
g.add((school.Mary, school.hasAge, Literal(30)))
g.add((school.Mary, school.takesCourse, school.Physics))

g.add((school.Maths, RDF.type, school.Course))
g.add((school.Maths, school.hasTitle, Literal("Mathematics")))

g.add((school.Physics, RDF.type, school.Course))
g.add((school.Physics, school.hasTitle, Literal("Physics")))

# Salve a ontologia em um arquivo RDF
g.serialize("school_ontology.rdf", format="xml")

# Consulta: Obtenha todas as pessoas que fazem um curso específico (por exemplo, "Mathematics")
query_students_in_course = """
    SELECT ?person ?name
    WHERE {
        ?person rdf:type foaf:Person .
        ?person foaf:name ?name .
        ?person school:takesCourse ?course .
        ?course school:hasTitle "Mathematics" .
    }
"""

result_students_in_course = g.query(query_students_in_course, initNs={"rdf": RDF, "foaf": FOAF, "school": school})

print("\nPessoas matriculadas em Mathematics:")
for row in result_students_in_course:
    print(f"{row.name}: {row.person}")
