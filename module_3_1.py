calls = 0
def count_calls():
    global calls
    calls +=56
def string_info(string):
    lost_1 = str(string)
    end = (len(lost_1), lost_1.upper(), lost_1.lower())
    count_calls()
    return end
def is_contains(string, list_to_search):
    message = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            end = True
            break
        else:
            end = False
            continue
    return end
print(string_info('Ugledar'))
print(string_info('Storm_shadow'))
print(is_contains('work', ['worK', 'worker', 'works']))
print(is_contains('WonDerfull', ['BancH', 'Lose', 'Gazelist', 'AgAte']))
print(calls)
