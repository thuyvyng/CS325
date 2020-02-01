def max_wis(a):
    mis = {}
    def _max_wis(a):
        if len(a) <=0:
            return 0, []
        if len(a) not in mis:
            val1, list1 = _max_wis(a[:len(a)-1])
            val2, list2 = _max_wis(a[:len(a)-2])
            val2 += a[len(a)-1]
            if (val1 > val2):
                mis[len(a)] =(val1,list1)
            else:
                list3 = list2[:]
                list3.append(a[len(a)-1])
                mis[len(a)] = (val2,list3)
        return mis[len(a)]
    return _max_wis(a)


def max_wis2(a):
    prev = 0
    val2 = 0
    val1 = 0
    list1 = []
    list2 =[]
    prev_list = []
    result_list = []

    for i in range(len(a)):
        prev_list = list1[:]
        prev = val1
        val2 += a[i]
        list2.append(a[i])

        if (val1 < val2 + a[i]):
            result_int = val2
            result_list = list2[:]

            list1 = list2[:]
            val1 = val2
        else:
            result_int = val1
            result_list = list1[:]
        list2 = prev_list[:]
        val2 = prev

    return result_int, result_list


