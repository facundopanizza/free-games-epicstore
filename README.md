# free-games-epicstore
Web scraping script that claims free games

You need to install with PIP the follow dependencies:
- pyotp
- selenium

After that you need to have installed chrome and in your PATH put the chrome webdriver or put it in the same folder as the script.
https://sites.google.com/a/chromium.org/chromedriver/

Configuration:
- twoFactorKey = 'YOURKEY' # If you have a two factor authentication system you need to put here the generated key used to activate the 2fa. Example: https://i.imgur.com/XnheZBY.png
- email = 'YOUREMAIL' # Your email or username for login
- passowrd = 'YOURPASSWORD' # Your password
