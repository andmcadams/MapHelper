if [[ ! -d ~/Library/Application\ Support/GIMP/2.10/plug-ins ]]
then
	mkdir ~/Library/Application\ Support/GIMP/2.10/plug-ins
else
	echo "Plug-in folder already exists..."
fi
cp *.py ~/Library/Application\ Support/GIMP/2.10/plug-ins
echo "Copied python files into plug-in folder"