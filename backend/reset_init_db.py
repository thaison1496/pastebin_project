import datetime

from app import db
from models import Pastes

db.drop_all()
db.create_all()

paste1 = Pastes(content='p1')
paste2 = Pastes(content='p2')

db.session.add(paste1)
db.session.add(paste2)
db.session.commit()

print(Pastes.query.all())
print(Pastes.query.first())