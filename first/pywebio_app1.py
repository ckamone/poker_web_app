from pywebio.input import *
from pywebio.output import *

def bmi():

    """BMI Calculation
    Simple application for calculating Body Mass Index.
    """

    put_markdown("""# Body Mass Index
    
    [Body mass index](https://en.wikipedia.org/wiki/Body_mass_index) (BMI) is a measure of body fat based on height and weight that applies to adult men and women. 
    
    BMI Categories:
    
    | Category             | BMI           |
    | -------------------- | ------------- |
    | Severely underweight | BMI<14.9      |
    | Underweight          | 14.9≤BMI<18.4 |
    | Normal               | 18.4≤BMI<22.9 |
    | Overweight           | 22.9≤BMI<27.5 |
    | Moderately obese     | 27.5≤BMI<40   |
    | Severely obese       | BMI≤40        |
    
    ## BMI calculation
    Return to [main](http://178.154.223.175/) page. 
    """, strip_indent=4)

    info = input_group('BMI calculation', [
        input("Your Height(cm)", name="height", type=FLOAT),
        input("Your Weight(kg)", name="weight", type=FLOAT),
    ])

    BMI = info['weight'] / (info['height'] / 100) ** 2

    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
            break