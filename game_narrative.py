def welcome_titile(tk, flag):
    if flag:
        first = "You woke up in the forest, and you don't remember anything.\n"
        second = "Look around and explore the forest. Be carefull !!!\n"
        third = "Aviable comands: arrow keys, up *, down *, left *, right *, exit.\n"
        fourth = "Intead of * can be number from 1 to 20"
        tk.print_info_message(first)
        tk.print_info_message(second)
        tk.print_info_message(third)
        tk.print_info_message(fourth)

def display(tk, message = 1):
    welcome_titile(tk, 1)