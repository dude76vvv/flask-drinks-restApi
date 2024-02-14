from flask_restx import fields

from .extensions import api


drink_model = api.model("Drinks", {
    "id": fields.Integer,
    "drinkName": fields.String,
    "company": fields. String
})

drink_model2 = api.model("Drinks", {
    "id": fields.Integer,
    "drinkName": fields.String,
})


drinkCompany_model = api.model("Drinks_company", {
    "id": fields.Integer,
    "companyName": fields.String,
    "drinks": fields.List(fields.Nested(drink_model2))
    # "drinks": fields.Nested(drink_model2)
})

company_input_model = api.model("CompanyInput", {
    "companyName": fields.String,
})

drink_input_model = api.model("DrinkInput", {
    "drinkName": fields.String,
    "company": fields.String
})
