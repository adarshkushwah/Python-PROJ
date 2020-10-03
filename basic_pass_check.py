user = input('Please enter your username : ')
passwd = input('Now please enter your password : ')

mask_pass_len = len(passwd) * '*'

print('Hi '+user+', your password is '+mask_pass_len+' characters long...')