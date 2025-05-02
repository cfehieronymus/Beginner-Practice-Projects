# Time Conversions
from unit_converter_conversions.unit_converter_time_conversions import(
    seconds_to_minutes, seconds_to_hours, 
    minutes_to_seconds, minutes_to_hours,
    hours_to_seconds, hours_to_minutes
)
# Length Conversions
from unit_converter_conversions.unit_converter_length_conversions import(
    millimeters_to_centimeters, millimeters_to_foot, millimeters_to_inch, millimeters_to_kilometers, millimeters_to_meters, millimeters_to_mile, millimeters_to_yard, 
    centimeters_to_foot, centimeters_to_inch, centimeters_to_kilometers, centimeters_to_meters, centimeters_to_mile, centimeters_to_millimeters, centimeters_to_yard, 
    meters_to_centimeters, meters_to_foot, meters_to_inch, meters_to_kilometers, meters_to_mile, meters_to_millimeters, meters_to_yard, 
    kilometers_to_centimeters, kilometers_to_foot, kilometers_to_inch, kilometers_to_meters, kilometers_to_mile, kilometers_to_millimeters, kilometers_to_yard, 
    inch_to_centimeters, inch_to_foot, inch_to_kilometers, inch_to_meters, inch_to_mile, inch_to_millimeters, inch_to_yard, 
    foot_to_inch, foot_to_meters, foot_to_centimeters, foot_to_kilometers, foot_to_mile, foot_to_millimeters, foot_to_yard, 
    yard_to_centimeters, yard_to_foot, yard_to_inch, yard_to_kilometers, yard_to_meters, yard_to_mile, yard_to_millimeters, 
    mile_to_foot, mile_to_centimeters, mile_to_inch, mile_to_kilometers, mile_to_meters, mile_to_millimeters, mile_to_yard,
)
# Weight Conversions 
from unit_converter_conversions.unit_converter_weight_conversions import (
    oz_to_lb, oz_to_ton, oz_to_g, oz_to_kg, oz_to_metric_ton, oz_to_mg, 
    lb_to_oz, lb_to_ton, lb_to_g, lb_to_kg, lb_to_metric_ton, lb_to_mg,
    ton_to_lb, ton_to_oz, ton_to_g, ton_to_kg, ton_to_metric_ton, ton_to_mg,
    mg_to_g, mg_to_kg, mg_to_metric_ton, mg_to_lb, mg_to_oz, mg_to_ton, 
    g_to_kg, g_to_metric_ton, g_to_mg, g_to_lb, g_to_oz,g_to_ton,
    kg_to_metric_ton, kg_to_g, kg_to_mg, kg_to_lb, kg_to_oz, kg_to_ton,
    metric_ton_to_g, metric_ton_to_kg, metric_ton_to_mg, metric_ton_to_lb, metric_ton_to_oz, metric_ton_to_ton
)
# Helper functions 
# Unit Function Help
def get_unit_name(choice):
    if choice == "1":
        return "Millimeters"
    elif choice == "2":
        return "Centimeters"
    elif choice == "3":
        return "Meters"
    elif choice == "4":
        return "Kilometers"
    elif choice == "5":
        return "Inches"
    elif choice == "6":
        return "Feet"
    elif choice == "7":
        return "Yards"
    elif choice == "8":
        return "Miles"
    else: 
        return "Unknown Unit"
    
# Time Function Help
def get_time_name(choice):
    if choice == "1":
        return "Seconds"
    elif choice == "2": 
        return "Minutes"
    elif choice == "3": 
        return "Hours"
    else: 
        return "Unknown time"
    
def get_weight_name(choice):
    if choice == "1":
        return "Ounces"
    elif choice == "2":
        return "Pounds"
    elif choice == "3":
        return "Ton"
    elif choice == "4":
        return "Milligram"
    elif choice == "5":
        return "Gram"
    elif choice == "6":
        return "Kilogram"
    elif choice == "7":
        return "Metric Ton"
    else: 
        return "Unknown Weight"

# Menu functions
def main():
    while True:
        print("Welcome to Unit Converter!")
        print("1. Time Conversions")
        print("2. Length Conversions")
        print("3. Weight Conversions")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ") 

        # Whatever user types is stored as a string in the variable choice. 
        # The input() function displays the text and waits for the user to 
        # type something. 
        if choice == "1":
            time_conversion() # Time function
        elif choice == "2":
            length_conversion() # Length function
        elif choice == "3": 
            weight_conversion()  # Weight function
        elif choice == "4":
            print("Goodbye!")
            break # Exit function
        else:
            print("Invalid input, please try again.")

# Time function code
def time_conversion():
    while True: 
        # Time Converter Menu
        print("\n --- Time Converter ---")
        # First menu: Select FROM time
        print("\nSelect the time to convert FROM: ") # \n creates a new line
        print("1. Seconds")
        print("2. Minutes")
        print("3. Hours")
        print("0. Back to Main Menu")

        from_choice = input("Enter your choice (0-3): ")

        if from_choice == "0":
            return
        
        if from_choice not in ["1", "2", "3"]:
            print("Invalid choice. Please try again.")
            return
        
        # Second Menu: Select the time to convert TO
        print("\nSelect the time to convert TO: ")
        print("1. Seconds")
        print("2. Minutes")
        print("3. Hours")
        print("0. Back")
    
        to_choice = input("Enter your choice (0-3: )")

        if to_choice == "0":
            return time_conversion()
        
        if to_choice not in ["1", "2", "3",]:
            print("Invalid choice. Please try again.")
            return
        
        if from_choice == to_choice: 
            print("Converting to the same time doesn't require conversion.")
            return
        
        # Get value to convert
        try: 
            value = float(input("\nEnter the value to convert: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        # Preform the conversion based on user choices
        result = 0 

        # FROM Seconds
        if from_choice == "1" and to_choice == "2":
            result = seconds_to_minutes(value)
        elif from_choice == "1" and to_choice == "3":
            result = seconds_to_hours(value)
        # FROM Minutes 
        elif from_choice == "2" and to_choice == "1":
            result = minutes_to_seconds(value)
        elif from_choice == "2" and to_choice == "3":
            result = minutes_to_hours(value)
        # FROM Hours
        elif from_choice == "3" and to_choice == "1":
            result = hours_to_seconds(value)
        elif from_choice == "3" and to_choice == "2":
            result = hours_to_minutes(value)
        else:
            return
        
        # Display result with proper times 
        from_time = get_time_name(from_choice)
        to_time = get_time_name(to_choice)

        print(f"\n{value} {from_time} = {result} {to_time}")

        another = input("\nWould you like to convert another time? (y/n): ").lower()
        if another != 'y':
            break
    
# Length function code
def length_conversion():
    while True:
        # Length Converter Menu
        print("\n --- Length Converter ---")
        # First menu: Select FROM unit
        print("\nSelect the unit to convert FROM: ")
        print("1. Millimeters")
        print("2. Centimeters")
        print("3. Meters")
        print("4. Kilometers")
        print("5. Inches")
        print("6. Feet")
        print("7. Yards")
        print("8. Miles")
        print("0. Back to Main Menu")

        from_choice = input("Enter your choice (0-8): ")

        if from_choice == "0":
            return 
        if from_choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("Invalid choice. Please try again.")
            continue

        # Second Menu: Select unit to convert TO
        print("\nSelect the unit to convert TO: ")
        print("1. Millimeters")
        print("2. Centimeters")
        print("3. Meters")
        print("4. Kilometers")
        print("5. Inches")
        print("6. Feet")
        print("7. Yards")
        print("8. Miles")
        print("0. Back")

        to_choice = input("Enter your choice (0-8): ")

        if to_choice == "0": 
            continue # Return to First menu
        if to_choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("Invalid choice. Please try again.")
            continue
        if from_choice == to_choice:
            print("Converting to the same unit doesn't require conversion.")
            continue
        # Get value to convert
        try: 
            value = float(input("\nEnter the value to convert: "))
        except ValueError:
            print("Invalid Input. Please enter a numeric value.")
            continue

        # Preform conversion based off of user choices 
        result = 0 

        # FROM Millimeters
        if from_choice == "1" and to_choice == "2":
            result = millimeters_to_centimeters(value)
        elif from_choice == "1" and to_choice == "3":
            result = millimeters_to_meters(value)
        elif from_choice == "1" and to_choice == "4":
            result = millimeters_to_kilometers(value)
        elif from_choice == "1" and to_choice == "5":
            result = millimeters_to_inch(value)
        elif from_choice == "1" and to_choice == "6":
            result = millimeters_to_foot(value)
        elif from_choice == "1" and to_choice == "7":
            result = millimeters_to_yard(value)
        elif from_choice == "1" and to_choice == "8":
            result = millimeters_to_mile(value)
        #FROM Centimeters
        elif from_choice == "2" and to_choice == "1":
            result = centimeters_to_millimeters(value)
        elif from_choice == "2" and to_choice == "3":
            result = centimeters_to_meters(value)
        elif from_choice == "2" and to_choice == "4":
            result = centimeters_to_kilometers(value)
        elif from_choice == "2" and to_choice == "5":
            result = centimeters_to_inch(value)
        elif from_choice == "2" and to_choice == "6":
            result = centimeters_to_foot(value)
        elif from_choice == "2" and to_choice == "7":
            result = centimeters_to_yard(value)
        elif from_choice == "2" and to_choice == "8":
            result = centimeters_to_mile(value)
        # FROM Meters
        elif from_choice == "3" and to_choice == "1":
            result = meters_to_millimeters(value)
        elif from_choice == "3" and to_choice == "2":
            result = meters_to_centimeters(value)
        elif from_choice == "3" and to_choice == "4":
            result = meters_to_kilometers(value)
        elif from_choice == "3" and to_choice == "5":
            result = meters_to_inch(value)
        elif from_choice == "3" and to_choice == "6":
            result = meters_to_foot(value)
        elif from_choice == "3" and to_choice == "7":
            result = meters_to_yard(value)
        elif from_choice == "3" and to_choice == "8":
            result = meters_to_mile(value)
        # FROM Kilometers
        elif from_choice == "4" and to_choice == "1":
            result = kilometers_to_millimeters(value)
        elif from_choice == "4" and to_choice == "2":
            result = kilometers_to_centimeters(value)
        elif from_choice == "4" and to_choice == "3":
            result = kilometers_to_meters(value)
        elif from_choice == "4" and to_choice == "5":
            result = kilometers_to_inch(value)
        elif from_choice == "4" and to_choice == "6":
            result = kilometers_to_foot(value)
        elif from_choice == "4" and to_choice == "7":
            result = kilometers_to_yard(value)
        elif from_choice == "4" and to_choice == "8":
            result = kilometers_to_mile(value)
        #FROM Inches
        elif from_choice == "5" and to_choice == "1":
            result = inch_to_millimeters(value)
        elif from_choice == "5" and to_choice == "2":
            result = inch_to_centimeters(value)
        elif from_choice == "5" and to_choice == "3":
            result = inch_to_meters(value)
        elif from_choice == "5" and to_choice == "4":
            result = inch_to_kilometers(value)
        elif from_choice == "5" and to_choice == "6":
            result = inch_to_foot(value)
        elif from_choice == "5" and to_choice == "7":
            result = inch_to_yard(value)
        elif from_choice == "5" and to_choice == "8":
            result = inch_to_mile(value)
        # FROM Feet
        elif from_choice == "6" and to_choice == "1":
            result = foot_to_millimeters(value)
        elif from_choice == "6" and to_choice == "2":
            result = foot_to_centimeters(value)
        elif from_choice == "6" and to_choice == "3":
            result = foot_to_meters(value)
        elif from_choice == "6" and to_choice == "4":
            result = foot_to_kilometers(value)
        elif from_choice == "6" and to_choice == "5":
            result = foot_to_inch(value)
        elif from_choice == "6" and to_choice == "7":
            result = foot_to_yard(value)
        elif from_choice == "6" and to_choice == "8":
            result = foot_to_mile(value)
        # FROM Yards
        elif from_choice == "7" and to_choice == "1":
            result = yard_to_millimeters(value)
        elif from_choice == "7" and to_choice == "2":
            result = yard_to_centimeters(value)
        elif from_choice == "7" and to_choice == "3":
            result = yard_to_meters(value)
        elif from_choice == "7" and to_choice == "4":
            result = yard_to_kilometers(value)
        elif from_choice == "7" and to_choice == "5":
            result = yard_to_inch(value)
        elif from_choice == "7" and to_choice == "6":
            result = yard_to_foot(value)
        elif from_choice == "7" and to_choice == "8":
            result = yard_to_mile(value)
        # FROM Miles
        elif from_choice == "8" and to_choice == "1":
            result = mile_to_millimeters(value)
        elif from_choice == "8" and to_choice == "2":
            result = mile_to_centimeters(value)
        elif from_choice == "8" and to_choice == "3":
            result = mile_to_meters(value)
        elif from_choice == "8" and to_choice == "4":
            result = mile_to_kilometers(value)
        elif from_choice == "8" and to_choice == "5":
            result = mile_to_inch(value)
        elif from_choice == "8" and to_choice == "6":
            result = mile_to_foot(value)
        elif from_choice == "8" and to_choice == "7":
            result = mile_to_yard(value)
        else:
            return
        
        #Display the result with proper units
        from_unit = get_unit_name(from_choice)
        to_unit = get_unit_name(to_choice)

        print(f"\n{value} {from_unit} = {result} {to_unit}")

        # Ask if the user wants to preform another conversion 
        another = input("\nWould you like to convert another length? (y/n): ").lower()
        if another != 'y':
            break
        
# Weight function code
def weight_conversion():
    while True:
        # Weight Converter Menu
        print("\n --- Weight Converter ---")
        # First menu: Select the FROM
        print("\nSelect the wight to convert FROM: ")
        print("1. Ounces")
        print("2. Pounds")
        print("3. Ton")
        print("4. Milligram")
        print("5. Gram")
        print("6. Kilogram")
        print("7. Metric Ton")
        print("0. Back to main menu")

        from_choice = input("Enter your choice (0-7): ")

        if from_choice == "0":
            return
        if from_choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice. Please try again.")
            continue
        
        # Second MenuL Select the unit to convert TO
        print("\nSelect the wight to convert TO: ")
        print("1. Ounces")
        print("2. Pounds")
        print("3. Ton")
        print("4. Milligram")
        print("5. Gram")
        print("6. Kilogram")
        print("7. Metric Ton")
        print("0. Back")

        to_choice = input("Enter your choice (0-7): ")

        if to_choice =="0":
            continue # Return to First Menu

        if to_choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice. Please try again.")
            continue
        if from_choice == to_choice: 
            print("Converting to the same unit doesn't require conversion.")
            continue

        # Get value to convert 
        try: 
            value = float(input("\nEnter the value to convert: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        # Preform conversion based on user choices 
        result = 0 

        # FROM oz 
        if from_choice == "1" and to_choice == "2":
            result = oz_to_lb(value)
        elif from_choice == "1" and to_choice == "3":
            result = oz_to_ton(value)
        elif from_choice == "1" and to_choice == "4":
            result = oz_to_mg(value)
        elif from_choice == "1" and to_choice == "5":
            result = oz_to_g(value)
        elif from_choice == "1" and to_choice == "6":
            result = oz_to_kg(value)
        elif from_choice == "1" and to_choice == "7":
            result = oz_to_metric_ton(value)
        elif from_choice == "2" and to_choice == "1":
            result = lb_to_oz(value)
        elif from_choice == "2" and to_choice == "3":
            result = lb_to_ton(value)
        elif from_choice == "2" and to_choice == "4":
            result = lb_to_mg(value)
        elif from_choice == "2" and to_choice == "5":
            result = lb_to_g(value)
        elif from_choice == "2" and to_choice == "6":
            result = lb_to_kg(value)
        elif from_choice == "2" and to_choice == "7":
            result = lb_to_metric_ton(value)
        elif from_choice == "3" and to_choice == "1":
            result = ton_to_oz(value)
        elif from_choice == "3" and to_choice == "2":
            result = ton_to_lb(value)
        elif from_choice == "3" and to_choice == "4":
            result = ton_to_mg(value)
        elif from_choice == "3" and to_choice == "5":
            result = ton_to_g(value)
        elif from_choice == "3" and to_choice == "6":
            result = ton_to_kg(value)
        elif from_choice == "3" and to_choice == "7":
            result = ton_to_metric_ton(value)
        elif from_choice == "4" and to_choice == "1":
            result = mg_to_oz(value)
        elif from_choice == "4" and to_choice == "2":
            result = mg_to_lb(value)
        elif from_choice == "4" and to_choice == "3":
            result = mg_to_ton(value)
        elif from_choice == "4" and to_choice == "5":
            result = mg_to_g(value)
        elif from_choice == "4" and to_choice == "6":
            result = mg_to_kg(value)
        elif from_choice == "4" and to_choice == "7":
            result = mg_to_metric_ton(value)
        elif from_choice == "5" and to_choice == "1":
            result = g_to_oz(value)
        elif from_choice == "5" and to_choice == "2":
            result = g_to_lb(value)
        elif from_choice == "5" and to_choice == "3":
            result = g_to_ton(value)
        elif from_choice == "5" and to_choice == "4":
            result = g_to_mg(value)
        elif from_choice == "5" and to_choice == "6":
            result = g_to_kg(value)
        elif from_choice == "5" and to_choice == "7":
            result = g_to_metric_ton(value)
        elif from_choice == "6" and to_choice == "1":
            result = kg_to_oz(value)
        elif from_choice == "6" and to_choice == "2":
            result = kg_to_lb(value)
        elif from_choice == "6" and to_choice == "3":
            result = kg_to_ton(value)
        elif from_choice == "6" and to_choice == "4":
            result = kg_to_mg(value)
        elif from_choice == "6" and to_choice == "5":
            result = kg_to_g(value)
        elif from_choice == "6" and to_choice == "7":
            result = kg_to_metric_ton(value)
        elif from_choice == "7" and to_choice == "1":
            result = metric_ton_to_oz(value)
        elif from_choice == "7" and to_choice == "2":
            result = metric_ton_to_lb(value)
        elif from_choice == "7" and to_choice == "3":
            result = metric_ton_to_ton(value)
        elif from_choice == "7" and to_choice == "4":
            result = metric_ton_to_mg(value)
        elif from_choice == "7" and to_choice == "5":
            result = metric_ton_to_g(value)
        elif from_choice == "7" and to_choice == "6":
            result = metric_ton_to_kg(value)
        else:
            return
        
        # Display result with proper weight
        from_weight = get_weight_name(from_choice)
        to_weight = get_weight_name(to_choice)

        print(f"\n{value} {from_weight} = {result} {to_weight}")

        another = input("\nWould you like to convert another weight (y/n): ").lower()
        if another != 'y':
            break


# Program entry point
if __name__ == "__main__":
    main()
