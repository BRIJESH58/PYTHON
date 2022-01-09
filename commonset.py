def IntersecOfSets(arr1, arr2, arr3):
    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)
    print('List = ',arr1)
    print('Tuple = ',arr2)
    print('Dictionary = ',arr3)
    set1 = s1.intersection(s2)
    result_set = set1.intersection(s3)
    final_list = set(result_set)
    print('common of members of list, tuple & dictionary =',final_list)

    if_name_=='__main__'
    list1 = [1, 2, 'ABC', 'xyz']
    tuple1 = (80, 50, 'ABC', 'xyz')
    dictionary1 = {300, 900, 'ABC', 'xyz'}
    IntersecOfSets(list1,tuple1,dictionary1)