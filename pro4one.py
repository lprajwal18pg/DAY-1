class TowerOfHanoi:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        
        self.rods = {
            'A': list(range(num_disks, 0, -1)),
            'B': [],
            'C': []
        }

    def is_valid_move(self, from_rod, to_rod):
        if not self.rods[from_rod]:
         
            print("Cannot move from an empty rod.")
            return False
        if self.rods[to_rod] and self.rods[from_rod][-1] > self.rods[to_rod][-1]:
        
            print("Cannot place a larger disk on top of a smaller one.")
            return False
        return True

    def make_move(self, from_rod, to_rod):
        if self.is_valid_move(from_rod, to_rod):
          
            disk = self.rods[from_rod].pop()
            self.rods[to_rod].append(disk)
            return True
        return False

    def play_game(self):
        print("the Tower of Hanoi game!")
        
        print("The goal is to move all disks from rod A to rod C in ascending order.")
        
        print("You can only move one disk at a time, and you cannot place a larger disk on top of a smaller one.")
        print("Let's start the game!")

        while True:
            print("\nA:", self.rods['A'])
            
            print("B:", self.rods['B'])
            
            print("C:", self.rods['C'])

            from_rod = input("Enter the rod to move from (A, B, C): ").upper()
            to_rod = input("Enter the rod to move to (A, B, C): ").upper()

            
            if self.make_move(from_rod, to_rod):
                if self.rods['C'] == list(range(self.num_disks, 0, -1)):
                    print("\nCongratulations, you won!")
                    break
            
            else:
                print("Invalid move, try again.")

if __name__ == "__main__":
    
    num_disks = int(input("Enter the number of disks: "))
    
    game = TowerOfHanoi(num_disks)
    game.play_game()