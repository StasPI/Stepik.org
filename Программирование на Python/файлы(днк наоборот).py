with open(r'A:\dataset_3363_2 (1).txt') as inf:  # открытие файла и его чтение
    file_str = inf.readline()
nubmer_str = str()
job_list = []
finish_str = str()
for element in file_str:  # делю строку на числа и буквы, и загружаю их в список
    if element.isalpha():  # если элемент буква проваливаюсь внутрь
        job_list.append(nubmer_str)
        job_list.append(element)
        nubmer_str = str()
    else:
        nubmer_str = nubmer_str + element  # накапливаю цифры для последующей загрузки
# по окончанию цикла гружу последнюю накопленную цифру
job_list.append(nubmer_str)
# удаляю пустую строку из списка которую пришлось внести что бы правильно запустить предыдущий цикл
del job_list[0]
while len(job_list) > 1:  # циком до последнего значения создаю строку для последующей записи в файл
    # т.к. нулей элемент списка буква умножаю ее на первый элемент число
    finish_str = finish_str + (job_list[0] * int(job_list[1]))
    # удаляю нулевой элемент то есть букву, и затем снова нулейвой но уже цифру так как она стала нулевым
    del job_list[0]
    del job_list[0]
# открываю файл на запись обратить внимание на r+ и записываю в него финальную строку
with open(r'A:\a.txt', 'r+') as ouf:
    ouf.write(finish_str)

# На прошлой неделе мы сжимали строки, используя кодирование повторов.Теперь нашей задачей будет
# восстановление исходной строки обратно.
# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования
# повторов, и производит обратную операцию, получая исходный текст.
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
# Примечание.Это первое задание типа Dataset Quiz.В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка
# "download your dataset".Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер.
# Запустите вашу программу, используя этот файл в качестве входных данных.Выходной файл, который при этом у вас
# получится, надо отправить в качестве ответа на эту задачу.
# Sample Input:
# a3b4c2e10b1
# Sample Output:
# aaabbbbcceeeeeeeeeeb
