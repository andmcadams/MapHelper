
install_darwin19_catalina() {
	if [[ ! -d $HOME/Library/Application\ Support/GIMP/2.10/plug-ins ]]
	then
		echo "Created plug-in folder at " $HOME/Library/Application\ Support/GIMP/2.10/plug-ins
		mkdir $HOME/Library/Application\ Support/GIMP/2.10/plug-ins
	else
		echo "Plug-in folder already exists..."
	fi
	cp *.py $HOME/Library/Application\ Support/GIMP/2.10/plug-ins
	echo "Copied python files into plug-in folder"
}

if [[ "$OSTYPE" == "darwin"* ]]
then
	install_darwin19_catalina
fi