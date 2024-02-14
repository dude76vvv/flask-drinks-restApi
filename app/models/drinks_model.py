from ..extensions import db


class Drinks_company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(50), unique=True, nullable=False)
    # referable by child as company
    drinks = db.relationship("Drinks", back_populates="company")

    def __repr__(self) -> str:
        return self.companyName


class Drinks(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    drinkName = db.Column(db.String(50), nullable=False)
    drinkCompanyId = db.Column(db.Integer, db.ForeignKey("drinks_company.id"))
    # referable by parent as drinks
    company = db.relationship("Drinks_company", back_populates="drinks")

    def __repr__(self) -> str:
        return self.drinkName

    # allow adding of same drinks name but to be from different company
    __table_args__ = (db.UniqueConstraint(
        "drinkName", "drinkCompanyId", name="company_drink_uc"),
    )
