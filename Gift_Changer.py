import sys
from random import shuffle
def input_name() :
	names=[]
	for name in sys.stdin:
		name = name.strip()
		if name == "OK" :
			ans = input("這些人"+",".join(names)+"(共{}人)".format(len(names))+"參加交換禮物對嗎?[y/n]")
			if ans == "y":
				return names
			else :
				input_name()
		if len(name)==2:
			name = name[0]+'　'+name[1]
		names.append(name)

def randomer(lis):
	tmp = lis
	Flag = False
	while Flag==False:
		tmp = tmp + [999]
		shuffle(tmp)
		tmp.remove(999)
		Flag = checker(lis,tmp)
	return tmp

def checker(lis_1,lis_2):
	for i in range(len(lis_1)):
		if lis_1[i]==lis_2[i]:
			return False
	return True
def main():
	print("請輸入名稱，完成後請輸入'OK'")
	namelis = input_name()
	print("================================================")
	goodgif = randomer(namelis)
	badgif  = randomer(namelis)
	for i in range(len(namelis)):
		print(" {} 應該要拿 {} 的好禮物 和 {} 的壞禮物".format(namelis[i],goodgif[i],badgif[i]))

if __name__ == "__main__":
	main()