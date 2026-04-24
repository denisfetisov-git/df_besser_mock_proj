####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata, MethodImplementationType
)

# Classes
Documents = Class(name="Documents")

# Documents class attributes and methods
Documents_name: Property = Property(name="name", type=StringType)
Documents_date: Property = Property(name="date", type=DateType)
Documents_ID: Property = Property(name="ID", type=IntegerType)
Documents.attributes={Documents_ID, Documents_date, Documents_name}

# Domain Model
domain_model = DomainModel(
    name="Class_Diagram",
    types={Documents},
    associations={},
    generalizations={},
    metadata=None
)
