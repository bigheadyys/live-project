import requests
import  json
from tqdm import  tqdm
key = "e4d859d84c865870e298270049e11847"

宝龙万象 = 691.1
泰禾 = 224.6
东百 = 573.3
中亭街 = 304


shangquan = {}
for i in range(1000):
    url = "https://restapi.amap.com/v3/place/text?key=e4d859d84c865870e298270049e11847&keywords=服饰+仓山万达&types=&city=福州&children=1&offset=25&page="+str(i)+"&extensions=all"

    text = requests.get(url).text
    data = json.loads(text)

    if (len(data["pois"]) == 0):
        break

    for x in data["pois"]:
        if len(x["business_area"]) == 0:
            continue

        if x["business_area"] not in shangquan.keys():
            shangquan[x["business_area"]] = 0
        else:
            try:
                shangquan[x["business_area"]] += float(x["biz_ext"]["rating"])
            except:
                pass

print(shangquan)
