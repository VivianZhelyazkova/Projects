import json
FILE_PATH = "data.txt"
def write_to_file(records):
    string_data = json.dumps(records)
    with open(FILE_PATH,'w') as file_writer:
        file_writer.write(string_data)


def read_from_file():
    with open(FILE_PATH,'r') as file_reader:
        file_content = file_reader.read()
    converted_json_to_dict = json.loads(file_content)
    return converted_json_to_dict

