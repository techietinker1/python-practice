from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

        def __repr__(self):
            return f"({self.ssn}) {self.firstname} {self.lastname}, ({self.gender}, {self.age})"
        

class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

        def __repr__(self):
            return f"({self.tid}) {self.description}, owned by {self.owner}"

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(12312, "Antra", "Sharma", "f", 16)
session.add(person)
session.commit()

p1 = Person(31234, "Arpit", "Sharma", "m", 17)
p2 = Person(34555, "Rupm", "Sharma", "f", 48)
p3 = Person(76533, "John", "Smith", "m", 34)
p4 = Person(98765, "Jane", "Smith", "f", 29)
p5 = Person(54321, "Alice", "Johnson", "f", 22)
p6 = Person(67890, "Bob", "Johnson", "m", 31)
p7 = Person(11223, "Charlie", "Brown", "m", 19)
p8 = Person(33445, "Eve", "Davis", "f", 27)
p9 = Person(55667, "Frank", "Miller", "m", 45)
p10 = Person(77889, "Grace", "Wilson", "f", 38)
session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
session.commit()

t1 = Thing(1, "Laptop", p1.ssn)
t2 = Thing(2, "Phone", p2.ssn)
t3 = Thing(3, "Tablet", p3.ssn)
t4 = Thing(4, "Headphones", p4.ssn)
t5 = Thing(5, "Camera", p5.ssn)
t6 = Thing(6, "Smartwatch", p6.ssn)
t7 = Thing(7, "Printer", p7.ssn)
t8 = Thing(8, "Monitor", p8.ssn)
t9 = Thing(9, "Keyboard", p9.ssn)
t10 = Thing(10, "Mouse", p10.ssn)
session.add_all([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10])
session.commit()

results = session.query(Thing, Person).filter(Person.ssn == "owner").filter(Person.firstname == "Antra").all()
for r in results:
    print(r)