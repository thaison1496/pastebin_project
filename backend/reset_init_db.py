import datetime

from app import db
from models import Pastes
import utils

db.drop_all()
db.create_all()

paste1 = Pastes(content='p1', paste_id=utils.generate_random_paste_id())
paste2 = Pastes(content='p2', paste_id=utils.generate_random_paste_id())

db.session.add(paste1)
db.session.add(paste2)
db.session.commit()

print(Pastes.query.all())
print(Pastes.query.filter(Pastes.content=='p2').first())

s = Pastes.query.filter(Pastes.content=='p2').first()
print(s.paste_id)
