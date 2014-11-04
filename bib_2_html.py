from pybtex.database.input import bibtex
from operator import itemgetter, attrgetter
import pprint
parser = bibtex.Parser()
bib_data = parser.parse_file('2.txt')

def sort_by_year(y, x):
    return int(x[1].fields['year']) - int(y[1].fields['year'])

bib_sorted = sorted(bib_data.entries.items(), cmp=sort_by_year)


f = open('html.txt' ,'wb')
pyear = '2014'
f.writelines('<h3>'+pyear+'</h3>\n')
for key, value in bib_sorted:
    # print key,value.fields
    # print type(value.fields)
    keys = value.fields.keys()
    year =  value.fields['year']
    authors =  value.fields['author']
    title = value.fields['title']
    if 'Journal' in keys or 'Booktitle' in keys or 'journal' in keys or 'booktitle' in keys:
	    try:
	    	pub = value.fields['Journal']
	    except:
	    	pub = value.fields['Booktitle']
    else:
    	pub = ' '
    if '{' in title:
    	title = title.replace('{','')
    if '}' in title:
    	title = title.replace('}','')
    if float(year)!=float(pyear) and float(year) > 2009:
    	f.writelines('<h3>'+year+'</h3>\n')
    	pyear = year 
    line = authors + ': "' + title + '", '+ pub+',' + year +'.'
    f.writelines('<li>'+line+'</li>'+'\n')
    print line   
