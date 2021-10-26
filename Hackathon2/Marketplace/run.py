import random
from app import app, db, models
from faker import Faker


def addfakead():
	print('add fake ad')
	fake = Faker()
	for _ in range(18):
		name = fake.word()
		photo = fake.image_url()
		price = str(random.randint(1, 5000))+'$'
		choices = ['New', 'Used', 'Barely used']
		condition = random.choice(choices)
		phonenumber = fake.phone_number()
		email = fake.email()
		description = fake.text()
		location = fake.address()
		ad = models.Ads(name=name, photo=photo, price=price, condition=condition, phonenumber=phonenumber, email=email,
						description=description, location=location)
		db.session.add(ad)
	db.session.commit()


if __name__ == '__main__':
	addfakead()
	app.run(debug=True)
