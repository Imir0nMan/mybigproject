def welcome_titile(tk, flag, k):
    if flag == 0:
        if k <= 30:
            first = """You woke up in the forest and don't remember anything:
Look around and explore the forest!!!
Available commands: arrow keys, up *, down *, left *, right *, exit:
instead of * there can be any number in the range from 1 to 20"""
            tk.print_info_message(first)
        else:
            tk.print_info_message("")
    elif flag == 13:
        end1 = """Congratulations, you have arrived in the city: The local police will help you get to the house 
where your sick mother was waiting for you.,
And this story about the forest will seem like a bad dream to you.\nThe game is over"""
        tk.print_info_message(end1)




def display(tk, message, k):
    welcome_titile(tk, message, k)
