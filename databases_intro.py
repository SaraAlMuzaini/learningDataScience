from sqlalchemy import create_engine

# The following code is in sql
engine = create_engine('sqlite:///census_nyc.sqlite')
connection = engine.connect()
stmt = 'SELECT * FROM people'
result_proxy = connection.execute(stmt)
results = result_proxy.fetchall()

# The following is in sqlalchemy (pythonic way)
from sqlalchemy import Table, MetaData
metadata = MetaData()
census = Table('census',metadata,autoload=True,autoload_with=engine)
stmt = select([census])
results = connection.execute(stmt).fetchall()

## To create a table with SQLAlchemy:

from sqlalchemy import Table, Column, String, Integer, Float, Boolean

data = Table('data',metadata,
            Column('name',String(255)),
            Column('count', Integer()),
            Column('amount', Float()),
            Column('valid', Boolean())
    )

#Use metadata to create the Table
metadata.create_all(engine)
print(repr(data))
