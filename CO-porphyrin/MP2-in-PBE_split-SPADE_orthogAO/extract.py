import os

coordinate = "results.txt"
#simulation_list = ["0_deg.out", "10_deg.out", "20_deg.out", "30_deg.out", "40_deg.out", "50_deg.out", "60_deg.out", "70_deg.out", "80_deg.out", "85_deg.out", "86_deg.out", "87_deg.out", "88_deg.out", "89_deg.out", "90_deg.out", "91_deg.out", "92_deg.out", "93_deg.out", "94_deg.out", "95_deg.out", "100_deg.out", "110_deg.out", "120_deg.out", "130_deg.out", "140_deg.out", "150_deg.out", "160_deg.out", "170_deg.out", "180_deg.out"]
simulation_list = ["CO.out", "reactant.out", "product.out"]

def read_n_to_last_line(filename, n = 1):
    """Returns the nth before last line of a file (n=1 gives last line)"""
    num_newlines = 0
    with open(filename, 'rb') as f:
        try:
            f.seek(-2, os.SEEK_END)    
            while num_newlines < n:
                f.seek(-2, os.SEEK_CUR)
                if f.read(1) == b'\n':
                    num_newlines += 1
        except OSError:
            f.seek(0)
        last_line = f.readline().decode()
    return last_line

for i in simulation_list:
    last_line = read_n_to_last_line(i, n = 2)
    with open(coordinate, "a") as output:
        #output.write(i)
        #output.write("\n")
        output.write(last_line)
