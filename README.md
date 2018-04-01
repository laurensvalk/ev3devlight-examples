# ev3devlight-examples
Examples for using [ev3devlight](https://github.com/laurensvalk/ev3devlight).

## Installation for micropython

- Make sure you are running a [recent ev3dev stretch image](https://oss.jfrog.org/list/oss-snapshot-local/org/ev3dev/brickstrap/).
- Run the following on your EV3:
```
upip install ev3devlight
```

## Installation for python 3 (optional)

- First follow the installation step above.
- The library also works with python3. We just need to tell it where to find the library. To do so, run:
```
ln -s /home/robot/.micropython/lib/ev3devlight /home/robot/.local/lib/python3.5/site-packages/ev3devlight 
```

## Usage
- For now, look at any of the examples above. 
- Use any method you like to run the programs, but I recommend the [vscode IDE for EV3](https://github.com/ev3dev/vscode-ev3dev-browser).