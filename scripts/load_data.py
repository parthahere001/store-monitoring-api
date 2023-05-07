from shopapiapp.models import storeStatusModel, menuHoursModel, timezoneModel
import csv
import datetime
import pytz
def run():
    with open("Menuhours.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header


        menuHoursModel.objects.all().delete()

        for row in reader:
            print(row)

           

            menuitem = menuHoursModel(store_id=row[0], day_num = row[1], start_time_local = row[2], end_time_local = row[3])
                      
            menuitem.save()

    with open("storestatus.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header
        storeStatusModel.objects.all().delete()
        

        for row in reader:
            print(row)

           
          
            menuitem = storeStatusModel(store_id=row[0], status = row[1], timestamp_uct = datetime.datetime.strptime(row[2][0:19:1],'%Y-%m-%d %H:%M:%S' ))
                      
            menuitem.save()
    with open("timestampdata.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header
        timezoneModel.objects.all().delete()
        

        for row in reader:
            print(row)

           
          
            menuitem = timezoneModel(store_id=row[0], timezone_str = row[1])
                      
            menuitem.save()
   