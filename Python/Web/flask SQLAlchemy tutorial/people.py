from flask import abort, make_response
from config import db
from models import Person, person_schema, people_schema

def read_all():
    people = Person.query.all()
    return people_schema.dump(people)


def create(person):
    lname = person.get("lname")
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if not existing_person:
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person)
    abort(406, f"Person with lname {lname} already exists")


def read_one(lname):
    person = Person.query.filter(Person.lname == lname).one_or_none()
    if person:
        return person_schema.dump(person)
    abort(404, f"Person with last name {lname} does not exist")


def update(lname, persona):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()
    if existing_person:
        update_person = person_schema.load(persona, session=db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()

        return person_schema.dump(existing_person), 201
        
    abort(404, f"Person with last name {lname} does not exist")


def delete(lname):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()
    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"{lname} successfully deleted", 200)
    abort(404, f"Person with last name {lname} does not exist")


