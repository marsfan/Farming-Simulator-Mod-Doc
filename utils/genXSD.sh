for dir in ./SortedXML/*; do
    # Get the name of the directory
    # See https://stackoverflow.com/questions/1371261/get-current-directory-name-without-full-path-in-a-bash-script
    dirName="${dir%"${dir##*[!/]}"}" # extglob-free multi-trailing-/ trim
    dirName="${dirName##*/}"

    trang -I xml -O xsd "$dir"/*.xml ../schemas/"$dirName".xsd
done