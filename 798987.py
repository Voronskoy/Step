result = []
def divider(a, b):
    try:
        if a < b:
          raise ValueError
        if b > 100:
          raise IndexError
        return a/b
    except Exception as e:
        return f"Exception - {e}"
data = {10:2, 2:5, "123":4, 18:0, '[]':15, 8:4}
try:
    for key in data: 
        res = divider (key, data[key]) 
        result.append(res)
except:
    print("!!!")

for key in result:
    print(key)