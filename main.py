from calculator import Calc
import csv


# import insurance file
with open('Code Academy\Medical Insurance\insurance.csv', newline='') as insurance:
    file = csv.DictReader(insurance)

    calc = Calc(file)

    # Base values to work with

    # Get Total Count
    total_count = calc.get_length()

    # Get Average Cost
    average_cost = calc.get_average_cost()

    # Get Average Age
    avg_age = calc.get_average_age()

    # Get Average BMI
    avg_bmi = calc.get_average_bmi()

    # Check correlation between average cost and kids

    # Get Average Cost With Kids
    avg_cost_with_kids = calc.get_average_cost_with_kids()

    # Get Average Cost Without Kids
    avg_cost_without_kids = calc.get_average_cost_without_kids()

    # print results of cost with kids
    print('-----Cost of insurance with our without kids-------')
    print('''The average cost is ${} dollars; the average cost with kids is ${} dollars; 
    the average cost without kids is ${} dollars. There is likely more to the picture, but those
    with kids are paying more than those without\n.'''.format(average_cost, avg_cost_with_kids, avg_cost_without_kids))

    # get avg values by region
    avg_region_cost, avg_region_bmi, avg_region_age = calc.get_average_by_region()

    # get the values of the average cost by region
    print('-----The average cost by region-------')
    for key, value in avg_region_cost.items():
        print("{} has an average cost of {}".format(key, value))
    print('\n')

    # get the values of the average bmi per region
    print('-----The average bmi by region-------')
    for key, value in avg_region_bmi.items():
        print("{} has an average bmi of {}".format(key, value))
    print('\n')

    # get the value of the average age by region
    print('-----The average bmi by region-------')
    for key, value in avg_region_age.items():
        print("{} has an average age of {}".format(key, value))

    print('\n')

    # provide Analysis
    print("""The southeast region has a higher avg cost of ${} dollars, 
    but they also have a higher avg bmi of %{} and a lower avg age of {}.""".format(avg_region_cost['southeast'],
                                                                                    avg_region_bmi['southeast'], avg_region_age['southeast']))
