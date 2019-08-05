from flask import request, render_template, flash, redirect, url_for, abort, Blueprint
from cmsdash.products.forms import NewProductForm
from cmsdash import db
from cmsdash.models import Product
from flask_login import current_user, login_required
from cmsdash.products.utils import save_picture

products = Blueprint('products', __name__)


@products.route('/product/new', methods=['GET', 'POST'])
@login_required
def new_product():
    form = NewProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data, price=form.price.data, in_stock=form.in_stock.data,
                          description=form.description.data, main_image=form.picture.data, weight=form.weight.data)
        db.session.add(product)
        db.session.commit()
        flash('Product added!', 'success')
        return redirect(url_for('main.home'))
    return render_template('new_product.html', title='Add Product', form=form, legend='Add Product')

@products.route('/product/<int:product_id>/update', methods=['GET', 'POST'])
@login_required
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = NewProductForm()
    if form.validate_on_submit():
        print(form.picture.data)
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            product.main_image = picture_file
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        product.in_stock = form.in_stock.data
        product.weight = form.weight.data
        db.session.commit()
        flash('Product updated!', 'success')
        return redirect(url_for('products.all_products'))
    elif request.method == 'GET':
        form.name.data = product.name
        form.description.data = product.description
        form.price.data = product.price
        form.in_stock.data = product.in_stock
        form.weight.data = product.weight
        form.picture.data = product.main_image
    return render_template('new_product.html', title='Update Product', form=form, legend='Update Product')


@products.route('/delete_product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted', 'danger')
    return redirect(url_for('products.all_products'))

@products.route('/all_products', methods=['GET', 'POST'])
@login_required
def all_products():
    page = request.args.get('page', 1, type=int)
    products = Product.query.order_by(Product.name.desc()).paginate(page=page, per_page=5)
    return render_template('product_dash.html', products=products)