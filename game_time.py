
#TODO fare una classe time statica
class GameTime():
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 7
        self.days = 15
        self.months = 2
        self.years = 2000
        self.wakeup_time = 7
        self.bedtime = 20
        self.start_prune_month = 2
        self.end_prune_month = 4
        self.start_prune_day = 15
        self.end_prune_day = 30
        self.start_harvest_month = 10
        self.end_harvest_month = 12
        self.start_harvest_day = 15
        self.end_harvest_day = 20
        self.current_tree_time = "prune"
    
    #convert a month number to a string of three letters
    def month_to_string(self,month):
        if month == 1:
            return "Jan"
        if month == 2:
            return "Feb"
        if month == 3:
            return "Mar"
        if month == 4:
            return "Apr"
        if month == 5:
            return "May"
        if month == 6:
            return "Jun"
        if month == 7:
            return "Jul"
        if month == 8:
            return "Aug"
        if month == 9:
            return "Sep"
        if month == 10:
            return "Oct"
        if month == 11:
            return "Nov"
        if month == 12:
            return "Dec"
    #input the month return the number of days in that month
    def days_in_month(self,month):
        if month == 1:
            return 31
        if month == 2:
            return 28
        if month == 3:
            return 31
        if month == 4:
            return 30
        if month == 5:
            return 31
        if month == 6:
            return 30
        if month == 7:
            return 31
        if month == 8:
            return 31
        if month == 9:
            return 30
        if month == 10:
            return 31
        if month == 11:
            return 30
        if month == 12:
            return 31
    #jump to the next day at wakeuptime 
    def next_day(self):
        self.days += 1
        if self.days == self.days_in_month(self.months):
            self.days = 1
            self.months += 1
        if self.months == 13:
            self.months = 1
            self.years += 1
        self.hours = self.wakeup_time
        self.minutes = 0
        self.seconds += (self.bedtime-self.wakeup_time)*6*74
        return self.get_current_time()
    #date_text.set_text(str(days) + ' ' + str(month_to_string(months)) + ' ' + str(years) + ' ' + f"{hours}" + ':' + f"{minutes:02}")

    #fast forward to prune time
    #if the year pass the prune time, it will jump to the next year
    def fast_forward_prune(self):
        if self.months > self.end_prune_month:
            self.years += 1
            self.months = self.start_prune_month
            self.days = self.start_prune_day
        if self.months == self.end_prune_month:
            if self.days > self.end_prune_day:
                self.years += 1
                self.months = self.start_prune_month
                self.days = self.start_prune_day
            else:
                self.months = self.start_prune_month
                self.days = self.start_prune_day
        else:
            self.months = self.start_prune_month
            self.days = self.start_prune_day
        self.hours = self.wakeup_time
        self.minutes = 0
        self.seconds += (self.bedtime-self.wakeup_time)*6*76
    
    
    #fast forward to harvest time
    # if the year pass the harvest time, it will jump to the next year
    def fast_forward_harvest(self):
        if self.months > self.end_harvest_month:
            self.years += 1
            self.months = self.start_harvest_month
            self.days = self.start_harvest_day
        if self.months == self.end_harvest_month:
            if self.days > self.end_harvest_day:
                self.years += 1
                self.months = self.start_harvest_month
                self.days = self.start_harvest_day
            else:
                self.months = self.start_harvest_month
                self.days = self.start_harvest_day
        else:
            self.months = self.start_harvest_month
            self.days = self.start_harvest_day
        self.hours = self.wakeup_time
        self.minutes = 0
        self.seconds += (self.bedtime-self.wakeup_time)*6
    #fast forward choice
    def fast_forward(self):
        
        if self.current_tree_time == "prune":
            self.fast_forward_harvest()
            self.current_tree_time = "harvest"
        elif self.current_tree_time == "harvest":
            self.fast_forward_prune()
            self.current_tree_time = "prune"
        #print(self.current_tree_time)
        return self.get_current_time()
        #date_text.set_text(str(days) + ' ' + str(month_to_string(months)) + ' ' + str(years) + ' ' + f"{hours}" + ':' + f"{minutes:02}")
    def get_current_time(self):
        return str(self.days) + ' ' + str(self.month_to_string(self.months)) + ' ' + str(self.years) + ' ' + f"{self.hours}" + ':' + f"{self.minutes:02}"
    def update(self):
        
        if self.hours != self.bedtime:
            self.seconds += 1
            self.minutes += 10
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        if self.hours == 24:
            self.hours = 0
            self.days += 1
        if self.days == self.days_in_month(self.months):
            self.days = 1
            self.months += 1
        if self.months == 13:
            self.months = 1
            self.years += 1
        return self.get_current_time()
        #date_text.set_text(str(days) + ' ' + str(month_to_string(months)) + ' ' + str(years) + ' ' + f"{hours}" + ':' + f"{minutes:02}")

    
