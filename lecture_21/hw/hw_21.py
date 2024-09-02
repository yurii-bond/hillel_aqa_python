filtered_log = []
lines_list = []

# Step 1 - Open file and read lines
# Todo: Try to use read line along with filtering
with open('hblog.txt', 'r') as file:
    lines_list.extend(file.readlines())

# Step 2 - Filter lines
for line in lines_list:
    if "TSTFEED0300|7E3E|0400" in line:
        filtered_log.append(line)

del lines_list

str_tmstmp = 'Timestamp '
start = filtered_log[0].find(str_tmstmp) + str_tmstmp.__len__()
end = start + 8
print(filtered_log[0][start:end])

# Todo: Try to not double converting of the time string