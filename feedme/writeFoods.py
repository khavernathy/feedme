def writeFoods( js, url, fname ):
    f = open(fname, "w")

    fid = str( js['id'] )
    name = str( js['name'] )
    desc = str( js['description'] ).replace("&amp;","&")
    pic = str( js['picture'] )
    serves = str( js['serve']) 
    time_Cooking = str( js['time_Cooking'] )
    time_Preparation = str( js['time_Preparation'])
    time_Total = str( js['time_Total'] )

    f.write( name + "\n\n" )
    f.write( desc + "\n\n"  )
    f.write("Link: " + url + "\n" )
    f.write("Picture: " + pic + "\n")
    f.write("Serves: " + serves + "\n")
    f.write("Prep time: " + time_Preparation + "\n")
    f.write( "Cook time: " + time_Cooking + "\n")
    f.write( "Total time: " + time_Total + "\n")
    f.write("\n")
    f.write( "Ingredients: " + "\n")
    for ing in js['ingdt']:
        f.write( " - " + ing['name'] + "\n")
    f.write( "\nMethods: " + "\n")
    c=1
    for meth in js['methods']:
        f.write( str(c) + ") " + meth['name'] + "\n")
        c += 1

    f.close()
