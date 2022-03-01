# Alfred HTTP

An [Alfred](http://www.alfredapp.com/) workflow for searching HTTP status codes. The workflow displays the
codes along with their reason-phrase (e.g. "Not Found") and a short sentence
describing the function of this code.

Hitting return opens a browser window with the proper RFC for that status code.

![alfred-http](https://cloud.githubusercontent.com/assets/1006966/5054136/93735f3c-6c1f-11e4-8bda-8f523cc9fb5a.jpg)

This is a fork which adds Cloudflare's [unique 5XX HTTP codes](https://support.cloudflare.com/hc/en-us/articles/115003014432-HTTP-Status-Codes) and some ⚡️ speed ⚡️.

## Installation

* Download the [latest release](https://github.com/d-lord/alfred-http/releases/latest)
* Open finder and doubleclick the `HTTP.Statuses.alfredworkflow` file

## Preparation

You shouldn't need to do this unless you're the author or playing with another hack. This lets you add and edit entries for the List Filter that Alfred uses.

The data lives in a JSON file for ease of editing, but must be re-imported into Alfred as a CSV, so `build.py` generates that CSV.

```sh
python build.py
# this will spit out a CSV and some instructions; follow them
```

## Contributing

Check out the [contributing guidelines](https://github.com/d-lord/alfred-http/blob/master/CONTRIBUTING.md)

## License

This software is licensed under the [MIT licence](https://github.com/d-lord/alfred-http/blob/master/LICENSE.md)
