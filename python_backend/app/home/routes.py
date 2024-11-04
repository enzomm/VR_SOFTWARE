from app.home import blueprint
from flask import jsonify, request, abort
from app.home.models import Product
from app.ext.database import db
from app.home.forms import ProductForm

    
@blueprint.route('/get_products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        result = [product.serialize() for product in products]
        return jsonify(result), 200
    except Exception as e:
        abort(500, description=str(e))


@blueprint.route('/get_product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        return jsonify(product.serialize()), 200
    except Exception as e:
        abort(500, description=str(e))


@blueprint.route('/set_product', methods=["POST"])
def set_product():
    data = request.get_json()
    form = ProductForm(data=data)
    if form.validate():
        try:
            new_product = Product(
                image=form.image.data,
                description=form.description.data,
                cost=form.cost.data,
                type=form.type.data
            )
            db.session.add(new_product)
            db.session.commit()
            return jsonify({'message': 'Product added successfully!'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else:        
        return jsonify({'errors': form.errors}), 400


@blueprint.route('/update_product', methods=['POST'])
def update_product():
    data = request.get_json()    
    form = ProductForm(data=data)
    if form.validate():
        try:
            product = Product.query.get_or_404(data['id'])
            product.image = form.image.data
            product.description = form.description.data
            product.cost = form.cost.data
            product.type = form.type.data
            db.session.commit()
            return jsonify({'message': 'Product updated successfully!'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else:        
        return jsonify({'errors': form.errors}), 400


@blueprint.route('/delete_product/<int:product_id>', methods=["DELETE"])
def delete_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))
