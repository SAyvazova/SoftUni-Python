def data_types(type_data, data):
    if type_data == "int":
        data = int(data)
        result = data * 2
    elif type_data == "real":
        data = float(data)
        result = f"{data * 1.5:.2f}"
    elif type_data == "string":
        result = f"${data}$"

    return result


data_type = input()
input_data = input()

print(data_types(data_type, input_data))