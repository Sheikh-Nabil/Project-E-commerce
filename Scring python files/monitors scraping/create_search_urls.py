f = open('search_urls.txt', 'w+')
url = 'https://www.amazon.com/s?k=monitor&i=computers-intl-ship&ref=nb_sb_noss_1'
f.write(url)
f.write('\n')


for i in range(2,200):
    url = 'https://www.amazon.com/s?k=monitor&i=computers-intl-ship&page='+str(i)+'&qid=1611052479&ref=sr_pg_'+str(i)
    f.write(url)
    f.write('\n')

f.close()
