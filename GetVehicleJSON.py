import json
import time
from urllib.request import urlopen

def main():
    while True:
        time.sleep(1)
        with open("vehicleJSON-serviceIN.txt", 'r+', encoding="utf-8") as fi:
            data = fi.read()
            fi.truncate(0)
            fi.close()
            if data:
                arr = data.split()
                if len(arr) == 1:
                    mydict = getVehicleJSON(arr[0])
                else:
                    mydict = getVehicleJSON(arr[0], arr[1:])
                with open("vehicleJSON-serviceOUT.txt", 'w', encoding="utf-8") as fo:
                    fo.write(json.dumps(mydict, indent=4))
                fo.close()



def getVehicleJSON(method_name, args = []):
    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/'
    method_name = method_name.replace(" ", "");
    method_name_lower = method_name.lower()
    url += method_name
    url_format ='format=json'

    # Decode VIN
    if method_name_lower == "decodevin":
        url+= "/" + args[0] + "?"
        if len(args) > 1:
            url += "&modelyear=" + args[1]
        print(url)
    # Get WMIs for Manufacturer
    elif method_name_lower == "getwmisformanufacturer":
      url += "/"
      for i in range(0, len(args)):
          if i == 2:
              url += "?vehicleType="
          url += args[i]
          if i == 1:
              url += "?"
      url += "?" if len(args) == 1 else "&"
    # Get Parts
    elif method_name_lower == "getparts":
        url += "?"
        for i in range(0, len(args)):
            if i == 0:
                url += "type=" + args[i]
            elif i == 1:
                url += "&fromDate=" + args[i]
            elif i == 2:
                url += "&toDate=" + args[i]
        url += "&"
    # Get all Manufacturers
    elif method_name_lower == "getallmanufacturers":
        url += "?"
        for arg in args:
            url += "ManufacturerType=" + arg
        url += "&"
    # Get Makes for Manufacturer by Manufacturer Name and Year
    elif method_name_lower == "getmakesformanufacturerandyear":
        url += "/"
        for i in range(0, len(args)):
            if i == 1:
                url += "year="
            url += args[i]
            if i == 0:
                url += "?"
        url += "&"
    # Get Models for Make and a combination of Year and Vehicle Type
    # note order must be make, model year, vehicle type
    elif (method_name_lower == "getmodelsformakeyear" or
         method_name_lower == "getmodelsformakeidyear"):
        url += "/"
        make = "make/" if method_name_lower == "getmodelsformakeyear" else "makeId/"
        for i in range(0, len(args)):
            if i == 0:
                url += make + args[i] + "/"
            elif i == 1:
                url += "modelyear/" + args[i] + "/"
            elif i == 2:
                url += "vehicletype/" + args[i] + "?"
        if len(args) < 3:
            url = url[:-1]
            url += "?"
    else:
        for arg in args:
            url += '/'
            url += arg
        url += "?"
    url += url_format
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

if __name__ == "__main__":
    main()