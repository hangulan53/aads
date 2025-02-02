from modules.node import Node

class AVLTree:
    def __init__(self):
        # Инициализация дерева
        self.root = None # корень
        self.count = 0 # количество элементов

    def get_count(self):
        # Возвращает количество узлов в дереве
        return self.count

    def get_height(self, node):
        # Возвращает высоту текущего узла
        if (not node):
            return 0
        return node.height
    
    def _update_height(self, node):
        # Увеличивает высоту текущего узла
        if (not node):
            return 0
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def _get_balance(self, node):
        # Возвращает значение баланса дерева
        if (not node):
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def _update_balance(self, node):
        # Выполняет балансировку дерева
        balance = self._get_balance(node)

        if (balance == 2):
            if (self._get_balance(node.left) == -1):
                node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if (balance == -2):
            if (self._get_balance(node.right) == 1):
                node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
        return node
    
    def find_min(self, root):
        # Выполняет поиск минимального элемента (для удаления)
        current = root
        while current.left:
            current = current.left
        return current
    
    def _right_rotate(self, y):
        # Правый поворот
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_height(y)
        self._update_height(x)
        return x

    def _left_rotate(self, x):
        # Левый поворот
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_height(x)
        self._update_height(y)
        return y
    


    def search(self, value):
        # "Обертка" для поиска
        return self._search_helper(self.root, value)

    def _search_helper(self, root, value):
        # Поиск
        if (not root or root.value == value):
            return root
        if (root.value < value):
            return self._search_helper(root.right, value)
        return self._search_helper(root.left, value)



    def insert(self, value):
        # "Обертка" для вставки
        self.root = self._insert_helper(self.root, value)
        self.count += 1

    def _insert_helper(self, root, value):
        # Вставка
        if (not root):
            return Node(value)
        elif (value < root.value):
            root.left = self._insert_helper(root.left, value)
        else:
            root.right = self._insert_helper(root.right, value)

        self._update_height(root)
        return self._update_balance(root)



    def delete(self, value):
        # "Обертка" для удаления
        self.root = self._delete_helper(self.root, value)
        self.count -= 1

    def _delete_helper(self, root, value):
        # Удаление
        if (not root):
            return root

        if (value < root.value):
            root.left = self._delete_helper(root.left, value)
        elif (value > root.value):
            root.right = self._delete_helper(root.right, value)
        else:
            if (not root.left):
                temp = root.right
                root = None
                return temp
            elif (not root.right):
                temp = root.left
                root = None
                return temp

            temp = self.find_min(root.right)
            root.value = temp.value
            root.right = self._delete_helper(root.right, temp.value)

        if (not root):
            return root

        self._update_height(root)
        return self._update_balance(root)



    def validator(self):
        # "Обертка" для проверки валидности дерева
        return self.validator_helper(self.root)

    def validator_helper(self, node):
        # Проверка валидности дерева
        if (not node):
            return True

        return (abs(self._get_balance(node)) <= 1 and self.validator_helper(node.left) and self.validator_helper(node.right))
    


    # Обходы возвращают массив с элементами, который можно либо печатать, либо использовать для сторонних целей

    def pre_order_traversal(self):
        # "Обертка" для прямого обхода
        return self._pre_order_traversal_helper(self.root, [])

    def _pre_order_traversal_helper(self, node, arr):
        # Прямой обход
        if (node):
            arr.append(node.value)
            self._pre_order_traversal_helper(node.left, arr)
            self._pre_order_traversal_helper(node.right, arr)
        return arr
    
    def in_order_traversal(self):
        # "Обертка" для центрированного прохода
        return self._in_order_traversal_helper(self.root, [])

    def _in_order_traversal_helper(self, node, arr):
        # Центрированный проход
        if (node):
            self._in_order_traversal_helper(node.left, arr)
            arr.append(node.value)
            self._in_order_traversal_helper(node.right, arr)
        return arr
    
    def post_order_traversal(self):
        # "Обертка" для обратного обхода
        return self._post_order_traversal_helper(self.root, [])

    def _post_order_traversal_helper(self, node, arr):
        # Обратный обход
        if (node):
            self._post_order_traversal_helper(node.left, arr)
            self._post_order_traversal_helper(node.right, arr)
            arr.append(node.value)
        return arr
    
    # Визуализация вовзращает строку, которую надо распечатать

    def visualize(self):
        # "Обертка" для визуализации дерева
        return self.visualize_helper(self.root, '', True)

    def visualize_helper(self, node, indent, last):
        # Визуализация дерева
        if (node):
            res = indent
            if (last):
                res += "└─ "
                indent += "   "
            else:
                res += "├─ "
                indent += "│  "
            res += str(node.value) + "\n"
            res += self.visualize_helper(node.right, indent, False)
            res += self.visualize_helper(node.left, indent, True)
            return res
        return ''
    


    def merge(self, other):
        # Слияние двух деревьев путем добавления элементов из одного в другое
        # Берется дерево с наименьшим количеством элементов, его элементы удаляются и добавляются в текущее дерево
        if (self.count < other.get_count()):
            values = self.in_order_traversal()
            for i in values:
                self.delete(i)
                other.insert(i)
            self.root = other.root
            self.count = other.count
        else:
            values = other.in_order_traversal()
            for i in values:
                other.delete(i)
                self.insert(i)

    def split(self, val):
        # Разделение дерева на два по заданному значению
        # Заданное значение остается в текущем дереве
        # Удаляется часть дерева, в которой меньше узлов относительного заданного элемента, из элементов этой части строится новое дерево
        # Возвращается два дерева в порядке "исходное дерево с данным значением", "новое дерево"
        values = self.in_order_traversal()
        new_tree = AVLTree()
        if (self.count > 1 and val in values):
            if (val < self.root.value):
                i = 0
                while (values[i] != val):
                    self.delete(values[i])
                    new_tree.insert(values[i])
                    i += 1
            else:
                i = self.count-1
                while (values[i] != val):
                    self.delete(values[i])
                    new_tree.insert(values[i])
                    i -= 1
        return self, new_tree