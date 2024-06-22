from database.Database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields

class Contactos(db.Model):
    __tablename__ = 'Contactos'

    Id_Contacto = db.Column(db.Integer, primary_key=True, nullable=False)
    Nombre = db.Column(db.String(50))
    Direccion = db.Column(db.String)
    Telefono = db.Column(db.Integer(8))
    Email = db.Column(db.String)

    def __init__(self, Id_Contacto, Nombre, Direccion, Telefono, Email):
        self.Id_Contacto = Id_Contacto
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Email = Email

class ContactoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Contactos
        load_instance = True

libro = fields.Nested(ContactoSchema)
libro_schema = ContactoSchema
libros_schema = ContactoSchema(many=True)