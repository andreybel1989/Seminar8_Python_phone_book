
def read_file(file):
    try:
        with open (file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError as err:           
        print("Телефонной книги еще нет\n")
        return[]

def show_data(data):
    
    for line in data:
        print(line.rstrip("\n"))

def save_data(file):
    print("Введите данные контакта")
    last_name = input("Введите фамилию ").replace(" ", "")
    first_name = input("Введите имя ").replace(" ", "")
    patronimys = input("Введите отчество ").replace(" ", "")
    phone_number = input("Введите номер телефона ").replace(" ", "")
    lines = read_file(file)
    for i in lines:
        i = i.split(" ")
        if last_name.lower() == i[0].lower() and first_name.lower() == i[1].lower() and patronimys.lower() == i[2].lower():
            print("Контакт с таким именем уже существует  в телефонной книге")
            return
    print("Контакт добавлен в телефонную книгу")    
    with open (file, "a", encoding="utf-8") as f:
        f.write(f"{last_name} {first_name} {patronimys} {phone_number}\n")

def search_data(contacts: list[str]):
    search_str = input("Введите фамилию для поиска: ").replace(" ", "").lower()
    founded = []

    for contact  in contacts:
        if search_str == contact.split(" ")[0].lower():
            founded.append(contact)
           
    if len(founded) > 1:
        search_str = input("Введите имя для поиска: ").replace(" ", "").lower()
        founded_copy = founded
        founded = []
        for contact  in founded_copy:
            if search_str == contact.split(" ")[1].lower():
                    founded.append(contact)
            
    if len(founded) > 1:
        search_str = input("Введите отчество для поиска: ").replace(" ", "").lower()
        founded_copy = founded
        founded = []
        for contact  in founded_copy:
            if search_str == contact.split(" ")[2].lower():
                    founded.append(contact)
    
    if len(founded) == 0:
        print("Такого контакта нет в телефонной книге")
           
     
    return founded        
def update_data(file):
    data = read_file(file)
    founded_data = search_data(data)
    if len(founded_data) != 0:
        print("Изменить контакт: ", end = "")
        show_data(founded_data)
        for i, contact in enumerate(data):
            if str(founded_data[0]) in contact:
                last_name = input("Введите новую фамилию ").replace(" ", "")
                first_name = input("Введите новое имя ").replace(" ", "")
                patronimys = input("Введите новое отчество ").replace(" ", "")
                phone_number = input("Введите новый номер телефона ").replace(" ", "")
                for j in data:
                    j = j.split(" ")
                    if last_name.lower() == j[0].lower() and first_name.lower() == j[1].lower() and patronimys.lower() == j[2].lower():
                        print("Контакт с таким именем уже существует в телефонной книге")
                        return
                data[i] = data[i].split(" ")
                data[i][0] = last_name
                data[i][1] = first_name
                data[i][2] = patronimys
                data[i][3] = phone_number + "\n"
                data[i] = ' '.join(map(str, data[i]))
        print("Контакт изменен")        
        with open(file, 'w', encoding="utf-8") as f:
            f.writelines(data)
    
def delete_contact(file):
    data = read_file(file)
    founded_data = search_data(data)
    if len(founded_data) != 0:
        
        data = [line for line in data if str(founded_data[0]) not in line]
        founded_data = founded_data[0].split(" ")
        print("Контакт удален из телефонной книги")
        with open(file, 'w', encoding="utf-8") as f:
            f.writelines(data)

def copy_phone_book(file, file_copy):
    data = read_file(file)
    print("Телефонная книга скопирована")
    with open(file_copy, 'w', encoding="utf-8") as f:
            f.writelines(data)

def copy_contact(file, file_copy):
    data = read_file(file)
    data_copy = read_file(file_copy)
    number_line = int(input("Введите номер строки, которую необходимо перенести из одной телефонной книги в другую "))    
    if 0 < number_line <= len(data):
        contact = data[number_line -1]
        for line in data_copy:
            if line == contact :
                print("Контакт с таким именем уже существует в телефонной книге") 
                return
        print("Контакт скопирован в новую телефонную книгу")       
        with open(file_copy, 'a', encoding="utf-8") as f:
                f.writelines(contact)      
    else:
        print("Данной строки не существует в телефонной книге") 
    
        

def main():
    file_name = "phone_book.txt"
    file_name_copy = "phone_book_new.txt"
    flag = True
    while flag:
        print("0 - выход")
        print("1 - добовление контакта в телефонную книгу")
        print("2 - показать телефонную книгу")
        print("3 - найти контакт в телефонной книге")
        print("4 - обновление контакта в телефонной книге")
        print("5 - удаление контакта из телефонной книги")
        print("6 - скопировать телефонную книгу")
        print("7 - скопировать строку телефонной книги")
        answer = input("Выберите действие:")
        if answer == "0":
            flag = False
        elif answer == "1":
            save_data(file_name)
        elif answer == "2":
            data = read_file(file_name)
            show_data(data)
        elif answer == "3":
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == "4":
            update_data(file_name)
        elif answer == "5":
            delete_contact(file_name)
        elif answer == "6":
            copy_phone_book(file_name, file_name_copy) 
        elif answer == "7":
            copy_contact(file_name, file_name_copy)                                            
if __name__ == "__main__":
    main()