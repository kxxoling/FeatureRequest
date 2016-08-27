from flask import Blueprint, abort, request
from flask_marshmallow import Marshmallow
from flask_marshmallow.sqla import ModelSchema
from .models import Feature

api = Blueprint('api', __name__, url_prefix='/api')

# Should be split to single file in big project
ma = Marshmallow()


class FeatureSchema(ModelSchema):
    class Meta:
        model = Feature
        exclude = ('time_created', 'time_nearest_updated')


feature_schema = FeatureSchema()
features_schema = FeatureSchema(many=True)


@api.route('/features')
def features():
    all_features = Feature.query.all()
    return features_schema.jsonify(all_features)


@api.route('/features', methods=['POST', 'OPTIONS'])
def create_feature():
    json_data = request.get_json()
    print json_data
    if not json_data:
        abort(401)
    loaded = feature_schema.load(json_data)

    if loaded.errors:
        abort(401, loaded.errors)
    feature = loaded.data
    feature.save()
    return feature_schema.jsonify(feature)


@api.route('/features/<pk>')
def feature(pk):
    feature = Feature.query.filter(Feature.pk == pk).first()
    if feature is None:
        abort(404, 'Object with pk `{}` not found.'.format(pk))
    return feature_schema.jsonify(feature)
