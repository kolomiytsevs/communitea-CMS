from flask import request, render_template, flash, redirect, url_for, abort, Blueprint
from cmsdash.products.forms import NewProductForm
from cmsdash import db
from cmsdash.models import Product
from flask_login import current_user, login_required

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
