![PRM_Logo_512](https://github.com/thethirdtype/Power-Requests-Monitor/assets/125661915/4cfc2f20-4030-42e2-801e-442692f37203)

# Power Requests Monitor
Is your computer finicky, and does it refuse to sleep or turn off the screen?  This application can help!  You get quick access to a list of processes that are preventing your system from sleeping, hibernating, turning off the screen, starting a screensaver, and more.

How is this possible?  Normally, to accomplish this, you would run the command "powercfg /requests" from an elevated command line terminal to get this information.  Once you have closed power hungry apps, you must run the command again to verify the request has been closed.

With this app, you can click on the icon to open, click to accept UAC, and that’s all it takes.  Your requests are visible with no typing.  Verifying closed requests is easy with one click of the refresh button.

## Screenshots
From initial commit:

<img width="602" alt="SS01" src="https://github.com/thethirdtype/Power-Requests-Monitor/assets/125661915/0dc355d3-6dde-4e0a-9bda-bb5831a2feb9">

Light Mode

<img width="602" alt="SS02" src="https://github.com/thethirdtype/Power-Requests-Monitor/assets/125661915/717fa377-ce90-4fd7-8ef3-f23cccbdb3ac">

Dark Mode


## Known Issues:
At the moment, running from a built exe requires placing the icon file in the same folder.

At the moment, running from a built exe causes a "Legacy Kernel Caller" request.
So, to properly run, for now, you must have python installed and run directly from the .py file found under src.
