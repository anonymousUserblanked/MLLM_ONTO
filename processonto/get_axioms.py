from owlready2 import *

# Load the ontology
onto = get_ontology("./ontology/RiceDO.owl").load()
# Define a class expression parser function
def parse_class_expression(expression):
    parts = expression.split(" some ")

    if len(parts) == 2:
        class_name = parts[0].strip()
        property_and_value = parts[1].strip()

        # Get the class from the ontology
        cls = onto[class_name]

        # Check if property restriction is present
        if " some " in property_and_value:
            prop_name, value = property_and_value.split(" some ")
            prop = onto[prop_name.strip()]
            return cls, prop, value.strip()
        else:
            return cls, None, None
    else:
        print("Invalid class expression format")
        return None, None, None

# Example usage
class_expression = "abnormalityGroup some TransplantingToFlowering"
cls, prop, value = parse_class_expression(class_expression)

if cls is not None:
    print(f"Class: {cls}")
    if prop:
        print(f"Property: {prop}")
        print(f"Value: {value}")
    else:
        print("No property restriction present in the expression")
else:
    print("Error parsing class expression")

