class HashTable:
    def __init__(self, n=10):
        # Инициализация
        self.data = [None]*n
        self.count = 0

    def _get_fullness(self):
        # Коэффициент заполненности
        return round(self.count / len(self.data), 2)

    def _find_hash(self, key):
        # Нахождение хэша
        return hash(key) % len(self.data)

    def get(self, key):
        # Получение значения по ключу
        hash = self._find_hash(key)
        if (self.data[hash] is not None):
            return self.data[hash][1:]

    def append(self, key, value):
        # Добавление пары ключ-значение
        hash = self._find_hash(key)
        if (self.data[hash] is None):
            self.data[hash] = [key, value]
            self.count += 1
        elif (key == self.data[hash][0]):
            self.data[hash].append(value)

        if (self._get_fullness() > 0.66):
            self._resize()

    def delete(self, key):
        # Удаление значения по ключу
        hash = self._find_hash(key)
        if (self.data[hash] is not None):
            self.data[hash] = None
            self.count -= 1

    def _resize(self):
        # Изменение размера и перенос всех данных 
        new_data = [None]*(len(self.data)*2)
        for i in self.data:
            if (i is not None):
                hash = self._find_hash(i[0])
                new_data[hash] = i
        self.data = new_data

    def keys(self):
        # Получение всех ключей
        res = []
        for i in range(len(self.data)):
            if (self.data[i] is not None):
                res.append(self.data[i][0])
        return res

    def values(self):
        # Получение всех значений
        res = []
        for i in range(len(self.data)):
            if (self.data[i] is not None):
                res.append(self.data[i][1:])
        return res
    
    def items(self):
        # Получение всех пар ключ-значение
        res = []
        for i in range(len(self.data)):
            if (self.data[i] is not None):
                res.append([self.data[i][0], self.data[i][1:]])
        return res