import handbook

if __name__ == "__main__":
    f_name = input('Enter the file name: ')
    print(handbook.find_pal(f_name))
    handbook.change_number(f_name)
    handbook.display(f_name)
