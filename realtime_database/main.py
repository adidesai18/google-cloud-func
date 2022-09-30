import firebase_admin
from firebase_admin import db



cred_obj = firebase_admin.credentials.Certificate('/Users/aditya_9009/Desktop/Desktop/Repositories/google-cloud-func/firebase_credentials.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':"https://easysenddemo-default-rtdb.asia-southeast1.firebasedatabase.app/"
	})



main_ref = db.reference()
# data=[
#   {
#     "ID": "1",
#     "Name": "Senpai",
#     "Gender": "1",
#     "Class": "32",
#     "Seat": "15",
#     "Club": "0",
#     "Persona": "1",
#     "Crush": "0",
#     "BreastSize": "0",
#     "Strength": "0",
#     "Hairstyle": "1",
#     "Color": "Black",
#     "Eyes": "Black",
#     "EyeType": "Default",
#     "Stockings": "None",
#     "Accessory": "0",
#     "ScheduleTime": "7_7_8_13.01_13.375_15.5_16_17.25_99_99",
#     "ScheduleDestination": "Spawn_Locker_Hangout_Seat_LunchSpot_Seat_Clean_Hangout_Locker_Exit",
#     "ScheduleAction": "Stand_Stand_Read_Sit_Eat_Sit_Clean_Read_Shoes_Stand",
#     "Info": "An average student. \n \n Average grades, average looks, average life... \n \n I'm not sure what you see in him."
#   },
#   {
#     "ID": "2",
#     "Name": "Yui Rio",
#     "Gender": "0",
#     "Class": "11",
#     "Seat": "14",
#     "Club": "1",
#     "Persona": "5",
#     "Crush": "0",
#     "BreastSize": "0.5",
#     "Strength": "0",
#     "Hairstyle": "2",
#     "Color": "Red",
#     "Eyes": "Red",
#     "EyeType": "Default",
#     "Stockings": "Red",
#     "Accessory": "0",
#     "ScheduleTime": "7_7_8_13_13.375_15.5_16_17.25_99_99",
#     "ScheduleDestination": "Spawn_Locker_Hangout_Seat_LunchSpot_Seat_Clean_Club_Locker_Exit",
#     "ScheduleAction": "Stand_Stand_Socialize_Sit_Socialize_Sit_Clean_SocialSit_Shoes_Stand",
#     "Info": ""
#   },
#   {
#     "ID": "3",
#     "Name": "Yuna Hina",
#     "Gender": "0",
#     "Class": "12",
#     "Seat": "14",
#     "Club": "1",
#     "Persona": "6",
#     "Crush": "0",
#     "BreastSize": "0.8",
#     "Strength": "0",
#     "Hairstyle": "3",
#     "Color": "Yellow",
#     "Eyes": "Yellow",
#     "EyeType": "Default",
#     "Stockings": "Yellow",
#     "Accessory": "0",
#     "ScheduleTime": "7_7_8_13_13.375_15.5_16_17.25_99_99",
#     "ScheduleDestination": "Spawn_Locker_Hangout_Seat_LunchSpot_Seat_Clean_Club_Locker_Exit",
#     "ScheduleAction": "Stand_Stand_Socialize_Sit_Socialize_Sit_Clean_SocialSit_Shoes_Stand",
#     "Info": ""
#   },
#   {
#     "ID": "4",
#     "Name": "Koharu Hinata",
#     "Gender": "0",
#     "Class": "21",
#     "Seat": "14",
#     "Club": "1",
#     "Persona": "6",
#     "Crush": "0",
#     "BreastSize": "1.1",
#     "Strength": "0",
#     "Hairstyle": "4",
#     "Color": "Green",
#     "Eyes": "Green",
#     "EyeType": "Default",
#     "Stockings": "Green",
#     "Accessory": "0",
#     "ScheduleTime": "7_7_8_13.0001_13.375_15.5001_16_17.25_99_99",
#     "ScheduleDestination": "Spawn_Locker_Hangout_Seat_LunchSpot_Seat_Clean_Club_Locker_Exit",
#     "ScheduleAction": "Stand_Stand_Socialize_Sit_Socialize_Sit_Clean_SocialSit_Shoes_Stand",
#     "Info": ""
#   },
#   {
#     "ID": "5",
#     "Name": "Mei Mio",
#     "Gender": "0",
#     "Class": "22",
#     "Seat": "14",
#     "Club": "1",
#     "Persona": "2",
#     "Crush": "0",
#     "BreastSize": "1.4",
#     "Strength": "0",
#     "Hairstyle": "5",
#     "Color": "Blue",
#     "Eyes": "Blue",
#     "EyeType": "Default",
#     "Stockings": "Blue",
#     "Accessory": "7",
#     "ScheduleTime": "7_7_8_13_13.375_15.5_16_17.25_99_99",
#     "ScheduleDestination": "Spawn_Locker_Hangout_Seat_LunchSpot_Seat_Clean_Club_Locker_Exit",
#     "ScheduleAction": "Stand_Stand_Socialize_Sit_Socialize_Sit_Clean_SocialSit_Shoes_Stand",
#     "Info": ""
#   },
#   {
#     "ID": "6",
#     "Name": "Saki Miyu",
#     "Gender": "0",
#     "Class": "31",
#     "Seat": "14",
#     "Club": "1",
#     "Persona": "6",
#     "Crush": "0",
#     "BreastSize": "1.7",
#     "Strength": "0",
#     "Hairstyle": "6",
#     "Color": "Cyan",
#     "Eyes": "Cyan",
#     "EyeType": "Default",
#     "Stockings": "Cyan",
#     "Accessory": "0",
#     "ScheduleTime": "7_7_8_13.01_13.375_15.5_16_17.25_99_99",
#     "ScheduleDestination": "Spawn_Locker_Hangout_Seat_LunchSpot_Seat_Clean_Club_Locker_Exit",
#     "ScheduleAction": "Stand_Stand_Socialize_Sit_Socialize_Sit_Clean_SocialSit_Shoes_Stand",
#     "Info": "Kokona Haruka's best friend and closest confidant. Kokona is likely to discuss personal matters with this girl."
#   },
#   {
#     "ID": "7",
#     "Name": "Kokona Haruka",
#     "Gender": "0",
#     "Class": "32",
#     "Seat": "14",
#     "Club": "1",
#     "Persona": "6",
#     "Crush": "1",
#     "BreastSize": "2",
#     "Strength": "0",
#     "Hairstyle": "7",
#     "Color": "Purple",
#     "Eyes": "Purple",
#     "EyeType": "Default",
#     "Stockings": "Purple",
#     "Accessory": "0",
#     "ScheduleTime": "7_7_8_13.01_13.375_15.51_16_17.25_99_99",
#     "ScheduleDestination": "Spawn_Locker_Hangout_Seat_LunchSpot_Seat_Clean_Club_Locker_Exit",
#     "ScheduleAction": "Stand_Stand_Socialize_Sit_Socialize_Sit_Clean_SocialSit_Shoes_Stand",
#     "Info": ""
#   },
#   {
#     "ID": "8",
#     "Name": "Haruto Yuto",
#     "Gender": "1",
#     "Class": "11",
#     "Seat": "12",
#     "Club": "0",
#     "Persona": "5",
#     "Crush": "0",
#     "BreastSize": "0",
#     "Strength": "0",
#     "Hairstyle": "2",
#     "Color": "Red",
#     "Eyes": "Red",
#     "EyeType": "Default",
#     "Stockings": "None",
#     "Accessory": "3",
#     "ScheduleTime": "7_7_8_13_13.375_15.5_16_16.5_99",
#     "ScheduleDestination": "Spawn_Locker_Hangout_Seat_LunchSpot_Seat_Clean_Locker_Exit",
#     "ScheduleAction": "Stand_Stand_Socialize_Sit_Socialize_Sit_Clean_Shoes_Stand",
#     "Info": ""
#   },
#   {
#     "ID": "9",
#     "Name": "Sota Yuki",
#     "Gender": "1",
#     "Class": "12",
#     "Seat": "12",
#     "Club": "0",
#     "Persona": "6",
#     "Crush": "0",
#     "BreastSize": "0",
#     "Strength": "0",
#     "Hairstyle": "3",
#     "Color": "Yellow",
#     "Eyes": "Yellow",
#     "EyeType": "Default",
#     "Stockings": "None",
#     "Accessory": "0",
#     "ScheduleTime": "7_7_8_13_13.375_15.5_16_16.5_99",
#     "ScheduleDestination": "Spawn_Locker_Hangout_Seat_LunchSpot_Seat_Clean_Locker_Exit",
#     "ScheduleAction": "Stand_Stand_Socialize_Sit_Socialize_Sit_Clean_Shoes_Stand",
#     "Info": ""
#   },
# ]
# key=ref.push().key
# ref.update(data)
# print(ref.get())
# snapshot = ref.order_by_key().get()
# print(snapshot)
# for key, val in snapshot.items():
#     print('{0} was {1} meters tall'.format(key, val))
# ----------------------------------------------------------------------------------------------------------

# for i in data:
#     ref.push(i)
# print(ref.get())
# print("\n\n")
# snapshot = ref.order_by_value().get()
# print(snapshot)
# ----------------------------------------------------------------------------------------------------------
# ref.child("-NCiDIOw6snd8PTZxWGB").delete()
# ----------------------------------------------------------------------------------------------------------
# print(list(ref.get()).count)
# print(ref.key)
# Students=ref.get()
# print(Students)
# for student in Students:
#     print(Students[student])
# ----------------------------------------------------------------------------------------------------------

# ref.update({
#   "lambeosaurus": {
#     "height" : 2.1,
#     "length" : 12.5,
#     "weight": 5000
#   },
#   "stegosaurus": {
#     "height" : 4,
#     "length" : 9,
#     "weight" : 2500
#   }
# })
# snapshot = ref.child("Student").order_by_child("ID").equal_to("4").get()
# snapshot_d = ref.child("dinosaurs").order_by_child("height").get()
# print(snapshot_d)
# students=ref.child("Student").order_by_child("ID").equal_to("2").get()

# ----------------------------------------------------------------------------------------------------------



data_={
    "send_count": 1,
    "total_receiver": 1,
      }

main_ref.child("Broadcast").update(
    {"44":data_})

# ref = db.reference('scores')
# snapshot = ref.order_by_value().get()
# for key, val in snapshot.items():
#     print('The {0} dinosaur\'s score is {1}'.format(key, val))


# ref = db.reference('dinosaurs')
# snapshot = ref.order_by_key().get()
# print(snapshot)


ref = main_ref.child("Broadcast/List")
# ref.update({
#     "Instance connected":True,
# })

# for i in range(5):
#     ref.update({
#     i:data
# })
# for i in range(6):
#     data_={
#             "send_count": 1,
#             "key": str(9),
#             "broadcast_name": "+917720063009",
#             "is_task_finished": True,
#             "total_receiver": 1,
#             "created_at": "2022-09-24T20:48:11.764674",
#             }
#     ref.update({i:data_})

# ref.child("0").delete()

# snapshot = ref.order_by_child("Count").get()
# for key, val in snapshot.items():
#     print(key,val)