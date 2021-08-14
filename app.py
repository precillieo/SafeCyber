from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app= Flask(__name__, template_folder= "templates")
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://egeyxqvvwyzdxm:1eef9bc22e70b9f307273cf3279f874b61e88d76fa2cb7530b57c936b2543f76@ec2-3-233-100-43.compute-1.amazonaws.com:5432/d2npo0hg6mu43l'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)



class User(db.Model):
	id= db.Column(db.Integer, primary_key=True)
	first_name= db.Column(db.String(20), nullable=False)
	last_name= db.Column(db.String(20), nullable=False)
	email_address= db.Column(db.String(120), unique=True, nullable=False)
	phone_number= db.Column(db.String(20), nullable=False)
	social_media_handle= db.Column(db.String(20), nullable=False)
	location= db.Column(db.String(100), nullable=False)
	attackers_identity= db.Column(db.String(120), nullable=False)
	summary_of_harassment= db.Column(db.String(1000), nullable=False)
	date_posted= db.Column(db.DateTime, nullable=False, default= datetime.utcnow)
	image_file= db.Column(db.String(20), nullable=False, default= 'default.jpg')
	category_of_harassment= db.Column(db.String(60), nullable=False, default= 'CyberStalking')
	db.create_all()

	def __repr__(self):
		return f"User('{self.first_name}', '{self.email_address}', '{self.date_posted}', '{self.category_of_harassment}')"



@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('main.html')


@app.route('/details', methods=['GET', 'POST'])
def details():
	if request.method == 'POST':
		user= User(first_name= request.form.get('fn'), last_name=request.form.get('ln'),
			email_address=request.form.get('email'), phone_number= request.form.get('phone'),
			social_media_handle=request.form.get('handle'), location=request.form.get('location'),
			attackers_identity=request.form.get('attackers_handle'), summary_of_harassment=request.form.get('comment'),
			image_file= request.files.get('imagefile'), category_of_harassment= request.form.get('category_of_harassment'))
		db.session.add(user)
		db.session.commit()
		print('Successfully added')

	return render_template('form.html')



@app.route('/admin', methods=['GET', 'POST'])
def admin_portal():
	return render_template('admin.html')


if __name__ == "__main__":
	app.run(debug=True)