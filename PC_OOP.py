# This is my first small programming project that I wrote during the summer vacation of 2021.

import time

username = "capellax"
password = "0002"

class PC():
    def __init__(self, pc_status, cpu, gpu, ram, ssd, games_working,
                 total_storage, storage_used, cpu_usage, gpu_usage,
                 motherboard, ram_usage, ssd_usage, brightness, volume, games):

        self.pc_status = pc_status
        self.cpu = cpu
        self.gpu = gpu
        self.motherboard = motherboard
        self.ram = ram
        self.ssd = ssd
        self.games = games
        self.games_working = games_working
        self.total_storage = total_storage
        self.storage_used = storage_used
        self.cpu_usage = cpu_usage
        self.gpu_usage = gpu_usage
        self.ram_usage = ram_usage
        self.ssd_usage = ssd_usage
        self.brightness = brightness
        self.volume = volume 

    def __str__(self):
        if self.pc_status == "Off":
            print("To perform this operation, please turn on the computer first!..")
        else:
            return f"""

 -------------------------------------------------     
 1
         Computer Component Specifications:
 -------------------------------------------------
            > MOTHERBOARD: {self.motherboard}
        > CPU (Processor): {self.cpu}
     > GPU (Graphic Card): {self.gpu}
                    > RAM: {self.ram}
 > SSD (Solid State Disk): {self.ssd}
        
        """

    def open_pc(self):

        attempt = 3

        while True:

            s_username = input("Enter your username: ")
            time.sleep(0.5)
            s_password = input("Enter your password: ")
            time.sleep(0.5)

            if s_username == username and s_password == password:
                time.sleep(1)
                print("Login Successful!")
                self.pc_status = "On"
                break
            elif s_username != username and s_password == password:
                time.sleep(1)
                print("Your username is incorrect!..")
                attempt -= 1
            elif s_username == username and s_password != password:
                time.sleep(1)
                print("Your password is incorrect!..")
                attempt -= 1
            elif s_username != username and s_password != password:
                time.sleep(1)
                print("Your username and password are incorrect!..")
                attempt -= 1
            if attempt == 0:
                print("System blocked! Please try again after 10 seconds...")
                time.sleep(1)
                break

    def close_pc(self):
        if self.pc_status == "Off":
            print("The computer is already off!")
        else:
            print("The computer is shutting down...")

    def games_list(self):
        if self.pc_status == "Off":
            print("To perform this operation, please turn on the computer first!..")
        else:
            print(f"The games in your list: {self.games}")

    def game_install(self, game_name):
        if self.pc_status == "Off":
            print("To perform this operation, please turn on the computer first!..")
        else:
            print("Adding new game...")
            time.sleep(1)
            self.games.append(game_name)
            print(f"Your updated game list:  {self.games}")

    def game_uninstall(self, game_name):
        if self.pc_status == "Off":
            print("To perform this operation, please turn on the computer first!..")
        else:
            print("Removing game...")
            time.sleep(1)
            self.games.remove(game_name)
            print(f"Your updated game list:  {self.games}")

    def volume_arrangement(self):
        if self.pc_status == "Off":
            print("To perform this operation, please turn on the computer first!..")
        else:

            while True:

                x = input("""

  > Press '+' to increase volume.
  > Press '-' to decrease volume.
  > Press 'q'/'Q' to cancel.
        
        """)

                if x == "Q" or x == "q":
                    print("Exiting volume settings...")
                    time.sleep(.75)
                    break
                elif x == "+":
                    if self.volume == 100:
                        time.sleep(1)
                        print(f"Volume is already at maximum!\n(Volume level: {self.volume})")
                    else:
                        print("Increasing volume...")
                        time.sleep(.5)
                        self.volume += 10
                        print(f"Updated volume level: {self.volume}")
                elif x == "-":
                    if self.volume == 0:
                        time.sleep(.75)
                        print(f"Volume is already at minimum!\n(Volume level: {self.volume})")
                    else:
                        print("Decreasing volume...")
                        time.sleep(.5)
                        self.volume -= 10
                        print(f"Updated volume level: {self.volume}")

    def brightness_arrangement(self):
        if self.pc_status == "Off":
            print("To perform this operation, please turn on the computer first!..")
        else:

            while True:

                i = input("""

  > Press '+' to increase brightness.
  > Press '-' to decrease brightness.
  > Press 'q'/'Q' to cancel.
        
        """)

                if i == "Q" or i == "q":
                    print("Exiting brightness settings...")
                    break
                elif i == "+":
                    if self.brightness == 100:
                        print(f"Brightness is already at maximum!\n(Brightness level: {self.brightness})")
                    else:
                        print("Increasing brightness...")
                        time.sleep(0.5)
                        self.brightness += 10
                        print(f"Updated brightness level: {self.brightness}")
                elif i == "-":
                    if self.brightness == 0:
                        print(f"Brightness is already at minimum!\n(Brightness level: {self.brightness})")
                    else:
                        print("Decreasing brightness...")
                        time.sleep(0.5)
                        self.brightness -= 10
                        print(f"Updated brightness level: {self.brightness}")

    def usages_and_info(self):

        if self.pc_status == "Off":
            print("To perform this operation, please turn on the computer first!..")
        else:
            print(f"""

    -------------------------------------------------
       >>> General System and Usage Information: <<<
    ------------------------------------------------- 
        > CPU Usage: % {self.cpu_usage}
        > GPU Usage: % {self.gpu_usage}
        > RAM Usage: % {self.ram_usage}
        > SSD Usage: % {self.ssd_usage} 
                    
        > Total Storage: {self.total_storage}
        > Available Storage: {self.storage_used}

        > Volume Level: % {self.volume}
        > Brightness Level: % {self.brightness}

        """)


pc = PC("Off","AMD Ryzen 7 5800H","AMD Radeon RX 6700M","16GB 3200MHz","120GB NVMe",
        ["CS:GO","PUBG"],"1024 GB","622 GB",33,57,"MSI Delta 15",42, 59, 80, 100, 
        ["CS:GO","PUBG","CoD:MW2","Overcooked 2"])

                 
print("""
         _______________________________________________

             > > >  OPERATIONS YOU CAN PERFORM:  < < < 
         _______________________________________________


            1. Turn on the computer.
            2. Turn off the computer.
         
            3. Computer Component Specifications
            4. General System and Usage Information

            5. View Games.
            6. Install Game(s).
            7. Uninstall Game(s).
            
            8. Adjust Volume Level.
            9. Adjust Brightness Level.

         ________________________________________________

""")

while True:

    operation = input("Select your operation number: ")

    if operation == "1":
        time.sleep(0.75)
        pc.open_pc()

    elif operation == "2":
        time.sleep(0.75)
        pc.close_pc()

    elif operation =="3":
        time.sleep(0.75)
        print(pc)

    elif operation == "4":
        time.sleep(0.75)
        pc.usages_and_info()

    elif operation == "5":
        time.sleep(0.75)
        pc.games_list()
        
    elif operation == "6":
        time.sleep(0.75)
        new_games = input("Please enter the games you want to install, separated by commas: ")
        games_list = new_games.split(",")
        for i in games_list:
            pc.game_install(i)

    elif operation == "7":
        time.sleep(0.75)
        games_to_be_deleted = input("Please enter the games you want to uninstall, separated by commas: ")
        games_list = games_to_be_deleted.split(",")
        for x in games_list:
            pc.game_uninstall(x)

    elif operation == "8":
        time.sleep(0.75)
        pc.volume_arrangement()

    elif operation == "9":
        time.sleep(0.75)
        pc.brightness_arrangement()

    else:
        time.sleep(1.25)
        print("Invalid operation! Please enter a valid operation number...")
