def tower_of_hanoi(num_disks, first_rod, second_rod, final_rod):
    if num_disks == 1: 
        print(f"Move disk 1 from rod {first_rod} to rod {second_rod}")
        return

    tower_of_hanoi(num_disks - 1, first_rod, final_rod, second_rod)  

    print(f"Move disk {num_disks} from rod {first_rod} to rod {second_rod}")
    
    tower_of_hanoi(num_disks - 1, final_rod, second_rod, first_rod)

 
num_disks = 3
first_rod = 'A'
second_rod = 'C'
final_rod = 'B'

tower_of_hanoi(num_disks, first_rod, second_rod, final_rod)
