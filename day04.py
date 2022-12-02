import hashlib


def get_md5(data):
    return hashlib.md5(data.encode("utf-8")).hexdigest()


key = "bgvyzdsv"
found = False
i = 0

while not found:
    result = get_md5(key + str(i))
    prefix = result[0:6]
    if prefix == "000000":
        found = True
    else:
        i += 1


print(f"{found=}")
print(f"{result=}")
print(f"{i=}")


# Too high
