# CS-361-Microservice
Microservice for partner
Once the user starts this process it will wait/listen for a file 'vehicleJSON-serviceIN.txt' (which should already exist in the same directory) to have data in it to read from. It will then take the data to call the selected API function appropriately. The result will be printed out to an output file 'vehicleJSON-serviceOUT.txt' (this will be created if it does not already exist). The input text file will be cleared empty during this process so that another command can be written to it and the listener process can make another API call.

The data should include the method name and, if there are any, any additional arguments. The method name should be one word (case does not matter) as should each individual argument (just separate each token with a space, no parenthesis or commas or anything like that, example:  GetVehicleTypesForMake mercedes). Also arguments should be given in the order they appear on the API site.

And for method names don't using the title, i.e.
'Get Makes for Manufacturer by Manufacturer Name and Year'
but rather the name part in the url:
/vehicles/GETMAKESFORMANUFACTURERANDYEAR/mer?year=2013&format=json

The process runs forever so it will have to be manually terminated, but I can change it to make the listener wait for an 'exit' keyword instead if needed.

-------REVISED-------

EXAMPLE CALLS:
To get all makes:
GetAllMakes

To get manufactorer details from all Honda cars:
GetManufacturerDetails Honda

To get makes for Mercedes cars in 2013:
GetMakesForManufacturerAndYear Mercedes 2013


Sequence Diagram:
![image](https://user-images.githubusercontent.com/77367181/220760539-f8fa25e9-3c88-4041-b45d-80aac34d0d5f.png)
