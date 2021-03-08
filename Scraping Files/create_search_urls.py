f = open('search_urls.txt', 'w+')

url = 'https://www.amazon.com/s?k=laptop&ref=nb_sb_noss_2'

f.write(url)
f.write('\n')

for i in range(2,51):
    url = "https://www.amazon.com/s?k=laptop&page=" + str(i)+ "&qid=1610650872&ref=sr_pg_" + str(i)
    f.write(url)
    f.write('\n')



f.close()