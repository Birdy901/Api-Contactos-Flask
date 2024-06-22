from flask import Blueprint, jsonify, request

from src.model.ContactsModel import Contactos, contacto_schema, contactos_schema
from database.Database import db

main=Blueprint('contactos_blueprint', __name__)

#Ruta para llamar todos los contactos
@main.route('/contactos', methods=['GET'])
def get_contactos():
    all_contactos = Contactos.query.all()
    result = contactos_schema.dump(all_contactos)

    return jsonify(result)

#Ruta para llamar todos los contactos con paginado
@main.route('/contactos', methods=['GET'])
def get_contactos_paginado():
    #Paginado
    page = request.args.get('page', type=int)
    per_page = request.args.get('per_page', type=int)

    contactos_pagination = Contactos.query.paginate(page=page, per_page=per_page)

    #Resultados
    all_contactos = contactos_pagination.items
    
    result = contactos_schema.dump(all_contactos)
    return jsonify(result)

#Ruta para llamar un contacto por ID
@main.route('/contactos/<id>', methods=['GET'])
def get_contacto(id):
    contacto = Contactos.query.filter_by(Id_Contacto=id).first_or_404()
    result = contacto_schema.dump(contacto)

    return jsonify(result)

#Ruta para crear un nuevo contacto
@main.route('/contactos', methods=['POST'])
def create_contacto():
    contacto_data = request.get_json()
    contacto = Contactos(
            Id_Contacto = None,
            Nombre=contacto_data.get('Nombre'),
            Telefono=contacto_data.get('Telefono'),
            Email=contacto_data.get('Email'),
            Direccion=contacto_data.get('Direccion')
        )

    db.session.add(contacto)
    db.session.commit()

    result = contacto_schema.dump(contacto)
    return jsonify(result), 201

#Ruta para editar un contacto por ID
@main.route('/contactos/<id>', methods=['PUT'])
def editar_contacto(id):
    contacto = Contactos.query.filter_by(Id_Contacto=id).first_or_404()
    
    contacto.Nombre = request.json['Nombre']
    contacto.Direccion = request.json['Nombre']
    contacto.Telefono = request.json['Telefono']
    contacto.Email = request.json['Email']
    db.session.commit()

    result = contacto_schema.dump(contacto)
    
    return jsonify(result)

#Ruta para eliminar un contacto por ID
@main.route('/contactos/<id>', methods=['DELETE'])
def delete_contacto(id):
    contacto = Contactos.query.filter_by(Id_Contacto=id).first_or_404()
    
    db.session.delete(contacto)
    db.session.commit()
    
    return jsonify({"msg": "contacto eliminado"})