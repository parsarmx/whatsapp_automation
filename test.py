with open("repo/text_field/text.txt") as file:
    text = file.readline()
    print(text.format(name="parsa", count="ramezani"))
