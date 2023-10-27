#!/bin/bash
# Muhammad Hauzan Dini Fakhri 
path="hdfs/data/data1"
name_of_directory="data1"

# Check if the directory exists
if [ -d "$path/$name_of_directory" ]; then
    echo "There is $name_of_directory Directory Exists!"
else
    echo "$name_of_directory Directory Not Exists!"
    
    # Create the directory inside the path
    mkdir -p "$path/$name_of_directory"
    
    if [ $? -eq 0 ]; then
        echo "Created $name_of_directory Directory."
    else
        echo "Failed to create $name_of_directory Directory."
    fi
fi

