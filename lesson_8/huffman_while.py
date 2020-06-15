from collections import Counter


class MyNode:
    def __init__(self, value, data=False, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.data = data

    def __str__(self):
        return '(value: ' + str(self.value) + ', data: ' + str(self.data) + ')'


def nodes_to_tree(nodes_as_list):
    while len(nodes_as_list) > 1:
        my_tree = MyNode(None)
        my_tree.left = nodes_as_list.pop()
        my_tree.right = nodes_as_list.pop()
        new_value = my_tree.left.value + my_tree.right.value
        my_tree.value = new_value
        current_len = len(nodes_as_list)
        for idx in range(current_len):
            if nodes_as_list[current_len - idx - 1].value >= new_value:
                nodes_as_list.insert(current_len - idx, my_tree)
                break
            elif current_len - idx - 1 == 0:
                nodes_as_list.insert(0, my_tree)
    return my_tree


def search(current_node, code_table_as_dict, path=''):
    if current_node.left is None and current_node.right is None:
        code_table_as_dict[current_node.data] = path
        return
    if current_node.left is not None:
        search(current_node.left, code_table_as_dict, path + '0')
    if current_node.right is not None:
        search(current_node.right, code_table_as_dict, path + '1')


def huffman_code(str):
    code_table_as_counter = Counter(str)
    code_table_as_nodes_list = []
    for n in range(len(code_table_as_counter)):
        dict_item_as_list = code_table_as_counter.most_common()
        data, value = dict_item_as_list[n]
        # print(value, data)
        code_table_as_nodes_list.append(MyNode(value, data))
    # for item in code_table_as_nodes_list:
    #      print(item)

    tree = nodes_to_tree(code_table_as_nodes_list)

    search(tree, code_table_as_dict, path='')
    # print(code_table_as_dict)
    str_coded_as_list = list()
    for letter in str:
        str_coded_as_list.append(code_table_as_dict[letter])
    # print(str_coded_as_list)
    str_coded = ('').join(str_coded_as_list)
    return str_coded, code_table_as_dict


my_str = 'Полковник открыл жестяную банку и обнаружил, что кофе осталось не больше чайной ложечки.';

code_table_as_dict = dict()
coded_as_str, code_table_as_dict = huffman_code(my_str)
print(coded_as_str)
print(code_table_as_dict)

def huffman_decode(str, code_table_as_dict):
    current_code_as_list = list()
    decoded_as_list = list()
    for elem in str:
        current_code_as_list.append(elem)
        current_code_as_str = ''.join(current_code_as_list)
        if current_code_as_str in code_table_as_dict.values():
            decoded_as_list.append(list(code_table_as_dict.keys())[list(code_table_as_dict.values()).index(current_code_as_str)])
            current_code_as_list = list()
    str_decoded = ''.join(decoded_as_list)
    return str_decoded


str_decoded = huffman_decode(coded_as_str, code_table_as_dict)
print(str_decoded)