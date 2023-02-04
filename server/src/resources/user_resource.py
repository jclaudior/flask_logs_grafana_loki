from src import app, logger
from flask import jsonify, request, make_response
from flask_api import status
from src.services.user_service import UserService
from src.exceptions.user_exception import EmptyValueInAtribute, UserNotFountInDelete
from src.utils.logger_pattern import format

service = UserService()

@app.route('/user', methods=['GET'])
def list_users():
    try:
        users = service.list()
        response = make_response(jsonify(users), status.HTTP_200_OK)
        response.headers["Content-Type"] = "application/json"
        logger.info(format(level='info', class_or_file='user_resource', method_or_func='list_users', menssage='List users successfuly!', http_code=status.HTTP_200_OK))
    except Exception as error:
        response = make_response(jsonify({"message": str(error)}), status.HTTP_500_INTERNAL_SERVER_ERROR)
        response.headers["Content-Type"] = "application/json"
        logger.error(format(level='error', class_or_file='user_resource', method_or_func='list_users', menssage=str(error), http_code=status.HTTP_500_INTERNAL_SERVER_ERROR, cause=str(error)))
    return response


@app.route('/user/<id>', methods=['GET'])
def get_user_by_id(id):
    try:
        user = service.get_by_id(id)
        response = make_response(jsonify(user), status.HTTP_200_OK)
        response.headers["Content-Type"] = "application/json"
        logger.info(format(level='info', class_or_file='user_resource', method_or_func='get_user_by_id', entity={'id': id}, menssage='User get by id successfuly!', http_code=status.HTTP_200_OK))
    except TypeError as error:
        response = make_response(jsonify({"message": 'User not found' + str(error)}), status.HTTP_404_NOT_FOUND)
        response.headers["Content-Type"] = "application/json"
        logger.error(format(level='error', class_or_file='user_resource', method_or_func='get_user_by_id', entity={'id': id}, menssage='User not found', http_code=status.HTTP_404_NOT_FOUND, cause=str(error)))
    except Exception as error:
        response = make_response(jsonify({"message": str(error)}), status.HTTP_500_INTERNAL_SERVER_ERROR)
        response.headers["Content-Type"] = "application/json"
        logger.error(format(level='error', class_or_file='user_resource', method_or_func='get_user_by_id', entity={'id': id}, menssage=str(error), http_code=status.HTTP_500_INTERNAL_SERVER_ERROR, cause=str(error)))
    return response


@app.route('/user/<id>', methods=['PUT'])
def update_user_by_id(id):
    data = request.get_json()
    try:
        user = service.update(id, data)
        response = make_response(jsonify(user), status.HTTP_200_OK)
        response.headers["Content-Type"] = "application/json"
        logger.info(format(level='info', class_or_file='user_resource', method_or_func='update_user_by_id', entity={'id': id, 'data': data}, menssage='User update successfuly!', http_code=status.HTTP_200_OK))
    except KeyError as error:
        response = make_response(jsonify({"message": 'Required atribute ' + str(error)}), status.HTTP_400_BAD_REQUEST)
        response.headers["Content-Type"] = "application/json"
        logger.error(format(level='error', class_or_file='user_resource', method_or_func='update_user_by_id', entity={'id': id, 'data': data}, menssage='Required atribute', http_code=status.HTTP_400_BAD_REQUEST, cause=str(error)))
    except EmptyValueInAtribute as error:
        response = make_response(jsonify({"message": str(error)}), status.HTTP_400_BAD_REQUEST)
        response.headers["Content-Type"] = "application/json"
        logger.error(format(level='error', class_or_file='user_resource', method_or_func='update_user_by_id', entity={'id': id, 'data': data}, menssage='Empty value in attribute', http_code=status.HTTP_400_BAD_REQUEST, cause=str(error)))
    except TypeError as error:
        response = make_response(jsonify({"message": 'User not found' + str(error)}), status.HTTP_404_NOT_FOUND)
        response.headers["Content-Type"] = "application/json"
        logger.error(format(level='error', class_or_file='user_resource', method_or_func='update_user_by_id', entity={'id': id, 'data': data}, menssage='User not found', http_code=status.HTTP_404_NOT_FOUND, cause=str(error)))
    except Exception as error:
        response = make_response(jsonify({"message": str(error)}), status.HTTP_500_INTERNAL_SERVER_ERROR)
        response.headers["Content-Type"] = "application/json"
        logger.error(format(level='error', class_or_file='user_resource', method_or_func='update_user_by_id', entity={'id': id, 'data': data}, menssage=str(error), http_code=status.HTTP_500_INTERNAL_SERVER_ERROR, cause=str(error)))
    return response


@app.route('/user/<id>', methods=['DELETE'])
def delete_user_by_id(id):
    try:
        service.delete(id)
        response = make_response('', status.HTTP_204_NO_CONTENT)
        logger.info(format(level='info', class_or_file='user_resource', method_or_func='delete_user_by_id', entity={'id': id}, menssage='User deleted successfuly!', http_code=status.HTTP_204_NO_CONTENT))
    except UserNotFountInDelete as error:
        response = make_response(jsonify({"message": str(error)}), status.HTTP_404_NOT_FOUND)
        response.headers["Content-Type"] = "application/json"
        logger.error(format(level='error', class_or_file='user_resource', method_or_func='delete_user_by_id', entity={'id': id}, menssage='Error in delete', http_code=status.HTTP_404_NOT_FOUND, cause=str(error)))
    except Exception as error:
        response = make_response(jsonify({"message": str(error)}), status.HTTP_500_INTERNAL_SERVER_ERROR)
        response.headers["Content-Type"] = "application/json"
        logger.error(format(level='error', class_or_file='user_resource', method_or_func='delete_user_by_id', entity={'id': id}, menssage=str(error), http_code=status.HTTP_500_INTERNAL_SERVER_ERROR, cause=str(error)))
    return response


@app.route('/user', methods=['POST'])
def save_user():
    data = request.get_json()
    try:
        user = service.save(data)
        response = make_response(jsonify(user), status.HTTP_201_CREATED)
        response.headers["Content-Type"] = "application/json"
        logger.info(format(level='info', class_or_file='user_resource', method_or_func='save_user', entity=data, menssage='User save successfuly!', http_code=status.HTTP_201_CREATED))
    except KeyError as error:
        response = make_response(jsonify({"message": 'Required atribute ' + str(error)}), status.HTTP_400_BAD_REQUEST)
        response.headers["Content-Type"] = "application/json"
        logger.error(format(level='error', class_or_file='user_resource', method_or_func='save_user', entity=data, menssage='Required atribute', http_code=status.HTTP_400_BAD_REQUEST, cause=str(error)))
    except EmptyValueInAtribute as error:
        response = make_response(jsonify({"message": str(error)}), status.HTTP_400_BAD_REQUEST)
        response.headers["Content-Type"] = "application/json"
        logger.error(format(level='error', class_or_file='user_resource', method_or_func='save_user', entity=data, menssage='Empty value in attribute', http_code=status.HTTP_400_BAD_REQUEST, cause=str(error)))
    except Exception as error:
        response = make_response(jsonify({"message": str(error)}), status.HTTP_500_INTERNAL_SERVER_ERROR)
        response.headers["Content-Type"] = "application/json"
        logger.error(format(level='error', class_or_file='user_resource', method_or_func='save_user', entity=data, menssage=str(error), http_code=status.HTTP_500_INTERNAL_SERVER_ERROR, cause=str(error)))
    return response
    

