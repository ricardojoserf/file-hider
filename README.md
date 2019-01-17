# file-hider

This hides your files in 'infinite' folders creating fake files which seem the same than the original.

The file created in each folder is not real, it is just a bunch of zeros and a one-bit in the exact position so the OS thinks it has the same size than the original file.

The original file gets stored in the route marked by the characters of the second parameter (so if the value is "abcd", it will be stored in "a/b/c/d" and in the other folders ("a/a/a/a", "a/a/a/b"...) a fake file with the same name and size gets stored).

## Usage

```
python hider.py $FILE $CHARACTERS
```

## Example

```
python hider.py file_to_hide.txt yzx
```

![Screenshot](img/Screenshot.png)

As the second parameter is *yzx* the original file is stored in *y/z/x/*. All the other files are fake.