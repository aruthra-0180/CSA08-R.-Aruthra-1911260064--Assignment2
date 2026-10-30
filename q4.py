import time

items = [f"Item{i}:Rs{i % 50}" for i in range(10000)]


def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text


def build_join(parts):
    return ";".join(parts) + ";"
def build_fstring(parts):
    result = []
    for p in parts:
        result.append(f"{p};")
    return "".join(result)
start = time.perf_counter()
a = build_plus(items)
t_plus = time.perf_counter() - start

start = time.perf_counter()
b = build_join(items)
t_join = time.perf_counter() - start

start = time.perf_counter()
c = build_fstring(items)
t_fstring = time.perf_counter() - start

print("Plus and join same:", a == b)
print("Plus and f-string same:", a == c)
print("Length:", len(a))

print(f"+= time: {t_plus:.4f} seconds")
print(f"join time: {t_join:.4f} seconds")
print(f"f-string time: {t_fstring:.4f} seconds")