for dir in ./SortedXML/**; do
    # Get the name of the directory
    # See https://stackoverflow.com/questions/1371261/get-current-directory-name-without-full-path-in-a-bash-script
    dirName="${dir%"${dir##*[!/]}"}"
    dirName="${dirName##*/}"

    mkdir -p ./generatedXSD

    trang -I xml -O xsd "$dir"/*.xml ./GeneratedXSD/"$dirName".xsd
done