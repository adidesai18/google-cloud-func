from email import message


def hello_world(request):
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
    return f" Hello {name}"

    