import bs4
from apt.package import unicode
from bs4 import ResultSet, NavigableString

file = 'Artificial_intelligence'
path = '/home/masha/dive_into_python/dive_into_python/web_services/week2/soup_sample/wiki/'

with open("{}{}".format(path, file)) as data:
    soup = bs4.BeautifulSoup(data, "lxml")

    t = soup.find('a')
    max_linkslen = 0
    while not (t == None):
        print('======= t:', t)

        # next_sublings: ResultSet = t.find_next_siblings()
        # print(next_sublings) # []

        # next_sublings = t.nextSibling
        # print(next_sublings) # depends on markup
        #
        # next_sublings = t.next_element
        # print(next_sublings) # sometime text

        #

        # next_sublings = t.find_next()
        # print(next_sublings) # None
        #
        linkslen = 0  # Длина максимальной последовательности ссылок, между которыми нет других тегов
        next_subling = t.find_next_sibling()
        while not (next_subling == None) and next_subling.name == 'a' :
            # and not (
            #     isinstance(next_element.next_element, NavigableString)  and len( unicode(next_element.next_element.string).strip()) > 0):
            # and next_element.next_element==None :

            linkslen += 1
            print('next_sibling>>>> ', next_subling)
            next_subling = next_subling.find_next_sibling()

        if max_linkslen < linkslen:
            max_linkslen = linkslen
            print('++++', max_linkslen)
        if next_subling == None:
            t = t.find_next('a')
        else:
            t = next_subling.find_next('a')
    print(max_linkslen)
#


# next_sublings = t.findNext
# print(next_sublings) # too many content
#
# next_sublings = t.findNextSibling
# print(next_sublings) # too many content
#
# next_sublings = t.findNextSiblings
# print(next_sublings) # too mane content
