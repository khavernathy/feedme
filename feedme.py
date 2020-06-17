# the setup.py script will install these dependencies
# but if you want to work for it..
## pip3 install beautifulsoup4
# or..
# apt-get install python3-bs4
from bs4 import BeautifulSoup
# pip3 install termcolor
from termcolor import colored

#these should come with python i guess
import math
import random
import urllib.request as urllib2
import sys
import json

# boldify
def b(s):
    return colored(s, attrs=['bold'])

def feedme():
    basename = "http://reciperoulette.tv/getRecipeInfoPrest?id="

    maxid = 50000

    goodlist = []
    for i in range(10000): # u will never read 10000 recipes bro relax
        rid = int( math.floor(  random.random() * maxid ) )
        url = basename + str(rid)

        response = urllib2.urlopen( url )
        # handle forward
        #goodurl = response.geturl()
        #response = urllib2.urlopen( goodurl )

        # read html
        page_source = response.read() 

        # soupify
        soup = BeautifulSoup( page_source, 'html.parser' )
        # jsonify the soup
        js = json.loads( str(soup) )

        try:
            print( colored( str(js['id']) + ": " + js['name'].replace("&amp;","&"), 'red', attrs=['bold'] ) )

            x = input("is sound good? [ (anything) for yes; (n) for no; (x) to exit >.<]:   ")
            if (x == "x"):
                print(colored("bye hope u eat nice meal", 'red'))
                sys.exit()
            elif (x != "n"):
                print("")
                print("")
                fid = str( js['id'] )
                name = str( js['name'] )
                desc = str( js['description'] ).replace("&amp;","&")
                pic = str( js['picture'] )
                serves = str( js['serve']) 
                time_Cooking = str( js['time_Cooking'] )
                time_Preparation = str( js['time_Preparation'])
                time_Total = str( js['time_Total'] )

                #print( fid + ": " + name + '\n' )
                print( colored( desc, 'white', 'on_red' ) + "\n" )
                print( b("Link: ") + url )
                print( b("Picture: ") + pic )
                print( b("Serves: ") + serves )
                print( b("Prep time: ") + time_Preparation )
                print( b("Cook time: ") + time_Cooking )
                print( b("Total time: ") + time_Total )
                print("")
                print( colored("Ingredients: ", 'green') )
                for ing in js['ingdt']:
                    print( " - " + ing['name'] )
                print("")
                print( colored("Methods: ", 'green') )
                c=1
                for meth in js['methods']:
                    print( b(str(c) + ") ") + meth['name'] )
                    print("")
                    c += 1
                
            else:
                print( colored( "ok i skip for u", 'red' ) )

        except SystemExit:
            sys.exit()
        except:
            pass
            #print(str(rid) + " not found: skipping that binch")

