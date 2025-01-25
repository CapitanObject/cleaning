from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email= db.Column(db.String(255), unique=True, nullable=False)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    adress = db.Column(db.Terxt, nullable=False )
    phone = db.Column(db.String(20), nullable=False)
    service_type = db.Column(db.String(255), nullable=False)
    custom_service = db.Column(db.Terxt, nullable=True )
    date_time=db.Column(db.DateTime, nullable=True )
    payment_type = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(20), default='new')
    cancel_reason = db.Column(db.Terxt, nullable=True )
