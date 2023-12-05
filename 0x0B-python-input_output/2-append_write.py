
#!/usr/bin/python3
""" my mmodule """


def append_write(filename="", text=""):
    """ Append to ile """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
