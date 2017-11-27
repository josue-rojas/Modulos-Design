### Creating and using SASS

#### NOTE: you must be running the custom server for the SASS to be imported in the main scss files

##### Steps

1. make a file filename.sass file in \_sass folder.
2. fill it with your styling.
3. on the data file of the page add
  ```YAML
  ---
    sass:
      - "otherfiles.sass"
      - "filename.sass"
  ```
4. wait for the server script make the custom scss file.
5. test and enjoy...
