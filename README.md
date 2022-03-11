# PP3-python-essentials README.md file

## For this project I elected to take the option of Project Example Idea 2: A Battleship console game.


![http://ami.responsivedesign.is/](images/PP3ResponsiveScreenShot.jpg "Responsive images of app")

------

## Code Source
For this project I utilised Battleship game code from [https://trinket.io/python/051179b6d3]

-----

## Development

In development, I utilised the [autopep8 tool](https://pypi.org/project/autopep8/) in the terminal. 
I installed it using pip.

`$ pip install --upgrade autopep8`

-----

## Deploying on Heroku

To deploy, I added the two buildpacks from the _Settings_ tab as instructed.

1. `heroku/python`
2. `heroku/nodejs`

I also created a _Config Var_ called `PORT`, and set this to `8000`

I connected my GitHub repository and the process was very smooth.

### The deployed app is here [https://pp3-python-essentials.herokuapp.com/]

-----

## Bugs

The code I utilised had some older Python layout quirks, but using VSCode I was able to identify and remedy these.

-----

## Testing

The game runs well in the terminal, but doesn't take keyboard inputs in mobile devices.
This is something I shall look into - there might be a module to enable this?