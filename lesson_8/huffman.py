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
    my_tree = MyNode(None)
    my_tree.left = nodes_as_list.pop()
    my_tree.right = nodes_as_list.pop()
    new_value = my_tree.left.value + my_tree.right.value
    my_tree.value = new_value
    current_len = len(nodes_as_list)
    if current_len == 0:
        print(my_tree)
        return my_tree
    for idx in range(current_len):
        if nodes_as_list[current_len - idx - 1].value >= new_value:
            nodes_as_list.insert(current_len - idx, my_tree)
            break
        elif current_len - idx - 1 == 0:
            nodes_as_list.insert(0, my_tree)

    # print('_' * 20)
    # for item in nodes_as_list:
    #     print(item)
    return nodes_to_tree(nodes_as_list)

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
    print(tree)
    code_table_as_list = list()
    # search(my_tree, code_table_as_list, path='')


my_str = 'Полковник открыл жестяную банку и обнаружил, что кофе осталось не больше чайной ложечки.';

huffman_code(my_str)
