class WaterJug:
    def __init__(self):
        self.jug1 = 0
        self.jug2 = 0
        self.capacity1 = 4
        self.capacity2 = 3

    def fill_jug1(self):
        self.jug1 = self.capacity1
        print("Filled water in JUG1 of 4L")

    def fill_jug2(self):
        self.jug2 = self.capacity2
        print("Filled water in JUG2 of 3L")

    def empty_jug1(self):
        self.jug1 = 0
        print("JUG1 is now empty")

    def empty_jug2(self):
        self.jug2 = 0
        print("JUG2 is now empty")

    def transfer_jug1_to_jug2(self):
        transfer_amount = min(self.jug1, self.capacity2 - self.jug2)
        self.jug1 -= transfer_amount
        self.jug2 += transfer_amount
        print(f"Transferred {transfer_amount}L from Jug 1 to Jug 2.")

    def transfer_jug2_to_jug1(self):
        transfer_amount = min(self.jug2, self.capacity1 - self.jug1)
        self.jug2 -= transfer_amount
        self.jug1 += transfer_amount
        print(f"Transferred {transfer_amount}L from Jug 2 to Jug 1.")  

    def check_goal(self):
        return self.jug1 == 2 or self.jug2 == 2

    def display_state(self):
        print(f"Jug 1: {self.jug1}L, Jug 2: {self.jug2}L")

    def start(self):
        while True:
            self.display_state()
            if self.check_goal():
                print("Goal Achieved: 2L in one of the jugs!")
                break
            print("Choose an action:")
            print("1. Fill Jug 1\n2. Fill Jug 2\n3. Empty Jug 1\n4. Empty Jug 2\n5. Transfer Jug 1 -> Jug 2\n6. Transfer Jug 2 -> Jug 1\n7. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.fill_jug1()
            elif choice == '2':
                self.fill_jug2()
            elif choice == '3':
                self.empty_jug1()
            elif choice == '4':
                self.empty_jug2()
            elif choice == '5':
                self.transfer_jug1_to_jug2()
            elif choice == '6':
                self.transfer_jug2_to_jug1()
            elif choice == '7':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    trythis = WaterJug()  
    trythis.start()