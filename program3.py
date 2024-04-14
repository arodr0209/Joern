def process_name(name):
    temp_list = []
    result_list = []

    temp_list.append(name)
    result_list.append(temp_list[0])

    print(result_list[0])

def main():
    user_name = input("Please enter your name: ")
    process_name(user_name)

main()
