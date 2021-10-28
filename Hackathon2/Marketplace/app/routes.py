from app import app, db, models
from flask import redirect, render_template, url_for, flash, request
from sqlalchemy import or_, func
import random
from faker import Faker


@app.context_processor  # pass ads_count information to templates
def provide_ads_count():
    ads_count = models.Ads.query.count()
    return {'ads_count': ads_count}


@app.route('/')
def index():
    our_ads = models.Ads.query.order_by(models.Ads.date_added)
    return render_template('index.html', our_ads=our_ads)


@app.route('/fakeads')
def fakeads():
    print('add fake ad')
    fake = Faker()
    for _ in range(5):
        name = fake.word()
        photo = fake.image_url()
        price = str(random.randint(1, 5000)) + '$'
        choices = ['New', 'Used', 'Barely used']
        condition = random.choice(choices)
        category_choices = ['Vehicles', 'Real Estate', 'Apparel', 'Electronics', 'Home Goods',
                            'Musical Instruments', 'Office Supplies', 'Sporting Goods',
                            'Toys & Games', 'Hobbies', 'Family', 'Entertainment', 'Other']
        category = random.choice(category_choices)
        phonenumber = fake.phone_number()
        email = fake.email()
        description = fake.text()
        location = fake.address()
        ad = models.Ads(name=name, photo=photo, price=price, condition=condition, phonenumber=phonenumber, email=email,
                        category=category, description=description, location=location)
        db.session.add(ad)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete')
def deleteads():
    print('deleted all ads')
    models.Ads.query.delete()
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/search')
def search():
    query = request.args['search']  # search=keyword from search bar
    # searches both name and description columns for search result
    nameresults = models.Ads.query.filter(or_(models.Ads.name.contains(query),
                                              models.Ads.description.contains(query),
                                              models.Ads.location.contains(query),
                                              ))
    return render_template('search.html', nameresults=nameresults)


@app.route('/item/<itemid>')
def item(itemid):
    ad = models.Ads.query.filter_by(id=itemid).first()
    return render_template('item.html', ad=ad)


@app.route('/category/<categoryname>')
def showcategory(categoryname):
    category_ads = models.Ads.query.filter(models.Ads.category.contains(categoryname))
    return render_template('category.html', category_ads=category_ads)


@app.route('/delete/<itemid>')
def delete(itemid):
    user_to_delete = models.Ads.query.get_or_404(itemid)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("Listing Deleted Successfully")
        return redirect(url_for('index'))
    except:
        flash("Whoops! there was a problem deleting the listing, try again...")
        return redirect(url_for('index'))


@app.route('/create', methods=("GET", "POST"))
def create():
    name = None
    form = models.AdForm()
    if form.validate_on_submit():  # Check if the form has been filled
        name = form.name.data
        photo = form.photo.data
        price = form.price.data
        condition = form.condition.data
        phonenumber = form.phonenumber.data
        email = form.email.data
        category = form.category.data
        description = form.description.data
        location = form.location.data
        ad = models.Ads(name=name, photo=photo, price=price, condition=condition, phonenumber=phonenumber, email=email,
                        category=category, description=description, location=location)
        db.session.add(ad)
        db.session.commit()
        form.name.data = ''
        form.photo.data = ''
        form.price.data = ''
        form.condition.data = ''
        form.phonenumber.data = ''
        form.email.data = ''
        form.category.data = ''
        form.description.data = ''
        form.location.data = ''
        flash("Listing added successfully")
        return redirect(url_for('create'))
    return render_template("create.html", form=form, name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
