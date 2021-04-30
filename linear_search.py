import random 

def lin_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1

def main():
  randomlist = random.sample(range(10, 30), 5)
  print(randomlist)

  print('Input number you want to search')
  i = input()
  i = int(i)
  i = lin_search(randomlist, i)
  print('Index found at: {}'.format(i))



if __name__ == "__main__":
    main()
