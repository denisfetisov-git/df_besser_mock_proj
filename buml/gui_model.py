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


###############
#  GUI MODEL  #
###############

from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen,
    ViewComponent, ViewContainer,
    Button, ButtonType, ButtonActionType,
    Text, Image, Link, InputField, InputFieldType,
    Form, Menu, MenuItem, DataList,
    DataSource, DataSourceElement, EmbeddedContent,
    Styling, Size, Position, Color, Layout, LayoutType,
    UnitSize, PositionType, Alignment
)
from besser.BUML.metamodel.gui.dashboard import (
    LineChart, BarChart, PieChart, RadarChart, RadialBarChart, Table, AgentComponent,
    Column, FieldColumn, LookupColumn, ExpressionColumn, MetricCard, Series
)
from besser.BUML.metamodel.gui.events_actions import (
    Event, EventType, Transition, Create, Read, Update, Delete, Parameter
)
from besser.BUML.metamodel.gui.binding import DataBinding

# Module: GUI_Module

# Screen: wrapper
wrapper = Screen(name="wrapper", description="Home", view_elements=set(), is_main_page=True, route_path="/home", screen_size="Medium")
wrapper.component_id = "9VNa8scBXvnTxdC4"
ibvt = Table(
    name="ibvt",
    title="Table Title",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="ibvt",
    display_order=0,
    css_classes=["table-component"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Table Title", "data-source": "", "show-header": True, "striped-rows": False, "show-pagination": True, "rows-per-page": 5, "action-buttons": True, "columns": [], "id": "ibvt"}
)
wrapper.view_elements = {ibvt}

gui_module = Module(
    name="GUI_Module",
    screens={wrapper}
)

# GUI Model
gui_model = GUIModel(
    name="GUI",
    package="",
    versionCode="1.0",
    versionName="1.0",
    modules={gui_module},
    description="GUI"
)
