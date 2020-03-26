import requests, os,bs4,re,random,time

urlbase = 'https://gocomics.com/calvinandhobbes/'
os.makedirs('CalvinHobbs',exist_ok=True)
print("hello")
date = []

for year in range(1989,1992):
    for month in range(1,13):
       for day in range(1,32):
           try:
                #date = "1989-04-16"
                date = str(year)+'/'+str(month)+'/'+str(day)
                file_date= str(year)+'-'+str(month)+'-'+str(day)
                print("Downloading...  ",urlbase+date )
                res = requests.get(urlbase+date)
                res.raise_for_status()
                soup = bs4.BeautifulSoup(res.text, 'html.parser')
                #print(soup)
                soupData = soup.findAll('picture')
               #  print(soupData)
                correct_picture = soupData[1]
                #print(correct_picture)
                #pic_only = correct_picture.find('img')
                re_pattern = re.compile(r'assets.amuniversal.com/\S+')
                #print('regular expression')

                imageLink = re_pattern.findall(str(correct_picture))[0]
                #print(imageLink)
                # imageLink = []
                # for tag in soup.findAll('assets.amuniversal.com/', alt=True):
                #         # data = tag['src']
                #         # if data[0:3] == "//a":
                #         #     print(data)
                #         #     imageLink = data
                #         imageLink = tag
                #         print(imageLink)

                imageFromWeb = requests.get("https://" + imageLink)
               # print(imageFromWeb)
                #print(imageFromWeb.raw)

                with open('CalvinHobbs/'+file_date+'.gif', "wb") as f:
                    f.write(imageFromWeb.content)
                time.sleep(random.randint(6,11))
           except:
                print(date)
                print("FAILUREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!")


print("Done")