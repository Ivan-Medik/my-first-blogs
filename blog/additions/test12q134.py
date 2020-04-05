num = 1
views_n = open("page_views.txt", 'r')
a = views_n.read()
count = int(a) + num
views_n.seek(0)
views_n.close()
views_n = open("page_views.txt", 'w')
views_n.write(str(count))
views_n.close()
