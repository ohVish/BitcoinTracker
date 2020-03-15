# BitcoinTracker
#### Windows system tray for tracking Bitcoin exchange value on Coinbase.


## Requirements
  * Python 3.
  * Package infi.systray for Python 3.
  * Package requests for Python 3.
  * Package sys for Python 3.

## Usage

The script is very simple to use. You only need to execute the file BTCTracking.py with Python 3:
```
python3 BTCTracking.py
```

You can change the currency of the tracking introducing the acronym of Coinbase. By default the currency is EUR. If you want the currency in United States Dollars:
```
python3 BTCTracking.py USD
```

You can execute it in background with the following batch command:
```
START /B python3 BTCTracking.py
```

Once you have executed the script, it will appear a new Windows system tray with the Bitcoin icon. You can double click on it to update the actual exchange value of the Bitcoin and it will appear on the header text of the system tray.
