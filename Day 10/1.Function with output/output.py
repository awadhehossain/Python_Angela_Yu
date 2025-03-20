def format_name(f_name,l_name):
    formated_f_name =f_name.title()
    formated_l_name =l_name.title()
    return f"{formated_f_name} {formated_l_name}"

full_name=format_name(input("What is your first name?\n"),input("What is your last name?\n"))
print(full_name)

    