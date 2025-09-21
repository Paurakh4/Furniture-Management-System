def file(furniture_dict, furniture_id):
    # Read furniture data from file and store in dictionary
    file = open("Furniture.txt", "r")
    for each_line in file:
        each_line = each_line.replace("\n", "")
        furniture_dict[furniture_id] = each_line.split(",")
        furniture_id += 1
    file.close()


def file_read():
    # Read & display furniture data from file
    file = open("Furniture.txt", "r")
    for each_line in file:
        # Eliminate the newline character at the end of the line.
        each_line = each_line[:-1]
        # Commas replaces with tab spaces
        formatted_line = each_line.replace(",", "\t\t")
        print(formatted_line)
    file.close()
