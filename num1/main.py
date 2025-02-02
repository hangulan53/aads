from modules.avl_tree import AVLTree
from tests import run_tests

if __name__ == "__main__":
    print("Примеры работы программы:")
    tree = AVLTree()
    for i in range(15):
        tree.insert(i)
    print("Созданное дерево:", tree.in_order_traversal())

    for j in range(1, 15, 2):
        tree.delete(j)
    print("Дерево после удаления элементов:", tree.in_order_traversal())

    new_tree = AVLTree()
    for i in range(1, 30, 2):
        new_tree.insert(i)

    tree.merge(new_tree)
    print("Дерево после мержа с другим:", tree.in_order_traversal())

    tree1, tree2 = tree.split(15)
    print("Деревья после сплита:", tree1.in_order_traversal(), tree2.in_order_traversal())

    print("Валидация дерева:", tree1.validator())

    print("Визуализация дерева:\n", tree1.visualize())

    run_tests()