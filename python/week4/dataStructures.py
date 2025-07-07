# A list of 5 of your favorite snacks
Josephsnacks = ["pealables", "snickers", "twix", "wachmacallit", "reses."]
for snack in Josephsnacks:
    print(snack)
# A tuple of 5 colleges you want to attend
Josephcolleges = ["Uc berkly", "howerd", "ccc", "stanfer", "uc ervine."]
for colleges in Josephcolleges:
    print(colleges)
# A set of with 5 pieces of data on anything you want; 
Josephdataanything = [""]
# A dictionary on a car; key must describe an attribute of the car, followed it's value.
carattribute = {"brand": "toyota",
                "model": "corrola",
                "year": 2023, 
                "engine": "4-cylinder",
                "wheelsize": "18in"  }
carattribute["color"] = "blue"
for attribute in carattribute:
    print(carattribute.get(attribute))
