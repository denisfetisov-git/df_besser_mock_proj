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

# Screen: ia4e
ia4e = Screen(name="ia4e", description="Home", view_elements=set(), is_main_page=True, route_path="/home", screen_size="Medium")
ia4e.component_id = "ESDrluMjPMObIm2n"
in99 = ViewContainer(
    name="in99",
    description=" container",
    view_elements=set(),
    styling=Styling(size=Size(width="70%", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default")),
    component_id="in99",
    display_order=0,
    css_classes=["gjs-cell"],
    custom_attributes={"id": "in99"}
)
iu4f = ViewContainer(
    name="iu4f",
    description=" container",
    view_elements={in99},
    styling=Styling(size=Size(width="100%", padding_top="10px", padding_right="10px", padding_bottom="10px", padding_left="10px", unit_size=UnitSize.PERCENTAGE), position=Position(display="table"), color=Color(color_palette="default")),
    component_id="iu4f",
    display_order=0,
    css_classes=["gjs-row"],
    custom_attributes={"id": "iu4f"}
)
text = Text(
    name="text",
    content="0",
    description="Text element",
    display_order=1
)
i0iu_col_0 = FieldColumn(label="Date", field=Documents_date)
i0iu_col_1 = FieldColumn(label="ID", field=Documents_ID)
i0iu = Table(
    name="i0iu",
    title="Table Title",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[i0iu_col_0, i0iu_col_1],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="i0iu",
    display_order=2,
    css_classes=["table-component", "has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Table Title", "data-source": "67bca227-0fe2-4327-8f35-3551974a23db", "show-header": True, "striped-rows": False, "show-pagination": True, "rows-per-page": 5, "action-buttons": True, "columns": [{'field': 'date', 'label': 'Date', 'columnType': 'field', '_expanded': False}, {'field': 'ID', 'label': 'ID', 'columnType': 'field', '_expanded': False}], "id": "i0iu"}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
i0iu_binding_domain = None
if domain_model_ref is not None:
    i0iu_binding_domain = domain_model_ref.get_class_by_name("Documents")
if i0iu_binding_domain:
    i0iu_binding = DataBinding(domain_concept=i0iu_binding_domain, name="DocumentsDataBinding")
else:
    # Domain class 'Documents' not resolved; data binding skipped.
    i0iu_binding = None
if i0iu_binding:
    i0iu.data_binding = i0iu_binding
ia4e.view_elements = {iu4f, text, i0iu}

gui_module = Module(
    name="GUI_Module",
    screens={ia4e}
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
