
'''
    The 'else' block will be executed only when the loop is not terminated abruptly by the 'break' keyword 
'''

def main():

    backend_lan = ['Python',"Java","C++","Ruby","Node.js"]
    for favorite_lang in backend_lan:
        if (favorite_lang == "C++"):
            print(f"I like C++")
            break
    else:
        print("I don't like C++")

    return
main()