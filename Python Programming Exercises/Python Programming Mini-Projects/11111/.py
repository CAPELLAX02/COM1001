def solve_towers(disks, source_peg, destination_peg, temp_peg):
 # base case -- only one disk to move
  if disks == 1:
    print("{} --> {}".format(source_peg, destination_peg) ) 
    return
  solve_towers(disks-1,source_peg,temp_peg,destination_peg)
  print("{} --> {}".format(source_peg, destination_peg) ) 
  solve_towers(disks-1,temp_peg,destination_peg,source_peg)

start_peg = 1 # value 1 used to indicate start_peg in output
end_peg = 3 # value 3 used to indicate end_peg in output
temp_peg = 2 # value 2 used to indicate temp_peg in output
total_disks = 3 # number of disks
solve_towers(total_disks, start_peg, end_peg, temp_peg)
