#include <stdio.h>

int search(int arr, int n, int x) {
  for (int i = 0; i < n; i++) {
    if (arr[i] == x) {
      return i;
    }
  }
  return -1;
}

int main() {
  int arr[] = {1, 2, 23,32, 12, 3, 0 ,23, 0, 1, 5, 8};
  int x = 8;
  int n = sizeof(arr) / sizeof(arr[0]);

  int result = search(arr, n , x);
  
  printf("Array:\n{");
  for (int i = 0; i < n; i++) {
    printf("%d", arr[i]);
    if (i < n - 1) {
      printf(", ");
    }
  }
  printf("}\n");

  printf("
  found %d at: %dth index\n", x, result);
  return 0;
}
