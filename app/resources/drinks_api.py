from flask import request, jsonify, make_response
from flask_restx import Resource, Namespace, abort, reqparse
from ..models.drinks_model import Drinks_company, Drinks as _Drinks
from ..serializer_model import drinkCompany_model, drink_model, company_input_model, drink_input_model
from ..extensions import db

# some custom exceptions that we can raise


class companyNotExistError(Exception):
    pass


class invalidRequestInputError(Exception):
    pass


# base api route
drinks = Namespace("api/v2")

# ========== glimpse of all available request ================


@drinks.route("/")
class AllDrinks(Resource):

    def get(self):
        '''show all available endpoints'''

        routes = [
            'GET /api/v2',
            'GET /api/v2/drink_companies',
            'GET /api/v2/drinks',

            'POST /api/v2/drink_companies',
            'POST /api/v2/drinks',

            'GET /api/v2/drink_companies/:id',
            'GET /api/v2/drinks/:id',

            'PUT /api/v2/drink_companies/:id',
            'PUT /api/v2/drinks/:id',

            'DELETE /api/v2/drink_companies/:id',
            'DELETE /api/v2/drinks/:id'

        ]

        return routes, 200

# ========== for drinks_companies request ================


@drinks.route("/drink_companies")
class DrinksCompanies(Resource):

    @drinks.marshal_list_with(drinkCompany_model)
    def get(self):
        return Drinks_company.query.all()

    @drinks.expect(company_input_model)
    @drinks.marshal_with(drinkCompany_model)
    def post(self):

        try:
            newCompany = Drinks_company(
                companyName=drinks.payload["companyName"])
            db.session.add(newCompany)
            db.session.commit()
            return newCompany, 201
        except Exception as e:
            print('An exception occurred')
            print(e)
            abort(400, f"Failed to create company with regards to: {e}")

# ========== for drinks request ================


@drinks.route("/drinks")
class Drinks(Resource):

    @drinks.marshal_list_with(drink_model)
    def get(self):
        return _Drinks.query.all()

    @drinks.expect(drink_input_model)
    @drinks.marshal_with(drink_model)
    def post(self):

        try:

            _drinkName = drinks.payload["drinkName"]
            temp_company = drinks.payload["company"]

            _company = Drinks_company.query.filter_by(
                companyName=temp_company).first()
            if not (_company):
                raise companyNotExistError

            newDrink = _Drinks(
                drinkName=_drinkName,
                drinkCompanyId=_company.id
                # company=_company
            )
            db.session.add(newDrink)
            db.session.commit()
            return newDrink, 201

        except companyNotExistError:
            abort(
                400, f"Drink Company {temp_company} does not exist. Pls create company first or verify your request")

        except Exception as e:
            print('An exception occurred')
            print(e)
            abort(400, f"Failed to create drinks with regards to: {e}")

# ========== for drinks_companies request with id ================


@drinks.route("/drink_companies/<int:id>")
class DrinksCompaniesId(Resource):

    @drinks.marshal_with(drinkCompany_model)
    def get(self, id):
        companyObj = Drinks_company.query.get_or_404(id)
        return companyObj

    @drinks.expect(company_input_model)
    @drinks.marshal_with(drinkCompany_model)
    def put(self, id):
        try:
            companyObj = Drinks_company.query.get_or_404(id)
            # companyObj.name = drinks.payload["companyName"]
            # another way of getting json data
            data = request.get_json()
            companyObj.companyName = data['companyName']
            db.session.commit()
            return companyObj

        except Exception as e:
            print('An exception occurred')
            abort(400, f"Failed to update company with regards to: {e}")

    def delete(self, id):

        try:
            companyObj = Drinks_company.query.get_or_404(id)
            db.session.delete(companyObj)
            db.session.commit()
            msg = f"company- {companyObj.companyName} was deleted"
            # return {'msg': msg}, 200
            return msg, 200
            # alternative 204 status code, but not no response body will be displayed

        except Exception as e:
            print(e)
            abort(400, f"Failed to delete company.{e}")


# ========== for drinks request with id ================

@drinks.route("/drinks/<int:id>")
class DrinksId(Resource):

    @drinks.marshal_with(drink_model)
    def get(self, id):
        drinkObj = _Drinks.query.get_or_404(id)
        return drinkObj

    @drinks.expect(drink_input_model)
    @drinks.marshal_with(drink_model)
    def put(self, id):
        try:
            drinkObj = _Drinks.query.get_or_404(id)
            # drinkObj.name = drinks.payload["companyName"]
            # another way of getting json data
            data = request.get_json()
            _drinkName = data['drinkName']
            _company = data['company']

            # do some simple validation here
            # company must exist in the datable
            # drink name must be valid -cannot be empty

            existComp = Drinks_company.query.filter_by(
                companyName=_company).first()

            if not existComp:
                raise companyNotExistError

            if not _drinkName:
                raise invalidRequestInputError

            if existComp and _drinkName:
                drinkObj.company = existComp
                drinkObj.drinkName = _drinkName
                db.session.commit()

            return drinkObj, 200

        except companyNotExistError:
            abort(
                400, f"Drink Company {_company} does not exist. Pls create company first or verify your request")

        except invalidRequestInputError:
            abort(
                400, f"invalid request. Pls verify your request. Drink name cannot be empty")

        except Exception as e:
            print('An exception occurred')
            abort(400, f"Failed to update drinks with regards to: {e}")

    def delete(self, id):

        try:
            drinkObj = _Drinks.query.get_or_404(id)
            cName = Drinks_company.query.get(
                drinkObj.drinkCompanyId).companyName
            db.session.delete(drinkObj)
            db.session.commit()
            msg = f"drink- {drinkObj.drinkName} from company {cName} was deleted"
            # return {'msg': msg}, 200
            return msg, 200
            # alternative 204 status code, but not no response body will be displayed

        except Exception as e:
            print(e)
            abort(400, f"Failed to delete drink.{e}")
