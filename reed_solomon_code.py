from reedsolo import RSCodec

def reed_solomon_example(data):
    # Создаем объект для кодирования/декодирования с возможностью исправления до 10 ошибок
    rs = RSCodec(10)

    # Кодируем данные
    encoded_data = rs.encode(data)
    print(f"Закодированные данные: {encoded_data}")

    # Симулируем ошибки в данных
    corrupted_data = bytearray(encoded_data)
    corrupted_data[5] ^= 0x01  # Инвертируем один байт
    corrupted_data[10] ^= 0x02  # Инвертируем другой байт

    print(f"Искаженные данные: {corrupted_data}")

    # Декодируем данные
    decoded_data = rs.decode(corrupted_data)
    print(f"Декодированные данные: {decoded_data}")