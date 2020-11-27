import copy
import discord
from db import cnx
class Model():
	table_name = None
	primary_key = None

	def __init__(self,**kwargs):
		self.table_name = type(self).__name__
		attrs = vars(self)
		if 'primary_key' in attrs:
			self.primary_key = attrs['primary_key']
		else: self.primary_key = 'id'
		
		setattr(self,self.primary_key,None)
		attrs = vars(self)
		for key,value in kwargs.items():
			if key not in attrs:
				raise AttributeError(f"Property '{key}' does not exist in class: {type(self).__name__}")
			setattr(self,key,value)

	def save(self):

		properties = copy.deepcopy(vars(self))
		print(self.name)
		properties.pop('table_name')
		properties.pop('primary_key')
		if getattr(self,self.primary_key) is None:
			properties.pop(self.primary_key)
		propNum = len(properties)

		if propNum < 1:
			raise ValueError("A table must have at least one property")

		table_columns = ''
		for key in properties.keys():
			table_columns+=key+","

		table_columns = table_columns.rstrip(',')
		sqlQuery = "INSERT INTO " + self.table_name + " (" + table_columns + ") VALUES (" + "%s,"*(propNum-1) + "%s)"
		vals = list()
		for value in properties.values():
			vals.append(str(value))

		cursor = cnx.cursor()
		cursor.execute(sqlQuery,vals)
		cnx.commit()

	def get_one(self,pk):
		sqlQuery = "SELECT * FROM " + self.table_name + " WHERE " + self.primary_key + " = %s"
		cursor = cnx.cursor()
		cursor.execute(sqlQuery,[pk])
		desc = cursor.description
		column_names = [col[0] for col in desc]
		data = [dict(zip(column_names, cursor.fetchone()))]
		return [self.instance(**obj) for obj in data][0]

	def order_by(self,*colum_names, ascending : bool = True):
		sqlQuery = "SELECT * FROM " + self.table_name + " ORDER BY " 
		num_columns = len(colum_names)
		for key in colum_names:
			sqlQuery += key
			if ascending:
				sqlQuery+=' ASC'
			else: sqlQuery+=' DESC'
			if num_columns > 1:
				sqlQuery += ", "
			num_columns-=1

		cursor = cnx.cursor()
		cursor.execute(sqlQuery)
		desc = cursor.description
		column_names = [col[0] for col in desc]
		data = [dict(zip(column_names, row)) for row in cursor.fetchall()]
		return [self.instance(**obj) for obj in data]

	
	def getAll(self):
		sqlQuery = "SELECT * FROM " + self.table_name
		cursor = cnx.cursor()
		cursor.execute(sqlQuery)
		desc = cursor.description
		column_names = [col[0] for col in desc]
		data = [dict(zip(column_names, row)) for row in cursor.fetchall()]
		return [self.instance(**obj) for obj in data]

	def instance(self,**vals):
		return self.__class__(**vals)
		
	def get(self, **conditions):
		sqlQuery = "SELECT * FROM " + self.table_name + " WHERE "
		num_conditions = len(conditions)
		for key,value in conditions:
			sqlQuery += key + " = \'" + value + "\' "
			if num_conditions > 1:
				sqlQuery += "AND "
			num_conditions-=1
		
		cursor = cnx.cursor()
		cursor.execute(sqlQuery)
		desc = cursor.description
		column_names = [col[0] for col in desc]
		data = [dict(zip(column_names, row)) for row in cursor.fetchall()]
		return [self.instance(**obj) for obj in data]

	def update(self):
		self.delete()
		self.save()

	def delete(self):
		pk = getattr(self,self.primary_key)
		if pk is not None:
			cursor = cnx.cursor()
			cursor.execute(f"DELETE FROM {self.table_name} WHERE {self.primary_key} = {pk}")
			cnx.commit()

	def __str__(self):
		return self.table_name


class Ingredients(Model):

	def __init__(self,**kwargs):
		self.name = 'String'
		super().__init__(**kwargs)

	def __repr__(self):
		return self.__str__()
class Recipe(Model):
	def __init__(self,**kwargs):
		self.name = 'String'
		self.steps = 'String'
		super().__init__(**kwargs)
		
	def __str__(self):
		return super().__str__() +": " + self.name

	def __repr__(self):
		return self.__str__()

class Queue(Model):

	def __init__(self,queue_owner_id,**kwargs):
		self.table_name = 'Queue-'+queue_owner_id
		self.memberID = None
		self.priority = None
		super().__init__()

	def __str__(self):
		return super().__str__()

	def __repr__(self):
		return self.__str__()

	def next(self):
		instance = self.getAll()[0]
		instance.delete()
		return instance.memberID
