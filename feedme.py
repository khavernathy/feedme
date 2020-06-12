# the setup.py script will install these dependencies
# but if you want to work for it..
## pip3 install beautifulsoup4
# or..
# apt-get install python3-bs4
from bs4 import BeautifulSoup
# pip3 install termcolor
from termcolor import colored

#these should come with python i guess
import sys
import math
import random
import urllib.request as urllib2
import sys
import json

def feedme():
    basename = "http://reciperoulette.tv/getRecipeInfoPrest?id="

    maxid = 40000

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
            print( colored( str(js['id']) + ": " + js['name'], 'red' ) )

            x = input("is sound good? [ (anything) for yes; (n) for no; (x) to exit >.<]:   ")
            if (x == "x"):
                print("bye hope u eat nice meal")
                sys.exit(0)
            elif (x != "n"):
                print("")
                print("")
                fid = str( js['id'] )
                name = str( js['name'] )
                desc = str( js['description'] )
                pic = str( js['picture'] )
                serves = str( js['serve']) 
                time_Cooking = str( js['time_Cooking'] )
                time_Preparation = str( js['time_Preparation'])
                time_Total = str( js['time_Total'] )

                print( fid + ": " + name + '\n' )
                print( desc + "\n" )
                print("Link: " + url )
                print( "Serves: " + serves )
                print( "Picture: " + pic )
                print( "Prep time: " + time_Preparation )
                print("Cook time: " + time_Cooking )
                print("Total time: " + time_Total )
                print("")
                print("Ingredients: ")
                for ing in js['ingdt']:
                    print( " - " + ing['name'] )
                print("")
                print("Methods: ")
                c=1
                for meth in js['methods']:
                    print( str(c) + ") " + meth['name'] )
                    print("")
                    c += 1
                
            else:
                print("ok i skip for u")

        except SystemExit:
            sys.exit(0)
        except:
            pass
            #print(str(rid) + " not found: skipping that binch")

