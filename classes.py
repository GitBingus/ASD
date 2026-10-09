class Holiday:
    def __init__(self, destination: str, duration: int, cost: float):
        self.destination = destination
        self.duration = duration
        self.cost = cost

    def getDuration(self):
        return self.duration

    def getCost(self): 
        return self.cost

    def __str__(self):
        return f"Holiday: {self.destination}\tDuration: {self.duration} days\tCost: ${self.cost:.2f}"



class TravelAgent:
    def __init__(self, name: str, postcode: str, holidays: list | None = None):
        self.name = name
        self.postcode = postcode
        self.holidays = holidays if holidays is not None else []


    def addHoliday(self, holiday: Holiday):
        self.holidays.append(holiday)

    def getName(self):
        return self.name

    def getPostcode(self):
        return self.postcode

    def __str__(self):
        return f"Travel Agent: {self.name}\tPostcode: {self.postcode}"

class RunTravelAgent:
    h1 =  Holiday("Bermuda", 2, 800)
    h2 =  Holiday("Hull", 14, 8)
    h3 =  Holiday("Los Angeles", 12, 2100)

    t1 = TravelAgent("CheapAsChips", "MA99 1CU")

    t1.addHoliday(h1)
    t1.addHoliday(h2)
    t1.addHoliday(h3)

    t2 = TravelAgent("Shoe String Tours", "CO33 2DX")

    print(t1)

    print("h3 Duration= "+str(h3.getDuration())+" days & Cost= "+str(h3.getCost()))
    print("t2 "+str(t2.getName())+" "+ str(t2.getPostcode()))