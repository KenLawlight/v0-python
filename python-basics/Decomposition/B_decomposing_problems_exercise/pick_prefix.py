def pick_prefix(strings, prefix):
    return [word for word in strings if word.startswith(prefix)]

print(pick_prefix(['connect','company','concert','cram'],'con'))
print(pick_prefix(['miner','mistake','misspeak','moose','mission'],'mis'))