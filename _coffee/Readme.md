### Creating and using coffeescript

#### NOTE: you must be running the custom server for the coffeescript to be compiled to js.

##### Steps

1. make a file filename.coffee file in \_coffee folder.
2. fill it with your script.
3. on the data file of the page add
  ```YAML
  ---
    coffee:
      - "otherfiles.coffee"
      - "filename.coffee"
  ```
4. wait for the server script to compile the code to js. (working on making it faster)
5. test and enjoy...
