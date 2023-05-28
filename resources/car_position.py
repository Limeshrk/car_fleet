from flask_restful import Resource, reqparse
from models.car import CarModel
from models.position import PositionModel
from datetime import datetime

class CarPosition(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('latitude',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('longitude',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self, plate):
        data = CarPosition.parser.parse_args()

        car = CarModel.find_by_attribute(license_plate=plate)
        if not car:
            return {'message': 'Car not found'}, 404

        car_position = PositionModel(date=datetime.now(), latitude=data['latitude'], longitude=data['longitude'], car_id=car.id)
        car_position.save_to_db()

        return {'message': 'Position saved successfully'}, 201
