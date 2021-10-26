from app import app, db, models
from flask import redirect, render_template, url_for, flash


@app.context_processor  # pass ads_count information to templates
def provide_ads_count():
    ads_count = models.Ads.query.count()
    return {'ads_count': ads_count}


@app.route('/')
def index():
    our_ads = models.Ads.query.order_by(models.Ads.date_added)
    return render_template('index.html', our_ads=our_ads)


@app.route('/item/<itemid>')
def item(itemid):
    ad = models.Ads.query.filter_by(id=itemid).first()
    return render_template('item.html', ad=ad)


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
        description = form.description.data
        location = form.location.data
        ad = models.Ads(name=name, photo=photo, price=price, condition=condition, phonenumber=phonenumber, email=email,
                    description=description, location=location)
        db.session.add(ad)
        db.session.commit()
        form.name.data = ''
        form.photo.data = ''
        form.price.data = ''
        form.condition.data = ''
        form.phonenumber.data = ''
        form.email.data = ''
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