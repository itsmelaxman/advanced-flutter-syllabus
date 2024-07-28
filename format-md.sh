#!/bin/bash

# Function to add ### to titles like 4.2, 4.3
add_titles() {
    sed -E 's/^([0-9]+\.[0-9]+.*)$/### \1/' "$1"
}

# Function to add #### to subtitles
add_subtitles() {
    sed -E 's/^(Depth of Coverage:|Practical Exercises:|Additional Resources:)$/#### \1/' "$1"
}

# Function to add - to list items under subtitles
add_list_items() {
    awk '{
        if ($0 ~ /^(Depth of Coverage:|Practical Exercises:|Additional Resources:)$/) { print $0 }
        else if ($0 ~ /^[[:space:]]*$/) { print $0 }
        else if ($0 ~ /^### /) { print $0 }
        else if ($0 ~ /^#### /) { print $0 }
        else { print "- " $0 }
    }' "$1"
}

# Apply the formatting functions
add_titles "$1" | add_subtitles | add_list_items > $1

echo "Formatted file saved as $1"