def fibonacci():
    aux = 0
    first = 0
    second = 1
    for i in range(0,99):
        print(second,end=" ")
        aux = second
        second += first
        first = aux

fibonacci()