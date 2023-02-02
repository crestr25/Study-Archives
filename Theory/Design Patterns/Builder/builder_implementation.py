class HtmlElement:

    indent_size = 2

    def __init__(self, name="", text="") -> None:
        self.text = text
        self.name = name
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')
        
        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    @staticmethod
    def create(name):
        return HtmlElement(name)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)

class HtmlBuilder:
    def __init__(self, root_name) -> None:
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def __str__(self):
        return str(self.__root)


html_builder = HtmlBuilder("ul")
html_builder.add_child("li", "hello baby")
html_builder.add_child("li", "holi again")
html_builder.add_child_fluent("li", "holi again x3").add_child_fluent("li", "holi chained")

print(html_builder)


####################
## Builder Facets ##
####################

class Person:
    def __init__(self):
        # address information
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment information
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
         return f"Address: {self.street_address}, {self.postcode}, {self.city}" +\
                f"Employed at {self.company_name} as a {self.position} earning {self.annual_income}"

class PersonBuilder:
    def __init__(self, person=None):
        if person:
            self.person = person
        else:
            self.person = Person()

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person

class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self

pb = PersonBuilder()
person = pb.lives.at('123 London Road').works.earning(3000).build()

print(person)
person1 = PersonBuilder()
print(person1.build())
person2 = PersonBuilder()
print(person2)


#########################
## Builder inheritance ##
#########################

class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
         return f"{self.name} born on {self.date_of_birth} works as {self.position}"

    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person

class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self

class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self

pb = PersonBirthDateBuilder()
me = pb.called("carlos").works_as_a('Software Engineer').build()
print(me)

######################
## Builder Exercise ##
######################

class Parameter:
    
    indent_size = 4
    
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __str__(self):
        return f'{" "*self.indent_size}self.{self.name} = {self.value}'

class CodeElement:
    
    indent_size = 2
    
    def __init__(self, class_name=""):
        self.class_name = class_name
        self.parameters = []
        
        
    def __str(self):
        lines = []
        i = ' ' * (self.indent_size)
        i2 = ' ' * (self.indent_size + 2)
        lines.append(f'class {self.class_name}:')
        lines.append(f"{i}def __init__(self):")

        if not self.parameters:
            lines.append(f"{i*2}pass")
        for e in self.parameters:
            lines.append(e.__str__())
        
        return '\n'.join(lines)
        
    @staticmethod
    def create(name):
        return CodeElement
        
    def __str__(self):
        return self.__str()

class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__rootclass = CodeElement(class_name=self.root_name)
        

    def add_field(self, name, value):
        self.__rootclass.parameters.append(Parameter(name, value))
        return self

    def __str__(self):
        return str(self.__rootclass)
        

cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
print(cb)

cb = CodeBuilder('Person')
print(cb)
