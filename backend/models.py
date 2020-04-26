from objects import db
from sqlalchemy.sql import func

class Pastes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    paste_id = db.Column(db.String(24), unique=True, nullable=False)
    create_date = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<Paste {self.paste_id} {self.create_date.strftime("%Y-%m-%d %H:%M:%S")}:\n "{self.content}">\n'