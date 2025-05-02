# Imperial Units 

# Ounce
def oz_to_lb(oz):
    return oz / 16

def oz_to_ton(oz):
    return oz / 32000

# Pound
def lb_to_oz(lb):
    return lb * 16

def lb_to_ton(lb):
    return lb / 2000

# Ton
def ton_to_oz(ton):
    return ton * 32000

def ton_to_lb(ton):
    return ton * 2000


# Metric Units

# Milligram
def mg_to_g(mg):
    return mg / 1000

def mg_to_kg(mg):
    return mg / 1000000

def mg_to_metric_ton(mg):
    return mg / 1000000000

# Gram
def g_to_mg(g):
    return g * 1000

def g_to_kg(g):
    return g / 1000

def g_to_metric_ton(g):
    return g / 1000000

# Kilogram
def kg_to_mg(kg):
    return kg * 1000000

def kg_to_g(kg):
    return kg * 1000

def kg_to_metric_ton(kg):
    return kg / 1000

# Metric Ton
def metric_ton_to_mg(metric_ton):
        return metric_ton * 1000000000

def metric_ton_to_g(metric_ton):
    return metric_ton * 1000000

def metric_ton_to_kg(metric_ton):
    return metric_ton * 1000

# Imperial to Metric 
# Ounces 
def oz_to_mg(oz):
    return oz * 28349.5
    
def oz_to_g(oz):
    return oz * 28.3495

def oz_to_kg(oz):
    return oz * 0.0283495

def oz_to_metric_ton(oz):
    return oz * 0.0000283495

# Pound 
def lb_to_mg(lb):
    return lb * 453592

def lb_to_g(lb):
    return lb * 453.592

def lb_to_kg(lb):
    return lb * 0.453592

def lb_to_metric_ton(lb):
    return lb * 0.000453592

# Ton
def ton_to_mg(ton):
    return ton * 907184740

def ton_to_g(ton):
    return ton * 907184.74

def ton_to_kg(ton):
    return ton * 907.18474

def ton_to_metric_ton(ton):
    return ton * 0.90718474

# Metric to Imperial 
# Milligrams 
def mg_to_oz(mg):
    return mg / 28349.5

def mg_to_lb(mg):
    return mg / 453592

def mg_to_ton(mg):
    return mg / 907184740

# Grams
def g_to_oz(g):
    return g / 28.3495

def g_to_lb(g):
    return g / 453.592

def g_to_ton(g):
    return g / 907184.74

# Kilograms
def kg_to_oz(kg):
    return kg * 35.274

def kg_to_lb(kg):
    return kg * 2.20462

def kg_to_ton(kg):
    return kg / 907.18474

# Metric Ton
def metric_ton_to_oz(metric_ton):
    return metric_ton * 35274

def metric_ton_to_lb(metric_ton):
    return metric_ton * 2204.62

def metric_ton_to_ton(metric_ton):
    return metric_ton * 1.10231