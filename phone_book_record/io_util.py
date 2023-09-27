import json
FILE_PATH = "data.txt"
def write_to_file(records):
    string_data = json.dumps(records)
    file_writer = open(FILE_PATH, "w")
    file_writer.write(string_data)
    file_writer.close()

def read_from_file():
    file_reader = open(FILE_PATH, 'r')
    file_content = file_reader.read()
    converted_json_to_dict = json.loads(file_content)
    return converted_json_to_dict

