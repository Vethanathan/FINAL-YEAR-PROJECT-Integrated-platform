import Daredevil
import Friday
Friday.pdf_to_txt("1.pdf","text1.txt")
# print(text1)
# exit()
Friday.pdf_to_txt("2.pdf","text2.txt")
print(Daredevil.compare_report("text1.txt","text2.txt"))

