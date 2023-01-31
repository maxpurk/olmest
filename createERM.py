from sqlalchemy import create_engine, MetaData
from sqlalchemy_schemadisplay import create_schema_graph


engine = create_engine('sqlite:///db.sqlite3')

myMetadata = MetaData()
myMetadata.reflect(bind=engine)

table_names = myMetadata.tables.keys()
print(table_names)

for table_name in table_names:
    table = myMetadata.tables[table_name]
    print(table.columns.keys())
