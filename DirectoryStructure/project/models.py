from project import db

import datetime 

class TABLENAME(db.Model):

	__tablename__ = TABLENAME


	column = db.Column(db.COLUMNTYPE, primary_key=True, nullable=False, default=datetime.datetime.utcnow(), db.ForeinKey(''))
             db.relationship('TABLENAMEP', backref='name')
	def __init__(self, CLUMNNAMES)
	    self.COLUMNNAME  = COLUMNNAME


	def __repr__(self):
		return ''.format(self.)

