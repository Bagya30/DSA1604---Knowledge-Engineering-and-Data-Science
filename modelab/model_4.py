
from owlready2 import *
onto = get_ontology("http://example.org/university.owl")
with onto:
    class Course(Thing):
        pass
    class CoreCourse(Course):
        pass
    class ElectiveCourse(Course):
        pass
    class Topic(Thing):
        pass
    class Student(Thing):
        pass
    class hasCompleted(ObjectProperty):
        domain = [Student]
        range = [Course]
    class hasPrerequisite(ObjectProperty):
        domain = [ElectiveCourse]
        range = [Course]
    class coversTopic(ObjectProperty):
        domain = [Course]
        range = [Topic]
    class altLabel(AnnotationProperty):
        pass
    class DatabaseTopic(Topic):
        pass
    class ProgrammingTopic(Topic):
        pass
    Python = CoreCourse("Python")
    Database = CoreCourse("Database_Systems")

    ML = ElectiveCourse("Machine_Learning")
    DM = ElectiveCourse("Data_Mining")

    # Prerequisites
    ML.hasPrerequisite = [Python]
    DM.hasPrerequisite = [Database]

    # Create topics
    SQL = DatabaseTopic("SQL")
    PythonTopic1 = ProgrammingTopic("Python_Topic")

    Python.coversTopic = [PythonTopic1]
    Database.coversTopic = [SQL]

    # Add synonyms
    Python.altLabel.append("Python Programming")
    Database.altLabel.append("DBMS")

    # Create students
    Bagyalakshmi = Student("Bagyalakshmi")
    Arun = Student("Arun")

    # Completed courses
    Bagyalakshmi.hasCompleted = [Python, Database]
    Arun.hasCompleted = [Python]

    # Eligibility classes
    class EligibleForML(Student):
        equivalent_to = [hasCompleted.some(Python)]

    class EligibleForDM(Student):
        equivalent_to = [hasCompleted.some(Database)]


# Run reasoner
with onto:
    sync_reasoner(infer_property_values=True)

# Display results
print("UNIVERSITY COURSE ADVISING SYSTEM")

for student in [Bagyalakshmi, Arun]:
    print("\nStudent:", student.name)

    print("Completed Courses:",
          [c.name for c in student.hasCompleted])

    print("Eligible Electives:")

    found = False

    if isinstance(student, EligibleForML):
        print("- Machine Learning")
        found = True

    if isinstance(student, EligibleForDM):
        print("- Data Mining")
        found = True

    if not found:
        print("No eligible electives")

print("\nReasoning Completed Successfully!")
