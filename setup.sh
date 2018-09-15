KST_PATH=`pwd`
BIN_PATH=$HOME/bin

mkdir -p $BIN_PATH

## 修改 tools 文件夹下的文件的 path 配置
## 将 init_kst_path_once 替换成 $KST_PATH
for T in `ls ${KST_PATH}/tools/`
do
	# 1> sed 后面一般用 's/abc/xxx'
	# 2> 遇到$变量的时候，可以使用 "s/abc/xxx"
	# 3> 如果$变量的值（一般是路径，如/usr/bin）包含's'后面的分隔符（一般是/），则更换分隔符，如#
	sed "s#init_kst_path_once#${KST_PATH}#g" $KST_PATH/tools/$T > $BIN_PATH/$T
	chmod +x $BIN_PATH/$T
	echo -e "| cmd '$T' is \033[32mOK\033[0m (path: $BIN_PATH)"
done

if [[ ! "$PATH" =~ "$BIN_PATH" ]]; then
	echo "Warning: you show add '$BIN_PATH' into \$PATH"
fi
