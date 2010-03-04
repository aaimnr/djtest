from django.http import HttpResponse 
def hello(request): 
    from urllib import urlopen
    import random, math
    r = random.random()
    ht = urlopen('http://xahlee.org/Periodic_dosage_dir/_p2/russell-lecture.html').read() 
    return HttpResponse(ht[int(r*10000):int(r*10000+10000)])

def rss(request):
    import string 
    import sys 
    import urllib2 
    from xml.dom import minidom
    return HttpResponse('rss')
