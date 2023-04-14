def bubble_sort(array):


    for item in range(len(array)-1):

        for i in range(len(array)-1):


            if array[i]>array[i+1]:

                array[i],array[i+1]=array[i+1],array[i]


    return array



test=[1,2,570,1,4,5,98,0]


print(bubble_sort(test))