def email_parse(email):
    parts = email.split("@")
    return {"username": parts[0], "domain": parts[1]}


print(email_parse("coolcoder42@goodmail.com"))
print(email_parse("az@woohoomail.com"))
print(email_parse("1337pr0graMmer@coldmail.edu"))
