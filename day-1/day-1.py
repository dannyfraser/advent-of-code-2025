position = 50
dial_size = 100
with open("day-1-input.txt") as f:
	instructions = f.readlines() 
#instructions = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
zero_count = 0
for i in instructions:
	# calculate the result of the rotation
	initial_position = position
	sign = -1 if i[0]=="L" else 1
	value = int(i[1:])
	full_rotations = value // dial_size
	position_change = value - (full_rotations * dial_size)
	# calculate the effective new position - values outside the range of the dial will pass zero
	new_position = (initial_position + (position_change* sign))
	# set the position for the next rotation
	position = new_position % dial_size
	# start with the number of full rotations
	zeroes = full_rotations
	# zero in passing 
	# - don't count instances where the dial STARTS at zero and moves to negative or > 100
	if initial_position != 0 and not (0 <= new_position <= 100):
		zeroes += 1
  	# zero as result of rotation
	if position == 0:
		zeroes += 1
	zero_count += zeroes
	if zeroes>2:
		print(f"{i=}, {sign=}, {initial_position=}, {value=}, {full_rotations=}, {position_change=}, {new_position=}, {position=}, {zeroes=}, {zero_count=}")
print(zero_count)