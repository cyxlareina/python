__author__ = 'lenovo'
result = [1]

candidates =[1,2,3,4,5,6,7,8,9,10]

base = 2

product = base


while candidates:

    while product < 10:

        if product in candidates:

            candidates.remove(product)

        product = product+base

    result.append(base)

    base = candidates[0]

    product = base

    del candidates[0]

    result.append(base)

    print (result)