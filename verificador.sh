function help(){

	echo "--- Debe ingresar 3 parámetros---"

}
if ! [ $# -eq 3 ]; then
	echo "son tres"
	help
	exit 1
fi
