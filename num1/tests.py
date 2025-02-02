from modules.avl_tree import AVLTree

def run_tests():
    print("Запуск тестов...")
    test_creating()
    test_search()
    test_incorrect_search()
    test_insert()
    test_delete()
    test_validator()
    test_height()
    test_count()
    test_merge()
    test_split()
    test_incorrect_split()
    print("Все тесты пройдены!")

def create_tree():
    tree = AVLTree()
    for i in range(10):
        tree.insert(i)
    return tree

def test_creating():
    tree = create_tree()
    assert tree.in_order_traversal() == [i for i in range(10)]

def test_search():
    tree = create_tree()
    assert tree.search(5) is not None

def test_incorrect_search():
    tree = create_tree()
    assert tree.search(125) is None

def test_insert():
    tree = create_tree()
    tree.insert(25)
    assert tree.in_order_traversal() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25]

def test_delete():
    tree = create_tree()
    for i in range(9):
        tree.delete(i)
    assert tree.in_order_traversal() == [9]

def test_validator():
    tree = create_tree()
    assert tree.validator() == True

def test_height():
    tree = create_tree()
    assert tree.get_height(tree.root) == 4

def test_count():
    tree = create_tree()
    assert tree.get_count() == 10

def test_merge():
    tree = create_tree()
    new_tree = AVLTree()
    for i in range(10, 16):
        new_tree.insert(i)
    tree.merge(new_tree)
    assert tree.in_order_traversal() == [i for i in range(16)]

def test_split():
    tree = create_tree()
    tree1, tree2 = tree.split(6)
    assert tree1.in_order_traversal() == [0, 1, 2, 3, 4, 5, 6] and tree2.in_order_traversal() == [i for i in range(7, 10)]

def test_incorrect_split():
    tree = AVLTree()
    tree.insert(1)
    tree.insert(2)
    tree1, tree2 = tree.split(15)
    assert tree1.in_order_traversal() == [1, 2] and tree2.in_order_traversal() == []