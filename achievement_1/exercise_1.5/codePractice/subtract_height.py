# Defines Height class
class Height(object):
    # Initializes data attributes
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
    
    # Defines function to convert given values for feet and inches into a string representation
    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output

    # Defines function to convert given heights in inches into feet and inches
    def __sub__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12  + other.inches

        # Defines subtraction behavior
        diff_height_inches = height_A_inches - height_B_inches

        # Converts output for feet into feet
        output_feet = diff_height_inches // 12

        # Converts output for inches into inches
        output_inches = diff_height_inches - (output_feet * 12)

        return Height(output_feet, output_inches)
    
person_A_height = Height(5, 10)
person_B_height = Height(3, 9)
height_diff = person_A_height - person_B_height

print("Difference in height:", height_diff)
