def transform_data(data):
    def modify_text(text):
        return "Transformed: " + text

    result = modify_text(data)
    return result

def main():
    user_input = input("Please enter a text to transform: ")
    transformed_result = transform_data(user_input)
    print("Transformed Text:", transformed_result)

main()


