class Calc:

    def __init__(self, dict):
        self.dict = dict
        self.lst = []

        # create a list that holds the dictreader values
        for line in self.dict:
            self.lst.append(line)

    def get_length(self):
        count = 0
        for line in self.lst:
            count += 1
        return count

    def get_average_cost(self):
        cost = 0
        for item in self.lst:
            cost += float(item['charges'])
        return round(cost / self.get_length(), 2)

    def get_average_age(self):
        age = 0
        for line in self.lst:
            age += float(line['age'])
        return round(age / self.get_length(), 2)

    def get_average_bmi(self):
        bmi = 0
        for line in self.lst:
            bmi += float(line['bmi'])
        return round(bmi / self.get_length(), 2)

    def get_average_cost_with_kids(self):
        count = 0
        cost = 0
        for line in self.lst:
            if float(line['children']) > 0:
                count += 1
                cost += float(line['charges'])
        return round(cost / count, 2)

    def get_average_cost_without_kids(self):
        count = 0
        cost = 0
        for line in self.lst:
            if float(line['children']) == 0:
                count += 1
                cost += float(line['charges'])
        return round(cost / count, 2)

    #
    # The below method gets the ave cost, bmi, and age by region and return each
    # in a dictionary
    #
    def get_average_by_region(self):
        common_region = []
        avg_region_cost = {}
        avg_bmi = {}
        avg_age = {}
        # get unique regions
        for line in self.lst:
            if line['region'] not in common_region:
                common_region.append(line['region'])

        # get avg cost for each region for each region
        for i in common_region:
            count = 0
            cost = 0
            for line in self.lst:
                if i == line['region']:
                    count += 1
                    cost += float(line['charges'])
            avg_region_cost[i] = round(cost / count, 2)

        # get avg bmi for each region
        for i in common_region:
            count = 0
            bmi = 0
            for line in self.lst:
                if i == line['region']:
                    count += 1
                    bmi += float(line['bmi'])
            avg_bmi[i] = round(bmi / count, 2)

        # get avg age for each region
        for i in common_region:
            count = 0
            age = 0
            for line in self.lst:
                if i == line['region']:
                    count += 1
                    age += float(line['age'])
            avg_age[i] = round(age / count, 2)

        return avg_region_cost, avg_bmi, avg_age
