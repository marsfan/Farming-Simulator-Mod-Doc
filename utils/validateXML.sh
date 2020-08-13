 # Super lightweight wrapper around xmllint to make it a bit eaiser to use.

 # What it does:
 # * Quiets output so that XML file is not sent to stdout
 # * Adds the --schema argument, so xmllint knows it is parsing from a XSD file.
 # * Redirects xmllint's stderr output to stdout, so that validation results can be piped to another script (e.g. grep)

# Use is identical to xmllint. The first argument is the schema file to use, and the rest are the files to check.
# Wildcards are supported for files to check (e.g. *.xml)



usage="$(basename "$0") [-h] schema file[s] -- Validate file(s) against an XML schema

    schema    The schema file to use
    file[s]       Files to validate against the schema. Can use wildcards, or be multiple paths
    -h          Show this help text"

if [[ $# -eq 0 ]] ; then
    echo "$usage"
    exit 0
fi

while getopts ":h" option; do
   case $option in
      h) # display Help
         echo "$usage"
         exit 0;;
   esac
done


xmllint  --noout --schema $1 "${@:2}" 2>&1

exit 0

