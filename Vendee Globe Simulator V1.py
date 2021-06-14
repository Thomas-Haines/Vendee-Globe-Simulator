import random
import time

startTime = time.time()
class Skipper():
    def __init__(self, name, sailor, boatnumber):
        #This determines what category of boat this vessel fits into
        boatType = ["Old", "Old", "Old","Old", "Old", "Old", "Old", "Old", "Old", "Old", "Updated", "Updated", "Updated", "Updated", "Updated", "Updated", "Updated", "New Foiler", "New Foiler", "New Foiler", "New Foiler", "New Foiler", "2nd Gen", "2nd Gen"]
        self.boatType = random.choice(boatType)
        #self.health determines the starting fragility of the ship, the closer to zero, the more likely it'll get damaged.
        if self.boatType == "Old":
            self.health = 80
        elif self.boatType == "Updated":
            self.health = 100
        elif self.boatType == "New Foiler":
            self.health = 60
        elif self.boatType == "2nd Gen":
            self.health = 100
        #This is the name of the ship.
        self.boatname = name
        #This is the name of the sailor
        self.boatsailor = sailor
        #This is the boat's number
        self.registration = boatnumber
        #This is the boat's current speed
        self.speed = 0
        #This is how far the boat has travelled
        self.distTravelled = 0
        #This is how far the boat has left to go
        self.distFinish = 24000
        #This is a counter variable
        self.count = 0
        #This helps to determine the speed of the boat.
        self.foilStatus = "Not Foiling"
        #This determines how skilled the sailor is.
        self.sailorSkill = random.randint(0, 100)
        #This determines how good the sailor is at getting the boat to foil.
        self.foilSkill = random.randint(0, 100)
        #This determines the health level at which the sailor will start repairs.
        self.repairBegin = random.randint(15, 35)
        #self.status can be any of the following: Sailing, Repairing, Retired, Finished
        self.status = "Sailing"
        #self.engineer determines how good they are at repairing their ship.
        self.engineer = random.randint(random.randint(0, self.sailorSkill), 100)
        #defines the weather the boat is currently experiencing.
        self.weather = ""
        #This one determines the type of repairs being done.
        self.mobileRepair = False
        #This determines the number of hours left until repairs are done.
        self.repairHours = 0
        #This one determines whether repairs are possible or not.
        self.repairsPossible = False
        #This one is a static variable that shows how long repairs were originally expected to take.
        self.originalRepairs = 0
        #This one is a timer of how long repairs have taken so far.
        self.repairTimer = 0

    def weatherUpdate(self, weather):
        if self.distTravelled <= 1000 and self.distTravelled >= 0:
            self.weather = weather[0]
        elif self.distTravelled <= 2200 and self.distTravelled >= 1001:
            self.weather = weather[1]
        elif self.distTravelled <= 3000 and self.distTravelled >= 2201:
            self.weather = weather[2]
        elif self.distTravelled <= 3900 and self.distTravelled >= 3001:
            self.weather = weather[3]
        elif self.distTravelled <= 5000 and self.distTravelled >= 3901:
            self.weather = weather[4]
        elif self.distTravelled <= 6000 and self.distTravelled >= 5001:
            self.weather = weather[5]
        elif self.distTravelled <= 7500 and self.distTravelled >= 6001:
            self.weather = weather[6]
        elif self.distTravelled <= 8000 and self.distTravelled >= 7501:
            self.weather = weather[7]
        elif self.distTravelled <= 9000 and self.distTravelled >= 8001:
            self.weather = weather[8]
        elif self.distTravelled <= 11000 and self.distTravelled >= 9001:
            self.weather = weather[9]
        elif self.distTravelled <= 12000 and self.distTravelled >= 11001:
            self.weather = weather[10]
        elif self.distTravelled <= 12500 and self.distTravelled >= 12001:
            self.weather = weather[11]
        elif self.distTravelled <= 12800 and self.distTravelled >= 12501:
            self.weather = weather[12]
        elif self.distTravelled <= 13250 and self.distTravelled >= 12801:
            self.weather = weather[13]
        elif self.distTravelled <= 13475 and self.distTravelled >= 13251:
            self.weather = weather[14]
        elif self.distTravelled <= 13800 and self.distTravelled >= 13476:
            self.weather = weather[15]
        elif self.distTravelled <= 14100 and self.distTravelled >= 13801:
            self.weather = weather[16]
        elif self.distTravelled <= 14600 and self.distTravelled >= 14101:
            self.weather = weather[17]
        elif self.distTravelled <= 15000 and self.distTravelled >= 14601:
            self.weather = weather[18]
        elif self.distTravelled <= 15100 and self.distTravelled >= 15001:
            self.weather = weather[19]
        elif self.distTravelled <= 15500 and self.distTravelled >= 15101:
            self.weather = weather[20]
        elif self.distTravelled <= 16000 and self.distTravelled >= 15501:
            self.weather = weather[21]
        elif self.distTravelled <= 16750 and self.distTravelled >= 16001:
            self.weather = weather[22]
        elif self.distTravelled <= 17250 and self.distTravelled >= 16751:
            self.weather = weather[23]
        elif self.distTravelled <= 17500 and self.distTravelled >= 17251:
            self.weather = weather[24]
        elif self.distTravelled <= 18000 and self.distTravelled >= 17501:
            self.weather = weather[25]
        elif self.distTravelled <= 20000 and self.distTravelled >= 18001:
            self.weather = weather[26]
        elif self.distTravelled <= 20300 and self.distTravelled >= 20001:
            self.weather = weather[27]
        elif self.distTravelled <= 22000 and self.distTravelled >= 20301:
            self.weather = weather[28]
        elif self.distTravelled <= 24000 and self.distTravelled >= 22001:
            self.weather = weather[29]

    def raceUpdate(self):
        if self.status == "Sailing" or self.status == "Repairing":
            if self.status == "Sailing":
                if self.health < self.repairBegin and self.mobileRepair == False:
                    planQual = random.choice(["Disastrous", "Disastrous", "Disastrous", "Poor", "Poor", "Poor", "Alright", "Alright", "Alright", "Alright", "Decent", "Decent", "Decent", "Decent", "Decent", "Good", "Good", "Good", "Good", "Fantastic", "Fantastic", "Fantastic", "Legendary", "Legendary"])
                    if self.weather == "Doldrums" or self.weather == "Light wind":
                        self.repairsPossible = True
                        if self.sailorSkill >= 60:
                            self.mobileRepair = True
                            self.status = "Sailing"
                            print("Due to damage to {}, {} has been forced to carry out repairs, though they will stay in the race while doing so, even if at a reduced speed. This is only really possible because of the brilliant conditions.".format(self.boatname.upper(), self.boatsailor.upper()))
                            if self.engineer >= 80:
                                if planQual == "Disastrous":
                                    self.repairHours = random.randint(24, 48)
                                elif planQual == "Poor":
                                    self.repairHours = random.randint(18, 24)
                                elif planQual == "Alright":
                                    self.repairHours = random.randint(12, 18)
                                elif planQual == "Decent":
                                    self.repairHours = random.randint(9, 12)
                                elif planQual == "Good":
                                    self.repairHours = random.randint(6, 9)
                                elif planQual == "Fantastic":
                                    self.repairHours = random.randint(3, 6)
                                elif planQual == "Legendary":
                                    self.repairHours = random.randint(1, 3)
                            elif self.engineer >= 60:
                                if planQual == "Disastrous":
                                    self.repairHours = random.randint(48, 72)
                                elif planQual == "Poor":
                                    self.repairHours = random.randint(24, 48)
                                elif planQual == "Alright":
                                    self.repairHours = random.randint(18, 24)
                                elif planQual == "Decent":
                                    self.repairHours = random.randint(12, 18)
                                elif planQual == "Good":
                                    self.repairHours = random.randint(9, 12)
                                elif planQual == "Fantastic":
                                    self.repairHours = random.randint(6, 9)
                                elif planQual == "Legendary":
                                    self.repairHours = random.randint(3, 6)
                            elif self.engineer < 60:
                                if planQual == "Disastrous":
                                    self.repairHours = random.randint(72, 96)
                                elif planQual == "Poor":
                                    self.repairHours = random.randint(48, 72)
                                elif planQual == "Alright":
                                    self.repairHours = random.randint(24, 48)
                                elif planQual == "Decent":
                                    self.repairHours = random.randint(18, 24)
                                elif planQual == "Good":
                                    self.repairHours = random.randint(12, 18)
                                elif planQual == "Fantastic":
                                    self.repairHours = random.randint(9, 12)
                                elif planQual == "Legendary":
                                    self.repairHours = random.randint(6, 9)
                        elif self.sailorSkill < 60:
                            self.mobileRepair = False
                            self.status = "Repairing"
                            self.foilStatus = "Not Foiling"
                            self.speed = 0
                            print("Due to damage to {}, {} has been forced to stop to carry out repairs. They are going to try and take advantage of the brilliant conditions for maintenance.".format(self.boatname.upper(), self.boatsailor.upper()))
                            if self.engineer >= 80:
                                if planQual == "Disastrous":
                                    self.repairHours = random.randint(20, 24)
                                elif planQual == "Poor":
                                    self.repairHours = random.randint(18, 20)
                                elif planQual == "Alright":
                                    self.repairHours = random.randint(15, 18)
                                elif planQual == "Decent":
                                    self.repairHours = random.randint(12, 15)
                                elif planQual == "Good":
                                    self.repairHours = random.randint(8, 12)
                                elif planQual == "Fantastic":
                                    self.repairHours = random.randint(3, 8)
                                elif planQual == "Legendary":
                                    self.repairHours = random.randint(1, 3)
                            elif self.engineer >= 60:
                                if planQual == "Disastrous":
                                    self.repairHours = random.randint(24, 32)
                                elif planQual == "Poor":
                                    self.repairHours = random.randint(20, 24)
                                elif planQual == "Alright":
                                    self.repairHours = random.randint(18, 20)
                                elif planQual == "Decent":
                                    self.repairHours = random.randint(15, 18)
                                elif planQual == "Good":
                                    self.repairHours = random.randint(12, 15)
                                elif planQual == "Fantastic":
                                    self.repairHours = random.randint(8, 12)
                                elif planQual == "Legendary":
                                    self.repairHours = random.randint(3, 8)
                            elif self.engineer < 60:
                                if planQual == "Disastrous":
                                    self.repairHours = random.randint(32, 48)
                                elif planQual == "Poor":
                                    self.repairHours = random.randint(24, 32)
                                elif planQual == "Alright":
                                    self.repairHours = random.randint(20, 24)
                                elif planQual == "Decent":
                                    self.repairHours = random.randint(18, 20)
                                elif planQual == "Good":
                                    self.repairHours = random.randint(15, 18)
                                elif planQual == "Fantastic":
                                    self.repairHours = random.randint(12, 15)
                                elif planQual == "Legendary":
                                    self.repairHours = random.randint(8, 12)
                    elif self.weather == "Average" or self.weather == "Favourable":
                        self.repairsPossible = True
                        if self.sailorSkill >= 75:
                            self.mobileRepair = True
                            self.status = "Sailing"
                            print("Due to damage to {}, {} has been forced to carry out repairs, though because the weather allows, they will still be racing during the repairs.".format(self.boatname.upper(), self.boatsailor.upper()))
                            if self.engineer >= 80:
                                if planQual == "Disastrous":
                                    self.repairHours = random.randint(48, 60)
                                elif planQual == "Poor":
                                    self.repairHours = random.randint(32, 48)
                                elif planQual == "Alright":
                                    self.repairHours = random.randint(24, 32)
                                elif planQual == "Decent":
                                    self.repairHours = random.randint(12, 24)
                                elif planQual == "Good":
                                    self.repairHours = random.randint(9, 12)
                                elif planQual == "Fantastic":
                                    self.repairHours = random.randint(6, 9)
                                elif planQual == "Legendary":
                                    self.repairHours = random.randint(3, 6)
                            elif self.engineer >= 60:
                                if planQual == "Disastrous":
                                    self.repairHours = random.randint(60, 72)
                                elif planQual == "Poor":
                                    self.repairHours = random.randint(48, 60)
                                elif planQual == "Alright":
                                    self.repairHours = random.randint(32, 48)
                                elif planQual == "Decent":
                                    self.repairHours = random.randint(24, 32)
                                elif planQual == "Good":
                                    self.repairHours = random.randint(12, 24)
                                elif planQual == "Fantastic":
                                    self.repairHours = random.randint(9, 12)
                                elif planQual == "Legendary":
                                    self.repairHours = random.randint(6, 9)
                            elif self.engineer < 60:
                                if planQual == "Disastrous":
                                    self.repairHours = random.randint(72, 84)
                                elif planQual == "Poor":
                                    self.repairHours = random.randint(60, 72)
                                elif planQual == "Alright":
                                    self.repairHours = random.randint(48, 60)
                                elif planQual == "Decent":
                                    self.repairHours = random.randint(32, 48)
                                elif planQual == "Good":
                                    self.repairHours = random.randint(24, 32)
                                elif planQual == "Fantastic":
                                    self.repairHours = random.randint(12, 24)
                                elif planQual == "Legendary":
                                    self.repairHours = random.randint(9, 12)
                        elif self.sailorSkill < 75:
                            self.mobileRepair = False
                            self.status = "Repairing"
                            self.foilStatus = "Not Foiling"
                            self.speed = 0
                            print("Due to damage to {}, {} has been forced to stop to carry out repairs. They are going to try and do this even though the conditions aren't quite right for repairs.".format(self.boatname.upper(), self.boatsailor.upper()))
                            if self.engineer >= 80:
                                if planQual == "Disastrous":
                                    self.repairHours = random.randint(28, 32)
                                elif planQual == "Poor":
                                    self.repairHours = random.randint(22, 28)
                                elif planQual == "Alright":
                                    self.repairHours = random.randint(17, 22)
                                elif planQual == "Decent":
                                    self.repairHours = random.randint(10, 17)
                                elif planQual == "Good":
                                    self.repairHours = random.randint(6, 10)
                                elif planQual == "Fantastic":
                                    self.repairHours = random.randint(3, 6)
                                elif planQual == "Legendary":
                                    self.repairHours = random.randint(1, 3)
                            elif self.engineer >= 60:
                                if planQual == "Disastrous":
                                    self.repairHours = random.randint(32, 48)
                                elif planQual == "Poor":
                                    self.repairHours = random.randint(28, 32)
                                elif planQual == "Alright":
                                    self.repairHours = random.randint(22, 28)
                                elif planQual == "Decent":
                                    self.repairHours = random.randint(17, 22)
                                elif planQual == "Good":
                                    self.repairHours = random.randint(10, 17)
                                elif planQual == "Fantastic":
                                    self.repairHours = random.randint(6, 10)
                                elif planQual == "Legendary":
                                    self.repairHours = random.randint(3, 6)
                            elif self.engineer < 60:
                                if planQual == "Disastrous":
                                    self.repairHours = random.randint(48, 60)
                                elif planQual == "Poor":
                                    self.repairHours = random.randint(32, 48)
                                elif planQual == "Alright":
                                    self.repairHours = random.randint(28, 32)
                                elif planQual == "Decent":
                                    self.repairHours = random.randint(22, 28)
                                elif planQual == "Good":
                                    self.repairHours = random.randint(17, 22)
                                elif planQual == "Fantastic":
                                    self.repairHours = random.randint(10, 17)
                                elif planQual == "Legendary":
                                    self.repairHours = random.randint(6, 10)
                    elif self.weather == "Stormy" or self.weather == "Hurricane":
                        if self.sailorSkill >= 90:
                            self.repairsPossible = True
                            self.mobileRepair = True
                            self.status = "Sailing"
                            print("Due to damage to {}, {} has been forced to carry out repairs, despite the violent weather currently. Again, because of the weather, they cannot stop to repair, so will continue racing while repairing.".format(self.boatname.upper(), self.boatsailor.upper()))
                            if self.engineer >= 80:
                                if planQual == "Disastrous":
                                    self.repairHours = random.randint(144, 168)
                                elif planQual == "Poor":
                                    self.repairHours = random.randint(120, 144)
                                elif planQual == "Alright":
                                    self.repairHours = random.randint(96, 120)
                                elif planQual == "Decent":
                                    self.repairHours = random.randint(72, 96)
                                elif planQual == "Good":
                                    self.repairHours = random.randint(48, 72)
                                elif planQual == "Fantastic":
                                    self.repairHours = random.randint(24, 48)
                                elif planQual == "Legendary":
                                    self.repairHours = random.randint(12, 24)
                            elif self.engineer >= 60:
                                if planQual == "Disastrous":
                                    self.repairHours = random.randint(168, 216)
                                elif planQual == "Poor":
                                    self.repairHours = random.randint(144, 168)
                                elif planQual == "Alright":
                                    self.repairHours = random.randint(120, 144)
                                elif planQual == "Decent":
                                    self.repairHours = random.randint(96, 120)
                                elif planQual == "Good":
                                    self.repairHours = random.randint(72, 96)
                                elif planQual == "Fantastic":
                                    self.repairHours = random.randint(48, 72)
                                elif planQual == "Legendary":
                                    self.repairHours = random.randint(24, 48)
                            elif self.engineer < 60:
                                if planQual == "Disastrous":
                                    self.repairHours = random.randint(216, 264)
                                elif planQual == "Poor":
                                    self.repairHours = random.randint(168, 216)
                                elif planQual == "Alright":
                                    self.repairHours = random.randint(144, 168)
                                elif planQual == "Decent":
                                    self.repairHours = random.randint(120, 144)
                                elif planQual == "Good":
                                    self.repairHours = random.randint(96, 120)
                                elif planQual == "Fantastic":
                                    self.repairHours = random.randint(72, 96)
                                elif planQual == "Legendary":
                                    self.repairHours = random.randint(48, 72)
                    if self.repairHours <= 48 and self.repairsPossible == True:
                        print("In the little time allowed, {}'s team have done a {} job at creating a repair plan, so the repairs have ended up being forecast to take {} hours.".format(self.boatsailor.upper(), planQual.lower(), self.repairHours))
                        time.sleep(10)
                    elif self.repairHours > 48 and self.repairsPossible == True:
                        print("In the little time allowed, {}'s team have done a {} job at creating a repair plan, so the repairs have ended up being forecast to take {} days and {} hours.".format(self.boatsailor.upper(), planQual.lower(), self.repairHours // 24, self.repairHours - (24 * (self.repairHours // 24))))
                        time.sleep(10)
                    self.originalRepairs = self.repairHours
                elif self.health <= 0:
                    print("It is sad news that", self.boatsailor.upper(), "onboard", self.boatname.upper(), "has had to retire from the race due to severe damage.")
                    self.status = "Retired"
                    self.speed = 0
                    time.sleep(5)
                elif self.distFinish <= 0:
                    print(self.boatsailor.upper(), "has finished the Vendee Globe onboard", self.boatname.upper())
                    self.status = "Finished"
                    self.speed = 0
                    time.sleep(5)
                else:
                    
                    if self.weather == "Doldrums":
                        if self.boatType == "Old":
                            self.speed = random.randint(0, 5)
                        elif self.boatType == "Updated":
                            self.foilStatus = "Not Foiling"
                            self.speed = random.randint(0, 8)
                        elif self.boatType == "New Foiler":
                            self.foilStatus = "Not Foiling"
                            if self.sailorSkill >= 50:
                                self.speed = random.randint(5, 10)
                            elif self.sailorSkill < 50:
                                self.speed = random.randint(0, 8)
                        elif self.boatType == "2nd Gen":
                            if self.foilSkill >= 90:
                                self.foilStatus = "Foiling"
                                self.speed = random.randint(25, 30)
                            elif self.foilSkill < 90:
                                self.foilStatus = "Not Foiling"
                                if self.sailorSkill >= 60:
                                    self.speed = random.randint(8, 10)
                                elif self.sailorSkill < 60:
                                    self.speed = random.randint(0, 8)
                                    
                    elif self.weather == "Light wind":
                        if self.boatType == "Old":
                            if self.sailorSkill >= 60:
                                self.speed = random.randint(3, 10)
                            elif self.sailorSkill < 60:
                                self.speed = random.randint(0, 5)
                        elif self.boatType == "Updated":
                            self.foilStatus = "Not Foiling"
                            if self.sailorSkill >= 80:
                                self.speed = random.randint(5, 13)
                            elif self.sailorSkill < 80:
                                self.speed = random.randint(0, 8)
                        elif self.boatType == "New Foiler":
                            if self.foilSkill >= 95:
                                self.foilStatus = "Foiling"
                                if self.sailorSkill >= 75:
                                    self.speed = random.randint(28, 32)
                                elif self.sailorSkill < 75:
                                    self.speed = random.randint(25, 30)
                            elif self.foilSkill < 95:
                                self.foilStatus = "Not Foiling"
                                if self.sailorSkill >= 80:
                                    self.speed = random.randint(10, 12)
                                elif self.sailorSkill < 80:
                                    self.speed = random.randint(5, 10)
                        elif self.boatType == "2nd Gen":
                            if self.foilSkill >= 75:
                                self.foilStatus = "Foiling"
                                if self.sailorSkill >= 75:
                                    self.speed = random.randint(32, 40)
                                elif self.sailorSkill < 75:
                                    self.speed = random.randint(25, 32)
                            elif self.foilSkill < 75:
                                self.foilStatus = "Not Foiling"
                                if self.sailorSkill >= 80:
                                    self.speed = random.randint(8, 10)
                                elif self.sailorSkill < 80:
                                    self.speed = random.randint(5, 8)
                                    
                    elif self.weather == "Average":
                        if self.boatType == "Old":
                            if self.sailorSkill >= 70:
                                self.speed = random.randint(12, 18)
                            elif self.sailorSkill < 70:
                                self.speed = random.randint(2, 10)
                        elif self.boatType == "Updated":
                            if self.foilSkill >= 90:
                                self.foilStatus = "Foiling"
                                if self.sailorSkill >= 90:
                                    self.speed = random.randint(24, 27)
                                elif self.sailorSkill < 90:
                                    self.speed = random.randint(20, 24)
                            elif self.foilSkill < 90:
                                self.foilStatus = "Not Foiling"
                                if self.sailorSkill >= 80:
                                    self.speed = random.randint(10, 15)
                                elif self.sailorSkill < 80:
                                    self.speed = random.randint(8, 12)
                        elif self.boatType == "New Foiler":
                            if self.foilSkill >= 75:
                                self.foilStatus = "Foiling"
                                if self.sailorSkill >= 75:
                                    self.speed = random.randint(32, 37)
                                elif self.sailorSkill < 75:
                                    self.speed = random.randint(25, 34)
                            elif self.foilSkill < 75:
                                self.foilStatus = "Not Foiling"
                                if self.sailorSkill >= 60:
                                    self.speed = random.randint(10, 12)
                                elif self.sailorSkill < 60:
                                    self.speed = random.randint(8, 10)
                        elif self.boatType == "2nd Gen":
                            self.foilStatus = "Foiling"
                            if self.foilSkill >= 75:
                                damage = 0
                            elif self.foilSkill >= 45:
                                damage = random.randint(1, 2)
                            elif self.foilSkill < 45:
                                damage = random.randint(5, 10)
                            self.health -= damage
                            if self.sailorSkill >= 70:
                                self.speed = random.randint(40, 45)
                            elif self.sailorSkill < 70:
                                self.speed = random.randint(30, 35)
                        
                    elif self.weather == "Favourable":
                        if self.boatType == "Old":
                            if self.sailorSkill >= 75:
                                self.speed = random.randint(18, 25)
                            elif self.sailorSkill < 75:
                                self.speed = random.randint(15, 20)
                        elif self.boatType == "Updated":
                            if self.foilSkill >= 75:
                                self.foilStatus = "Foiling"
                                if self.sailorSkill >= 60:
                                    self.speed = random.randint(25, 30)
                                elif self.sailorSkill < 60:
                                    self.speed = random.randint(22, 28)
                            elif self.foilSkill < 75:
                                self.foilStatus = "Not Foiling"
                                if self.sailorSkill >= 50:
                                    self.speed = random.randint(14, 15)
                                elif self.sailorSkill < 50:
                                    self.speed = random.randint(12,13)
                        elif self.boatType == "New Foiler":
                            self.foilStatus = "Foiling"
                            if self.foilSkill >= 90:
                                damage = 0
                            elif self.foilSkill >= 80:
                                damage = random.randint(1, 2)
                            elif self.foilSkill >= 65:
                                damage = random.randint(5, 10)
                            elif self.foilSkill < 65:
                                print(self.boatsailor.upper(), "onboard", self.boatname.upper(), "has suffered a large amount of damage from foiling.")
                                damage = random.randint(15, 30)
                                time.sleep(5)
                            self.health -= damage
                            if self.sailorSkill >= 75:
                                self.speed = random.randint(35, 40)
                            elif self.sailorSkill < 75:
                                self.speed = random.randint(30, 35)
                        elif self.boatType == "2nd Gen":
                            self.foilStatus = "Foiling"
                            if self.foilSkill >= 75:
                                damage = 0
                            elif self.foilSkill >= 45:
                                damage = random.randint(1,2)
                            elif self.foilSkill < 45:
                                damage = random.randint(5, 10)
                            self.health -= damage
                            if self.sailorSkill >= 70:
                                self.speed = random.randint(45, 50)
                            elif self.sailorSkill < 70:
                                self.speed = random.randint(38, 45)
                        
                    elif self.weather == "Stormy":
                        if self.boatType == "Old":
                            if self.sailorSkill >= 90:
                                damage = 0
                            elif self.sailorSkill >= 65:
                                damage = random.randint(1,2)
                            elif self.sailorSkill < 65:
                                damage = random.randint(5, 10)
                            self.health -= damage
                            if self.sailorSkill >= 50:
                                self.speed = random.randint(22, 25)
                            elif self.sailorSkill < 50:
                                self.speed = random.randint(20,22)
                        elif self.boatType == "Updated":
                            self.foilStatus = "Foiling"
                            if self.foilSkill >= 85:
                                damage = 0
                            elif self.foilSkill >= 55:
                                damage = random.randint(1, 2)
                            elif self.foilSkill < 55:
                                damage = random.randint(5, 10)
                            self.health -= damage
                            if self.sailorSkill >= 50:
                                self.speed = random.randint(28, 30)
                            elif self.sailorSkill < 50:
                                self.speed = random.randint(25, 28)
                        elif self.boatType == "New Foiler":
                            self.foilStatus = "Foiling"
                            if self.sailorSkill >= 50:
                                self.speed = random.randint(37, 40)
                            elif self.sailorSkill < 50:
                                self.speed = random.randint(32, 37)
                            if self.sailorSkill >= 90:
                                damage = 0
                            elif self.sailorSkill >= 75:
                                damage = random.randint(1, 2)
                            elif self.sailorSkill >= 50:
                                damage = random.randint(5, 10)
                            elif self.sailorSkill < 50:
                                print(self.boatsailor.upper(), "onboard", self.boatname.upper(), "has suffered a large amount of damage from stormy weather.")
                                damage = random.randint(15, 30)
                                time.sleep(5)
                            if self.foilSkill >= 90:
                                damage += 0
                            elif self.foilSkill >= 75:
                                damage += random.randint(1, 2)
                            elif self.foilSkill >= 60:
                                damage += random.randint(5, 10)
                            elif self.foilSkill < 60:
                                print(self.boatsailor.upper(), "onboard", self.boatname.upper(), "has suffered a large amount of damage from foiling.")
                                damage += random.randint(15, 30)
                                time.sleep(5)
                            self.health -= damage
                        elif self.boatType == "2nd Gen":
                            self.foilStatus = "Foiling"
                            if self.sailorSkill >= 50:
                                self.speed = random.randint(45, 50)
                            elif self.sailorSkill < 50:
                                self.speed = random.randint(40, 45)
                            if self.foilSkill >= 80:
                                damage = 0
                            elif self.foilSkill >= 50:
                                damage = random.randint(1, 2)
                            elif self.foilSkill < 50:
                                damage = random.randint(5, 10)
                            self.health -= damage
                        
                    elif self.weather == "Hurricane":
                        if self.boatType == "Old":
                            self.speed = random.randint(23, 25)
                            if self.sailorSkill >= 90:
                                damage = 0
                            elif self.sailorSkill >= 80:
                                damage = random.randint(1, 2)
                            elif self.sailorSkill >= 60:
                                damage = random.randint(5, 10)
                            elif self.sailorSkill < 60:
                                print(self.boatsailor.upper(), "onboard", self.boatname.upper(), "has suffered a large amount of damage from hurricane conditions.")
                                damage = random.randint(15, 30)
                                time.sleep(5)
                        elif self.boatType == "Updated":
                            self.foilStatus = "Foiling"
                            self.speed = random.randint(25, 30)
                            if self.sailorSkill >= 95:
                                damage = 0
                            elif self.sailorSkill >= 75:
                                damage = random.randint(1, 2)
                            elif self.sailorSkill < 75:
                                damage = random.randint(5, 10)
                            if self.foilSkill >= 95:
                                damage += 0
                            elif self.foilSkill >= 80:
                                damage += random.randint(1, 2)
                            elif self.foilSkill >= 55:
                                damage += random.randint(5, 10)
                            elif self.foilSkill < 55:
                                print(self.boatsailor.upper(), "onboard", self.boatname.upper(), "has suffered a large amount of damage from foiling in hurricane conditions.")
                                damage += random.randint(15, 30)
                                time.sleep(5)
                            self.health -= damage
                        elif self.boatType == "New Foiler":
                            self.foilStatus = "Foiling"
                            self.speed = random.randint(35, 40)
                            if self.sailorSkill >= 95:
                                damage = 0
                            elif self.sailorSkill >= 80:
                                damage = random.randint(1, 2)
                            elif self.sailorSkill >= 60:
                                damage = random.randint(5, 10)
                            elif self.sailorSkill >= 40:
                                print(self.boatsailor.upper(), "onboard", self.boatname.upper(), "has suffered a large amount of damage from hurricane conditions.")
                                damage = random.randint(15, 30)
                                time.sleep(5)
                            elif self.sailorSkill < 40:
                                print(self.boatsailor.upper(), "onboard", self.boatname.upper(), "has suffered potentially race-threatning damage from hurricane conditions, but for the moment will soldier on.")
                                damage = random.randint(35, 55)
                                time.sleep(5)
                            if self.foilSkill >= 95:
                                damage += 0
                            elif self.foilSkill >= 80:
                                damage += random.randint(1, 2)
                            elif self.foilSkill >= 60:
                                damage += random.randint(5, 10)
                            elif self.foilSkill >= 40:
                                print(self.boatsailor.upper(), "onboard", self.boatname.upper(), "has suffered a large amount of damage from foiling in hurricane conditions.")
                                damage += random.randint(15, 30)
                                time.sleep(5)
                            elif self.foilSkill < 40:
                                print(self.boatsailor.upper(), "onboard", self.boatname.upper(), "has suffered potentially race-threatning damage from foiling in hurricane conditions, but for the moment will soldier on.")
                                damage += random.randint(35, 55)
                                time.sleep(5)
                            self.health -= damage
                        elif self.boatType == "2nd Gen":
                            self.foilStatus = "Foiling"
                            self.speed = random.randint(45, 50)
                            if self.sailorSkill >= 95:
                                damage = 0
                            elif self.sailorSkill >= 75:
                                damage = random.randint(1, 2)
                            elif self.sailorSkill < 75:
                                damage = random.randint(5, 10)
                            if self.foilSkill >= 95:
                                damage += 0
                            elif self.foilSkill >= 75:
                                damage += random.randint(1, 2)
                            elif self.foilSkill >= 50:
                                damage += random.randint(5, 10)
                            elif self.foilSkill < 50:
                                print(self.boatsailor.upper(), "onboard", self.boatname.upper(), "has suffered a large amount of damage from foiling in hurricane conditions.")
                                damage += random.randint(15, 30)
                                time.sleep(5)
                            self.health -= damage
                if self.mobileRepair == True:
                    self.speed /= 2
                    if self.repairTimer <= self.originalRepairs:
                        self.focus = random.randint(random.randint(1, self.engineer), random.randint(self.engineer, 100))
                    elif self.repairTimer > self.originalRepairs:
                        print("{} is now motivated to finish the repairs. They should have been done by now!".format(self.boatsailor.upper()))
                        self.focus = random.randint(40, 60)
                    if self.focus >= 80:
                        self.health += random.randint(10, 15)
                        self.repairHours -= 3
                        print("{}'s repairs have had a massive breakthrough, and as such, the completion estimate has been brought forward by 2 hours! They should now be finished in {} hours.".format(self.boatsailor.upper(), self.repairHours))
                    elif self.focus >= 60:
                        self.health += random.randint(10, 15)
                        self.repairHours -= 2
                        print("{}'s repairs have had a breakthrough, and as such, the completion estimate has been brought forward by 1 hour! They should now be finished in {} hours.".format(self.boatsailor.upper(), self.repairHours))
                    elif self.focus >= 40:
                        self.health += random.randint(5, 10)
                        self.repairHours -= 1
                        print("{}'s repairs have been continuing at a steady pace. They should be done in {} hours.".format(self.boatsailor.upper(), self.repairHours))
                    elif self.focus >= 20:
                        self.health += random.randint(1, 5)
                        print("{}'s repairs have suffered a minor delay. This means the completion estimate for the repairs has had to be pushed back by an hour... They should now be done in {} hours.".format(self.boatsailor.upper(), self.repairHours))
                    elif self.focus < 20:
                        self.health += random.randint(1, 5)
                        self.repairHours += 1
                        print("{}'s repairs have suffered a major delay. This means the completion estimate for the repairs has had to be pushed back by 2 hours... They should now be done in {} hours.".format(self.boatsailor.upper(), self.repairHours))
                    if self.repairHours <= 0:
                        self.repairHours = 0
                        self.repairTimer = 0
                        self.originalRepairs = 0
                        self.mobileRepair = False
                        self.repairsPossible = False
                        print("{}'s repairs aboard {} have been complete. They can now safely return to full race mode.".format(self.boatsailor.upper(), self.boatname.upper()))
                    self.repairTimer += 1
                    time.sleep(3)
                        
            elif self.status == "Repairing":
                if self.repairTimer <= self.originalRepairs:
                    self.focus = random.randint(random.randint(1, self.engineer), random.randint(self.engineer, 100))
                elif self.repairTimer > self.originalRepairs:
                    print("{} is now motivated to finish the repairs. They should have been done by now!".format(self.boatsailor.upper()))
                    self.focus = random.randint(40, 60)
                if self.focus >= 80:
                    self.health += random.randint(10, 15)
                    self.repairHours -= 3
                    print("{}'s repairs have had a massive breakthrough, and as such, the completion estimate has been brought forward by 2 hours! They should now be finished in {} hours.".format(self.boatsailor.upper(), self.repairHours))
                elif self.focus >= 60:
                    self.health += random.randint(10, 15)
                    self.repairHours -= 2
                    print("{}'s repairs have had a breakthrough, and as such, the completion estimate has been brought forward by 1 hour! They should now be finished in {} hours.".format(self.boatsailor.upper(), self.repairHours))
                elif self.focus >= 40:
                    self.health += random.randint(5, 10)
                    self.repairHours -= 1
                    print("{}'s repairs have been continuing at a steady pace. They should be done in {} hours.".format(self.boatsailor.upper(), self.repairHours))
                elif self.focus >= 20:
                    self.health += random.randint(1, 5)
                    print("{}'s repairs have suffered a minor delay. This means the completion estimate for the repairs has had to be pushed back by an hour... They should now be done in {} hours.".format(self.boatsailor.upper(), self.repairHours))
                elif self.focus < 20:
                    self.health += random.randint(1, 5)
                    self.repairHours += 1
                    print("{}'s repairs have suffered a major delay. This means the completion estimate for the repairs has had to be pushed back by 2 hours... They should now be done in {} hours.".format(self.boatsailor.upper(), self.repairHours))
                if self.repairHours <= 0:
                    self.repairHours = 0
                    self.repairTimer = 0
                    self.originalRepairs = 0
                    self.status = "Sailing"
                    self.repairsPossible = False
                    print("{}'s repairs aboard {} have been complete. They can now safely return to the race.".format(self.boatsailor.upper(), self.boatname.upper()))
                self.repairTimer += 1
                time.sleep(3)

            distDay = self.speed * random.choice([2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-1,-2])
            self.distTravelled += self.speed
            self.distFinish -= distDay
        
        if self.distFinish <= 21400 and self.distFinish > 21400 - 40 and self.count == 0:
            print(self.boatsailor, "onboard", self.boatname, "has entered the Southern Hemisphere.")
            self.count += 1
            time.sleep(3)
        if self.distFinish <= 17500 and self.distFinish > 17500 - 40 and self.count == 1:
            print(self.boatsailor, "onboard", self.boatname, "has rounded the Cape of Good Hope.")
            self.count += 1
            time.sleep(3)
        if self.distFinish <= 13500 and self.distFinish > 13500 - 40 and self.count == 2:
            print(self.boatsailor, "onboard", self.boatname, "has rounded the Cape Leeuwin.")
            self.count += 1
            time.sleep(3)
        if self.distFinish <= 6900 and self.distFinish > 6900 - 40 and self.count == 3:
            print(self.boatsailor, "onboard", self.boatname, "has rounded Cape Horn.")
            self.count += 1
            time.sleep(3)
        if self.distFinish <= 3225 and self.distFinish > 3225 - 40 and self.count == 4:
            print(self.boatsailor, "onboard", self.boatname, "has entered the Northern Hemisphere.")
            self.count += 1
            time.sleep(3)
    def finishRace(self, noWeeks, noDays, noHours):
        if self.count == 5:
            self.weeks = noWeeks
            self.days = noDays
            self.hours = noHours
            self.finish = True
            print(self.boatsailor, "has finished the Vendee Globe")
            self.count += 1

sailorChoice = input("Do you want to use real people? (Y/N): ")
print()
print()
WORLDCOMPANIES = ("Whiz Motors", "Buzzy Bee Networks", "Global Coms", "Ridgeco", "Daydreammotors", "Wavigations", "Tigertainment", "Micromobile", "Icedream", "Smilecloud", "Pixy Co.", "Ghost Media", "Surprise Motors", "Flowertainment", "Voyagetronics", "Arcanetworks", "Nightelligence", "Boardream", "Marblecloud", "Leopardworks", "River Lightning", "Fjord Sports", "Hurricane", "Elitelligence", "Apachicorp", "Canics", "Sunlightning", "Honeyware", "Shadowdream", "Caverncast", "Equinox Limited", "Goblin Aviation", "Witch", "Lokilutions", "Ecliprises", "Blossomotors", "Vertexoftwards", "Yellowfruit", "Shadetales", "Luckywood", "Life Electronics", "Gale Foods", "Nimble Foods", "Cruxolutions", "Lucentertainment", "Solsticetems", "Silver Linetworks", "Nimblenite", "Vinesys", "Driftshack", "Mermaid Lighting", "Nemo Navigations", "Forest Media", "Equinetworks", "Rabbitechnologies", "Gnomelectrics", "Lionetworks", "Typhoonshadow", "Coreland", "Wizardsys", "Squid", "Drift Enterprises", "Brisk Coms", "Thorerecords", "Shrubrews", "Whiteoutwares", "Sphereshack", "Voidnite", "Diamondfruit", "APIVIA", "LinkedOut", "Bureau Vallee 2",   "Maitre Coq IV", "Groupe APICIL", "Yes we Cam!", "OMIA - Water Family", "Seaexplorer - Yacht Club de Monaco", "MACSF", "Prysmian Group", "V and B Mayenne", "Pure - Best Western Hotels and Resorts", "Banque Populaire X", "L'Occitane en Provence", "La Fabrique", "Time for Oceans", "La Mie Caline - Artisans Artipole", "Groupe Setin", "One Planet One Ocean", "Medallia", "Newrest - Arts et Fenetres", "Campagne de France", "TSE - 4myplanet", "Campagnie du Lit - Jiliti", "Stark", "DMG MORI Global One", "Merci", "Charal", "Initiatives-Coeur", "ARKEA PAPREC", "HUGO BOSS", "PRB", "CORUM L'Epargne", "Hillsong Church", "BBC Children In Need", "Comic Relief", "UNICEF", "FC Nantes", "Vendee Poire-Sur-Vie", "Angers SCO", "Hillsong College", "JMD Transport Group", "MT Rail Corporation", "SNCF", "RENFE", "Great British Railways", "Generali Concorde", "Grinaker", "O-Kay", "Cacharel", "Pen Duick III", "UAP", "36.15 MET", "Lada Poch", "Duracell", "Le Nouvel Observateur", "TBS-Charente Maritime", "Credit Agricole IV", "Fleury Michon X", "Ecureuil d'Aquitaine II", "Bagages Superior", "Groupe Sofap-Helvim", "Cacolac d'Aquitaine", "K&H Banque Matav", "Euskadi Europa 93 BBK", "Solo Nantes", "Vuarnet Watches", "Everlast", "Neil Pryde Sails", "Groupe LG", "Cardiff Discovery", "Fujicolor III", "Maitre Coq", "Le Monde", "Nigel Burgess Yatchs", "Coyote" "Geodis", "Credit Immobilier", "Groupe LG-Traitmat", "Cafe Legal-Le Gout", "Aqua Quorum", "Whirlpool-Europe 2", "Aquitaine Innovations", "Pommes Rhone Alpes", "Exide Challenger", "Amnesty International", "Budapest", "Club 60e Sud", "Afibel", "Groupe-LG2", "Algimouss", "Kingfisher", "Sill Matines La potagere", "Active Wear", "Union bancaire Privee", "Sodebo", "Team Group 4", "Voila.fr", "Gartmore", "Chocolats du Monde", "VM Materiaux", "Aquarelle.com", "DDP", "Wind Telecomunicazioni", "Whirlpool", "Solidaires", "Sogal Extenso", "Modern Univ.", "Humanities", "Old Spice", "Euroka Services", "This Time", "Argos", "Help for Autistic Children", "Armor Lux", "foies Gras", "Libre Belgique", "Bonduelle", "Ecover", "Temenos", "VMI", "Virbac-Paprec", "Hellomoto", "Arcelor Dunkerque", "Ocean Planet", "Max Havelaar", "Best Western", "ROXY", "AKENA Verandas", "Benefic", "Pro-Form", "Sill Veolia", "VM Materiaux", "Skandia", "UUDS", "Brother", "Foncia", "Brit Air", "Safran", "Bahrain Team Pindar", "Aviva", "Toe In The Water", "Great American III", "Fondation Ocean Vital", "Nauticsport-Kapsch", "Veolia Environnement", "Artemis", "Paprec-Virbac 2", "Algimouss Spirit of Canada", "BT", "Generali", "Ecover 3", "Groupe Maisonneuve", "Gitana Eighty", "Cheminees Poujoulat", "Pakea Bizkaia", "Delta Dore", "Energies Autour du Monde", "DCNS", "Groupe Bel", "Macif", "Banque Populaire", "Virbac-Paprec 3", "SynerCiel", "Gamesa", "Mirabaud", "Votre Nom autour du Monde avec EDM Projets", "Team Plastique", "Energat", "Saveol", "Bureau Vallee", "Banque Populaire VIII", "StMichel-Virbac", "Queginer-Leucemie Espoir", "Finistere Mer Vent", "Spirit of Hungary", "Comme un seul homme", "La Mie Caline", "Newrest-Matmut", "La Fabrique", "Great American IV", "One Planet One Ocean", "Famille Mary - Etamine du Lys", "Foresight Natural Energy", "No Way Back", "TechnoFirst-FaceOcean", "Kilcullen Voyager - Team Ireland", "SMA", "Compagnie du Lit - Boulogne Billancourt", "Le Souffle du Nord pour Le Projet Imagine", "Gitana - Edmond de Rothschild", "Bastide-Otio", "Spirit of Yukoh", "Safran II")
noBoats = random.randint(20, 100)
boatList = []
boatRegistryList = []
sailorList = []
boatDistance = []
competingBoats = []
RACEDISTANCE = 24000
print()
print("There will be", noBoats, "boats in this year's Vendee Globe.")
print()
for i in range(noBoats):
    while 1 == 1:
        sailorFirst = ["Charlie", "Louis", "Thomas", "Yannick", "Damien", "Jean", "Benjamin", "Boris", "Isabelle", "Giancarlo", "Maxime", "Romain", "Clarisse", "Sebastien", "Samantha", "Alan", "Stephane", "Armel", "Arnaud", "Manuel", "Didac", "Pip", "Fabrice", "Miranda", "Alexia", "Clement", "Ari", "Kojiro", "Sebastien", "Jeremie", "Alex", "Kevin", "Nicolas", "Taya", "Brooke", "Joel", "Jadwin", "Jonathon", "Aodhan", "Matt", "Jihea", "David", "Michael Guy", "Dylan", "Nigel", "Alexander", "Benjamin", "Benjamin", "Alban", "Denis", "Charly", "Andrei", "Jean-Charles", "Thomas", "Nicolas", "Charles", "Sebastian", "Dennis", "Abdoulaye", "Pedro", "Batista", "Imran", "Ludovic", "Roli", "Moses", "Anthony", "Marcus", "Abdoul Kader", "Randal", "Jean-Kevin", "Kalifa", "Renaud", "Bridge", "Thomas", "Jorge", "Taya", "Brooke", "Frankie", "Conal", "Phillipa", "Maddison", "Ubaid", "Tobi", "Caolan", "Diesel", "Jasmine", "Amara", "Herbert", "Lola-Rose", "Lillie-Rose", "Che", "Izaak", "Dina", "John", "Milton", "Aidan", "Inez", "Marcos", "Kloe", "Isra", "Lorena"]
        sailorLast = ["Dalin", "Burton", "Ruyant", "Bestaven", "Sequin", "Le Cam", "Dutreaux", "Herrmann", "Joschke", "Pedote", "Sorel", "Attanasio", "Cremer", "Simon", "Davies", "Roura", "Le Diraison", "Tripon", "Boissieres", "Cousin", "Costa", "Hare", "Amedeo", "Merron", "Barrier", "Giraud", "Huusela", "Shiraishi", "Destremau", "Beyou", "Thomson", "Escoffier", "Troussel", "Gaukrodger", "Fraser", "Houston", "Gillies", "Douglass", "King", "Crocker", "Oh", "Ware", "Chislett", "Thomas", "Hendroff", "Pappas", "Tennikoff", "Hastings", "Lafont", "Petric", "Jan", "Girotto", "Casteletto", "Basila", "Pallois", "Traore", "Corchia", "Appiah", "Toure", "Chirivella", "Mendy", "Louza", "Blas", "Pereira de Sa", "Simon", "Limbombe", "Coco", "Bamber", "Kolo Muani", "Augustin", "Coulibaly", "Emond", "Ndilu", "Haines", "Da Silva", "Smith", "Ligterwood", "Chester", "Goldsmith", "Bright", "Dawe", "Clegg", "Rawlings", "Corrigan", "Haas", "Cantu", "Decker", "Robin", "Haney", "Cash", "Alfaro", "Muir", "Fitzpatrick", "Cherry", "White", "Lamb", "Roberts", "Whitaker", "Ewing", "Bull", "Rivera"]
        if sailorChoice.upper() == "Y" or sailorChoice.upper() == "YES":
            sailorChoose = random.randint(0, len(sailorFirst) - 1)
            sailorName = sailorFirst[sailorChoose] + " " + sailorLast[sailorChoose]
        else:
            sailorName = random.choice(sailorFirst) + " " + random.choice(sailorLast)
        if sailorName not in sailorList:
            sailorList.append(sailorName)
            break
    while 1 == 1:
        boatname = random.choice(WORLDCOMPANIES)
        if boatname not in boatList:
            boatList.append(boatname)
            boatDistance.append(-1)
            break
    boatRegistryList.append(Skipper(boatname, sailorName, i))
    competingBoats.append(boatRegistryList[len(boatRegistryList) - 1])
    print("Sailor no.", i + 1, "is", sailorName, "onboard", boatname)
    print("         ", boatname, "is a", boatRegistryList[len(boatRegistryList) - 1].boatType)
    if boatRegistryList[len(boatRegistryList) - 1].sailorSkill <= 20:
        print(sailorName, "is an awful sailor.")
    elif boatRegistryList[len(boatRegistryList) - 1].sailorSkill <= 40:
        print(sailorName, "is not a good sailor.")
    elif boatRegistryList[len(boatRegistryList) - 1].sailorSkill <= 60:
        print(sailorName, "is a decent sailor.")
    elif boatRegistryList[len(boatRegistryList) - 1].sailorSkill <= 80:
        print(sailorName, "is a good sailor.")
    elif boatRegistryList[len(boatRegistryList) - 1].sailorSkill > 80:
        print(sailorName, "is a legendary sailor.")
    if boatRegistryList[len(boatRegistryList) - 1].boatType == "Updated" or boatRegistryList[len(boatRegistryList) - 1].boatType == "New Foiler" or boatRegistryList[len(boatRegistryList) - 1].boatType == "2nd Gen":
        if boatRegistryList[len(boatRegistryList) - 1].foilSkill <= 20:
            print(sailorName, "is an awful foiler of a boat.")
        elif boatRegistryList[len(boatRegistryList) - 1].foilSkill <= 40:
            print(sailorName, "is not a good foiler of a boat.")
        elif boatRegistryList[len(boatRegistryList) - 1].foilSkill <= 60:
            print(sailorName, "is a decent foiler of a boat.")
        elif boatRegistryList[len(boatRegistryList) - 1].foilSkill <= 80:
            print(sailorName, "is a good foiler of a boat.")
        elif boatRegistryList[len(boatRegistryList) - 1].foilSkill >= 80:
            print(sailorName, "is a legendary foiler of a boat.")
    if boatRegistryList[len(boatRegistryList) - 1].engineer <= 20:
        print(sailorName, "is awful at repairing boats.")
    elif boatRegistryList[len(boatRegistryList) - 1].engineer <= 40:
        print(sailorName, "is untrained at repairing boats.")
    elif boatRegistryList[len(boatRegistryList) - 1].engineer <= 60:
        print(sailorName, "is alright at repairing boats.")
    elif boatRegistryList[len(boatRegistryList) - 1].engineer <= 80:
        print(sailorName, "is well trained at repairing boats.")
    elif boatRegistryList[len(boatRegistryList) - 1].engineer >= 80:
        print(sailorName, "is an absolutely fantastic engineer. They can repair boats easily!")
    if boatRegistryList[len(boatRegistryList) - 1].repairBegin > 25:
        print("         ", sailorName, "is very conservative when looking after their boat.")
    elif boatRegistryList[len(boatRegistryList) - 1].repairBegin <= 25:
        print("         ", sailorName, "is definitely a risk taker when looking after their boat.")
    print()
    time.sleep(5)

print()
print()

weatherList = []
for i in range(30):
    weatherChoice = ["Doldrums", "Light wind", "Average", "Favourable", "Favourable", "Stormy", "Hurricane"]
    weatherList.append(weatherChoice)

noHours = 0
noDays = 0
noWeeks = 0
noMonths = 0
noTotalHours = 0
noTotalDays = 0
finishedList = []
abandonedList = []
finished = False
while len(competingBoats) > 0 and noMonths < 24:
    print()
    print()
    print()
    for i in range(len(boatRegistryList)):
        sailor = boatRegistryList[i]
        sailor.weatherUpdate(weatherList)
        if sailor in competingBoats:
            if sailor.status == "Sailing":
                sailor.raceUpdate()
                boatDistance[i] = sailor.distTravelled
            elif sailor.status == "Repairing":
                sailor.raceUpdate()
                boatDistance[i] = sailor.distTravelled
            else:
                competingBoats.remove(sailor)
                if sailor.status == "Finished":
                    finishedList.append(sailor)
                    sailor.finishRace(noWeeks, noDays, noHours)
                elif sailor.status == "Retired":
                    abandonedList.append(sailor)

    for x in range(len(weatherList)):
        if noTotalHours % (random.randint(1, 12)) == 0:
            weatherChoice = random.choice([weatherList[x], weatherList[x], weatherList[x], weatherList[x], "Doldrums", "Doldrums", "Light wind", "Light wind", "Average", "Average", "Favourable", "Favourable", "Favourable", "Favourable", "Stormy", "Stormy", "Stormy", "Stormy", "Hurricane"])
            weatherList[x] = weatherChoice

    noHours += 1
    noTotalHours += 1
    if noHours % 24 == 0:
        print()
        print()
        noHours = 0
        noDays += 1
        noTotalDays += 1
        print("We've been racing for", noTotalDays, "days.")
        ind = boatDistance.index(max(boatDistance))
        leader = boatRegistryList[ind]
        print("The leader is", leader.boatsailor, "having travelled", leader.distTravelled, "nautical miles on a", leader.boatType, "boat.")
        print("The weather over the leader is", leader.weather + ".")
        if leader.foilStatus == "Foiling":
            print("The leader is foiling and is travelling at", leader.speed, "knots.")
        elif leader.foilStatus == "Not Foiling":
            print("The leader is not foiling and is travelling at", leader.speed, "knots.")
        if leader.status == "Sailing":
            if leader.mobileRepair == True:
                print("{} is still sailing, though they are carrying out repairs at the same time, so their speed is reduced.".format(leader.boatsailor.upper()))
            elif leader.mobileRepair == False:
                print("{} is still sailing at full speed with no issues.".format(leader.boatsailor.upper()))
        elif leader.status == "Repairing":
            print("{} is currently stopped and repairing {}.".format(leader.boatsailor.upper(), leader.boatname.upper()))
        print("We have", len(competingBoats), "sailors still in this race.")
        print("Of the ones who are out,", len(abandonedList), "have retired, whilst the other", len(finishedList), "have finished the race.")
        print("Total time taken =", noMonths, "months,", noWeeks, "weeks,", noDays, "days,", noHours, "hours.")
        print()
        time.sleep(20)
        if noDays % 7 == 0:
            noDays = 0
            noWeeks += 1
            if noWeeks % 4 == 0:
                noWeeks = 0
                noMonths += 1
                if noMonths % 12 == 0:
                    noMonths = 0
                    noYears += 1

winner = boatDistance.index(max(boatDistance))
print("The winner of this year's Vendee Globe is", boatRegistryList[winner].boatsailor, "onboard", boatRegistryList[winner].boatname, "having taken", boatRegistryList[winner].weeks, "weeks", boatRegistryList[winner].days, "days and", boatRegistryList[winner].hours, "hours.")
loser = boatDistance.index(min(boatDistance))
print("The winner of this year's Vendee Globe is", boatRegistryList[loser].boatsailor, "onboard", boatRegistryList[loser].boatname, "having taken", boatRegistryList[loser].weeks, "weeks", boatRegistryList[loser].days, "days and", boatRegistryList[loser].hours, "hours.")
print("--------------------------------------------------")
print()
print()
print("--------------------------------------------------")
print("Here is a list of all the times:")
for i in range(len(boatRegistryList)):
    print()
    print(boatRegistryList[i].boatsailor, ":", boatRegistryList[i].boatname)
    print(boatRegistryList[i].weeks, "weeks,", boatRegistryList[i].days, "days, and", boatRegistryList[i].hours, "hours.")
    print()

end = time.time()

secondsTaken = end - start
minutesTaken = secondsTaken / 60
hoursTaken = minutesTaken / 60

print("This program took", secondsTaken, "seconds to simulate.")
print("This program took", minutesTaken, "minutes to simulate.")
print("This program took", hoursTaken, "hours to simulate.")
