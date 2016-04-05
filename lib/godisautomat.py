print "1 choklad 10 kr"
print "2 festis 8 kr"
print "tryck nummer for onskad vara"

nr = int(raw_input("nr "))

if nr == 1:
    print "Lagg in 10 kr"
if nr == 2:
    print "Lagg in 8 kr"

kr= int(raw_input("kr "))

#check nr pris ar lika med  kr


if nr == 1:
    if kr >= 10:
        print "Tack!"
        print "Vaxel: %s" % (kr - 10)
    elif kr < 10:
        print "For lite pengar"

if nr == 2:
    if kr >= 8:
        print "Tack!"
        print "Vaxel: %s" % (kr - 8)
    elif kr < 8:
        print "For lite pengar"
