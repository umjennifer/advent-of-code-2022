# https://adventofcode.com/2022/day/1

def get_file_content(input_file):
    f = open(input_file, "r")
    lines = f.read().splitlines()
    return lines

def convert_file_content(content):
    elf_to_calories = {
        0: {
            "calories": [],
            "calories_sum": 0,
        }
    }
    elf_index = 0
    elf_calories = []
    for line in content:
        if len(line) == 0:
            elf_to_calories[elf_index] = {
                "calories": elf_calories,
                "calories_sum": sum(elf_calories)
            }
            elf_calories = []
            elf_index += 1
        else:
            elf_calories.append(int(line))
    return elf_to_calories

def get_max_calories(elf_info):
    max_calories = elf_info[0]["calories_sum"]
    for info in elf_info.values():
        if info["calories_sum"] > max_calories:
            max_calories = info["calories_sum"]
    return max_calories

def get_sum_top_three_calories(elf_info):
    all_sums = get_list_calories_sum(elf_info)
    all_sums.sort(reverse=True)
    return all_sums[0] + all_sums[1] + all_sums[2]
    

def get_list_calories_sum(elf_info):
    all_calories_sum = []
    for info in elf_info.values():
        all_calories_sum.append(info["calories_sum"])
    return all_calories_sum

    

if __name__ == "__main__":
    file_content = get_file_content("input.txt")
    # print(file_content)
    elf_calories_info = convert_file_content(file_content)

    # answer = get_max_calories(elf_calories_info)
    # print("answer={}".format(answer))

    answer = get_sum_top_three_calories(elf_calories_info)
    print("answer={}".format(answer))
