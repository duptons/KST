
# 进度条模拟
loading(){
	echo -e "\033[?25l\c" # 禁止光标

	echo -e "loading: [    \c"
	sleep 0.5
	for ((i=0; i<$1; i++))
	do
		echo -e "\b\b\c\\c"
		sleep 0.1
		echo -e "\b|\c"
		sleep 0.1
		echo -e "\b/\c"
		sleep 0.1
		echo -e "\b=> ]\c"
	done
	sleep 0.5

	echo -e "\033[?25h" # 开启光标
}

loading 26
