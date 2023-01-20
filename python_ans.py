def pricCheck(products, productPrices, productSold, soldPrice):
    dictProdcuts = {}
    cnt = 0
    for i in range(len(products)):
        dictProdcuts[products[i]] = productPrices[i];
    for i in range(len(productSold)):
        if productSold[i] in dictProdcuts:
            if dictProdcuts[productSold[i]] != soldPrice[i]:
                cnt += 1
    return cnt


def recursiveDigit(n):
    if n == 0:
        return 0
    return (n % 10 + recursiveDigit(int(n / 10)))


def recursiveSequencerWrapper(numArr, index, __max, cnt):
    num = int(numArr[index])
    if num == 0:
        return cnt, __max
    if num > __max:
        __max = num
        cnt = 1
    elif num == __max:
        cnt += 1
    return recursiveSequencerWrapper(numArr, index + 1, __max, cnt)


def recursiveSequencer(stream):
    numArr = stream.split(' ')
    tup_cnt = recursiveSequencerWrapper(numArr, 0, 0, 0)
    print(tup_cnt)


if __name__ == "__main__":
    '''print(pricCheck(['rice', 'sugar', 'wheat', 'cheese'],[16.89, 56.92, 20.89, 345.99],['rice', 'cheese','cheese'],
[18.99, 400.89,345.99]))
    print(recursiveDigit(2347623))'''
    recursiveSequencer("1 5 42 -376 5 19 5 3 42 2 0")
