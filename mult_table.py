
for i in range(1,13,1):
    output_line = ""
    for j in range(1, 13, 1):
        output_line = output_line + "{:>4}".format(str(i * j))

    print output_line.strip()

