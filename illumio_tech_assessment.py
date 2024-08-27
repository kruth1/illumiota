#illumio technical assessment - 08/27/24 by kruthi kanduri

#reading protocol number mapping
protocol_mapping = {}
with open('protocol-numbers-1.csv') as protocol_numbers:
    next(protocol_numbers) #skip header row
    for line in protocol_numbers:
        tokens = line.strip().split(',') 

        #lines withoit numbers/keywords
        if len(tokens) < 2: 
            print(f"Skip malformed line: {line.strip()}")
            continue

        number, protocol_keyword, *_ = tokens
        protocol_mapping[number] = protocol_keyword.lower() #mapping number to keyword ignoring case

#reading in lookup table
lookup_table = {}
with open('lookup_table.csv') as file:
    next(file) #skipping header row
    for line in file:
        dstport, protocol, tag = line.strip().split(',') #extracting column values
        protocol = protocol.lower() #ignore case
        lookup_table[(dstport, protocol)] = tag #dstport and protocol decide what tag can be applied

#reading in flow logs
flow_logs=[]
with open('flow_logs.txt') as log_file:
    for line in log_file:
        tokens = line.strip().split() #splitting flow log columns up
        dstport = tokens[5] #dstport in 6th column
        protocol_number = tokens[7].lower() #protocol number in 8th column
        protocol = protocol_mapping.get(protocol_number, 'unknown').lower() #translating protocol number to protocol code
        flow_logs.append((dstport,protocol)) #creating a new column that acts as key

#initializing counters
tag_count = {}
port_protocol_count = {}
untagged_count = 0

#using lookup table to assign tags based on key of dstport and protocol
for dstport, protocol in flow_logs:
    if (dstport, protocol) in lookup_table:
        tag = lookup_table[(dstport,protocol)] 
        tag_count[tag] = tag_count.get(tag, 0) + 1 #increment tag count after assigning tag
    else:
        untagged_count += 1 #keep track of untagged logs (potential discrepancy)

    port_protocol_count[(dstport, protocol)] = port_protocol_count.get((dstport, protocol), 0) + 1 #keep track of every key combo

#writing output with parsed log flow data
with open('parsed_logs.txt','x') as output:
    #count of matches for each tag
    output.write("Tag Counts:\n")
    output.write("Tag,Count\n")
    for tag, count in tag_count.items():
        output.write(f"{tag},{count}\n")
    output.write(f"Untagged,{untagged_count}\n\n")

    #count of matches for each port/protocol combination
    output.write("Port/Protocol Combination Counts:\n")
    output.write("Port, Protocol, Count\n")
    for (dstport, protocol), count in port_protocol_count.items():
        output.write(f"{dstport},{protocol},{count}\n")
