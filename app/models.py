from datetime import datetime

from . import db


class Submission(db.Model):
    """Simple model to store data submitted from the front-end form."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:  
        return f"<Submission {self.id} {self.email}>"

