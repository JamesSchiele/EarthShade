import random

class Robot:
    def __init__(self, distance, data, enemies, speed, shield_level):
        self.distance = distance
        self.data = data
        self.enemies = enemies
        self.speed = speed
        self.shield_level = shield_level
        self.power = 100  # Robot starts with 100% power
        
    def calculate_power_consumption(self):
        # Power consumption factors:
        # Speed: higher speed consumes more power
        # Data: carrying more data consumes more power
        # Shield: higher shield level consumes more power
        return (self.speed * 0.5) + (self.data * 0.2) + (self.shield_level * 0.3)
    
    def encounter_enemy(self):
        # Encountering an enemy causes damage based on their attack power
        damage = random.randint(10, 30)  # Random damage for simplicity
        print(f"An enemy attacks! Damage: {damage}")
        
        if self.shield_level > 0:
            # Shields absorb some of the damage
            shield_absorption = min(self.shield_level, damage)
            self.shield_level -= shield_absorption
            damage -= shield_absorption
            print(f"Shield absorbed {shield_absorption} damage. Remaining shield: {self.shield_level}")
        
        # Remaining damage hits the robot's power
        self.power -= damage
        print(f"Remaining power after attack: {self.power}")
        
    def travel(self):
        while self.distance > 0 and self.power > 0:
            power_consumption = self.calculate_power_consumption()
            self.power -= power_consumption
            print(f"Robot moves. Power consumption this step: {power_consumption}, remaining power: {self.power}")
            
            # # Check if any enemies are encountered randomly
            # if random.random() < 0.3:  # 30% chance to encounter an enemy on each move
            #     self.encounter_enemy()
                
            # Reduce distance traveled
            distance_travelled = self.speed
            self.distance -= distance_travelled
            print(f"Robot travels {distance_travelled} meters. Distance remaining: {self.distance}")
            
            if self.power <= 0:
                print("Power exhausted. Robot failed!")
                return False
        
        print("Robot reached the destination!")
        return True

class Game:
    def __init__(self):
        self.log = []  # Store all input configurations and results
    
    def log_inputs(self, speed, shield_level, data, success, distance_travelled):
        # Log the player's input values and the result
        self.log.append({
            "speed": speed,
            "shield_level": shield_level,
            "data": data,
            "success": success,
            "distance_travelled": distance_travelled
        })
    
    def display_log(self):
        # Display the log of previous attempts
        if not self.log:
            print("No attempts have been logged yet.")
        else:
            print("\nAttempt Log:")
            for entry in self.log:
                status = "Success" if entry["success"] else "Failure"
                print(f"Speed: {entry['speed']}, Shield: {entry['shield_level']}, Data: {entry['data']} KB | "
                      f"Status: {status} | Distance Traveled: {entry['distance_travelled']} meters")

    def game_simulation(self, distance, data, enemies):
        print(f"\nThe robot needs to travel {distance} meters with {data} KB of data.")
        print(f"There are {enemies} enemies in the vicinity, and they will damage the robot if encountered.")
        
        # Ask the player for their inputs
        speed = int(input("What speed should the robot move at? (Choose a value between 1 and 20): "))
        shield_level = int(input("What shield level should the robot have? (Choose a value between 0 and 100): "))
        data = int(input("How much data should the robot carry? (Choose a value between 0 and 500 KB): "))
        
        # Create a Robot object with player choices
        robot = Robot(distance, data, enemies, speed, shield_level)
        
        # Simulate the robot's travel
        success = robot.travel()
        
        # Log the inputs and result
        self.log_inputs(speed, shield_level, data, success, distance - robot.distance)
        
        if success:
            print(f"\nSuccess! The robot delivered {data} KB of data.")
        else:
            print(f"\nFailure! The robot traveled {distance - robot.distance} meters before running out of power.")
        
# Start the game
game = Game()
distance = 100  # 1000 meters to travel
data = 200  # 200 KB of data
enemies = 5  # Number of enemies

# Game loop for multiple attempts
while True:
    game.game_simulation(distance, data, enemies)
    # Ask if the player wants to see the log or try again
    action = input("\nDo you want to (1) try again, (2) view the attempt log, or (3) quit? Enter 1, 2, or 3: ")
    if action == "2":
        game.display_log()
    elif action == "3":
        print("Thanks for playing!")
        break
