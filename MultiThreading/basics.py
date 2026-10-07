# import threading
# from concurrent.futures import ThreadPoolExecutor 

# def transformations(inputing):
#      src  = inputing['src']
#      dest = inputing['dest']

#      print(f"Reading from {src}")
#      print("Transforming.....")
#      print(f"Writing data to {dest}")
#      return f"Done {src} to {dest}"

# array = [
#      {"src": "table-1","dest": "table-1"},
#      {"src": "table-2","dest": "table-2"},
#      {"src": "table-3","dest": "table-3"}
# ]

# with ThreadPoolExecutor(max_workers=3) as executor:
#      futures = executor.map(transformations,array)
# print(f"Reuturned values are {list(futures)}")

n = int(input())
n_sum = 0
for i in range(1,n+1):
    n_sum += i

print(n_sum)

