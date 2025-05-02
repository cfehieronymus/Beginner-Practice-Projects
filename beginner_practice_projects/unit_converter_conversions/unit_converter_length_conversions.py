# Length Conversions

# Metric conversions
# Millimeters
def millimeters_to_centimeters(millimeters):
    return millimeters / 10

def millimeters_to_meters(millimeters):
    return millimeters / 1000

def millimeters_to_kilometers(millimeters):
    return millimeters / 1000000

# Centimeters
def centimeters_to_millimeters(centimeters):
    return centimeters * 10

def centimeters_to_meters(centimeters):
    return centimeters / 100

def centimeters_to_kilometers(centimeters):
    return centimeters / 100000

# Meters
def meters_to_millimeters(meters):
    return meters * 1000

def meters_to_centimeters(meters):
    return meters * 100

def meters_to_kilometers(meters):
    return meters / 1000

# Kilometers
def kilometers_to_millimeters(kilometers):
    return kilometers * 1000000

def kilometers_to_centimeters(kilometers):
    return kilometers  * 100000

def kilometers_to_meters(kilometers):
    return kilometers * 1000


# Imperial Conversions 
# Inch
def inch_to_foot(inch):
    return inch / 12

def inch_to_yard(inch):
    return inch / 36

def inch_to_mile(inch):
    return inch / 63360

# Foot
def foot_to_inch(foot):
    return foot * 12

def foot_to_yard(foot):
    return foot / 3

def foot_to_mile(foot):
    return foot / 5280

# Yard
def yard_to_inch(yard):
    return yard * 36

def yard_to_foot(yard):
    return yard * 3

def yard_to_mile(yard):
    return yard / 1760

# Mile
def mile_to_inch(mile):
    return mile * 63360

def mile_to_foot(mile):
    return mile * 5280

def mile_to_yard(mile):
    return mile * 1760


# Metric to Imperial Conversions
# Millimeters
def millimeters_to_inch(millimeters):
    return millimeters / 25.4

def millimeters_to_foot(millimeters):
    return millimeters / 304.8

def millimeters_to_yard(millimeters):
    return millimeters / 914.4

def millimeters_to_mile(millimeters):
    return millimeters / 1609344

# Centimeters
def centimeters_to_inch(centimeters):
    return centimeters / 2.54

def centimeters_to_foot(centimeters):
    return centimeters / 30.48

def centimeters_to_yard(centimeters):
    return centimeters / 91.44

def centimeters_to_mile(centimeters):
    return centimeters / 160934.4

# Meters
def meters_to_inch(meters):
    return meters * 39.3701

def meters_to_foot(meters):
    return meters * 3.28084

def meters_to_yard(meters):
    return meters * 1.09361

def meters_to_mile(meters):
    return meters / 1609.344
    
# Kilometers
def kilometers_to_inch(kilometers):
    return kilometers * 39370.1

def kilometers_to_foot(kilometers):
    return kilometers * 3280.84

def kilometers_to_yard(kilometers):
    return kilometers * 1093.61

def kilometers_to_mile(kilometers):
    return kilometers * 0.621371


# Imperial to Metric Conversions
# Inch
def inch_to_millimeters(inch):
    return inch * 25.4

def inch_to_centimeters(inch):
    return inch * 2.54

def inch_to_meters(inch):
    return inch * 0.0254

def inch_to_kilometers(inch):
    return inch * 0.0000254

# Foot
def foot_to_millimeters(foot):
    return foot * 304.8

def foot_to_centimeters(foot):
    return foot * 30.48

def foot_to_meters(foot):
    return foot * 0.3048

def foot_to_kilometers(foot):
    return foot * 0.0003048

# Yard
def yard_to_millimeters(yard):
    return yard * 914.4
    
def yard_to_centimeters(yard):
    return yard * 91.44

def yard_to_meters(yard):
    return yard * 0.9144

def yard_to_kilometers(yard):
    return yard * 0.0009144

# Mile
def mile_to_millimeters(mile):
    return mile * 1609344

def mile_to_centimeters(mile):
    return mile * 160934.4

def mile_to_meters(mile):
    return mile * 1609.344

def mile_to_kilometers(mile):
    return mile * 1.60934