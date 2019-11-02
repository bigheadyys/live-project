import requests
import re

def location(address):
    params = {
        'key': 'fc641da1ae198d2cdd11a784732a247a',
        'address': address
    }
    r = requests.get('https://restapi.amap.com/v3/geocode/geo', params=params)
    data=r.json()
    loca=data.get('geocodes')[0].get('location')
    return loca

def around(loca):
    params = {
        'key': 'fc641da1ae198d2cdd11a784732a247a',
        'location': loca,
        'keywords':'美食'
    }
    r = requests.get('https://restapi.amap.com/v3/place/around', params=params)
    data=r.json()
    pois=data.get('pois')
    list=[]
    print(pois)
    for each in pois:
        list.append(each.get('name'))
    return list

def map(loca):
    params={
        'key': 'fc641da1ae198d2cdd11a784732a247a',
        'location': loca,
        'zoom':'17'
    }
    r = requests.get('https://restapi.amap.com/v3/staticmap', params=params)
    with open('test.jpg','wb') as f:
        f.write(r.content)

def poi(n):
    params = {
        'key': 'fc641da1ae198d2cdd11a784732a247a',
        'city': '福州',
        'keywords':'美食',
        'types':'050100',
        'extensions':'all',
        'page':str(n)
    }
    r = requests.get('https://restapi.amap.com/v3/place/text', params=params)
    pois = r.json().get('pois')
    return pois

if __name__ =='__main__':
    list1=[]
    for i in range(2,3):
        list1+=poi(i)
    print(list1)
    dic1 = {}
    list2=[]
    for each in list1:
        tmp=each.get('biz_ext').get('cost')
        if isinstance(tmp,list):
            list2+=''.join(tmp)
        '''
        if float(each.get('biz_ext').get('cost')) < 50:
            dic1[each.get('name')] = float(each.get('biz_ext').get('rating')) / float(each.get('biz_ext').get('cost'))
        '''
    print(list2)