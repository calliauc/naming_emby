import os

print(os.path.abspath('.'))
print(os.path.dirname(os.path.abspath('.')))
print(os.path.basename(os.path.abspath('.')))

old_name = os.path.abspath('.')
new_name = f"{os.path.dirname(os.path.abspath('.'))}/stargate"

print(old_name)
print(new_name)

os.rename(old_name, new_name)