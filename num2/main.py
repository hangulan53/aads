from modules.hashtable import HashTable

if __name__ == "__main__":
    print("Примеры работы программы:")
    ht = HashTable()
    for i in range(15):
        ht.append(i, i**3)
        if (i%3 == 0):
            ht.append(i, i*13)

    print("Созданный ассоциативный массив:", ht.items())

    for j in range(1, 15, 2):
        ht.delete(j)
    print("Массив после удаления элементов с нечетным ключом:", ht.items())

    for k in range(0, 15, 2):
        print("Получение очередного массива с четным ключом:", ht.get(k))