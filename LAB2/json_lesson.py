""" json example
"""
import json

# simple serialization
data = {
    "student": {
        "name": "Arman",
        "species": "Ca de Bou",
        "group": "noname"
    }
}

with open('student_list.json', 'w') as f:
    json.dump(data, f, indent=4)


json_string = json.dumps(data, indent=4)
print(json_string)


student = ('Arman', 'Ca de Bou')
encoded_student = json.dumps(student)
decoded_student = json.loads(encoded_student)

print(student == decoded_student)

print(type(student))
print(type(decoded_student))
print(student == tuple(decoded_student))

# simple deserialization
with open('student_list.json', 'r') as f:
    decoded_students = json.load(f)

print(type(decoded_students))
print(decoded_students)

# # kved investigation
# PATH="kved.json"
#
# with open(PATH, 'r', encoding='utf-8') as f:
#     decoded_kved = json.load(f)
#
# print(type(decoded_kved), len(decoded_kved.keys()))
# print(decoded_kved.keys())
# print(type(decoded_kved['sections']), len(decoded_kved['sections']))
# print(len(decoded_kved['sections'][0]))
# sections = len(decoded_kved['sections'][0])
#
# for i in range(sections):
#     print(type(decoded_kved['sections'][0][i]),
#                decoded_kved['sections'][0][i].keys())
#
# for i in range(sections):
#     print(type(decoded_kved['sections'][0][i]['sectionCode']),
#           type(decoded_kved['sections'][0][i]['sectionName']),
#           type(decoded_kved['sections'][0][i]['divisions']))
#
# for i in range(sections):
#     print(type(decoded_kved['sections'][0][i]['sectionCode']),
#           type(decoded_kved['sections'][0][i]['sectionName']),
#           type(decoded_kved['sections'][0][i]['divisions']),
#           len(decoded_kved['sections'][0][i]['divisions']))
#
# print(decoded_kved['sections'][0][0]['divisions'][0])
# print(type(decoded_kved['sections'][0][0]['divisions'][0]))
#
# print(decoded_kved['sections'][0][0]['divisions'][0].keys())
#
# print(decoded_kved['sections'][0][0]['divisions'][1].keys())
# print(decoded_kved['sections'][0][0]['divisions'][0]['groups'])
# print(len(decoded_kved['sections'][0][0]['divisions'][0]['groups']))
# print(len(decoded_kved['sections'][0][0]['divisions'][1]['groups']))
# print(decoded_kved['sections'][0][0]['divisions'][0]['groups'][0])
# print(decoded_kved['sections'][0][0]['divisions'][0]['groups'][6])
# print(type(decoded_kved['sections'][0][0]['divisions'][0]['groups'][6]))
# print(decoded_kved['sections'][0][0]['divisions'][0]['groups'][6].keys())
# print(decoded_kved['sections'][0][0]['divisions'][0]['groups'][6]['classes'])
# print(decoded_kved['sections'][0][0]['divisions'][0]['groups'][0]['classes'])
#
#
