import re

# Define the input file path
input_file = "TE.txt"

# Read data from the input file
with open(input_file, 'r') as file:
    data = file.read()

# Command to clear the counter Total Errors
print("Command to clear the counter Total Errors")

# Initialize a list to store the generated commands for Total Errors
total_error_commands = []

# Split the data into sections for each node
node_sections = re.split(r'Node:\s+', data)[1:]  # Skip the first empty element

for node_section in node_sections:
    # Extract the node name (including hyphens)
    node_match = re.search(r'(\S+)', node_section)
    if node_match:
        node_name = node_match.group(1)

    # Split the node section into sections for each interface
    interface_sections = re.split(r'-- interface\s+', node_section)

    for interface_section in interface_sections[1:]:  # Skip the first empty element
        # Extract the interface name
        interface_match = re.search(r'\s*([\w\d-]+)\s+\(', interface_section)
        if interface_match:
            interface_name = interface_match.group(1)

        # Check for total errors in RECEIVE and TRANSMIT sections
        receive_errors_match = re.search(r'RECEIVE[\s\S]*?Total errors:\s+(\d+)', interface_section)
        transmit_errors_match = re.search(r'TRANSMIT[\s\S]*?Total errors:\s+(\d+)', interface_section)

        receive_errors = int(receive_errors_match.group(1)) if receive_errors_match else 0
        transmit_errors = int(transmit_errors_match.group(1)) if transmit_errors_match else 0
        total_errors = receive_errors + transmit_errors

        if total_errors > 0:
            # Generate and add the command to the total_error_commands list
            total_command = f"node run -node {node_name} -command ifstat -z {interface_name}"
            total_error_commands.append(total_command)

# Print the commands for clearing Total Errors
for command in total_error_commands:
    print(command)

#CRC error section
# Read data from the input file
with open(input_file, 'r') as file:
    data = file.read()

# Command to clear the counter CRC Errors
print("Command to clear the counter CRC Errors")

# Initialize a list to store the generated commands for CRC errors
crc_error_commands = []

# Split the data into sections for each node
node_sections = re.split(r'Node:\s+', data)[1:]  # Skip the first empty element

for node_section in node_sections:
    # Extract the node name (including hyphens)
    node_match = re.search(r'(\S+)', node_section)
    if node_match:
        node_name = node_match.group(1)
    
    # Split the node section into sections for each interface
    interface_sections = re.split(r'-- interface\s+', node_section)
    
    for section in interface_sections[1:]:  # Skip the first empty element
        # Extract the interface name
        interface_match = re.search(r'\s*([\w\d-]+)\s+\(', section)
        if interface_match:
            interface_name = interface_match.group(1)
        
        # Check for CRC errors in RECEIVE section
        crc_errors_match = re.search(r'RECEIVE[\s\S]*?CRC errors:\s+(\d+)', section)
        if crc_errors_match:
            crc_errors = int(crc_errors_match.group(1))
            if crc_errors > 0:
                # Generate and add the command to the crc_error_commands list
                crc_command = f"node run -node {node_name} -command ifstat -z {interface_name}"
                crc_error_commands.append(crc_command)

# Print the commands for clearing CRC Errors
for command in crc_error_commands:
    print(command)
