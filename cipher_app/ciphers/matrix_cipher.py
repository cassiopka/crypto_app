import numpy as np

def matrix_cipher(text_numeric, key_matrix):
    """Матричный шифр."""
    encrypted_messages = []
    print("<SDM> [matrix_cipher scope] encrypted_messages: ", encrypted_messages)

    key_size = key_matrix.shape[0]
    print("<SDM> [matrix_cipher scope] key_size: ", key_size)
    

    # Подготовка текста к шифрованию: разбиение на векторы длиной key_size
    text_chunks = [text_numeric[i:i+key_size] for i in range(0, len(text_numeric), key_size)]
    print("<SDM> [matrix_cipher scope] text_chunks: ", text_chunks)

    # Шифрование каждого вектора текста
    for chunk in text_chunks:
        # Дополнение вектора нулями до длины key_size, если необходимо
        while len(chunk) < key_size:
            chunk.append(0)
        # Умножение ключевой матрицы на вектор текста
        encrypted_vector = np.dot(key_matrix, chunk)
        print("<SDM> [matrix_cipher scope] encrypted_vector: ", encrypted_vector)

        # Добавление зашифрованного вектора в список зашифрованных сообщений
        encrypted_messages.append(encrypted_vector)

    # Конвертация списка зашифрованных сообщений в строку
    encrypted_str = ' '.join([str(vector) for vector in encrypted_messages]).replace('[', '').replace(']', '')
    return encrypted_str

def matrix_decipher(encrypted_message, key_matrix):
    """Дешифрование матричного шифра."""
    decrypted_messages = []  
    print("<SDM> [matrix_decipher scope] decrypted_messages: ", decrypted_messages)

    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  
    key_size = key_matrix.shape[0]  
    print("<SDM> [matrix_decipher scope] key_size: ", key_size)

    split_message = encrypted_message.split()  # Разбиваем зашифрованное сообщение на блоки по пробелам
    print("<SDM> [matrix_decipher scope] split_message: ", split_message)

    vectors = [] 
    print("<SDM> [matrix_decipher scope] vectors: ", vectors)

    for vector_block in split_message:
        vector_block = vector_block.replace(' ', '')  # Удаляем пробелы из блока
        vectors.append(vector_block)
    print("<SDM> [matrix_decipher scope] vectors: ", vectors)

    for i in range(0, len(split_message), key_size):
        vector_block = split_message[i:i+key_size]
        print("<SDM> [matrix_decipher scope] vector_block: ", vector_block)

        while len(vector_block) < key_size:
            vector_block.append('00')  # Дополняем векторы нулями до длины key_size
        vectors.append([int(num) for num in vector_block])

    encrypted_vectors = np.array(vectors, dtype=int)  
    print("<SDM> [matrix_decipher scope] encrypted_vectors: ", encrypted_vectors)


    inverse_key_matrix = np.linalg.inv(key_matrix)  # Вычисляем обратную матрицу для заданной ключевой матрицы
    print("<SDM> [matrix_decipher scope] inverse_key_matrix: ", inverse_key_matrix)


    for vector in encrypted_vectors:  # Проходим по каждому зашифрованному вектору
        decrypted_vector = np.dot(inverse_key_matrix, vector)  # Выполняем умножение обратной ключевой матрицы на зашифрованный вектор
        print("<SDM> [matrix_decipher scope] decrypted_vector: ", decrypted_vector)

        decrypted_str = ''.join([str(int(round(x))) for x in decrypted_vector])  # Преобразуем расшифрованный вектор в строку
        decrypted_messages.append(decrypted_str)  # Добавляем расшифрованное сообщение в список расшифрованных сообщений

    decrypted_text = ''  # Создаем пустую строку для хранения окончательного расшифрованного текста
    for message in decrypted_messages:  # Проходим по каждому расшифрованному сообщению
        for num in message:  # Проходим по каждой цифре в расшифрованном сообщении
            if num != '':  # Проверяем, что цифра не пустая
                letter_index = int(num) - 1  # Вычисляем индекс буквы в алфавите
                print("<SDM> [matrix_decipher scope] letter_index: ", letter_index)

                decrypted_text += alphabet[letter_index]  # Добавляем расшифрованную букву в окончательный расшифрованный текст

    return ''.join(decrypted_text)
