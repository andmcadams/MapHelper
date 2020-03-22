
install_darwin19_catalina() {
	# The plug-ins folder may not exist on MacOS
	if [[ ! -d $HOME/Library/Application\ Support/GIMP/2.10/plug-ins ]]
	then
		echo "Created plug-in folder at " $HOME/Library/Application\ Support/GIMP/2.10/plug-ins
		mkdir $HOME/Library/Application\ Support/GIMP/2.10/plug-ins
	else
		echo "Plug-in folder already exists..."
	fi

	# Copy the files over
	cp *.py $HOME/Library/Application\ Support/GIMP/2.10/plug-ins
	echo "Copied python files into plug-in folder"
}

install_linux_gnu() {
	# Some installs of GIMP don't come with gimp-python, so make sure it is installed.
	dpkg-query -l "gimp-python" > /dev/null
	if [ ! $? -eq 0 ]
	then
		echo "You need to have gimp-python installed. Some distributions do not package gimp-python with GIMP."
		echo "You might want to try: sudo apt-get install gimp-python"
		exit 1
	fi

	# Copy the files over
	cp *.py $HOME/.config/GIMP/2.10/plug-ins/
	echo "Copied python files into plug-in folder"
}

# So far I only know this works for darwin19 (macOS Catalina)
if [[ "$OSTYPE" == "darwin"* ]]
then
	install_darwin19_catalina
fi

if [[ "$OSTYPE" == "linux-gnu" ]]
then
	install_linux_gnu
fi