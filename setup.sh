KST_PATH=`pwd`
BIN_PATH=$HOME/bin

mkdir -p $BIN_PATH

for T in `ls ${KST_PATH}/tools/`
do
	# sed 后面一般用 's/abc/xxx'
	# 遇到$变量的时候，可以使用 "s/abc/xxx"
	# 如果$变量的值（一般是路径，如/usr/bin）包含's'后面的分隔符（一般是/），则更换分隔符，如#
	sed "s#init_kst_path_once#${KST_PATH}#g" $KST_PATH/tools/$T > $BIN_PATH/$T
	chmod +x $BIN_PATH/$T
done

export PATH=$PATH:$HOME/bin
