

# Power Requests Monitor
Is your computer finicky, and does it refuse to sleep or turn off the screen?  This application can help!  You get quick access to a list of processes that are preventing your system from sleeping, hibernating, turning off the screen, starting a screensaver, and more.
How is this possible?  Normally, to accomplish this, you would run the command "powercfg /requests" from an elevated command line terminal to get this information.  Once you have closed power hungry apps, you must run the command again to verify the request has been closed.
With this app, you can click on the icon to open, click to accept UAC, and that’s all it takes.  Your requests are visible with no typing.  Verifying closed requests is easy with one click of the refresh button.

## Screenshots
From initial commit:


## Known Issues:
At the moment, running from a built exe requires placing the icon file in the same folder.

At the moment, running from a built exe causes a "Legacy Kernel Caller" request.
So, to properly run, for now, you must have python installed and run directly from the .py file found under src.