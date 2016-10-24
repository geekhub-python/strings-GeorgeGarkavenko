#!/usr/bin/env python3

def handle_task_1(string):
    print(string[2]) # 1
    print(string[-2]) # 2
    print(string[:5]) # 3
    print(string[:-2]) # 4
    print(len(string)) # 5
    print(string[::2]) # 6
    print(string[1::2]) # 7
    print(''.join(reversed(string))) # 8
    print(''.join(reversed(string))[::2]) # 9
    
def handle_task_2(string):
    return len( string.split() )
    
def handle_task_3(string):
    small_half = len(string) // 2
    return string[-small_half:] + string[:-small_half]
    
def handle_task_4(string):
    return ' '.join( reversed(string.split()) )
    
def handle_task_5(string):
    return string.replace('1', 'one')

def handle_task_6(string):
    return string.replace('@', '')

def handle_task_7(string):
    
    if string.count('h') < 3:
        return string
    
    with_right = string.rsplit('h', 1)
    
    with_left = with_right[0].split('h', 1)
    middle_side = with_left[1].replace('h', 'H');
    
    return '{left}h{middle}h{right}'\
        .format( left=with_left[0],
                middle=middle_side,
                right=with_right[1] )

def handle_task_8(string):
    f_count = string.count('f')
    if f_count < 1:
        return None
    elif f_count < 2:
        return string.find('f')
    else:
        return string.find('f'), string.rfind('f')

def handle_task_9(string):
    f_count = string.count('f')
    if f_count < 1:
        return -2
    elif f_count < 2:
        return -1
    else:
        substring = string.split('f', 1)
        return len(substring[0]) + 1 + substring[1].find('f')
 
def handle_task_10(string):
    if string.count('h') < 2:
        return None
    with_right = string.rsplit('h', 1)
    with_left = with_right[0].split('h', 1)
    
    return  with_left[0] + with_right[1] 
    
 
def handle_task_11(string):
    
    if string.count('h') < 2:
        return None
    with_right = string.rsplit('h', 1)
    with_left = with_right[0].split('h', 1)
    
    middle_reversed = reversed(with_left[1])
    
    return  ''.join(middle_reversed)    
   
def handle_task_12(string):
    return ''.join(val for i, val in enumerate(string) if i % 3 != 0)
    
 
def main():
    test_string_num = '0123456789'
    test_string_verb = 'I am number 1. And my 1 e-mail is garkavenkogeorge@gmail.com . '
    test_string_two_words = 'Hello World'
    
    test_string_h = 'oohme 1hh2 orshe Ha'
    test_string_f = 'FFfaafoome ofrse hhFHha'
    
    print('Task 1 ')
    print('input: ' + test_string_num)
    print('output: ', end='')
    handle_task_1(test_string_num)
    print('=================================')
    print('Task 2 ')
    print('input: ' + test_string_verb)
    print('output: ', end='')
    print(handle_task_2(test_string_verb))
    print('=================================')
    print('Task 3 ')
    print('input: ' + test_string_num)
    print('output: ', end='')
    print(handle_task_3(test_string_num))
    print('=================================')
    print('Task 4 ')
    print('input: ' + test_string_two_words)
    print('output: ', end='')
    print(handle_task_4(test_string_two_words))
    print('=================================')
    print('Task 5 ')
    print('input: ' + test_string_verb)
    print('output: ', end='')
    print(handle_task_5(test_string_verb))
    print('=================================')
    print('Task 6 ')
    print('input: ' + test_string_verb)
    print('output: ', end='')
    print(handle_task_6(test_string_verb))
    print('=================================')
    print('Task 7 ')
    print('input: ' + test_string_h)
    print('output: ', end='')
    print(handle_task_7(test_string_h))
    print('=================================')
    print('Task 8 ')
    print('input: ' + test_string_f)
    print('output: ', end='')
    print(handle_task_8(test_string_f))
    print('=================================')
    print('Task 9 ')
    print('input: ' + test_string_f)
    print('output: ', end='')
    print(handle_task_9(test_string_f))
    print('=================================')
    print('Task 10 ')
    print('input: ' + test_string_h)
    print('output: ', end='')
    print(handle_task_10(test_string_h))
    print('=================================')
    print('Task 11 ')
    print('input: ' + test_string_h)
    print('output: ', end='')
    print(handle_task_11(test_string_h))
    print('=================================')
    print('Task 12 ')
    print('input: ' + test_string_num)
    print('output: ', end='')
    print(handle_task_12(test_string_num))
    print('=================================')
  
if __name__ == '__main__':
    main()