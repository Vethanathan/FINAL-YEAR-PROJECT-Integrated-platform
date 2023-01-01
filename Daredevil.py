from difflib import SequenceMatcher

def compare_report(file_1,file_2):
    with open(file_1) as file1, open(file_2) as file2:
        file1_data = file1.read()
        file2_data = file2.read()
        similarity = SequenceMatcher(None, file1_data, file2_data).ratio()
        return similarity*100
        # print(f"The contents are {similarity*100}% common")
