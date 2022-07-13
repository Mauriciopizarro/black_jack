def ClientErrorResponse(code, description=''):
    description_dict = {
        'description': description,
        'code': code
    }
    return description_dict, 400

