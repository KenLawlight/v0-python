def pluck(d, keys):
    result = {}
    for key in keys:
        if key in d:
            result[key] = d[key]
    return result


print(pluck(
    {"name":"Fido","color":"Brown","breed":"German Shepherd"},
    ["name","breed"]
))

print(pluck(
    {"make":"Tesla","mpg":93,"model":"Model X","color":"white"},
    ["make","model"]
))
