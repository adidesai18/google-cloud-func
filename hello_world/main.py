import flask

def hello_world(request=flask.request):
    print(type(request))
    request_args=request.args
    request_json=request.get_json(silent=True)
    print(request_args)
    print(request_json)
    if request_args and "name" in request_args:
        names_list = request_args["name"].split(",")
        if(request_args["name"]==""):
            name="Empyt name filed"
            return f"{name}"
        else:
            name=names_list[0]
    elif request_json :
        names_list = request_json["name"]
        if(not len(request_json["name"])):
            message="Empyt name filed"
            return f"{message}"
        else:
            name=names_list[1]
    # if(request_args):
    #     for arg in request_args:
    #         counter+=1
    #     return f"{counter}"
    else:
        name="world"
    headers= {
        'Access-Control-Allow-Origin': '*',
        'Content-Type':'application/json'
        }

    # text = '{"id1":"'+id1+'","var1":"'+var1+'"}'
    response={
        "name":request_json["name"],
        "age":request_json["age"],
    }
    # return (
    #         'Could not verify your access level for that URL.\n'
    #         'You have to login with proper credentials', 401,
    #         {'WWW-Authenticate': 'Basic realm="Login Required"'})
    return flask.make_response(response, 200, headers)
    # return response(f" Hello {name})"

    