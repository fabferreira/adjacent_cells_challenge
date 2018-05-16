import json


def load_data(file_name):
    """ load matrix from a json file """
    with open(file_name, 'r') as outfile:
        data = json.load(outfile)
    outfile.close()
    return data


def get_points(points_list, list):
    """ get list with all coordinates with value 1 """
    try:
        for i in range(len(list)):
            for j in range(len(list[0])):
                if list[i][j] == 1:
                    points_list.append([i, j])
    except Exception as e:
        print(e, "- Attention, matrix dimensions error")


def get_group(points_list, results_list, coord=None):
    """ get list with coordinates of all points from a group """
    if coord is None:
        coord = [points_list[0][0], points_list[0][1]]
    i = coord[0]
    j = coord[1]
    if [i, j] not in results_list and [i, j] in points_list:
        results_list.append([i, j])
    if coord in points_list:
        points_list.remove(coord)
    for elem in ([i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]):
        if elem in points_list:
            results_list.append(elem)
            points_list.remove(elem)
            get_group(points_list, results_list, elem)


lista = []
final = []

input_file = "100x100.json"
input_matrix = load_data(input_file)
get_points(lista, input_matrix)

while len(lista) > 0:
    result = []
    get_group(lista, result)
    if len(result) > 1:
        final.append(result)
        print(result)
