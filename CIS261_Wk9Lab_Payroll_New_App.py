
def get_user_ids():
  file = open('top_secret.txt', 'r+')
  data = file.read()
  lines_of_data = data.split('\n')
  lines_of_data.pop()
  new_list=[]
  for l in lines_of_data:
    line_split = l.split('|')
    new_list.append(line_split[0])
  return file, new_list

def get_user_info(file, user_id_list):
  while True :
    user_id = input('USER_ID: ') 
    password = input('PASSWORD: ')
    auth_code = input('AUTHORIZATION CODE: ')
    if user_id.lower() == 'end':
      break
    elif user_id.lower() in user_id_list:
      print('User_ID Exists, Try Again.')
    else:
      if auth_code == 'Admin' or auth_code == 'User':
        new_record = f'{user_id.lower()}|{password}|{auth_code}\n'
        file.write(new_record)
      else:
        print('Incorrect Authorization Code Given, Try Again.')
  file.close()

def display_info(file):
  file = open('top_secret.txt', 'rt')
  data = file.read()
  file.close()
  print(data)

if __name__ == '__main__':
  file, user_id_list = get_user_ids()
  get_user_info(file, user_id_list)
  display_info(file)