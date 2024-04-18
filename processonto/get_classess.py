from owlready2 import *

# Load your ontology
onto = get_ontology("./ontology/RiceDO.owl").load()

# get all colors 
# Define the class "Abnormality"
Abnormality = onto.Abnormality

# Find the class "Color" under "Abnormality"
Color = None
for cls in Abnormality.subclasses():
    if cls.name == "ColorAbnormality":
        Color = cls
        break

# Check if "Color" is found
if Color:
    # Function to extract all subclasses recursively
    def extract_subclasses(cls):
        subclasses = []
        for subclass in cls.subclasses():
            subclasses.append(subclass.name)
            subclasses.extend(extract_subclasses(subclass))
        return subclasses

    # Extract subclasses of the "Color" class
    subclasses_vector = extract_subclasses(Color)

    # Print the subclasses vector
    print(subclasses_vector)
else:
    print("Class 'Color' not found under 'Abnormality'.")


# get all symptoms
# Find the class "Symptom" under "Abnormality"
Symptom = None
for cls in Abnormality.subclasses():
    if cls.name == "SymptomAbnormality":
        Symptom = cls
        break

# Check if "Color" is found
if Symptom:
    # Function to extract all subclasses recursively
    def extract_subclasses(cls):
        subclasses = []
        for subclass in cls.subclasses():
            subclasses.append(subclass.name)
            subclasses.extend(extract_subclasses(subclass))
        return subclasses

    # Extract subclasses of the "Color" class
    subclasses_vector = extract_subclasses(Symptom)

    # Print the subclasses vector
    print(subclasses_vector)
else:
    print("Class 'Symptom' not found under 'Abnormality'.")

# get all shapes 

Shape = None
for cls in Abnormality.subclasses():
    if cls.name == "ShapeAbnormality":
        Shape = cls
        break

# Check if "Shape" is found
if Shape:
    # Function to extract all subclasses recursively
    def extract_subclasses(cls):
        subclasses = []
        for subclass in cls.subclasses():
            subclasses.append(subclass.name)
            subclasses.extend(extract_subclasses(subclass))
        return subclasses

    # Extract subclasses of the "Shape" class
    subclasses_vector = extract_subclasses(Shape)

    # Print the subclasses vector
    print(subclasses_vector)
else:
    print("Class 'Shape' not found under 'Abnormality'.")
