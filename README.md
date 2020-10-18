# JoinMeet

JoinMeet is a function (cuz' i don't know how to make it a library yet...) which allows you to connect to online meetings like [zoom](https://zoom.us/), [Google Meet](https://meet.google.com/) & [Jitsi Meet](https://meet.jit.si/) using python!
## Installation

Ah.. You know how to install don't you ;). But still here it goes....

```bash
git clone https://github.com/sky-stingray/joinmeet.git
```

## Usage
Possible values for platform-name = ["zoom","googlemeet","jitsi"]

```python
import joinmeet

#joinmeet.joinmeet(platform-name, id, password)

joinmeet.joinmeet("zoom",123456789,"pythonisallweneed") # opens zoom with creds you gave duh...
joinmeet.joinmeet("googlemeet","abc-klmn-xyz","this is not consider but who cares") # joins google meet blah blah
joinmeet.joinmeet("jitsi","samegoesforthis","but i am not bias to python ;>") # really you need this?
```
btw more platforms comming soon...
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

made with [makareadme](https://www.makeareadme.com/) 'cuz
 I am laz...
## License
[MIT](https://choosealicense.com/licenses/mit/) (I dont what it does tho)
