dict_errors = {
    'out': 'Вы вышли из системы ',
    'noaccess': 'У вас нет доступа в этот раздел',
    'unknown': 'Неизвестная ошибка',
    'timeout': 'Система долго не отвечает',
    'robot': 'Ваши действия похожи на робота',
}
def get_errors(*errors):
    list_error = []
    
    for i in errors:
        error = dict_errors[i]
        list_error.append(error)
    print(list_error)
    return list_error

get_errors('out', 'noaccess')
