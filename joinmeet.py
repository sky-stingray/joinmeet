import webbrowser

def joinmeet(platform, id, pwd):
	if platform.lower() == "zoom":
		webbrowser.open('zoommtg://zoom.us/join?confno='+str(id)+'&pwd='+str(pwd))

	elif platform.lower() == "googlemeet":
		webbrowser.open("meet.google.com/"+str(id))

	elif platform.lower() == "jitsi":
		webbrowser.open("meet.jitsi.org/"+str(id))


