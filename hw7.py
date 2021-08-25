#!/usr/bin/env python3

def get_file_content(file_name):
    f = open(file_name, 'r')
    file_content = f.readlines()
    f.close()
    return file_content

def display_dict(data):
    for key, val in data.items():
        print(key, ':',','.join(val))

file_passwd = get_file_content('passwd')

passwd_keys = ['user_name', 'password', 'uid', 'gid', 'info', 'home_dir', 'bash']
passwd_list = [dict(zip(passwd_keys, line.split(':'))) for line in file_passwd]

bash_lst = [dct['bash'].replace('\n', '') for dct in passwd_list]

bash_counts = {bash: bash_lst.count(bash) for bash in set(bash_lst)}
print(bash_counts)

file_group = get_file_content('group')

group_keys = ['group_name', 'password', 'gid', 'users']
group_list = [dict(zip(group_keys, line.split(':'))) for line in file_group]

users_group = {}
users_list = []


for group in group_list:
    for user in passwd_list:
        if user['gid'] == group['gid']:
            users_list.append(user['uid'])
    users_group.setdefault(group['group_name'], users_list)
    users_list = []
   
display_dict(users_group)
